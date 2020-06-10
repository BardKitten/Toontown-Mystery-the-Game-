from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.distributed.PyDatagram import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task import Task
from LobbyGlobals import *
from datetime import datetime, timedelta
from panda3d.core import *

class GlobalLobbyManagerUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('GlobalLobbyManagerUD')

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)
        self.notify.debug("GLMUD generated")
        self.senders2Mgrs = {}
        self.host2LobbyId = {}
        self.id2Lobby = {}
        self.lobby2PubInfo = {}
        self.tempSlots = {}
        self.lobbyAllocator = UniqueIdAllocator(0, 100000000)

    def _makeAIMsg(self, field, values, recipient):
        return self.air.dclassesByName['DistributedLobbyManagerUD'].getFieldByName(field).aiFormatUpdate(recipient, recipient, simbase.air.ourChannel, values)

    def sendToAI(self, field, values, sender=None):
        if not sender:
            sender = self.air.getAvatarIdFromSender()
        dg = self._makeAIMsg(field, values, self.senders2Mgrs.get(sender, sender + 8))
        self.air.send(dg)

    def _makeAvMsg(self, field, values, recipient):
        return self.air.dclassesByName['DistributedToonUD'].getFieldByName(field).aiFormatUpdate(recipient, recipient, simbase.air.ourChannel, values)

    def sendToAv(self, avId, field, values):
        dg = self._makeAvMsg(field, values, avId)
        self.air.send(dg)

    def _formatLobby(self, lobbyDict):
        return [lobbyDict['lobbyId'], lobbyDict['hostId']]

    def avatarJoined(self, avId):
        lobbyId = self.host2LobbyId.get(avId, None)
        if lobbyId:
            lobby = self.id2Lobby.get(lobbyId, None)
            if not lobby:
                return
            self.sendToAv(avId, 'setHostedLobby', [[self._formatLobby(lobby)]])

    def __updateLobbyCount(self, lobbyId):
        for sender in self.senders2Mgrs.keys():
            self.sendToAI('updateToPublicLobbyCountUdToAllAi', [self.lobby2PubInfo[lobbyId]['numGuests'], lobbyId], sender=sender)

    def lobbyDone(self, lobbyId):
        del self.lobby2PubInfo[lobbyId]
        self.id2Lobby[lobbyId]['status'] = LobbyStatus.Finished
        lobby = self.id2Lobby.get(lobbyId, None)
        self.sendToAv(lobby['hostId'], 'setHostedLobby', [[self._formatLobby(lobby)]])
        del self.id2Lobby[lobbyId]
        self.air.writeServerEvent('lobby-done', '%s')

    def toonJoinedLobby(self, lobbyId, avId):
        if avId in self.tempSlots:
            del self.tempSlots[avId]
            return
        self.lobby2PubInfo.get(lobbyId, {'numGuests': 0})['numGuests'] += 1
        self.__updateLobbyCount(lobbyId)

    def toonLeftLobby(self, lobbyId, avId):
        self.lobby2PubInfo.get(lobbyId, {'numGuests': 0})['numGuests'] -= 1
        self.__updateLobbyCount(lobbyId)

    def lobbyManagerAIHello(self, channel):
        print 'AI with base channel %s, will send replies to DPM %s' % (simbase.air.getAvatarIdFromSender(), channel)
        self.senders2Mgrs[simbase.air.getAvatarIdFromSender()] = channel
        self.sendToAI('lobbyManagerUdStartingUp', [])
        self.air.addPostRemove(self._makeAIMsg('lobbyManagerUdLost', [], channel))

    def addLobby(self, avId, lobbyId):
        if avId in self.host2LobbyId:
            self.sendToAI('addLobbyResponseUdToAi', [lobbyId, AddLobbyErrorCode.TooManyHostedLobbies, self._formatLobby(self.id2Lobby[lobbyId])])
        self.id2Lobby[lobbyId] = {'lobbyId': lobbyId, 'hostId': avId}
        self.host2LobbyId[avId] = lobbyId
        self.sendToAI('addLobbyResponseUdToAi', [lobbyId, AddLobbyErrorCode.AllOk, self._formatLobby(self.id2Lobby[lobbyId])])

    def queryLobby(self, hostId):
        if hostId in self.host2LobbyId:
            lobby = self.id2Lobby[self.host2LobbyId[hostId]]
            self.sendToAI('lobbyInfoOfHostResponseUdToAi', [self._formatLobby(lobby)])
            return
        print 'query failed, av %s isnt hosting anything' % hostId

    def requestLobbySlot(self, lobbyId, avId):
        lobby = self.lobby2PubInfo[lobbyId]
        if lobby['numGuests'] >= lobby['maxGuests']:
            recipient = self.GetPuppetConnectionChannel(avId)
            sender = simbase.air.getAvatarIdFromSender()
            #dg = self.air.dclassesByName['DistributedPartyGateAI'].getFieldByName('partyRequestDenied').aiFormatUpdate(gateId, recipient, sender, [PartyGateDenialReasons.Full])
            #self.air.send(dg)
            return
        lobby['numGuests'] += 1
        self.__updateLobbyCount(lobbyId)
        self.tempSlots[avId] = lobbyId

        taskMgr.doMethodLater(60, self._removeTempSlot, 'lobbyManagerTempSlot%d' % avId, extraArgs=[avId])

        info = [lobby['shardId'], lobby['zoneId'], lobby['numGuests'], lobby['hostName']]
        hostId = self.id2Lobby[lobby['lobbyId']]['hostId']
        recipient = self.GetPuppetConnectionChannel(avId)
        sender = simbase.air.getAvatarIdFromSender()
        #dg = self.air.dclassesByName['DistributedPartyGateAI'].getFieldByName('setParty').aiFormatUpdate(gateId, recipient, sender, [info, hostId])
        #self.air.send(dg)

    def _removeTempSlot(self, avId):
        lobbyId = self.tempSlots.get(avId)
        if lobbyId:
            del self.tempSlots[avId]
            self.lobby2PubInfo.get(lobbyId, {'numGuests': 0})['numGuests'] -= 1
            self.__updateLobbyCount(lobbyId)

    def allocIds(self, numIds):
        ids = []
        while len(ids) < numIds:
            ids.append(self.lobbyAllocator.allocate())
        self.sendToAI('receiveId', ids)

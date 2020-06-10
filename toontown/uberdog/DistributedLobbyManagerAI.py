from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedLobbyManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedLobbyManagerAI")

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        self.lobbyId2Zone = {}
        self.lobbyId2PlanningZone = {}
        self.lobbyId2Host = {}
        self.host2LobbyId = {}
        self.avId2LobbyId = {}
        self.id2Lobby = {}
        self.pubLobbyInfo = {}
        self.idPool = range(self.air.ourChannel, self.air.ourChannel + 100000)

    def receiveId(self, ids):
        self.idPool += ids

    def _makeLobbyDict(self, struct):
        lobby = {}
        lobby['lobbyId'] = struct[0]
        lobby['hostId'] = struct[1]
        return lobby

    def lobbyManagerUdStartingUp(self):
        self.notify.info("LobbyManager UD is starting")

    def lobbyManagerUdLost(self):
        self.notify.warning("LobbyManager UD is lost")

    def addLobbyRequest(self, hostId):
        simbase.air.globalLobbyMgr.sendAddLobby(hostId, self.host2LobbyId[hostId])

    def addLobbyResponseUdToAi(self, lobbyId, errorCode, lobbyStruct):
        avId = lobbyStruct[1]
        self.sendUpdateToAvatarId(avId, 'addLobbyResponse', [avId, errorCode])
        self.air.doId2do[avId].sendUpdate('setHostedLobby', [[lobbyStruct]])
        pass

    def getLobbyZone(self, hostId, zoneId, isAvAboutToCreateLobby):
        avId = self.air.getAvatarIdFromSender()
        if isAvAboutToCreateLobby:
            lobbyId = self.idPool.pop()
            self.lobbyId2Host[lobbyId] = hostId
            self.lobbyId2PlanningZone[lobbyId] = zoneId
            self.host2LobbyId[hostId] = lobbyId
        else:
            if hostId not in self.host2LobbyId:
                self.air.globalLobbyMgr.queryLobbyForHost(hostId)
                return
            lobbyId = self.host2LobbyId[hostId]
            if lobbyId in self.lobbyId2Zone:
                zoneId = self.lobbyId2Zone[lobbyId]
        self.sendUpdateToAvatarId(avId, 'receiveLobbyZone', [hostId, lobbyId, zoneId])

    def lobbyInfoOfHostResponseUdToAi(self, lobbyStruct):
        lobby = self._makeLobbyDict(lobbyStruct)
        av = self.air.doId2do.get(lobby['hostId'], None)
        if not av:
            return
        lobbyId = lobby['lobbyId']
        zoneId = self.air.allocateZone()
        self.lobbyId2Zone[lobbyId] = zoneId
        self.host2LobbyId[lobby['hostId']] = lobbyId

        lobbyAI = DistributedLobbyAI(self.air, lobby['hostId'], zoneId, lobby)
        lobbyAI.generateWithRequiredAndId(self.air.allocateChannel(), self.air.districtId, zoneId)
        self.id2Lobby[lobbyId] = lobbyAI

        self.air.globalLobbyMgr.d_lobbyStarted(lobbyId, self.air.ourChannel, zoneId, av.getName())
        self.sendUpdateToAvatarId(lobby['hostId'], 'receiveLobbyZone', [lobby['hostId'], lobbyId, zoneId])

    def closeLobby(self, lobbyId):
        lobbyAI = self.id2Lobby[lobbyId]
        self.air.globalLobbyMgr.d_lobbyDone(lobbyId)
        for av in lobbyAI.avIdsInLobby:
            self.sendUpdateToAvatarId(av, 'sendAvToPlayground', [av, 0])
        lobbyAI.b_setLobbyState(LobbyStatus.Finished)
        taskMgr.doMethodLater(10, self.__deleteLobby, 'closeLobby%d' % lobbyId, extraArgs=[lobbyId])

    def __deleteLobby(self, lobbyId):
        lobbyAI = self.id2Lobby[lobbyId]
        for av in lobbyAI.avIdsAtLobby:
            self.sendUpdateToAvatarId(av, 'sendAvToPlayground', [av, 1])
        lobbyAI.requestDelete()
        zoneId = self.lobbyId2Zone[lobbyId]
        del self.lobbyId2Zone[lobbyId]
        del self.id2Lobby[lobbyId]
        del self.pubLobbyInfo[lobbyId]
        self.air.deallocateZone(zoneId)

    def freeZoneIdFromLobby(self, hostId, zoneId):
        sender = self.air.getAvatarIdFromSender()
        lobbyId = self.host2LobbyId[hostId]
        if lobbyId in self.lobbyId2PlanningZone:
            self.air.deallocateZone(self.lobbyId2PlanningZone[lobbyId])
            del self.lobbyId2PlanningZone[lobbyId]
            del self.host2LobbyId[hostId]
            del self.lobbyId2Host[lobbyId]

    def exitLobby(self, lobbyZone):
        avId = simbase.air.getAvatarIdFromSender()
        for lobbyInfo in self.pubLobbyInfo.values():
            if lobbyInfo['zoneId'] == lobbyZone:
                lobby = self.id2Lobby.get(lobbyInfo['lobbyId'])
                if lobby:
                    lobby._removeAvatar(avId)

    def getPublicLobbies(self):
        p = []
        for lobbyId in self.pubLobbyInfo:
            lobby = self.pubLobbyInfo[lobbyId]
            toons = lobby.get('numToons', 0)
            if toons > 8:
                toons = 8
            elif toons < 0:
                toons = 0
            p.append([lobby['shardId'], lobby['zoneId'], toons, lobby.get('hostName', '')])
        return p

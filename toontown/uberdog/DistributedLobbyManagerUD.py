from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class DistributedLobbyManagerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedLobbyManagerUD")

    def announceGenerate(self):
        DistributedObjectUD.announceGenerate(self)
        self.sendUpdate('lobbyManagerUdStartingUp')

    def addLobby(self, todo0, todo1, todo2, todo3):
        pass

    def addLobbyRequest(self, hostId):
        pass

    def addLobbyResponse(self, hostId, errorCode):
        pass

    def getLobbyZone(self, avId, zoneId, isAvAboutToCreateLobby):
        pass

    def receiveLobbyZone(self, todo0, todo1, todo2):
        pass

    def freeZoneIdFromCreatedLobby(self, avId, zoneId):
        pass

    def sendAvToPlayground(self, todo0, todo1):
        pass

    def exitParty(self, zoneIdOfAv):
        pass

    def lobbyManagerAIStartingUp(self, todo0, todo1):
        pass

    def lobbyManagerAIGoingDown(self, todo0, todo1):
        pass

    def lobbyHasStartedAiToUd(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def requestShardIdZoneIdForHostId(self, hostId):
        pass

    def sendShardIdZoneIdToAvatar(self, shardId, zoneId):
        pass

    def toonHasEnteredPartyAiToUd(self, todo0):
        pass

    def toonHasExitedPartyAiToUd(self, todo0):
        pass

    def lobbyHasFinishedUdToAllAi(self, todo0):
        pass

    def lobbyManagerUdStartingUp(self):
        pass

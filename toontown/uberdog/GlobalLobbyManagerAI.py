from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.distributed.PyDatagram import *
from direct.directnotify.DirectNotifyGlobal import directNotify

class GlobalLobbyManagerAI(DistributedObjectGlobalAI):
    notify = directNotify.newCategory('GlobalLobbyManagerAI')

    def announceGenerate(self):
        DistributedObjectGlobalAI.announceGenerate(self)
        self.sendUpdate('lobbyManagerAIHello', [simbase.air.lobbyManager.doId])

    def sendAddLobby(self, avId, lobbyId):
        self.sendUpdate('addLobby', [avId, lobbyId])

    def queryLobbyForHost(self, hostId):
        self.sendUpdate('queryLobby', [hostId])

    def d_lobbyStarted(self, lobbyId, shardId, zoneId, hostName):
        self.sendUpdate('lobbyHasStarted', [lobbyId, shardId, zoneId, hostName])

    def lobbyStarted(self, lobbyId, shardId, zoneId, hostName):
        pass

    def d_lobbyDone(self, lobbyId):
        self.sendUpdate('lobbyDone', [lobbyId])

    def lobbyDone(self, lobbyId):
        pass

    def d_toonJoinedLobby(self, lobbyId, avId):
        self.sendUpdate('toonJoinedLobby', [lobbyId, avId])

    def toonJoinedLobby(self, lobbyId, avId):
        pass

    def d_toonLeftLobby(self, lobbyId, avId):
        self.sendUpdate('toonLeftLobby', [lobbyId, avId])

    def toonLeftLobby(self, lobbyId, avId):
        pass

    def d_requestLobbySlot(self, lobbyId, avId):
        self.sendUpdate('requestLobbySlot', [lobbyId, avId])

    def requestLobbySlot(self, lobbyId, avId):
        pass

    def d_allocIds(self, numIds):
        self.sendUpdate('allocIds', [numIds])

    def allocIds(self, numIds):
        pass

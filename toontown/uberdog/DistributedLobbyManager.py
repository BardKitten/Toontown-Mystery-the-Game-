from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObject import DistributedObject

class DistributedLobbyManager(DistributedObject):
    neverDisable = 1
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLobbyManager')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        base.cr.lobbyManager = self
        self.allowUnreleased = False

    def delete(self):
        DistributedObject.delete(self)
        self.cr.lobbyManager = None

    def disable(self):
        self.ignore('deallocateZoneIdFromPlannedLobby')
        self.ignoreAll()
        DistributedObject.disable(self)

    def generate(self):
        DistributedObject.generate(self)
        self.accept('deallocateZoneIdFromPlannedLobby', self.deallocateZoneIdFromPlannedLobby)

    def deallocateZoneIdFromPlannedLobby(self, zoneId):
        self.sendUpdate('freeZoneIdFromPlannedLobby', [base.localAvatar.doId, zoneId])

    def allowUnreleasedClient(self):
        return self.allowUnreleased

    def setAllowUnreleaseClient(self, newValue):
        self.allowUnreleased = newValue

    def toggleAllowUnreleasedClient(self):
        self.allowUnreleased = not self.allowUnreleased
        return self.allowUnreleased

    def sendAddLobby(self, hostId):
        self.sendUpdate('addPartyRequest', [hostId])

    def requestLobbyZone(self, avId, zoneId, callback):
        if zoneId < 0:
            zoneId = 0
        self.acceptOnce('requestLobbyZoneComplete', callback)
        if hasattr(base.localAvatar, 'aboutToCreateLobby'):
            if base.localAvatar.aboutToCreateLobby:
                self.sendUpdate('getLobbyZone', [avId, zoneId, True])
        self.sendUpdate('getLobbyZone', [avId, zoneId, False])

    def receiveLobbyZone(self, hostId, lobbyId, zoneId):
        if lobbyId != 0 and zoneId != 0:
            if base.localAvatar.doId == hostId:
                lobbyInfo = base.localAvatar.hostedLobby
                if lobbyInfo.lobbyId == lobbyId:
                    lobbyInfo.status == LobbyGlobals.LobbyStatus.Open
        messenger.send('requestLobbyZoneComplete', [hostId, lobbyId, zoneId])

    def leaveLobby(self):
        if self.isDisabled():
            return
        self.sendUpdate('exitLobby', [localAvatar.zoneId])

    def sendAvatarToLobby(self, hostId):
        self.sendUpdate('requestShardIdZoneIdForHostId', [hostId])

    def sendShardIdZoneIdToAvatar(self, shardId, zoneId):
        # Avatar goes through door.
        pass

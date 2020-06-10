from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.toonbase import ToontownGlobals
from toontown.toon import DistributedToonAI

class ToontownDistrictStatsAI(DistributedObjectAI):
    notify = directNotify.newCategory('ToontownDistrictStatsAI')

    districtId = 0
    avatarCount = 0
    invasionStatus = 0
    groupAvCount = [0] * len(ToontownGlobals.GROUP_ZONES)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

        # We want to handle shard status queries so that a ShardStatusReceiver
        # being created after we're generated will know where we're at:
        self.air.accept('queryShardStatus', self.handleShardStatusQuery)
        taskMgr.doMethodLater(15, self.__countGroups, self.uniqueName('countGroups'))
    
    def delete(self):
        taskMgr.remove(self.uniqueName('countGroups'))
        DistributedObjectAI.delete(self)

    def handleShardStatusQuery(self):
        # Send a shard status update containing our population:
        status = {'population': self.avatarCount}
        self.air.sendNetEvent('shardStatus', [self.air.ourChannel, status])

    def setDistrictId(self, districtId):
        self.districtId = districtId

    def d_setDistrictId(self, districtId):
        self.sendUpdate('setDistrictId', [districtId])

    def b_setDistrictId(self, districtId):
        self.setDistrictId(districtId)
        self.d_setDistrictId(districtId)

    def getDistrictId(self):
        return self.districtId

    def setAvatarCount(self, avatarCount):
        self.avatarCount = avatarCount

        # Send a shard status update containing our population:
        status = {'population': self.avatarCount}
        self.air.sendNetEvent('shardStatus', [self.air.ourChannel, status])

    def d_setAvatarCount(self, avatarCount):
        self.sendUpdate('setAvatarCount', [avatarCount])

    def b_setAvatarCount(self, avatarCount):
        self.d_setAvatarCount(avatarCount)
        self.setAvatarCount(avatarCount)

    def getAvatarCount(self):
        return self.avatarCount

    def setInvasionStatus(self, invasionStatus):
        self.invasionStatus = invasionStatus

    def d_setInvasionStatus(self, invasionStatus):
        self.sendUpdate('setInvasionStatus', [invasionStatus])

    def b_setInvasionStatus(self, invasionStatus):
        self.setInvasionStatus(invasionStatus)
        self.d_setInvasionStatus(invasionStatus)

    def getInvasionStatus(self):
        return self.invasionStatus
    
    def setGroupAvCount(self, groupAvCount):
        self.groupAvCount = groupAvCount

    def d_setGroupAvCount(self, groupAvCount):
        self.sendUpdate('setGroupAvCount', [groupAvCount])

    def b_setGroupAvCount(self, groupAvCount):
        self.setGroupAvCount(groupAvCount)
        self.d_setGroupAvCount(groupAvCount)

    def getGroupAvCount(self):
        return self.groupAvCount
    
    def __countGroups(self, task):
        zones = ToontownGlobals.GROUP_ZONES
        self.groupAvCount = [0] * len(zones)
        
        for av in self.air.doId2do.values():
            if isinstance(av, DistributedToonAI.DistributedToonAI) and av.isPlayerControlled() and av.zoneId in zones:
                self.groupAvCount[zones.index(av.zoneId)] += 1

        taskMgr.doMethodLater(15, self.__countGroups, self.uniqueName('countGroups'))
        self.b_setGroupAvCount(self.groupAvCount)
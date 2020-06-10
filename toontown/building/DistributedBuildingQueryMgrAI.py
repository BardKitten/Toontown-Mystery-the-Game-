from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed import DistributedObjectAI


class DistributedBuildingQueryMgrAI(DistributedObjectAI.DistributedObjectAI):
    notify = directNotify.newCategory('DistributedBuildingQueryMgrAI')

    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.buildings = {}

    def isSuit(self, context, zoneId):
        avId = self.air.getAvatarIdFromSender()
        if zoneId not in self.buildings:
            self.sendUpdateToAvatarId(avId, 'response', [context, False])
        else:
            self.sendUpdateToAvatarId(avId, 'response', [context, self.buildings[zoneId].isSuitBlock()])

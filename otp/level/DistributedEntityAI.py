from direct.distributed import DistributedObjectAI
import Entity
from direct.directnotify import DirectNotifyGlobal

class DistributedEntityAI(DistributedObjectAI.DistributedObjectAI, Entity.Entity):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedEntityAI')

    def __init__(self, level, entId):
        if hasattr(level, 'air'):
            air = level.air
            self.levelDoId = level.doId
        else:
            air = level
            level = None
            self.levelDoId = 0
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        Entity.Entity.__init__(self, level, entId)
        return

    def generate(self):
        self.notify.debug('generate')
        DistributedObjectAI.DistributedObjectAI.generate(self)

    def destroy(self):
        self.notify.debug('destroy')
        Entity.Entity.destroy(self)
        self.requestDelete()

    def delete(self):
        self.notify.debug('delete')
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def getLevelDoId(self):
        return self.levelDoId

    def getEntId(self):
        return self.entId

from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed import DistributedObject


class DistributedBuildingQueryMgr(DistributedObject.DistributedObject):
    notify = directNotify.newCategory('DistributedBuildingQueryMgr')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.__callbacks = {}
        self.__context = 0
        self.cr = cr

    def announceGenerate(self):
        self.notify.debug('announceGenerate')
        DistributedObject.DistributedObject.announceGenerate(self)
        self.cr.buildingQueryMgr = self

    def delete(self):
        self.notify.debug('delete')
        DistributedObject.DistributedObject.delete(self)
        self.cr.buildingQueryMgr = None

    def d_isSuit(self, zoneId, callback):
        self.__context = (self.__context + 1) % 255
        self.__callbacks[self.__context] = callback
        self.sendUpdate('isSuit', [self.__context, zoneId])

    def response(self, context, flag):
        self.__callbacks.pop(context, lambda x: 0)(flag)

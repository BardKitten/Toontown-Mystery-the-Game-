from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObject import DistributedObject
from toontown.toonbase import ToontownGlobals

class DistributedBlackCatMgr(DistributedObject):
    neverDisable = 1
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBlackCatMgr')

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        base.cr.blackCatMgr = self

    def delete(self):
        base.cr.blackCatMgr = None
        DistributedObject.delete(self)

    def requestBlackCatTransformation(self):
        if not base.cr.newsManager.isHolidayRunning(ToontownGlobals.BLACK_CAT_DAY):
            return

        self.sendUpdate('requestBlackCatTransformation')

    def doBlackCatTransformation(self):
        base.localAvatar.getDustCloud(0.0, color=base.localAvatar.style.getBlackColor()).start()

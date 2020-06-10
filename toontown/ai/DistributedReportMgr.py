from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject

class DistributedReportMgr(DistributedObject.DistributedObject):
    neverDisable = 1
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedReportMgr')

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        base.cr.reportMgr = self

    def delete(self):
        base.cr.reportMgr = None
        DistributedObject.DistributedObject.delete(self)

    def sendReport(self, avId, category):
        self.sendUpdate('sendReport', [avId, category])

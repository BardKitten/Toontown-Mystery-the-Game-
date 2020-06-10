from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify.DirectNotifyGlobal import directNotify

class TTCodeRedemptionMgr(DistributedObject):
    neverDisable = 1
    notify = directNotify.newCategory('TTCodeRedemptionMgr')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        base.cr.codeRedemptionMgr = self

    def delete(self):
        if hasattr(base.cr, 'codeRedemptionMgr'):
            del base.cr.codeRedemptionMgr
        DistributedObject.delete(self)

    def redeemCode(self, code, callback):
        self.callback = callback
        self.sendUpdate('redeemCode', [code])

    def redeemCodeResult(self, result):
        self.callback(result)

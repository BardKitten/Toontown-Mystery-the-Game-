from direct.directnotify import DirectNotifyGlobal
import DistributedFactory

class DistributedMegaCorp(DistributedFactory.DistributedFactory):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMegaCorp')

    def __init__(self, cr):
        DistributedFactory.DistributedFactory.__init__(self, cr)

    def getFloorOuchLevel(self):
        return 8

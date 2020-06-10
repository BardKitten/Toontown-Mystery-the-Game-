from toontown.hood import HoodAI
from toontown.safezone import ButterflyGlobals
from toontown.safezone import DistributedButterflyAI
from toontown.safezone import DistributedDGFlowerAI
from toontown.safezone import DistributedTrolleyAI
from toontown.toonbase import ToontownGlobals
from toontown.ai import DistributedEffectMgrAI

class DGHoodAI(HoodAI.HoodAI):

    def __init__(self, air):
        HoodAI.HoodAI.__init__(self, air,
                               ToontownGlobals.DaisyGardens,
                               ToontownGlobals.DaisyGardens)

        self.trolley = None
        self.flower = None

        self.startup()

    def startup(self):
        HoodAI.HoodAI.startup(self)

        if simbase.config.GetBool('want-minigames', True):
            self.createTrolley()
        self.createFlower()
        if simbase.config.GetBool('want-butterflies', True):
            self.createButterflies()

        self.greenToonMgr = DistributedEffectMgrAI.DistributedEffectMgrAI(self.air, ToontownGlobals.IDES_OF_MARCH, 15)
        self.greenToonMgr.generateWithRequired(5819)

        self.trickOrTreatMgr = DistributedEffectMgrAI.DistributedEffectMgrAI(self.air, ToontownGlobals.HALLOWEEN, 12)
        self.trickOrTreatMgr.generateWithRequired(5620) # Rake It Inn, Elm Street

        self.winterCarolingMgr = DistributedEffectMgrAI.DistributedEffectMgrAI(self.air, ToontownGlobals.CHRISTMAS, 14)
        self.winterCarolingMgr.generateWithRequired(5626) # Pine Needle Crafts, Elm Street

    def shutdown(self):
        HoodAI.HoodAI.shutdown(self)

        ButterflyGlobals.clearIndexes(self.zoneId)

    def createTrolley(self):
        self.trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        self.trolley.generateWithRequired(self.zoneId)
        self.trolley.start()

    def createFlower(self):
        self.flower = DistributedDGFlowerAI.DistributedDGFlowerAI(self.air)
        self.flower.generateWithRequired(self.zoneId)
        self.flower.start()

    def createButterflies(self):
        playground = ButterflyGlobals.DG
        ButterflyGlobals.generateIndexes(self.zoneId, ButterflyGlobals.DG)

        for i in xrange(0, ButterflyGlobals.NUM_BUTTERFLY_AREAS[ButterflyGlobals.DG]):
            for _ in xrange(0, ButterflyGlobals.NUM_BUTTERFLIES[ButterflyGlobals.DG]):
                butterfly = DistributedButterflyAI.DistributedButterflyAI(self.air, playground, i, self.zoneId)
                butterfly.generateWithRequired(self.zoneId)
                butterfly.start()

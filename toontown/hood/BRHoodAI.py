from toontown.hood import HoodAI
from toontown.safezone import DistributedTrolleyAI
from toontown.toonbase import ToontownGlobals
from toontown.ai import DistributedPolarPlaceEffectMgrAI
from toontown.ai import DistributedEffectMgrAI

class BRHoodAI(HoodAI.HoodAI):
    def __init__(self, air):
        HoodAI.HoodAI.__init__(self, air,
                               ToontownGlobals.TheBrrrgh,
                               ToontownGlobals.TheBrrrgh)

        self.trolley = None

        self.startup()

    def startup(self):
        HoodAI.HoodAI.startup(self)

        if simbase.config.GetBool('want-minigames', True):
            self.createTrolley()

        self.PolarPlaceEffectManager = DistributedPolarPlaceEffectMgrAI.DistributedPolarPlaceEffectMgrAI(self.air)
        self.PolarPlaceEffectManager.generateWithRequired(3821)

        self.trickOrTreatMgr = DistributedEffectMgrAI.DistributedEffectMgrAI(self.air, ToontownGlobals.HALLOWEEN, 12)
        self.trickOrTreatMgr.generateWithRequired(3707) # Snowplace Like Home, Sleet Street

        self.winterCarolingMgr = DistributedEffectMgrAI.DistributedEffectMgrAI(self.air, ToontownGlobals.CHRISTMAS, 14)
        self.winterCarolingMgr.generateWithRequired(3828) # Snowman's Land, Polar Place

    def createTrolley(self):
        self.trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        self.trolley.generateWithRequired(self.zoneId)
        self.trolley.start()

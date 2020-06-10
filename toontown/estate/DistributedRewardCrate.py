from direct.interval.IntervalGlobal import *
from toontown.effects import DustCloud
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.toontowngui import TTDialog
from toontown.quest import Quests
from DistributedFurnitureItem import DistributedFurnitureItem

class DistributedRewardCrate(DistributedFurnitureItem):

    def __init__(self, cr):
        DistributedFurnitureItem.__init__(self, cr)
        self.dialog = None
        self.accept('exitingStoppedState', self.destroyDialog)
    
    def loadModel(self):
        model = DistributedFurnitureItem.loadModel(self)
        cSphere = CollisionSphere(0.0, 0.0, 1.0, 2.25)
        cSphere.setTangible(0)
        colNode = CollisionNode('Crate-%s' % self.doId)
        colNode.addSolid(cSphere)
        cSpherePath = model.attachNewNode(colNode)
        cSpherePath.setCollideMask(ToontownGlobals.WallBitmask)
        self.accept('enterCrate-%s' % self.doId, self.__enterSphere)
        return model
    
    def disable(self):
        self.ignoreAll()
        dustCloud = DustCloud.DustCloud(fBillboard=0, wantSound=1)
        dustCloud.setBillboardAxis(2.0)
        dustCloud.setScale(0.6)
        dustCloud.createTrack()
        Sequence(Func(dustCloud.reparentTo, render), Func(dustCloud.setPos, self.getPos()), dustCloud.track, Func(dustCloud.detachNode), Func(dustCloud.destroy)).start()
        DistributedFurnitureItem.disable(self)
    
    def destroyDialog(self):
        if self.dialog:
            self.dialog.destroy()
            self.dialog = None
    
    def showDialog(self, text):
        base.cr.playGame.getPlace().setState('stopped')
        self.dialog = TTDialog.TTDialog(style=TTDialog.Acknowledge, text=text, text_wordwrap=15, fadeScreen=1, command=self.__destroyDialog)
    
    def __destroyDialog(self, arg):
        self.destroyDialog()
        base.cr.playGame.getPlace().setState('walk')
    
    def __enterSphere(self, collisionEntry):
        if base.localAvatar.doId != self.furnitureMgr.ownerId:
            self.useKeyResponse(ToontownGlobals.CRATE_NOT_OWNER, 0)
            return
        elif not base.localAvatar.getCrateKeys():
            self.useKeyResponse(ToontownGlobals.CRATE_NO_KEYS, 0)
            return
        
        base.cr.playGame.getPlace().setState('stopped')
        self.dialog = TTDialog.TTDialog(style=TTDialog.TwoChoice, text=TTLocalizer.CrateAskToUse, fadeScreen=1, command=self.__handleDialogResponse)
    
    def __handleDialogResponse(self, response):
        self.destroyDialog()
        
        if response < 0:
            base.cr.playGame.getPlace().setState('walk')
            return
        
        self.sendUpdate('requestKeyUsage')
    
    def useKeyResponse(self, responseCode, amount):
        if responseCode == ToontownGlobals.CRATE_NOT_OWNER:
            self.showDialog(TTLocalizer.CrateNotOwner)
            return
        elif responseCode == ToontownGlobals.CRATE_NO_KEYS:
            self.showDialog(TTLocalizer.CrateNoKeys)
            return
        elif responseCode == ToontownGlobals.CRATE_BEANS:
            self.showDialog(TTLocalizer.CrateBeanPrize % amount)
        elif responseCode == ToontownGlobals.CRATE_BUFFS:
            buff = Quests.RewardDict[amount]
            
            self.showDialog(TTLocalizer.CrateBuffPrize % buff[0](amount, buff[1:]).getString())
        elif responseCode == ToontownGlobals.CRATE_NAMETAGS:
            self.showDialog(TTLocalizer.CrateNametagPrize)
        elif responseCode == ToontownGlobals.CRATE_EMOTES:
            self.showDialog(TTLocalizer.CrateEmotePrize)
        elif responseCode == ToontownGlobals.CRATE_CLOTHING:
            self.showDialog(TTLocalizer.CrateClothingPrize)
        elif responseCode == ToontownGlobals.CRATE_ACCESSORIES:
            self.showDialog(TTLocalizer.CrateAccessoryPrize)
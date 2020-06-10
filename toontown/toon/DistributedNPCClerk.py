from otp.nametag.NametagConstants import CFSpeech, CFTimeout
from toontown.minigame import ClerkPurchase
from toontown.toonbase import TTLocalizer, ToontownGlobals
from toontown.toon import NPCToons
from DistributedNPCToonBase import DistributedNPCToonBase
import time

class DistributedNPCClerk(DistributedNPCToonBase):

    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.lastCollision = 0
        self.purchaseGui = None

    def disable(self):
        self.destroyDialog()
        DistributedNPCToonBase.disable(self)

    def destroyDialog(self):
        self.ignoreAll()
        self.clearChat()
        taskMgr.remove(self.uniqueName('popupPurchaseGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))

        if self.purchaseGui:
            self.purchaseGui.exit()
            self.purchaseGui.unload()
            self.purchaseGui = None
    
    def freeAvatar(self):
        base.localAvatar.posCamera(0, 0)
        base.cr.playGame.getPlace().fsm.request('walk')

    def handleCollisionSphereEnter(self, collEntry):
        if self.lastCollision > time.time():
            return
        
        self.lastCollision = time.time() + ToontownGlobals.NPCCollisionDelay
        
        if not base.localAvatar.getMoney():
            self.setChatAbsolute(TTLocalizer.STOREOWNER_NEEDJELLYBEANS, CFSpeech | CFTimeout)
            return
        
        self.d_setState(ToontownGlobals.CLERK_GREETING)
        base.cr.playGame.getPlace().fsm.request('purchase')
        camera.wrtReparentTo(render)
        camera.posQuatInterval(1, Vec3(-5, 9, self.getHeight() - 0.5), Vec3(-150, -2, 0), other=self, blendType='easeOut', name=self.uniqueName('lerpCamera')).start()
        taskMgr.doMethodLater(1.0, self.popupPurchaseGUI, self.uniqueName('popupPurchaseGUI'))
    
    def d_setInventory(self, inventory, money):
        self.sendUpdate('setInventory', [inventory, money])
    
    def d_setState(self, state):
        self.sendUpdate('setState', [0, state])
    
    def setState(self, avId, state):
        av = base.cr.doId2do.get(avId)

        if not av:
            return

        if state == ToontownGlobals.CLERK_GOODBYE:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_GOODBYE, CFSpeech | CFTimeout)
        elif state == ToontownGlobals.CLERK_GREETING:
            self.lookAtAvatar(av)
            self.setChatAbsolute(TTLocalizer.STOREOWNER_GREETING, CFSpeech | CFTimeout)
            return
        elif state == ToontownGlobals.CLERK_TOOKTOOLONG:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_TOOKTOOLONG, CFSpeech | CFTimeout)

        self.initToonState()
   
    def popupPurchaseGUI(self, task):
        self.clearChat()
        self.acceptOnce('purchaseClerkDone', self.__handlePurchaseDone)
        self.purchaseGui = ClerkPurchase.ClerkPurchase(base.localAvatar, NPCToons.CLERK_COUNTDOWN_TIME, 'purchaseClerkDone')
        self.purchaseGui.load()
        self.purchaseGui.enter()

    def __handlePurchaseDone(self, state):
        self.d_setInventory(base.localAvatar.inventory.makeNetString(), base.localAvatar.getMoney())
        self.destroyDialog()
        self.freeAvatar()
        self.detectAvatars()
        self.d_setState(state)
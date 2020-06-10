from otp.nametag.NametagConstants import CFSpeech, CFTimeout
from toontown.toonbase import TTLocalizer, ToontownGlobals
from toontown.toon import NPCToons
from DistributedNPCToonBase import DistributedNPCToonBase
import GloveNPCGlobals, GloveShopGui, time

class DistributedNPCGlove(DistributedNPCToonBase):

    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.lastCollision = 0
        self.gloveDialog = None

    def disable(self):
        self.ignoreAll()
        self.destroyDialog()
        DistributedNPCToonBase.disable(self)

    def destroyDialog(self):
        self.clearChat()

        if self.gloveDialog:
            self.gloveDialog.destroy()
            self.gloveDialog = None

    def initToonState(self):
        self.setAnimState('neutral', 0.9, None, None)

        if self.name in NPCToons.GlovePositions:
            pos = NPCToons.GlovePositions[self.name]
            self.setPos(*pos[0])
            self.setH(pos[1])

    def getCollSphereRadius(self):
        return 1.25

    def handleCollisionSphereEnter(self, collEntry):
        if self.lastCollision > time.time():
            return

        self.lastCollision = time.time() + ToontownGlobals.NPCCollisionDelay

        if base.localAvatar.getTotalMoney() < ToontownGlobals.GloveCost:
            self.setChatAbsolute(TTLocalizer.GloveMoreMoneyMessage % ToontownGlobals.GloveCost, CFSpeech|CFTimeout)
            return

        base.cr.playGame.getPlace().fsm.request('stopped')
        base.setCellsAvailable(base.bottomCells, 0)
        self.setChatAbsolute(TTLocalizer.GlovePickColorMessage, CFSpeech|CFTimeout)
        self.acceptOnce('gloveShopDone', self.__gloveShopDone)
        self.gloveDialog = GloveShopGui.GloveShopGui()

    def freeAvatar(self):
        base.cr.playGame.getPlace().fsm.request('walk')
        base.setCellsAvailable(base.bottomCells, 1)

    def __gloveShopDone(self, state, glove):
        self.freeAvatar()

        if state == GloveNPCGlobals.TIMER_END:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_TOOKTOOLONG, CFSpeech|CFTimeout)
            return
        elif state == GloveNPCGlobals.USER_CANCEL:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_GOODBYE, CFSpeech|CFTimeout)
            return
        elif state == GloveNPCGlobals.CHANGE:
            self.sendUpdate('changeGlove', [glove])

    def changeGloveResult(self, avId, state):
        if state in GloveNPCGlobals.ChangeMessages:
            self.setChatAbsolute(GloveNPCGlobals.ChangeMessages[state], CFSpeech|CFTimeout)

        if state == GloveNPCGlobals.CHANGE_SUCCESSFUL:
            av = self.cr.doId2do.get(avId)

            if av:
                av.getDustCloud().start()

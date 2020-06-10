import ShtikerPage, DisguisePage
from toontown.toonbase import ToontownBattleGlobals
from direct.gui.DirectGui import *
from panda3d.core import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.coghq import CogDisguiseGlobals
from toontown.suit import SuitDNA

class InventoryPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.meritBars = []
        self.currentTrackInfo = None
        self.onscreen = 0
        self.lastInventoryTime = globalClock.getRealTime()

    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.InventoryPageTitle, text_scale=0.12, textMayChange=1, pos=(0, 0, 0.62))
        self.gagFrame = DirectFrame(parent=self, relief=None, pos=(-0.05, 0, -0.47), scale=(0.35, 0.35, 0.35), geom=DGG.getDefaultDialogGeom(), geom_color=ToontownGlobals.GlobalDialogColor)
        self.trackInfo = DirectFrame(parent=self, relief=None, pos=(-0.55, 0, -0.47), scale=(0.35, 0.35, 0.35), geom=DGG.getDefaultDialogGeom(), geom_scale=(1.4, 1, 1), geom_color=ToontownGlobals.GlobalDialogColor, text='', text_wordwrap=11, text_align=TextNode.ALeft, text_scale=0.12, text_pos=(-0.65, 0.3), text_fg=(0.05, 0.14, 0.4, 1))
        self.trackProgress = DirectWaitBar(parent=self.trackInfo, pos=(0, 0, -0.2), relief=DGG.SUNKEN, frameSize=(-0.6,
         0.6,
         -0.1,
         0.1), borderWidth=(0.025, 0.025), scale=1.1, frameColor=(0.4, 0.6, 0.4, 1), barColor=(0.9, 1, 0.7, 1), text='0/0', text_scale=0.15, text_fg=(0.05, 0.14, 0.4, 1), text_align=TextNode.ACenter, text_pos=(0, -0.22))
        self.trackProgress.hide()
        jarGui = loader.loadModel('phase_3.5/models/gui/jar_gui')
        catalogGui = loader.loadModel('phase_5.5/models/gui/catalog_gui')
        self.moneyDisplay = DirectLabel(parent=self, relief=None, pos=(0.35, 0, -0.5), scale=0.8, text=str(base.localAvatar.getMoney()), text_scale=0.18, text_fg=(0.95, 0.95, 0, 1), text_shadow=(0, 0, 0, 1), text_pos=(0, -0.1, 0), image=jarGui.find('**/Jar'), text_font=ToontownGlobals.getSignFont())
        self.bankMoneyDisplay = DirectLabel(self, relief=None, pos=(0.35, 0, -0.1), scale=0.6, image=catalogGui.find('**/bean_bank'), text=str(base.localAvatar.getBankMoney()), text_align=TextNode.ARight, text_scale=0.11, text_fg=(0.95, 0.95, 0, 1), text_shadow=(0, 0, 0, 1), text_pos=(0.75, -0.81), text_font=ToontownGlobals.getSignFont())
        self.createMeritBars()
        jarGui.removeNode()
        catalogGui.removeNode()

    def unload(self):
        self.ignoreAll()
        del self.title
        self.destroyMeritBars()
        ShtikerPage.ShtikerPage.unload(self)

    def createMeritBars(self):
        if self.meritBars:
            return

        for i in xrange(len(SuitDNA.suitDepts)):
            self.meritBars.append(DirectWaitBar(parent=self.trackInfo, relief=DGG.SUNKEN, frameSize=(-1, 1, -0.15, 0.15),
             borderWidth=(0.02, 0.02), scale=0.65, text='', text_scale=0.18, text_fg=(0, 0, 0, 1), text_align=TextNode.ALeft,
             text_pos=(-0.96, -0.05), pos=(0, 0, 0.365 - 0.24 * i), frameColor=(DisguisePage.DeptColors[i][0] * 0.7,
             DisguisePage.DeptColors[i][1] * 0.7, DisguisePage.DeptColors[i][2] * 0.7, 1), barColor=(DisguisePage.DeptColors[i][0] * 0.8,
             DisguisePage.DeptColors[i][1] * 0.8, DisguisePage.DeptColors[i][2] * 0.8, 1)))

        self.accept(localAvatar.uniqueName('cogMeritsChange'), self.updateMeritBars)
        self.updateMeritBars()

    def destroyMeritBars(self):
        if not self.meritBars:
            return

        for meritBar in self.meritBars:
            meritBar.destroy()

        self.meritBars = []

    def changeMeritBars(self, hide):
        if not self.meritBars:
            return

        for i in xrange(len(self.meritBars)):
            meritBar = self.meritBars[i]

            if CogDisguiseGlobals.isSuitComplete(base.localAvatar.cogParts, i):
                meritBar.hide() if hide else meritBar.show()
            else:
                meritBar.hide()

    def updateMeritBars(self):
        if not self.meritBars:
            return

        for i in xrange(len(self.meritBars)):
            meritBar = self.meritBars[i]

            if CogDisguiseGlobals.isSuitComplete(base.localAvatar.cogParts, i):
                meritBar.show()
                totalMerits = CogDisguiseGlobals.getTotalMerits(base.localAvatar, i)
                merits = base.localAvatar.cogMerits[i]

                if totalMerits:
                    meritBar['range'] = totalMerits
                    meritBar['value'] = merits

                    if merits == totalMerits:
                        meritBar['text'] = TTLocalizer.RewardPanelMeritAlert
                    else:
                        meritBar['text'] = '%s/%s %s' % (merits, totalMerits, TTLocalizer.RewardPanelMeritBarLabels[i])
                else:
                    meritBar['range'] = 1
                    meritBar['value'] = 1
                    meritBar['text'] = TTLocalizer.RewardPanelMeritsMaxed
            else:
                meritBar.hide()

    def __moneyChange(self, money):
        self.moneyDisplay['text'] = str(money)

    def __bankMoneyChange(self, bankMoney):
        self.bankMoneyDisplay['text'] = str(bankMoney)

    def enter(self):
        ShtikerPage.ShtikerPage.enter(self)
        base.localAvatar.inventory.setActivateMode('book')
        base.localAvatar.inventory.show()
        base.localAvatar.inventory.reparentTo(self)
        self.__moneyChange(base.localAvatar.getMoney())
        self.__bankMoneyChange(base.localAvatar.getBankMoney())
        self.accept('enterTrackFrame', self.updateTrackInfo)
        self.accept('exitTrackFrame', self.clearTrackInfo)
        self.accept(localAvatar.uniqueName('moneyChange'), self.__moneyChange)
        self.accept(localAvatar.uniqueName('bankMoneyChange'), self.__bankMoneyChange)

    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        self.clearTrackInfo(self.currentTrackInfo)
        self.ignore('enterTrackFrame')
        self.ignore('exitTrackFrame')
        self.ignore(localAvatar.uniqueName('moneyChange'))
        self.ignore(localAvatar.uniqueName('bankMoneyChange'))
        self.makePageWhite(None)
        base.localAvatar.inventory.hide()
        base.localAvatar.inventory.reparentTo(hidden)

    def updateTrackInfo(self, trackIndex):
        self.currentTrackInfo = trackIndex
        trackName = TextEncoder.upper(ToontownBattleGlobals.Tracks[trackIndex])
        self.changeMeritBars(True)
        self.trackInfo.show()
        if base.localAvatar.hasTrackAccess(trackIndex):
            curExp, nextExp = base.localAvatar.inventory.getCurAndNextExpValues(trackIndex)
            trackText = '%s / %s' % (curExp, nextExp)
            self.trackProgress['range'] = nextExp
            self.trackProgress['value'] = curExp
            if curExp >= ToontownBattleGlobals.regMaxSkill:
                str = TTLocalizer.InventoryPageTrackFull % trackName
                trackText = TTLocalizer.InventoryUberTrackExp % {'nextExp': ToontownBattleGlobals.MaxSkill - curExp}
                self.trackProgress['range'] = ToontownBattleGlobals.UberSkill
                uberCurrExp = curExp - ToontownBattleGlobals.regMaxSkill
                self.trackProgress['value'] = uberCurrExp
            else:
                morePoints = nextExp - curExp
                if morePoints == 1:
                    str = TTLocalizer.InventoryPageSinglePoint % {'trackName': trackName,
                     'numPoints': morePoints}
                else:
                    str = TTLocalizer.InventoryPagePluralPoints % {'trackName': trackName,
                     'numPoints': morePoints}
            self.trackInfo['text'] = str
            self.trackProgress['text'] = trackText
            self.trackProgress['frameColor'] = (ToontownBattleGlobals.TrackColors[trackIndex][0] * 0.6,
             ToontownBattleGlobals.TrackColors[trackIndex][1] * 0.6,
             ToontownBattleGlobals.TrackColors[trackIndex][2] * 0.6,
             1)
            self.trackProgress['barColor'] = (ToontownBattleGlobals.TrackColors[trackIndex][0],
             ToontownBattleGlobals.TrackColors[trackIndex][1],
             ToontownBattleGlobals.TrackColors[trackIndex][2],
             1)
            self.trackProgress.show()
        else:
            str = TTLocalizer.InventoryPageNoAccess % trackName
            self.trackInfo['text'] = str
            self.trackProgress.hide()

    def clearTrackInfo(self, trackIndex):
        if self.currentTrackInfo == trackIndex:
            self.trackInfo['text'] = ''
            self.trackProgress.hide()
            self.currentTrackInfo = None
            self.changeMeritBars(False)

    def acceptOnscreenHooks(self):
        self.accept(ToontownGlobals.InventoryHotkeyOn, self.showInventoryOnscreen)
        self.accept(ToontownGlobals.InventoryHotkeyOff, self.hideInventoryOnscreen)

    def ignoreOnscreenHooks(self):
        self.ignore(ToontownGlobals.InventoryHotkeyOn)
        self.ignore(ToontownGlobals.InventoryHotkeyOff)

    def showInventoryOnscreen(self):
        messenger.send('wakeup')
        timedif = globalClock.getRealTime() - self.lastInventoryTime
        if timedif < 0.7:
            return
        self.lastInventoryTime = globalClock.getRealTime()
        if self.onscreen or base.localAvatar.questPage.onscreen:
            return
        self.onscreen = 1
        base.localAvatar.inventory.setActivateMode('book')
        base.localAvatar.inventory.show()
        base.localAvatar.inventory.reparentTo(self)
        self.__moneyChange(base.localAvatar.getMoney())
        self.__bankMoneyChange(base.localAvatar.getBankMoney())
        self.accept('enterTrackFrame', self.updateTrackInfo)
        self.accept('exitTrackFrame', self.clearTrackInfo)
        self.accept(localAvatar.uniqueName('moneyChange'), self.__moneyChange)
        self.accept(localAvatar.uniqueName('bankMoneyChange'), self.__bankMoneyChange)
        self.reparentTo(aspect2d)
        self.title.hide()
        self.show()

    def hideInventoryOnscreen(self):
        if not self.onscreen:
            return
        self.onscreen = 0
        self.ignore('enterTrackFrame')
        self.ignore('exitTrackFrame')
        self.ignore(localAvatar.uniqueName('moneyChange'))
        self.ignore(localAvatar.uniqueName('bankMoneyChange'))
        base.localAvatar.inventory.hide()
        base.localAvatar.inventory.reparentTo(hidden)
        self.reparentTo(self.book)
        self.title.show()
        self.hide()

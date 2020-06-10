from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from direct.gui.DirectGui import *
from direct.showbase import DirectObject
from panda3d.core import *

from toontown.effects import DistributedFireworkShow
from otp.nametag import NametagGlobals
from toontown.parties import DistributedPartyFireworksActivity
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals


class ShtikerBook(DirectFrame, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('ShtikerBook')

    def __init__(self, doneEvent):
        DirectFrame.__init__(self, relief=None, sortOrder=DGG.BACKGROUND_SORT_INDEX)
        self.initialiseoptions(ShtikerBook)
        StateData.StateData.__init__(self, doneEvent)
        self.pages = []
        self.pageTabs = []
        self.currPageTabIndex = None
        self.pageTabFrames = [self.createPageTabFrame(x) for x in (-0.93, 0.93)]
        self.currPageIndex = None
        self.entered = 0
        self.safeMode = 0
        self.__obscured = 0
        self.__shown = 0
        self.__isOpen = 0
        self.hide()
        self.setPos(0, 0, 0.1)
        self.pageOrder = [TTLocalizer.OptionsPageTitle,
         TTLocalizer.ShardPageTitle,
         TTLocalizer.MapPageTitle,
         TTLocalizer.InventoryPageTitle,
         TTLocalizer.QuestPageToonTasks,
         TTLocalizer.TrackPageShortTitle,
         TTLocalizer.SuitPageTitle,
         TTLocalizer.FishPageTitle,
         TTLocalizer.KartPageTitle,
         TTLocalizer.DisguisePageTitle,
         TTLocalizer.NPCFriendPageTitle,
         TTLocalizer.GardenPageTitle,
         TTLocalizer.GolfPageTitle,
         TTLocalizer.PhotoPageTitle,
         TTLocalizer.EventsPageName,
         TTLocalizer.StatPageTitle]
    
    def createPageTabFrame(self, x):
        frame = DirectFrame(parent=self, relief=None, pos=(x, 0, 0.66), scale=1.25)
        frame.hide()
        return frame

    def setSafeMode(self, setting):
        self.safeMode = setting

    def enter(self):
        if base.config.GetBool('want-qa-regression', 0):
            self.notify.info('QA-REGRESSION: SHTICKERBOOK: Open')
        if self.entered:
            return
        self.entered = 1
        messenger.send('releaseDirector')
        messenger.send('stickerBookEntered')
        base.playSfx(self.openSound)
        base.disableMouse()
        base.render.hide()
        base.setBackgroundColor(0.05, 0.15, 0.4)
        base.setCellsAvailable([base.rightCells[0]], 0)
        self.oldMin2dAlpha = NametagGlobals.getMin2dAlpha()
        self.oldMax2dAlpha = NametagGlobals.getMax2dAlpha()
        NametagGlobals.setMin2dAlpha(0.8)
        NametagGlobals.setMax2dAlpha(1.0)
        self.__isOpen = 1
        self.__setButtonVisibility()
        self.show()
        self.showPageArrows()
        if not self.safeMode:
            self.accept('shtiker-page-done', self.__pageDone)
            self.accept(ToontownGlobals.StickerBookHotkey, self.__close)
            self.accept(ToontownGlobals.OptionsPageHotkey, self.__close)
            for tab in self.pageTabFrames:
                tab.show()
        self.pages[self.currPageIndex].enter()

    def exit(self):
        if not self.entered:
            return
        self.entered = 0
        messenger.send('stickerBookExited')
        base.playSfx(self.closeSound)
        self.pages[self.currPageIndex].exit()
        base.render.show()
        setBlackBackground = 0
        for obj in base.cr.doId2do.values():
            if isinstance(obj, DistributedFireworkShow.DistributedFireworkShow) or isinstance(obj, DistributedPartyFireworksActivity.DistributedPartyFireworksActivity):
                setBlackBackground = 1

        if setBlackBackground:
            base.setBackgroundColor(Vec4(0, 0, 0, 1))
        else:
            base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
        gsg = base.win.getGsg()
        if gsg:
            base.render.prepareScene(gsg)
        NametagGlobals.setMin2dAlpha(self.oldMin2dAlpha)
        NametagGlobals.setMax2dAlpha(self.oldMax2dAlpha)
        base.setCellsAvailable([base.rightCells[0]], 1)
        self.__isOpen = 0
        self.hide()
        self.hideButton()
        cleanupDialog('globalDialog')
        for tab in self.pageTabFrames:
            tab.hide()
        self.ignore('shtiker-page-done')
        self.ignore(ToontownGlobals.StickerBookHotkey)
        self.ignore(ToontownGlobals.OptionsPageHotkey)
        self.ignore('arrow_right')
        self.ignore('arrow_left')
        if base.config.GetBool('want-qa-regression', 0):
            self.notify.info('QA-REGRESSION: SHTICKERBOOK: Close')

    def load(self):
        self.checkGardenStarted = localAvatar.getGardenStarted()
        bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
        self['image'] = bookModel.find('**/big_book')
        self['image_scale'] = (2, 1, 1.5)
        self.resetFrameSize()
        self.bookOpenButton = DirectButton(image=(bookModel.find('**/BookIcon_CLSD'), bookModel.find('**/BookIcon_OPEN'), bookModel.find('**/BookIcon_RLVR')), relief=None, pos=(-0.158, 0, 0.17), parent=base.a2dBottomRight, scale=0.305, command=self.__open)
        self.bookCloseButton = DirectButton(image=(bookModel.find('**/BookIcon_OPEN'), bookModel.find('**/BookIcon_CLSD'), bookModel.find('**/BookIcon_RLVR2')), relief=None, pos=(-0.158, 0, 0.17), parent=base.a2dBottomRight, scale=0.305, command=self.__close)
        self.bookOpenButton.hide()
        self.bookCloseButton.hide()
        self.nextArrow = DirectButton(parent=self, relief=None, image=(bookModel.find('**/arrow_button'), bookModel.find('**/arrow_down'), bookModel.find('**/arrow_rollover')), scale=(0.1, 0.1, 0.1), pos=(0.838, 0, -0.661), command=self.__pageChange, extraArgs=[1])
        self.prevArrow = DirectButton(parent=self, relief=None, image=(bookModel.find('**/arrow_button'), bookModel.find('**/arrow_down'), bookModel.find('**/arrow_rollover')), scale=(-0.1, 0.1, 0.1), pos=(-0.838, 0, -0.661), command=self.__pageChange, extraArgs=[-1])
        bookModel.removeNode()
        self.openSound = base.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_open.ogg')
        self.closeSound = base.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_delete.ogg')
        self.pageSound = base.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_turn.ogg')
        return

    def unload(self):
        loader.unloadModel('phase_3.5/models/gui/stickerbook_gui')
        self.destroy()
        self.bookOpenButton.destroy()
        del self.bookOpenButton
        self.bookCloseButton.destroy()
        del self.bookCloseButton
        self.nextArrow.destroy()
        del self.nextArrow
        self.prevArrow.destroy()
        del self.prevArrow
        for page in self.pages:
            page.unload()

        del self.pages
        for pageTab in self.pageTabs:
            pageTab.destroy()

        del self.pageTabs
        del self.currPageTabIndex
        del self.openSound
        del self.closeSound
        del self.pageSound

    def addPage(self, page, pageName = 'Page'):
        if pageName not in self.pageOrder:
            self.notify.error('Trying to add page %s in the ShtickerBook. Page not listed in the order.' % pageName)
            return
        self.pages.append(page)
        pageIndex = len(self.pages) - 1
        page.setBook(self)
        page.setPageName(pageName)
        page.reparentTo(self)
        self.addPageTab(page, pageIndex, pageName)

    def addPageTab(self, page, pageIndex, pageName = 'Page'):
        tabIndex = len(self.pageTabs)

        def goToPage():
            messenger.send('wakeup')
            base.playSfx(self.pageSound)
            self.setPage(page)
            if base.config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: SHTICKERBOOK: Browse tabs %s' % page.pageName)

        yOffset = 0.07 * (pageIndex % 16)
        iconGeom = None
        iconImage = None
        iconScale = 1
        iconColor = (1, 1, 1, 1)
        buttonPressedCommand = goToPage
        extraArgs = []
        if pageName == TTLocalizer.OptionsPageTitle:
            iconModels = loader.loadModel('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/switch')
            iconModels.detachNode()
        elif pageName == TTLocalizer.ShardPageTitle:
            iconModels = loader.loadModel('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/district')
            iconModels.detachNode()
        elif pageName == TTLocalizer.MapPageTitle:
            iconModels = loader.loadModel('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/teleportIcon')
            iconModels.detachNode()
        elif pageName == TTLocalizer.InventoryPageTitle:
            iconModels = loader.loadModel('phase_3.5/models/gui/inventory_icons')
            iconGeom = iconModels.find('**/inventory_tart')
            iconScale = 7
            iconModels.detachNode()
        elif pageName == TTLocalizer.QuestPageToonTasks:
            iconModels = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
            iconGeom = iconModels.find('**/questCard')
            iconScale = 0.9
            iconModels.detachNode()
        elif pageName == TTLocalizer.TrackPageShortTitle:
            iconGeom = iconModels = loader.loadModel('phase_3.5/models/gui/filmstrip')
            iconScale = 1.1
            iconColor = Vec4(0.7, 0.7, 0.7, 1)
            iconModels.detachNode()
        elif pageName == TTLocalizer.SuitPageTitle:
            iconModels = loader.loadModel('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/gui_gear')
            iconModels.detachNode()
        elif pageName == TTLocalizer.FishPageTitle:
            iconModels = loader.loadModel('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/fish')
            iconModels.detachNode()
        elif pageName == TTLocalizer.GardenPageTitle:
            iconModels = loader.loadModel('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/gardenIcon')
            iconModels.detachNode()
        elif pageName == TTLocalizer.DisguisePageTitle:
            iconModels = loader.loadModel('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/disguise2')
            iconColor = Vec4(0.7, 0.7, 0.7, 1)
            iconModels.detachNode()
        elif pageName == TTLocalizer.NPCFriendPageTitle:
            iconModels = loader.loadModel('phase_3.5/models/gui/playingCard')
            iconImage = iconModels.find('**/card_back')
            iconGeom = iconModels.find('**/logo')
            iconScale = 0.22
            iconModels.detachNode()
        elif pageName == TTLocalizer.KartPageTitle:
            iconModels = loader.loadModel('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/kartIcon')
            iconModels.detachNode()
        elif pageName == TTLocalizer.GolfPageTitle:
            iconModels = loader.loadModel('phase_6/models/golf/golf_gui')
            iconGeom = iconModels.find('**/score_card_icon')
            iconModels.detachNode()
        elif pageName == TTLocalizer.EventsPageName:
            iconModels = loader.loadModel('phase_4/models/parties/partyStickerbook')
            iconGeom = iconModels.find('**/Stickerbook_PartyIcon')
            iconModels.detachNode()
        elif pageName == TTLocalizer.PhotoPageTitle:
            iconGeom = iconModels = loader.loadModel('phase_4/models/minigames/photogame_filmroll')
            iconScale = (1.9, 1.5, 1.5)
            iconModels.detachNode()
        elif pageName == TTLocalizer.StatPageTitle:
            iconGeom = iconModels = loader.loadModel('phase_3.5/models/gui/name_star')
            iconColor = (0, 0.6, 1, 1)
            iconModels.detachNode()
        if pageName == TTLocalizer.OptionsPageTitle:
            pageName = TTLocalizer.OptionsTabTitle
        rightSide = pageIndex < 16
        pageTab = DirectButton(parent=self.pageTabFrames[rightSide], relief=DGG.RAISED, frameSize=(-0.575,
         0.575,
         -0.575,
         0.575), borderWidth=(0.05, 0.05), text=('',
         '',
         pageName,
         ''), text_align=TextNode.ALeft, text_pos=(1 if rightSide else -4, -0.2), text_scale=TTLocalizer.SBpageTab, text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), image=iconImage, image_scale=iconScale, geom=iconGeom, geom_scale=iconScale, geom_color=iconColor, pos=(0, 0, -yOffset), scale=0.06, command=buttonPressedCommand, extraArgs=extraArgs)
        self.pageTabs.insert(pageIndex, pageTab)
        return

    def setPage(self, page, enterPage = True):
        if self.currPageIndex is not None:
            self.pages[self.currPageIndex].exit()
        self.currPageIndex = self.pages.index(page)
        self.setPageTabIndex(self.currPageIndex)
        if enterPage:
            self.showPageArrows()
            page.enter()
        return

    def setPageTabIndex(self, pageTabIndex):
        if self.currPageTabIndex is not None and pageTabIndex != self.currPageTabIndex:
            self.pageTabs[self.currPageTabIndex]['relief'] = DGG.RAISED
        self.currPageTabIndex = pageTabIndex
        self.pageTabs[self.currPageTabIndex]['relief'] = DGG.SUNKEN
        return

    def isOnPage(self, page):
        result = False
        if self.currPageIndex is not None:
            curPage = self.pages[self.currPageIndex]
            if curPage == page:
                result = True
        return result

    def obscureButton(self, obscured):
        self.__obscured = obscured
        self.__setButtonVisibility()

    def isObscured(self):
        return self.__obscured

    def showButton(self):
        self.__shown = 1
        self.__setButtonVisibility()

    def hideButton(self):
        self.__shown = 0
        self.__setButtonVisibility()

    def __setButtonVisibility(self):
        if self.__isOpen:
            self.bookOpenButton.hide()
            self.bookCloseButton.show()
        elif self.__shown and not self.__obscured:
            self.bookOpenButton.show()
            self.bookCloseButton.hide()
        else:
            self.bookOpenButton.hide()
            self.bookCloseButton.hide()

    def shouldBookButtonBeHidden(self):
        result = False
        if self.__isOpen:
            pass
        elif self.__shown and not self.__obscured:
            pass
        else:
            result = True
        return result

    def __open(self):
        messenger.send('enterStickerBook')
        if not localAvatar.getGardenStarted():
            for tab in self.pageTabs:
                if tab['text'][2] == TTLocalizer.GardenPageTitle:
                    tab.hide()

    def __close(self):
        base.playSfx(self.closeSound)
        self.doneStatus = {'mode': 'close'}
        messenger.send('exitStickerBook')
        messenger.send(self.doneEvent)

    def closeBook(self):
        self.__close()

    def __pageDone(self):
        page = self.pages[self.currPageIndex]
        pageDoneStatus = page.getDoneStatus()
        if pageDoneStatus:
            if pageDoneStatus['mode'] == 'close':
                self.__close()
            else:
                self.doneStatus = pageDoneStatus
                messenger.send(self.doneEvent)

    def __pageChange(self, offset):
        messenger.send('wakeup')
        base.playSfx(self.pageSound)
        self.pages[self.currPageIndex].exit()
        self.currPageIndex = self.currPageIndex + offset
        messenger.send('stickerBookPageChange-' + str(self.currPageIndex))
        self.currPageIndex = max(self.currPageIndex, 0)
        self.currPageIndex = min(self.currPageIndex, len(self.pages) - 1)
        self.setPageTabIndex(self.currPageIndex)
        self.showPageArrows()
        page = self.pages[self.currPageIndex]
        page.enter()

    def showPageArrows(self):
        if self.currPageIndex == len(self.pages) - 1:
            self.prevArrow.show()
            self.nextArrow.hide()
        else:
            self.prevArrow.show()
            self.nextArrow.show()
        self.__checkForPage()
        if self.currPageIndex == 0:
            self.prevArrow.hide()
            self.nextArrow.show()

    def __checkForPage(self):
        self.accept('arrow_right', self.__pageChange, [1])
        self.accept('arrow_left', self.__pageChange, [-1])

    def disableBookCloseButton(self):
        if self.bookCloseButton:
            self.bookCloseButton['command'] = None
        return

    def enableBookCloseButton(self):
        if self.bookCloseButton:
            self.bookCloseButton['command'] = self.__close

    def disableAllPageTabs(self):
        for button in self.pageTabs:
            button['state'] = DGG.DISABLED

    def enableAllPageTabs(self):
        for button in self.pageTabs:
            button['state'] = DGG.NORMAL

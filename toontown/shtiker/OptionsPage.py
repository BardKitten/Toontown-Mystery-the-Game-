from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import *
from direct.showbase import PythonUtil
from direct.task import Task
from panda3d.core import *

import DisplaySettingsDialog
import ShtikerPage
import OptionChooser
from otp.speedchat import SCColorScheme
from otp.speedchat import SCStaticTextTerminal
from otp.speedchat import SpeedChat
from toontown.toonbase import TTLocalizer, ToontownGlobals
from toontown.toon import Toon
from toontown.toontowngui import TTDialog
import webbrowser


speedChatStyles = (
    (
        2000,
        (200 / 255.0, 60 / 255.0, 229 / 255.0),
        (200 / 255.0, 135 / 255.0, 255 / 255.0),
        (220 / 255.0, 195 / 255.0, 229 / 255.0)
    ),
    (
        2012,
        (142 / 255.0, 151 / 255.0, 230 / 255.0),
        (173 / 255.0, 180 / 255.0, 237 / 255.0),
        (220 / 255.0, 195 / 255.0, 229 / 255.0)
    ),
    (
        2001,
        (0 / 255.0, 0 / 255.0, 255 / 255.0),
        (140 / 255.0, 150 / 255.0, 235 / 255.0),
        (201 / 255.0, 215 / 255.0, 255 / 255.0)
    ),
    (
        2010,
        (0 / 255.0, 119 / 255.0, 190 / 255.0),
        (53 / 255.0, 180 / 255.0, 255 / 255.0),
        (201 / 255.0, 215 / 255.0, 255 / 255.0)
    ),
    (
        2014,
        (0 / 255.0, 64 / 255.0, 128 / 255.0),
        (0 / 255.0, 64 / 255.0, 128 / 255.0),
        (201 / 255.0, 215 / 255.0, 255 / 255.0)
    ),
    (
        2002,
        (90 / 255.0, 175 / 255.0, 225 / 255.0),
        (120 / 255.0, 215 / 255.0, 255 / 255.0),
        (208 / 255.0, 230 / 255.0, 250 / 255.0)
    ),
    (
        2003,
        (130 / 255.0, 235 / 255.0, 235 / 255.0),
        (120 / 255.0, 225 / 255.0, 225 / 255.0),
        (234 / 255.0, 255 / 255.0, 255 / 255.0)
    ),
    (
        2004,
        (0 / 255.0, 200 / 255.0, 70 / 255.0),
        (0 / 255.0, 200 / 255.0, 80 / 255.0),
        (204 / 255.0, 255 / 255.0, 204 / 255.0)
    ),
    (
        2015,
        (13 / 255.0, 255 / 255.0, 100 / 255.0),
        (64 / 255.0, 255 / 255.0, 131 / 255.0),
        (204 / 255.0, 255 / 255.0, 204 / 255.0)
    ),
    (
        2005,
        (235 / 255.0, 230 / 255.0, 0 / 255.0),
        (255 / 255.0, 250 / 255.0, 100 / 255.0),
        (255 / 255.0, 250 / 255.0, 204 / 255.0)
    ),
    (
        2006,
        (255 / 255.0, 153 / 255.0, 0 / 255.0),
        (229 / 255.0, 147 / 255.0, 0 / 255.0),
        (255 / 255.0, 234 / 255.0, 204 / 255.0)
    ),
    (
        2011,
        (255 / 255.0, 177 / 255.0, 62 / 255.0),
        (255 / 255.0, 200 / 255.0, 117 / 255.0),
        (255 / 255.0, 234 / 255.0, 204 / 255.0)
    ),
    (
        2007,
        (255 / 255.0, 0 / 255.0, 50 / 255.0),
        (229 / 255.0, 0 / 255.0, 50 / 255.0),
        (255 / 255.0, 204 / 255.0, 204 / 255.0)
    ),
    (
        2013,
        (130 / 255.0, 0 / 255.0, 26 / 255.0),
        (179 / 255.0, 0 / 255.0, 50 / 255.0),
        (255 / 255.0, 204 / 255.0, 204 / 255.0)
    ),
    (
        2016,
        (176 / 255.0, 35 / 255.0, 0 / 255.0),
        (240 / 255.0, 48 / 255.0, 0 / 255.0),
        (255 / 255.0, 204 / 255.0, 204 / 255.0)
    ),
    (
        2008,
        (255 / 255.0, 153 / 255.0, 193 / 255.0),
        (240 / 255.0, 157 / 255.0, 192 / 255.0),
        (255 / 255.0, 215 / 255.0, 238 / 255.0)
    ),
    (
        2009,
        (170 / 255.0, 120 / 255.0, 20 / 255.0),
        (165 / 255.0, 120 / 255.0, 50 / 255.0),
        (210 / 255.0, 200 / 255.0, 180 / 255.0)
    )
)
PageMode = PythonUtil.Enum('Options, Codes, Extra')


class OptionsPage(ShtikerPage.ShtikerPage):
    notify = directNotify.newCategory('OptionsPage')

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

        self.optionsTabPage = None
        self.codesTabPage = None
        self.extraOptionsTabPage = None
        self.title = None
        self.optionsTab = None
        self.codesTab = None
        self.extraOptionsTab = None

    def load(self):
        ShtikerPage.ShtikerPage.load(self)

        self.optionsTabPage = OptionsTabPage(self)
        self.optionsTabPage.hide()
        self.codesTabPage = CodesTabPage(self)
        self.codesTabPage.hide()
        self.extraOptionsTabPage = ExtraOptionsTabPage(self)
        self.extraOptionsTabPage.hide()

        self.title = DirectLabel(
            parent=self, relief=None, text=TTLocalizer.OptionsPageTitle,
            text_scale=0.12, pos=(0, 0, 0.61))

        gui = loader.loadModel('phase_3.5/models/gui/fishingBook.bam')
        normalColor = (1, 1, 1, 1)
        clickColor = (0.8, 0.8, 0, 1)
        rolloverColor = (0.15, 0.82, 1.0, 1)
        diabledColor = (1.0, 0.98, 0.15, 1)
        self.optionsTab = DirectButton(
            parent=self, relief=None, text=TTLocalizer.OptionsPageTitle,
            text_scale=TTLocalizer.OPoptionsTab, text_align=TextNode.ALeft,
            text_pos=(0.01, 0.0, 0.0), image=gui.find('**/tabs/polySurface1'),
            image_pos=(0.55, 1, -0.91), image_hpr=(0, 0, -90),
            image_scale=(0.033, 0.033, 0.035), image_color=normalColor,
            image1_color=clickColor, image2_color=rolloverColor,
            image3_color=diabledColor, text_fg=Vec4(0.2, 0.1, 0, 1),
            command=self.setMode, extraArgs=[PageMode.Options],
            pos=(-0.64, 0, 0.77))
        self.codesTab = DirectButton(
            parent=self, relief=None, text=TTLocalizer.OptionsPageCodesTab,
            text_scale=TTLocalizer.OPoptionsTab, text_align=TextNode.ALeft,
            text_pos=(-0.035, 0.0, 0.0),
            image=gui.find('**/tabs/polySurface2'), image_pos=(0.12, 1, -0.91),
            image_hpr=(0, 0, -90), image_scale=(0.033, 0.033, 0.035),
            image_color=normalColor, image1_color=clickColor,
            image2_color=rolloverColor, image3_color=diabledColor,
            text_fg=Vec4(0.2, 0.1, 0, 1), command=self.setMode,
            extraArgs=[PageMode.Codes], pos=(-0.12, 0, 0.77))
        self.extraOptionsTab = DirectButton(
            parent=self, relief=None, text=TTLocalizer.ExtraOptionsPageTitle,
            text_scale=TTLocalizer.OPextraOptionsTab, text_align=TextNode.ALeft,
            text_pos=(0.027, 0.0, 0.0),
            image=gui.find('**/tabs/polySurface2'), image_pos=(0.12, 1, -0.91),
            image_hpr=(0, 0, -90), image_scale=(0.033, 0.033, 0.035),
            image_color=normalColor, image1_color=clickColor,
            image2_color=rolloverColor, image3_color=diabledColor,
            text_fg=Vec4(0.2, 0.1, 0, 1), command=self.setMode,
            extraArgs=[PageMode.Extra], pos=(0.42, 0, 0.77))
        gui.removeNode()

    def enter(self):
        self.setMode(PageMode.Options, updateAnyways=1)

        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        self.optionsTabPage.exit()
        self.codesTabPage.exit()
        self.extraOptionsTabPage.exit()
        
        ShtikerPage.ShtikerPage.exit(self)

    def unload(self):
        if self.optionsTabPage is not None:
            self.optionsTabPage.unload()
            self.optionsTabPage = None

        if self.codesTabPage is not None:
            self.codesTabPage.unload()
            self.codesTabPage = None

        if self.title is not None:
            self.title.destroy()
            self.title = None

        if self.optionsTab is not None:
            self.optionsTab.destroy()
            self.optionsTab = None

        if self.codesTab is not None:
            self.codesTab.destroy()
            self.codesTab = None
        
        if self.extraOptionsTab is not None:
            self.extraOptionsTab.destroy()
            self.extraOptionsTab = None

        ShtikerPage.ShtikerPage.unload(self)

    def setMode(self, mode, updateAnyways=0):
        messenger.send('wakeup')

        if not updateAnyways:
            if self.mode == mode:
                return

        self.mode = mode

        if mode == PageMode.Options:
            self.title['text'] = TTLocalizer.OptionsPageTitle
            self.optionsTab['state'] = DGG.DISABLED
            self.optionsTabPage.enter()
            self.codesTab['state'] = DGG.NORMAL
            self.codesTabPage.exit()
            self.extraOptionsTab['state'] = DGG.NORMAL
            self.extraOptionsTabPage.exit()
        elif mode == PageMode.Codes:
            self.title['text'] = TTLocalizer.CdrPageTitle
            self.optionsTab['state'] = DGG.NORMAL
            self.optionsTabPage.exit()
            self.extraOptionsTab['state'] = DGG.NORMAL
            self.extraOptionsTabPage.exit()
            self.codesTab['state'] = DGG.DISABLED
            self.codesTabPage.enter()
        elif mode == PageMode.Extra:
            self.title['text'] = TTLocalizer.ExtraOptionsPageTitle
            self.optionsTab['state'] = DGG.NORMAL
            self.optionsTabPage.exit()
            self.codesTab['state'] = DGG.NORMAL
            self.codesTabPage.exit()
            self.extraOptionsTab['state'] = DGG.DISABLED
            self.extraOptionsTabPage.enter()

class OptionsTabPage(DirectFrame):
    notify = directNotify.newCategory('OptionsTabPage')
    DisplaySettingsTaskName = 'save-display-settings'
    DisplaySettingsDelay = 60
    ChangeDisplaySettings = base.config.GetBool('change-display-settings', 1)
    ChangeDisplayAPI = base.config.GetBool('change-display-api', 0)

    def __init__(self, parent = aspect2d):
        self.parent = parent
        self.currentSizeIndex = None

        DirectFrame.__init__(self, parent=self.parent, relief=None, pos=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0))

        self.load()

    def destroy(self):
        self.parent = None

        DirectFrame.destroy(self)

    def load(self):
        self.displaySettings = None
        self.displaySettingsChanged = 0
        self.displaySettingsSize = (None, None)
        self.displaySettingsFullscreen = None
        self.displaySettingsApi = None
        self.displaySettingsApiChanged = 0
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        circleModel = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_nameShop')
        titleHeight = 0.61
        textStartHeight = 0.45
        textRowHeight = 0.145
        leftMargin = -0.72
        buttonbase_xcoord = 0.35
        buttonbase_ycoord = 0.45
        button_image_scale = (0.7, 1, 1)
        button_textpos = (0, -0.02)
        options_text_scale = 0.052
        disabled_arrow_color = Vec4(0.6, 0.6, 0.6, 1.0)
        self.speed_chat_scale = 0.055
        self.Music_Label = DirectLabel(parent=self, relief=None, text=TTLocalizer.OptionsPageMusic, text_align=TextNode.ALeft, text_scale=options_text_scale, pos=(leftMargin, 0, textStartHeight))
        self.SoundFX_Label = DirectLabel(parent=self, relief=None, text=TTLocalizer.OptionsPageSFX, text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - textRowHeight))
        self.Friends_Label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 3 * textRowHeight))
        self.Whispers_Label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 4 * textRowHeight))
        self.DisplaySettings_Label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=10, pos=(leftMargin, 0, textStartHeight - 5 * textRowHeight))
        self.SpeedChatStyle_Label = DirectLabel(parent=self, relief=None, text=TTLocalizer.OptionsPageSpeedChatStyleLabel, text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=10, pos=(leftMargin, 0, textStartHeight - 6 * textRowHeight))
        self.ToonChatSounds_Label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=15, pos=(leftMargin, 0, textStartHeight - 2 * textRowHeight + 0.025))
        self.ToonChatSounds_Label.setScale(0.9)
        self.Music_toggleSlider = DirectSlider(parent=self, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord),
                                               value=settings['musicVol']*100, pageSize=5, range=(0, 100), command=self.__doMusicLevel,
                                               thumb_geom=(circleModel.find('**/tt_t_gui_mat_namePanelCircle')), thumb_relief=None, thumb_geom_scale=2)
        self.Music_toggleSlider.setScale(0.25)
        self.SoundFX_toggleSlider = DirectSlider(parent=self, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight),
                                               value=settings['sfxVol']*100, pageSize=5, range=(0, 100), command=self.__doSfxLevel,
                                               thumb_geom=(circleModel.find('**/tt_t_gui_mat_namePanelCircle')), thumb_relief=None, thumb_geom_scale=2)
        self.SoundFX_toggleSlider.setScale(0.25)
        self.Friends_toggleButton = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 3), command=self.__doToggleAcceptFriends)
        self.Whispers_toggleButton = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 4), command=self.__doToggleAcceptWhispers)
        self.DisplaySettingsButton = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image3_color=Vec4(0.5, 0.5, 0.5, 0.5), image_scale=button_image_scale, text=TTLocalizer.OptionsPageChange, text3_fg=(0.5, 0.5, 0.5, 0.75), text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 5), command=self.__doDisplaySettings)
        self.speedChatStyleLeftArrow = DirectButton(parent=self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), image3_color=Vec4(1, 1, 1, 0.5), scale=(-1.0, 1.0, 1.0), pos=(0.25, 0, buttonbase_ycoord - textRowHeight * 6), command=self.__doSpeedChatStyleLeft)
        self.speedChatStyleRightArrow = DirectButton(parent=self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), image3_color=Vec4(1, 1, 1, 0.5), pos=(0.65, 0, buttonbase_ycoord - textRowHeight * 6), command=self.__doSpeedChatStyleRight)
        self.ToonChatSounds_toggleButton = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'),
         guiButton.find('**/QuitBtn_DN'),
         guiButton.find('**/QuitBtn_RLVR'),
         guiButton.find('**/QuitBtn_UP')), image3_color=Vec4(0.5, 0.5, 0.5, 0.5), image_scale=button_image_scale, text='', text3_fg=(0.5, 0.5, 0.5, 0.75), text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 2 + 0.025), command=self.__doToggleToonChatSounds)
        self.ToonChatSounds_toggleButton.setScale(0.8)
        self.speedChatStyleText = SpeedChat.SpeedChat(name='OptionsPageStyleText', structure=[2000], backgroundModelName='phase_3/models/gui/ChatPanel', guiModelName='phase_3.5/models/gui/speedChatGui')
        self.speedChatStyleText.setScale(self.speed_chat_scale)
        self.speedChatStyleText.setPos(0.37, 0, buttonbase_ycoord - textRowHeight * 6 + 0.03)
        self.speedChatStyleText.reparentTo(self, DGG.FOREGROUND_SORT_INDEX)
        self.exitButton = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=1.15, text=TTLocalizer.OptionsPageExitToontown, text_scale=options_text_scale, text_pos=button_textpos, textMayChange=0, pos=(0.45, 0, -0.6), command=self.__handleExitShowWithConfirm)
        guiButton.removeNode()
        gui.removeNode()

    def enter(self):
        self.show()
        taskMgr.remove(self.DisplaySettingsTaskName)
        self.settingsChanged = 0
        self.__setAcceptFriendsButton()
        self.__setAcceptWhispersButton()
        self.__setDisplaySettings()
        self.__setToonChatSoundsButton()
        self.speedChatStyleText.enter()
        self.speedChatStyleIndex = base.localAvatar.getSpeedChatStyleIndex()
        self.updateSpeedChatStyle()
        if self.parent.book.safeMode:
            self.exitButton.hide()
        else:
            self.exitButton.show()

    def exit(self):
        self.ignore('confirmDone')
        self.hide()
        self.speedChatStyleText.exit()
        if self.displaySettingsChanged:
            taskMgr.doMethodLater(self.DisplaySettingsDelay, self.writeDisplaySettings, self.DisplaySettingsTaskName)

    def unload(self):
        self.writeDisplaySettings()
        taskMgr.remove(self.DisplaySettingsTaskName)
        if self.displaySettings != None:
            self.ignore(self.displaySettings.doneEvent)
            self.displaySettings.unload()
        self.displaySettings = None
        self.exitButton.destroy()
        self.Music_toggleSlider.destroy()
        self.SoundFX_toggleSlider.destroy()
        self.Friends_toggleButton.destroy()
        self.Whispers_toggleButton.destroy()
        self.DisplaySettingsButton.destroy()
        self.speedChatStyleLeftArrow.destroy()
        self.speedChatStyleRightArrow.destroy()
        del self.exitButton
        del self.SoundFX_Label
        del self.Music_Label
        del self.Friends_Label
        del self.Whispers_Label
        del self.SpeedChatStyle_Label
        del self.SoundFX_toggleSlider
        del self.Music_toggleSlider
        del self.Friends_toggleButton
        del self.Whispers_toggleButton
        del self.speedChatStyleLeftArrow
        del self.speedChatStyleRightArrow
        self.speedChatStyleText.exit()
        self.speedChatStyleText.destroy()
        del self.speedChatStyleText
        self.currentSizeIndex = None

    def __doMusicLevel(self):
        vol = self.Music_toggleSlider['value']
        vol = float(vol) / 100
        settings['musicVol'] = vol
        base.musicManager.setVolume(vol)
        base.musicActive = vol > 0.0

    def __doSfxLevel(self):
        vol = self.SoundFX_toggleSlider['value']
        vol = float(vol) / 100
        settings['sfxVol'] = vol
        for sfm in base.sfxManagerList:
            sfm.setVolume(vol)
        base.sfxActive = vol > 0.0
        self.__setToonChatSoundsButton()

    def __doToggleToonChatSounds(self):
        messenger.send('wakeup')
        if base.toonChatSounds:
            base.toonChatSounds = 0
            settings['toonChatSounds'] = False
        else:
            base.toonChatSounds = 1
            settings['toonChatSounds'] = True
        self.settingsChanged = 1
        self.__setToonChatSoundsButton()

    def __setToonChatSoundsButton(self):
        if base.toonChatSounds:
            self.ToonChatSounds_Label['text'] = TTLocalizer.OptionsPageToonChatSoundsOnLabel
            self.ToonChatSounds_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff
        else:
            self.ToonChatSounds_Label['text'] = TTLocalizer.OptionsPageToonChatSoundsOffLabel
            self.ToonChatSounds_toggleButton['text'] = TTLocalizer.OptionsPageToggleOn
        if base.sfxActive:
            self.ToonChatSounds_Label.setColorScale(1.0, 1.0, 1.0, 1.0)
            self.ToonChatSounds_toggleButton['state'] = DGG.NORMAL
        else:
            self.ToonChatSounds_Label.setColorScale(0.5, 0.5, 0.5, 0.5)
            self.ToonChatSounds_toggleButton['state'] = DGG.DISABLED

    def __doToggleAcceptFriends(self):
        messenger.send('wakeup')
        acceptingNewFriends = settings.get('acceptingNewFriends', {})
        if base.localAvatar.acceptingNewFriends:
            base.localAvatar.acceptingNewFriends = 0
            acceptingNewFriends[str(base.localAvatar.doId)] = False
        else:
            base.localAvatar.acceptingNewFriends = 1
            acceptingNewFriends[str(base.localAvatar.doId)] = True
        settings['acceptingNewFriends'] = acceptingNewFriends
        self.settingsChanged = 1
        self.__setAcceptFriendsButton()

    def __doToggleAcceptWhispers(self):
        messenger.send('wakeup')
        acceptingNonFriendWhispers = settings.get('acceptingNonFriendWhispers', {})
        if base.localAvatar.acceptingNonFriendWhispers:
            base.localAvatar.acceptingNonFriendWhispers = 0
            acceptingNonFriendWhispers[str(base.localAvatar.doId)] = False
        else:
            base.localAvatar.acceptingNonFriendWhispers = 1
            acceptingNonFriendWhispers[str(base.localAvatar.doId)] = True
        settings['acceptingNonFriendWhispers'] = acceptingNonFriendWhispers
        self.settingsChanged = 1
        self.__setAcceptWhispersButton()

    def __setAcceptFriendsButton(self):
        if base.localAvatar.acceptingNewFriends:
            self.Friends_Label['text'] = TTLocalizer.OptionsPageFriendsEnabledLabel
            self.Friends_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff
        else:
            self.Friends_Label['text'] = TTLocalizer.OptionsPageFriendsDisabledLabel
            self.Friends_toggleButton['text'] = TTLocalizer.OptionsPageToggleOn

    def __setAcceptWhispersButton(self):
        if base.localAvatar.acceptingNonFriendWhispers:
            self.Whispers_Label['text'] = TTLocalizer.OptionsPageWhisperEnabledLabel
            self.Whispers_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff
        else:
            self.Whispers_Label['text'] = TTLocalizer.OptionsPageWhisperDisabledLabel
            self.Whispers_toggleButton['text'] = TTLocalizer.OptionsPageToggleOn

    def __doDisplaySettings(self):
        if self.displaySettings == None:
            self.displaySettings = DisplaySettingsDialog.DisplaySettingsDialog()
            self.displaySettings.load()
            self.accept(self.displaySettings.doneEvent, self.__doneDisplaySettings)
        self.displaySettings.enter(self.ChangeDisplaySettings, self.ChangeDisplayAPI)

    def __doneDisplaySettings(self, anyChanged, apiChanged):
        if anyChanged:
            self.__setDisplaySettings()
            properties = base.win.getProperties()
            self.displaySettingsChanged = 1
            self.displaySettingsSize = (properties.getXSize(), properties.getYSize())
            self.displaySettingsFullscreen = properties.getFullscreen()
            self.displaySettingsApi = base.pipe.getInterfaceName()
            self.displaySettingsApiChanged = apiChanged

    def __setDisplaySettings(self):
        properties = base.win.getProperties()
        if properties.getFullscreen():
            screensize = '%s x %s' % (properties.getXSize(), properties.getYSize())
        else:
            screensize = TTLocalizer.OptionsPageDisplayWindowed
        api = base.pipe.getInterfaceName()
        settings = {'screensize': screensize,
         'api': api}
        if self.ChangeDisplayAPI:
            OptionsPage.notify.debug('change display settings...')
            text = TTLocalizer.OptionsPageDisplaySettings % settings
        else:
            OptionsPage.notify.debug('no change display settings...')
            text = TTLocalizer.OptionsPageDisplaySettingsNoApi % settings
        self.DisplaySettings_Label['text'] = text

    def __doSpeedChatStyleLeft(self):
        if self.speedChatStyleIndex > 0:
            self.speedChatStyleIndex = self.speedChatStyleIndex - 1
            self.updateSpeedChatStyle()

    def __doSpeedChatStyleRight(self):
        if self.speedChatStyleIndex < len(speedChatStyles) - 1:
            self.speedChatStyleIndex = self.speedChatStyleIndex + 1
            self.updateSpeedChatStyle()

    def updateSpeedChatStyle(self):
        nameKey, arrowColor, rolloverColor, frameColor = speedChatStyles[self.speedChatStyleIndex]
        newSCColorScheme = SCColorScheme.SCColorScheme(arrowColor=arrowColor, rolloverColor=rolloverColor, frameColor=frameColor)
        self.speedChatStyleText.setColorScheme(newSCColorScheme)
        self.speedChatStyleText.clearMenu()
        colorName = SCStaticTextTerminal.SCStaticTextTerminal(nameKey)
        self.speedChatStyleText.append(colorName)
        self.speedChatStyleText.finalize()
        self.speedChatStyleText.setPos(0.445 - self.speedChatStyleText.getWidth() * self.speed_chat_scale / 2, 0, self.speedChatStyleText.getPos()[2])
        if self.speedChatStyleIndex > 0:
            self.speedChatStyleLeftArrow['state'] = DGG.NORMAL
        else:
            self.speedChatStyleLeftArrow['state'] = DGG.DISABLED
        if self.speedChatStyleIndex < len(speedChatStyles) - 1:
            self.speedChatStyleRightArrow['state'] = DGG.NORMAL
        else:
            self.speedChatStyleRightArrow['state'] = DGG.DISABLED
        base.localAvatar.b_setSpeedChatStyleIndex(self.speedChatStyleIndex)

    def writeDisplaySettings(self, task=None):
        if not self.displaySettingsChanged:
            return
        taskMgr.remove(self.DisplaySettingsTaskName)
        settings['res'] = (self.displaySettingsSize[0], self.displaySettingsSize[1])
        settings['fullscreen'] = self.displaySettingsFullscreen
        return Task.done

    def __handleExitShowWithConfirm(self):
        self.confirm = TTDialog.TTGlobalDialog(doneEvent='confirmDone', message=TTLocalizer.OptionsPageExitConfirm, style=TTDialog.TwoChoice)
        self.confirm.show()
        self.parent.doneStatus = {'mode': 'exit',
         'exitTo': 'closeShard'}
        self.accept('confirmDone', self.__handleConfirm)

    def __handleConfirm(self):
        status = self.confirm.doneStatus
        self.ignore('confirmDone')
        self.confirm.cleanup()
        del self.confirm
        if status == 'ok':
            base.cr._userLoggingOut = True
            messenger.send(self.parent.doneEvent)


class CodesTabPage(DirectFrame):
    notify = directNotify.newCategory('CodesTabPage')

    def __init__(self, parent = aspect2d):
        self.parent = parent
        DirectFrame.__init__(self, parent=self.parent, relief=None, pos=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0))
        self.load()
        return

    def destroy(self):
        self.parent = None
        DirectFrame.destroy(self)
        return

    def load(self):
        self.notice = DirectLabel(parent=self, relief=None, text='NOTICE: All codes can only be entered once!', text_scale=0.06, pos=(0.0, 0, 0.53), text_fg=Vec4(1.0, 0, 0, 1))
        cdrGui = loader.loadModel('phase_3.5/models/gui/tt_m_gui_sbk_codeRedemptionGui')
        instructionGui = cdrGui.find('**/tt_t_gui_sbk_cdrPresent')
        flippyGui = cdrGui.find('**/tt_t_gui_sbk_cdrFlippy')
        codeBoxGui = cdrGui.find('**/tt_t_gui_sbk_cdrCodeBox')
        self.resultPanelSuccessGui = cdrGui.find('**/tt_t_gui_sbk_cdrResultPanel_success')
        self.resultPanelFailureGui = cdrGui.find('**/tt_t_gui_sbk_cdrResultPanel_failure')
        self.resultPanelErrorGui = cdrGui.find('**/tt_t_gui_sbk_cdrResultPanel_error')
        self.successSfx = base.loadSfx('phase_3.5/audio/sfx/tt_s_gui_sbk_cdrSuccess.ogg')
        self.failureSfx = base.loadSfx('phase_3.5/audio/sfx/tt_s_gui_sbk_cdrFailure.ogg')
        self.instructionPanel = DirectFrame(parent=self, relief=None, image=instructionGui, image_scale=0.8, text=TTLocalizer.CdrInstructions, text_pos=TTLocalizer.OPCodesInstructionPanelTextPos, text_align=TextNode.ACenter, text_scale=TTLocalizer.OPCodesResultPanelTextScale, text_wordwrap=TTLocalizer.OPCodesInstructionPanelTextWordWrap, pos=(-0.429, 0, -0.05))
        self.codeBox = DirectFrame(parent=self, relief=None, image=codeBoxGui, pos=(0.433, 0, 0.35))
        self.flippyFrame = DirectFrame(parent=self, relief=None, image=flippyGui, pos=(0.44, 0, -0.353))
        self.codeInput = DirectEntry(parent=self.codeBox, relief=DGG.GROOVE, scale=0.08, pos=(-0.33, 0, -0.006), borderWidth=(0.05, 0.05), frameColor=((1, 1, 1, 1), (1, 1, 1, 1), (0.5, 0.5, 0.5, 0.5)), state=DGG.NORMAL, text_align=TextNode.ALeft, text_scale=TTLocalizer.OPCodesInputTextScale, width=10.5, numLines=1, focus=1, backgroundFocus=0, cursorKeys=1, text_fg=(0, 0, 0, 1), suppressMouse=1, autoCapitalize=0, command=self.__submitCode)
        submitButtonGui = loader.loadModel('phase_3/models/gui/quit_button')
        self.submitButton = DirectButton(parent=self, relief=None, image=(submitButtonGui.find('**/QuitBtn_UP'),
         submitButtonGui.find('**/QuitBtn_DN'),
         submitButtonGui.find('**/QuitBtn_RLVR'),
         submitButtonGui.find('**/QuitBtn_UP')), image3_color=Vec4(0.5, 0.5, 0.5, 0.5), image_scale=1.15, state=DGG.NORMAL, text=TTLocalizer.NameShopSubmitButton, text_scale=TTLocalizer.OPCodesSubmitTextScale, text_align=TextNode.ACenter, text_pos=TTLocalizer.OPCodesSubmitTextPos, text3_fg=(0.5, 0.5, 0.5, 0.75), textMayChange=0, pos=(0.45, 0.0, 0.0896), command=self.__submitCode)
        self.resultPanel = DirectFrame(parent=self, relief=None, image=self.resultPanelSuccessGui, text='', text_pos=TTLocalizer.OPCodesResultPanelTextPos, text_align=TextNode.ACenter, text_scale=TTLocalizer.OPCodesResultPanelTextScale, text_wordwrap=TTLocalizer.OPCodesResultPanelTextWordWrap, pos=(-0.42, 0, -0.0567))
        self.resultPanel.hide()
        closeButtonGui = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        self.closeButton = DirectButton(parent=self.resultPanel, pos=(0.296, 0, -0.466), relief=None, state=DGG.NORMAL, image=(closeButtonGui.find('**/CloseBtn_UP'), closeButtonGui.find('**/CloseBtn_DN'), closeButtonGui.find('**/CloseBtn_Rllvr')), image_scale=(1, 1, 1), command=self.__hideResultPanel)
        closeButtonGui.removeNode()
        cdrGui.removeNode()
        submitButtonGui.removeNode()
        return

    def enter(self):
        self.show()
        localAvatar.chatMgr.fsm.request('otherDialog')
        self.codeInput['focus'] = 1
        self.codeInput.enterText('')
        self.__enableCodeEntry()

    def exit(self):
        self.resultPanel.hide()
        self.hide()
        localAvatar.chatMgr.fsm.request('mainMenu')

    def unload(self):
        self.instructionPanel.destroy()
        self.instructionPanel = None
        self.codeBox.destroy()
        self.codeBox = None
        self.flippyFrame.destroy()
        self.flippyFrame = None
        self.codeInput.destroy()
        self.codeInput = None
        self.submitButton.destroy()
        self.submitButton = None
        self.resultPanel.destroy()
        self.resultPanel = None
        self.closeButton.destroy()
        self.closeButton = None
        del self.successSfx
        del self.failureSfx
        return

    def __submitCode(self, input = None):
        if input == None:
            input = self.codeInput.get()
        self.codeInput['focus'] = 1
        if input == '':
            return
        messenger.send('wakeup')
        if hasattr(base.cr, 'codeRedemptionMgr'):
            base.cr.codeRedemptionMgr.redeemCode(input, self.__getCodeResult)
        self.codeInput.enterText('')
        self.__disableCodeEntry()
        return

    def __getCodeResult(self, result):
        self.notify.debug('result = %s' % result)
        self.__enableCodeEntry()
        if result == 0:
            self.resultPanel['image'] = self.resultPanelSuccessGui
            self.resultPanel['text'] = TTLocalizer.CdrResultSuccess
        elif result == 1:
            self.resultPanel['image'] = self.resultPanelFailureGui
            self.resultPanel['text'] = TTLocalizer.CdrResultInvalidCode
        elif result == 2:
            self.resultPanel['image'] = self.resultPanelFailureGui
            self.resultPanel['text'] = TTLocalizer.CdrResultExpiredCode
        elif result == 3:
            self.resultPanel['image'] = self.resultPanelErrorGui
        elif result == 4:
            self.resultPanel['image'] = self.resultPanelErrorGui
            self.resultPanel['text'] = TTLocalizer.CdrResultAlreadyRedeemed
        elif result == 5:
            self.resultPanel['image'] = self.resultPanelErrorGui
            self.resultPanel['text'] = TTLocalizer.CdrResultNotReady
        elif result == 6:
            self.resultPanel['image'] = self.resultPanelErrorGui
            self.resultPanel['text'] = TTLocalizer.CdrResultNotEligible
        if result == 0:
            self.successSfx.play()
        else:
            self.failureSfx.play()
        self.resultPanel.show()

    def __hideResultPanel(self):
        self.resultPanel.hide()

    def __disableCodeEntry(self):
        self.codeInput['state'] = DGG.DISABLED
        self.submitButton['state'] = DGG.DISABLED

    def __enableCodeEntry(self):
        self.codeInput['state'] = DGG.NORMAL
        self.codeInput['focus'] = 1
        self.submitButton['state'] = DGG.NORMAL

class ExtraOptionsTabPage(DirectFrame):
    notify = directNotify.newCategory('ExtraOptionsTabPage')

    def __init__(self, parent = aspect2d):
        self.parent = parent
        self.currentSizeIndex = None
        self.optionChoosers = {}

        DirectFrame.__init__(self, parent=self.parent, relief=None, pos=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0))

        self.load()

    def destroy(self):
        self.parent = None
        DirectFrame.destroy(self)

    def load(self):
        self.optionChoosers = {}
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        circleModel = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_nameShop')
        titleHeight = 0.61
        textStartHeight = 0.45
        textRowHeight = 0.145
        leftMargin = -0.72
        buttonbase_xcoord = 0.35
        buttonbase_ycoord = 0.45
        button_image_scale = (0.7, 1, 1)
        button_textpos = (0, -0.02)
        options_text_scale = 0.052
        disabled_arrow_color = Vec4(0.6, 0.6, 0.6, 1.0)
        button_image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
        self.speed_chat_scale = 0.055
        self.fov_label = DirectLabel(parent=self, relief=None, text=TTLocalizer.FieldOfViewLabel, text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight))
        self.cogInterface_label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - textRowHeight))
        self.tpTransition_label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 2 * textRowHeight))
        self.fpsMeter_label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 3 * textRowHeight))
        self.teleport_label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 4 * textRowHeight))
        self.fov_slider = DirectSlider(parent=self, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord),
                                               value=settings['fov'], pageSize=5, range=(ToontownGlobals.DefaultCameraFov, ToontownGlobals.MaxCameraFov), command=self.__doFov,
                                               thumb_geom=(circleModel.find('**/tt_t_gui_mat_namePanelCircle')), thumb_relief=None, thumb_geom_scale=2)
        self.fov_slider.setScale(0.25)
        self.cogInterface_toggleButton = DirectButton(parent=self, relief=None, image=button_image, image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight), command=self.__doToggleCogInterface)
        self.tpTransition_toggleButton = DirectButton(parent=self, relief=None, image=button_image, image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - 2 * textRowHeight), command=self.__doToggleTpTransition)
        self.fpsMeter_toggleButton = DirectButton(parent=self, relief=None, image=button_image, image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - 3 * textRowHeight), command=self.__doToggleFpsMeter)
        self.teleport_toggleButton = DirectButton(parent=self, relief=None, image=button_image, image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - 4 * textRowHeight), command=self.__doToggleTeleport)
        self.bugReportButton = DirectButton(parent=self, relief=None, text=TTLocalizer.BugReportButton, image=button_image, image_scale=button_image_scale, text_pos=(0, -0.01), text_fg=(0, 0, 0, 1),
        command=self.showReportNotice, pos=(0.0, 0.0, -0.6), text_scale=(0.045))
        guiButton.removeNode()
        circleModel.removeNode()

        self.optionChoosers['pole'] = OptionChooser.OptionChooser(self, TTLocalizer.FishingPoleLabel, 5, self.__updateFishingPole, [False], self.__applyFishingPole)
        self.optionChoosers['nametag_style'] = OptionChooser.OptionChooser(self, TTLocalizer.NametagStyleLabel, 6, self.__updateNametagStyle, [False], self.__applyNametagStyle)

    def enter(self):
        self.show()
        self.settingsChanged = 0
        self.__setCogInterfaceButton()
        self.__setTpTransitionButton()
        self.__setFpsMeterButton()
        self.__setTeleportButton()
        self.__updateNametagStyle()
        self.__updateFishingPole()
        self.accept('refreshNametagStyle', self.__updateNametagStyle)
        self.accept('refreshFishingRod', self.__updateFishingPole)

    def exit(self):
        self.ignoreAll()
        self.destroyReportNotice()
        self.hide()
        
        for chooser in self.optionChoosers.values():
            chooser.exit(chooser.index)

    def unload(self):
        self.fov_label.destroy()
        del self.fov_label
        self.fov_slider.destroy()
        del self.fov_slider
        self.cogInterface_label.destroy()
        del self.cogInterface_label
        self.cogInterface_toggleButton.destroy()
        del self.cogInterface_label
        self.tpTransition_label.destroy()
        del self.tpTransition_label
        self.tpTransition_toggleButton.destroy()
        del self.tpTransition_toggleButton
        self.fpsMeter_label.destroy()
        del self.fpsMeter_label
        self.fpsMeter_toggleButton.destroy()
        del self.fpsMeter_toggleButton
        self.teleport_label.destroy()
        del self.teleport_label
        self.teleport_toggleButton.destroy()
        del self.teleport_toggleButton
        self.bugReportButton.destroy()
        del self.bugReportButton
        self.destroyReportNotice()
        
        for chooser in self.optionChoosers.values():
            optionChooser.unload()

    def __doFov(self):
        fov = self.fov_slider['value']
        settings['fov'] = fov
        base.camLens.setMinFov(fov/(4./3.))

    def __doToggleCogInterface(self):
        messenger.send('wakeup')
        settings['cogInterface'] = not settings['cogInterface']
        self.settingsChanged = 1
        self.__setCogInterfaceButton()

    def __setCogInterfaceButton(self):
        self.cogInterface_label['text'] = TTLocalizer.CogInterfaceLabelOn if settings['cogInterface'] else TTLocalizer.CogInterfaceLabelOff
        self.cogInterface_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff if settings['cogInterface'] else TTLocalizer.OptionsPageToggleOn

    def __doToggleTpTransition(self):
        messenger.send('wakeup')
        settings['tpTransition'] = not settings['tpTransition']
        self.settingsChanged = 1
        self.__setTpTransitionButton()

    def __setTpTransitionButton(self):
        self.tpTransition_label['text'] = TTLocalizer.TpTransitionLabelOn if settings['tpTransition'] else TTLocalizer.TpTransitionLabelOff
        self.tpTransition_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff if settings['tpTransition'] else TTLocalizer.OptionsPageToggleOn
    
    def __doToggleFpsMeter(self):
        messenger.send('wakeup')
        settings['fpsMeter'] = not settings['fpsMeter']
        base.setFrameRateMeter(settings['fpsMeter'])
        self.settingsChanged = 1
        self.__setFpsMeterButton()

    def __setFpsMeterButton(self):
        self.fpsMeter_label['text'] = TTLocalizer.FpsMeterLabelOn if settings['fpsMeter'] else TTLocalizer.FpsMeterLabelOff
        self.fpsMeter_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff if settings['fpsMeter'] else TTLocalizer.OptionsPageToggleOn
    
    def __doToggleTeleport(self):
        messenger.send('wakeup')
        acceptingTeleport = settings.get('acceptingTeleport', {})
        if base.localAvatar.acceptingTeleport:
            base.localAvatar.acceptingTeleport = 0
            acceptingTeleport[str(base.localAvatar.doId)] = False
        else:
            base.localAvatar.acceptingTeleport  = 1
            acceptingTeleport[str(base.localAvatar.doId)] = True
        settings['acceptingTeleport'] = acceptingTeleport
        self.settingsChanged = 1
        self.__setTeleportButton()
    
    def __setTeleportButton(self):
        self.teleport_label['text'] = TTLocalizer.TeleportLabelOn if base.localAvatar.acceptingTeleport else TTLocalizer.TeleportLabelOff
        self.teleport_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff if base.localAvatar.acceptingTeleport else TTLocalizer.OptionsPageToggleOn

    def __updateNametagStyle(self, resetIndex=True):
        chooser = self.optionChoosers['nametag_style']

        if resetIndex:
            chooser.setIndex(base.localAvatar.nametagStyles.index(base.localAvatar.getNametagStyle()))

        nametagId = base.localAvatar.nametagStyles[chooser.index]
        chooser.setDisplayText('%s\n%s' % (base.localAvatar.getName(), TTLocalizer.NametagFontNames[nametagId]))
        chooser.setDisplayFont(ToontownGlobals.getNametagFont(nametagId))
        chooser.decideButtons(0, len(base.localAvatar.nametagStyles) - 1)
    
    def __applyNametagStyle(self, index):
        if index != -1 and index != base.localAvatar.nametagStyles.index(base.localAvatar.getNametagStyle()):
            base.localAvatar.requestNametagStyle(base.localAvatar.nametagStyles[index])

    def __updateFishingPole(self, resetIndex=True):
        chooser = self.optionChoosers['pole']

        if resetIndex:
            chooser.setIndex(base.localAvatar.getFishingRod())

        chooser.setDisplayText(TTLocalizer.FishingRodNameDict[chooser.index])
        chooser.decideButtons(0, base.localAvatar.maxFishingRod)
    
    def __applyFishingPole(self, index):
        if index != -1 and index != base.localAvatar.getFishingRod():
            base.localAvatar.requestFishingRod(index)
    
    def destroyReportNotice(self):
        if hasattr(self, 'dialog'):
            self.dialog.destroy()
            del self.dialog

    def showReportNotice(self):
        self.destroyReportNotice()
        self.dialog = TTDialog.TTDialog(style=TTDialog.YesNo, text=TTLocalizer.BugReportNotice, command=self.confirmBugReport)
        self.dialog.show()

    def confirmBugReport(self, value):
        self.destroyReportNotice()

        if value > 0:
            webbrowser.open(ToontownGlobals.BugReportSite, new=2, autoraise=True)

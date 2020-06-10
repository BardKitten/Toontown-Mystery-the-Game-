from direct.showbase import DirectObject
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLocalizer
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from panda3d.core import *
from otp.chat import ChatManager
from TTChatInputSpeedChat import TTChatInputSpeedChat
from TTChatInputWhiteList import TTChatInputWhiteList

class ToontownChatManager(ChatManager.ChatManager):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownChatManager')

    def __init__(self, cr, localAvatar):
        gui = loader.loadModel('phase_3.5/models/gui/chat_input_gui')
        self.normalButton = DirectButton(image=(gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos=(0.0683, 0, -0.072), parent=base.a2dTopLeft, scale=1.179, relief=None, image_color=Vec4(1, 1, 1, 1), text=('', OTPLocalizer.ChatManagerChat, OTPLocalizer.ChatManagerChat), text_align=TextNode.ALeft, text_scale=TTLocalizer.TCMnormalButton, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(-0.0525, -0.09), textMayChange=0, sortOrder=DGG.FOREGROUND_SORT_INDEX, command=self.__normalButtonPressed)
        self.normalButton.hide()
        self.openScSfx = loader.loadSfx('phase_3.5/audio/sfx/GUI_quicktalker.ogg')
        self.openScSfx.setVolume(0.6)
        self.scButton = DirectButton(image=(gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos=TTLocalizer.TCMscButtonPos, parent=base.a2dTopLeft, scale=1.179, relief=None, image_color=Vec4(0.75, 1, 0.6, 1), text=('', OTPLocalizer.GlobalSpeedChatName, OTPLocalizer.GlobalSpeedChatName), text_scale=TTLocalizer.TCMscButton, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(0, -0.09), textMayChange=0, sortOrder=DGG.FOREGROUND_SORT_INDEX, command=self.__scButtonPressed, clickSound=self.openScSfx)
        self.scButton.hide()
        self.whisperFrame = DirectFrame(parent=base.a2dTopLeft, relief=None, image=DGG.getDefaultDialogGeom(), image_scale=(0.77, 0.70, 0.20), image_color=OTPGlobals.GlobalDialogColor, pos=(0.40, 0, -0.105), text=OTPLocalizer.ChatManagerWhisperTo, text_wordwrap=6.5, text_scale=TTLocalizer.TCMwhisperFrame, text_fg=Vec4(0, 0, 0, 1), text_pos=(0.18, 0.01), textMayChange=1, sortOrder=DGG.FOREGROUND_SORT_INDEX)
        self.whisperFrame.hide()
        self.whisperButton = DirectButton(parent=self.whisperFrame, image=(gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos=(-0.33, 0, 0.033), scale=1.179, relief=None, image_color=Vec4(1, 1, 1, 1), text=('',
         OTPLocalizer.ChatManagerChat,
         OTPLocalizer.ChatManagerChat,
         ''), image3_color=Vec4(0.6, 0.6, 0.6, 0.6), text_scale=TTLocalizer.TCMwhisperButton, text_fg=(0, 0, 0, 1), text_pos=(0, -0.09), textMayChange=0, command=self.__whisperButtonPressed)
        self.whisperScButton = DirectButton(parent=self.whisperFrame, image=(gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos=(-0.195, 0, 0.033), scale=1.179, relief=None, image_color=Vec4(0.75, 1, 0.6, 1), text=('',
         OTPLocalizer.GlobalSpeedChatName,
         OTPLocalizer.GlobalSpeedChatName,
         ''), image3_color=Vec4(0.6, 0.6, 0.6, 0.6), text_scale=TTLocalizer.TCMwhisperScButton, text_fg=(0, 0, 0, 1), text_pos=(0, -0.09), textMayChange=0, command=self.__whisperScButtonPressed)
        self.whisperCancelButton = DirectButton(parent=self.whisperFrame, image=(gui.find('**/CloseBtn_UP'), gui.find('**/CloseBtn_DN'), gui.find('**/CloseBtn_Rllvr')), pos=(-0.06, 0, 0.033), scale=1.179, relief=None, text=('', OTPLocalizer.ChatManagerCancel, OTPLocalizer.ChatManagerCancel), text_scale=0.05, text_fg=(0, 0, 0, 1), text_pos=(0, -0.09), textMayChange=0, command=self.__whisperCancelPressed)
        gui.removeNode()
        ChatManager.ChatManager.__init__(self, cr, localAvatar)
        self.defaultToWhiteList = config.GetBool('white-list-is-default', 1)
        self.chatInputSpeedChat = TTChatInputSpeedChat(self)
        self.normalPos = Vec3(0.25, 0, -0.196)
        self.whisperPos = Vec3(0.25, 0, -0.28)
        self.speedChatPlusPos = Vec3(-0.35, 0, 0.71)
        self.chatInputWhiteList = TTChatInputWhiteList()
        if self.defaultToWhiteList:
            self.chatInputNormal = self.chatInputWhiteList
            self.chatInputNormal.setPos(self.normalPos)
            self.chatInputNormal.desc = 'chatInputNormal'
        else:
            self.chatInputNormal = TTChatInputNormal(self)
        self.chatInputWhiteList.setPos(self.speedChatPlusPos)
        self.chatInputWhiteList.reparentTo(base.a2dTopLeft)
        self.chatInputWhiteList.desc = 'chatInputWhiteList'
        return

    def delete(self):
        ChatManager.ChatManager.delete(self)
        loader.unloadModel('phase_3.5/models/gui/chat_input_gui')
        self.normalButton.destroy()
        del self.normalButton
        self.scButton.destroy()
        del self.scButton
        del self.openScSfx
        self.whisperFrame.destroy()
        del self.whisperFrame
        self.whisperButton.destroy()
        del self.whisperButton
        self.whisperScButton.destroy()
        del self.whisperScButton
        self.whisperCancelButton.destroy()
        del self.whisperCancelButton
        self.chatInputWhiteList.destroy()
        del self.chatInputWhiteList

    def sendSCResistanceChatMessage(self, textId):
        messenger.send('chatUpdateSCResistance', [textId])
        self.announceSCChat()

    def sendSCToontaskChatMessage(self, taskId, toNpcId, toonProgress, msgIndex):
        messenger.send('chatUpdateSCToontask', [taskId,
         toNpcId,
         toonProgress,
         msgIndex])
        self.announceSCChat()

    def sendSCToontaskWhisperMessage(self, taskId, toNpcId, toonProgress, msgIndex, whisperAvatarId):
        messenger.send('whisperUpdateSCToontask', [taskId,
         toNpcId,
         toonProgress,
         msgIndex,
         whisperAvatarId])

    def enterMainMenu(self):
        self.chatInputNormal.setPos(self.normalPos)
        self.chatInputNormal.reparentTo(base.a2dTopLeft)
        if self.chatInputWhiteList.isActive():
            self.notify.debug('enterMainMenu calling checkObscured')
            ChatManager.ChatManager.checkObscurred(self)
        else:
            ChatManager.ChatManager.enterMainMenu(self)

    def enterNoTrueFriends(self):
        if self.noTrueFriends == None:
            buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.noTrueFriends = DirectFrame(parent=aspect2dp, pos=(0.0, 0.1, 0.2), relief=None, image=DGG.getDefaultDialogGeom(), image_color=OTPGlobals.GlobalDialogColor, image_scale=(1.4, 1.0, 1.1), text=OTPLocalizer.NoTrueFriends, text_wordwrap=20, textMayChange=0, text_scale=0.06, text_pos=(0, 0.3))
            DirectLabel(parent=self.noTrueFriends, relief=None, pos=(0, 0, 0.4), text=OTPLocalizer.NoTrueFriendsTitle, textMayChange=0, text_scale=0.08)
            DirectButton(self.noTrueFriends, image=okButtonImage, relief=None, text=OTPLocalizer.NoTrueFriendsOK, text_scale=0.05, text_pos=(0.0, -0.1), textMayChange=0, pos=(0.0, 0.0, -0.4), command=self.__handleNoTrueFriendsOK)
            buttons.removeNode()
        self.noTrueFriends.show()
        return

    def exitNoTrueFriends(self):
        self.noTrueFriends.hide()

    def __normalButtonPressed(self):
        if base.config.GetBool('want-qa-regression', 0):
            self.notify.info('QA-REGRESSION: CHAT: Speedchat Plus')
        messenger.send('wakeup')
        if not base.cr.wantTypedChat():
            self.fsm.request('noSpeedchatPlus')
            return
        self.fsm.request('normalChat')

    def __scButtonPressed(self):
        messenger.send('wakeup')
        if self.fsm.getCurrentState().getName() == 'speedChat':
            self.fsm.request('mainMenu')
        else:
            self.fsm.request('speedChat')

    def __whisperButtonPressed(self, avatarName, avatarId):
        messenger.send('wakeup')
        if not base.cr.wantTypedChat():
            self.fsm.request('noSpeedchatPlus')
            return
        if avatarId:
            self.enterWhisperChat(avatarName, avatarId)
        self.whisperFrame.hide()

    def enterNormalChat(self):
        if not base.cr.wantTypedChat() or not base.localAvatar.getTutorialAck() or not ChatManager.ChatManager.enterNormalChat(self):
            self.fsm.request('mainMenu')

    def enterWhisperChat(self, avatarName, avatarId):
        if not base.cr.wantTypedChat():
            self.fsm.request('mainMenu')
            return
        result = ChatManager.ChatManager.enterWhisperChat(self, avatarName, avatarId)
        self.chatInputNormal.setPos(self.whisperPos)
        if result == None:
            self.notify.warning('something went wrong in enterWhisperChat, falling back to main menu')
            self.fsm.request('mainMenu')

    def enterNoSpeedchatPlus(self):
        if self.noSpeedchatPlus == None:
            buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.noSpeedchatPlus = DirectFrame(parent=aspect2dp, pos=(0.0, 0.1, 0.05), relief=None, image=DGG.getDefaultDialogGeom(), image_color=OTPGlobals.GlobalDialogColor, image_scale=(1.4, 1.0, 1.58), text=OTPLocalizer.NoSpeedchatPlus, text_wordwrap=20, textMayChange=0, text_scale=0.06, text_pos=(0, 0.55))
            DirectLabel(parent=self.noSpeedchatPlus, relief=None, pos=(0, 0, 0.67), text=OTPLocalizer.NoSpeedchatPlusTitle, textMayChange=0, text_scale=0.08)
            DirectButton(self.noSpeedchatPlus, image=okButtonImage, relief=None, text=OTPLocalizer.NoTrueFriendsOK, text_scale=0.05, text_pos=(0.0, -0.1), textMayChange=0, pos=(0.0, 0.0, -0.64), command=self.__handleNoTrueFriendsOK)
            buttons.removeNode()
        self.noSpeedchatPlus.show()
        return

    def exitNoSpeedchatPlus(self):
        self.noSpeedchatPlus.hide()

    def __whisperScButtonPressed(self, avatarName, avatarId):
        messenger.send('wakeup')
        if avatarId:
            if self.fsm.getCurrentState().getName() == 'whisperSpeedChat':
                self.fsm.request('whisper', [avatarName, avatarId])
            else:
                self.fsm.request('whisperSpeedChat', [avatarId])

    def __whisperCancelPressed(self):
        self.fsm.request('mainMenu')

    def __handleNoTrueFriendsOK(self):
        self.fsm.request('mainMenu')

    def messageSent(self):
        pass

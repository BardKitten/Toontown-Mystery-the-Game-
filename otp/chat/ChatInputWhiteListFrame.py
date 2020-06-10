from panda3d.core import *
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from direct.fsm import FSM
from otp.otpbase import OTPGlobals

class ChatInputWhiteListFrame(FSM.FSM, DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('ChatInputWhiteList')

    def __init__(self, entryOptions, parent = None, **kw):
        FSM.FSM.__init__(self, 'ChatInputWhiteListFrame')
        self.receiverId = None
        DirectFrame.__init__(self, parent=aspect2dp, pos=(0, 0, 0.3), relief=None, image=DGG.getDefaultDialogGeom(), image_scale=(1.6, 1, 1.4), image_pos=(0, 0, -0.05), image_color=OTPGlobals.GlobalDialogColor, borderWidth=(0.01, 0.01))
        optiondefs = {'parent': self,
         'relief': DGG.SUNKEN,
         'scale': 0.05,
         'frameSize': (-0.2, 25.3, -0.5, 1.2),
         'borderWidth': (0.1, 0.1),
         'frameColor': (0.9, 0.9, 0.85, 0.8),
         'pos': (-0.2, 0, 0.11),
         'entryFont': OTPGlobals.getInterfaceFont(),
         'width': 8.6,
         'numLines': 3,
         'cursorKeys': 1,
         'backgroundFocus': 0,
         'suppressKeys': 1,
         'suppressMouse': 1,
         'command': self.sendChat,
         'focus': 0,
         'text': '',
         'sortOrder': DGG.FOREGROUND_SORT_INDEX}
        entryOptions['parent'] = self
        self.chatEntry = DirectEntry(**entryOptions)
        self.whisperId = None
        self.chatEntry.bind(DGG.OVERFLOW, self.chatOverflow)
        self.active = 0
        self.autoOff = 0
        self.sendBy = 'Mode'
        from direct.gui import DirectGuiGlobals
        self.chatEntry.bind(DirectGuiGlobals.TYPE, self.applyFilter)
        self.chatEntry.bind(DirectGuiGlobals.ERASE, self.applyFilter)

    def destroy(self):
        from direct.gui import DirectGuiGlobals
        self.chatEntry.unbind(DGG.OVERFLOW)
        self.chatEntry.unbind(DirectGuiGlobals.TYPE)
        self.chatEntry.unbind(DirectGuiGlobals.ERASE)
        self.chatEntry.ignoreAll()
        DirectFrame.destroy(self)

    def delete(self):
        self.ignore('arrow_up-up')
        self.ignore('arrow_down-up')

    def requestMode(self, mode, *args):
        return self.request(mode, *args)

    def enterOff(self):
        self.deactivate()
        localAvatar.chatMgr.fsm.request('mainMenu')

    def exitOff(self):
        self.activate()

    def enterAllChat(self):
        self.chatEntry['focus'] = 1
        self.show()

    def exitAllChat(self):
        pass

    def enterAvatarWhisper(self):
        self.tempText = self.chatEntry.get()
        self.activate()

    def exitAvatarWhisper(self):
        self.chatEntry.set(self.tempText)
        self.whisperId = None

    def activateByData(self, receiverId = None):
        self.receiverId = receiverId
        result = None
        if not self.receiverId:
            result = self.requestMode('AllChat')
        elif self.receiverId:
            self.whisperId = receiverId
            result = self.requestMode('AvatarWhisper')
        return result

    def activate(self):
        self.chatEntry['focus'] = 1
        self.show()
        self.active = 1
        self.chatEntry.guiItem.setAcceptEnabled(True)

    def deactivate(self):
        self.chatEntry.set('')
        self.chatEntry['focus'] = 0
        self.hide()
        self.active = 0

    def isActive(self):
        return self.active

    def sendChat(self, text, overflow = False):
        if not (len(text) > 0 and text[0] in ['~', '>']):
            text = self.chatEntry.get(plain=True)

        if text:
            self.chatEntry.set('')

            if not base.cr.chatAgent.verifyMessage(text):
                return

            self.sendChatBySwitch(text)

        if not overflow:
            self.hide()
            if self.autoOff:
                self.requestMode('Off')

            localAvatar.chatMgr.messageSent()

    def sendChatBySwitch(self, text):
        if len(text) > 0 and text[0] == '~':
            base.talkAssistant.sendOpenTalk(text)
        elif self.sendBy == 'Mode':
            self.sendChatByMode(text)
        elif self.sendBy == 'Data':
            self.sendChatByData(text)
        else:
            self.sendChatByMode(text)

    def sendChatByData(self, text):
        if self.receiverId:
            base.talkAssistant.sendWhisperTalk(text, self.receiverId)
        else:
            base.talkAssistant.sendOpenTalk(text)

    def sendChatByMode(self, text):
        state = self.getCurrentOrNextState()
        messenger.send('sentRegularChat')
        if state == 'AvatarWhisper':
            base.talkAssistant.sendAvatarWhisperWLChat(text, self.whisperId)
        else:
            base.talkAssistant.sendOpenTalk(text)

    def chatOverflow(self, overflowText):
        self.notify.debug('chatOverflow')
        self.sendChat(self.chatEntry.get(plain=True), overflow=True)

    def applyFilter(self, keyArgs):
        if base.whiteList:
            self.chatEntry.set(base.whiteList.processThroughAll(self.chatEntry.get(plain=True)))

from otp.speedchat.SCTerminal import SCTerminal
from otp.otpbase.OTPLocalizer import SpeedChatStaticText
SCStaticTextMsgEvent = 'SCStaticTextMsg'

class TTSCWhiteListTerminal(SCTerminal):

    def __init__(self, textId, parentMenu = None):
        SCTerminal.__init__(self)
        self.parentClass = parentMenu
        self.textId = textId
        self.text = SpeedChatStaticText[self.textId]
        print 'SpeedText %s %s' % (self.textId, self.text)

    def handleSelect(self):
        SCTerminal.handleSelect(self)
        if not self.parentClass.whisperAvatarId:
            base.localAvatar.chatMgr.fsm.request('whiteListOpenChat')
        else:
            base.localAvatar.chatMgr.fsm.request('whiteListAvatarChat', [self.parentClass.whisperAvatarId])

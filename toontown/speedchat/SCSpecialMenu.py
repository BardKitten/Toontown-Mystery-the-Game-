from otp.otpbase import OTPLocalizer
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat import SCMenuHolder, SCStaticTextTerminal

class SCSpecialMenu(SCMenu):

    def __init__(self, sections):
        SCMenu.__init__(self)
        self.sections = sections
        self.__messagesChanged()

    def appendPhrases(self, section, menu):
        for phrase in section[1]:
            if phrase not in OTPLocalizer.SpeedChatStaticText:
                print 'warning: tried to link speedchat menu phrase %s which does not seem to exist' % phrase
                break

            menu.append(SCStaticTextTerminal.SCStaticTextTerminal(phrase))

    def __messagesChanged(self):
        self.clearMenu()

        try:
            lt = base.localAvatar
        except:
            return

        for section in self.sections:
            if section[0] == -1:
                self.appendPhrases(section, self)
            else:
                menu = SCMenu()

                self.appendPhrases(section, menu)
                self.append(SCMenuHolder.SCMenuHolder(str(section[0]), menu))

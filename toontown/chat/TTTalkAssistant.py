from direct.directnotify import DirectNotifyGlobal
from otp.chat.TalkAssistant import TalkAssistant
from otp.chat.ChatGlobals import *

class TTTalkAssistant(TalkAssistant):
    notify = DirectNotifyGlobal.directNotify.newCategory('TTTalkAssistant')

    def sendToonTaskSpeedChat(self, taskId, toNpcId, toonProgress, msgIndex):
        messenger.send(SCChatEvent)
        messenger.send('chatUpdateSCToontask', [taskId, toNpcId, toonProgress, msgIndex])

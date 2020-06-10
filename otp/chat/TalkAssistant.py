from direct.directnotify import DirectNotifyGlobal
from direct.showbase import DirectObject
from otp.chat.ChatGlobals import *
from otp.nametag.NametagConstants import *
import ChatUtil

class TalkAssistant(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('TalkAssistant')

    def delete(self):
        self.ignoreAll()

    def start(self):
        pass

    def stop(self):
        pass

    def sendOpenTalk(self, message):
        if len(message) > 0 and message[0] == '~':
            messenger.send('magicWord', [message])
        else:
            chatFlags = CFSpeech | CFTimeout
            if ChatUtil.isThought(message):
                chatFlags = CFThought
            base.cr.chatAgent.sendChatMessage(message)
            messenger.send('chatUpdate', [message, chatFlags])

    def sendWhisperTalk(self, message, receiverAvId):
        base.cr.ttsFriendsManager.sendUpdate('sendTalkWhisper', [receiverAvId, message])

    def sendOpenSpeedChat(self, type, messageIndex):
        if type == SPEEDCHAT_NORMAL:
            messenger.send(SCChatEvent)
            messenger.send('chatUpdateSC', [messageIndex])
            base.localAvatar.b_setSC(messageIndex)
        elif type == SPEEDCHAT_EMOTE:
            messenger.send('chatUpdateSCEmote', [messageIndex])
            messenger.send(SCEmoteChatEvent)
            base.localAvatar.b_setSCEmote(messageIndex)
        elif type == SPEEDCHAT_CUSTOM:
            messenger.send('chatUpdateSCCustom', [messageIndex])
            messenger.send(SCCustomChatEvent)
            base.localAvatar.b_setSCCustom(messageIndex)

    def sendAvatarWhisperSpeedChat(self, type, messageIndex, receiverId):
        if type == SPEEDCHAT_NORMAL:
            base.localAvatar.whisperSCTo(messageIndex, receiverId)
        elif type == SPEEDCHAT_EMOTE:
            base.localAvatar.whisperSCEmoteTo(messageIndex, receiverId)
        elif type == SPEEDCHAT_CUSTOM:
            base.localAvatar.whisperSCCustomTo(messageIndex, receiverId)

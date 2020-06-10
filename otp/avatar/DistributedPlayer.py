from direct.showbase import PythonUtil
from direct.task import Task
from panda3d.core import *
import string
import time

from otp.ai.MagicWordGlobal import *
from otp.avatar import Avatar, PlayerBase, DistributedAvatar
from otp.avatar.Avatar import teleportNotify
from otp.chat import ChatGarbler, TalkAssistant
from otp.distributed.TelemetryLimited import TelemetryLimited
from otp.otpbase import OTPGlobals, OTPLocalizer
from otp.speedchat import SCDecoders
from otp.nametag.NametagConstants import *
from otp.margins.WhisperPopup import WhisperPopup

class DistributedPlayer(DistributedAvatar.DistributedAvatar, PlayerBase.PlayerBase, TelemetryLimited):
    chatGarbler = ChatGarbler.ChatGarbler({'default': OTPLocalizer.ChatGarblerDefault})

    def __init__(self, cr):
        try:
            self.DistributedPlayer_initialized
        except:
            self.DistributedPlayer_initialized = 1
            DistributedAvatar.DistributedAvatar.__init__(self, cr)
            TelemetryLimited.__init__(self)
            self.__teleportAvailable = 0
            self.inventory = None
            self.experience = None
            self.friendsList = []
            self._districtWeAreGeneratedOn = None
            self.DISLid = 0
            self.adminAccess = 0
            self.autoRun = 0
            self.lastTeleportQuery = time.time()

    @staticmethod
    def GetPlayerGenerateEvent():
        return 'DistributedPlayerGenerateEvent'

    @staticmethod
    def GetPlayerNetworkDeleteEvent():
        return 'DistributedPlayerNetworkDeleteEvent'

    @staticmethod
    def GetPlayerDeleteEvent():
        return 'DistributedPlayerDeleteEvent'

    def networkDelete(self):
        DistributedAvatar.DistributedAvatar.networkDelete(self)
        messenger.send(self.GetPlayerNetworkDeleteEvent(), [self])

    def disable(self):
        DistributedAvatar.DistributedAvatar.disable(self)
        messenger.send(self.GetPlayerDeleteEvent(), [self])

    def delete(self):
        try:
            self.DistributedPlayer_deleted
        except:
            self.DistributedPlayer_deleted = 1
            del self.experience
            if self.inventory:
                self.inventory.unload()
            del self.inventory
            DistributedAvatar.DistributedAvatar.delete(self)

    def generate(self):
        DistributedAvatar.DistributedAvatar.generate(self)

    def announceGenerate(self):
        DistributedAvatar.DistributedAvatar.announceGenerate(self)
        messenger.send(self.GetPlayerGenerateEvent(), [self])

    def setLocation(self, parentId, zoneId):
        DistributedAvatar.DistributedAvatar.setLocation(self, parentId, zoneId)
        if not (parentId in (0, None) and zoneId in (0, None)):
            if not self.cr._isValidPlayerLocation(parentId, zoneId):
                self.cr.disableDoId(self.doId)
                self.cr.deleteObject(self.doId)
        return None

    def isGeneratedOnDistrict(self, districtId = None):
        return True # fix for the task button
        if districtId is None:
            return self._districtWeAreGeneratedOn is not None
        else:
            return self._districtWeAreGeneratedOn == districtId
        return

    def getArrivedOnDistrictEvent(self, districtId = None):
        if districtId is None:
            return 'arrivedOnDistrict'
        else:
            return 'arrivedOnDistrict-%s' % districtId
        return

    def arrivedOnDistrict(self, districtId):
        curFrameTime = globalClock.getFrameTime()
        if hasattr(self, 'frameTimeWeArrivedOnDistrict') and curFrameTime == self.frameTimeWeArrivedOnDistrict:
            if districtId == 0 and self._districtWeAreGeneratedOn:
                self.notify.warning('ignoring arrivedOnDistrict 0, since arrivedOnDistrict %d occured on the same frame' % self._districtWeAreGeneratedOn)
                return
        self._districtWeAreGeneratedOn = districtId
        self.frameTimeWeArrivedOnDistrict = globalClock.getFrameTime()
        messenger.send(self.getArrivedOnDistrictEvent(districtId))
        messenger.send(self.getArrivedOnDistrictEvent())

    def setLeftDistrict(self):
        self._districtWeAreGeneratedOn = None
        return

    def hasParentingRules(self):
        if self is localAvatar:
            return True

    def setSystemMessage(self, aboutId, chatString, whisperType = WhisperPopup.WTSystem):
        self.displayWhisper(aboutId, chatString, whisperType)

    def displayWhisper(self, fromId, chatString, whisperType):
        print 'Whisper type %s from %s: %s' % (whisperType, fromId, chatString)

    def whisperSCTo(self, msgIndex, sendToId):
        messenger.send('wakeup')
        base.cr.ttsFriendsManager.d_whisperSCTo(sendToId, msgIndex)

    def setWhisperSCFrom(self, fromId, msgIndex):
        handle = base.cr.identifyAvatar(fromId)
        if handle == None or base.localAvatar.isIgnored(fromId):
            return
        chatString = SCDecoders.decodeSCStaticTextMsg(msgIndex)
        if chatString:
            self.displayWhisper(fromId, chatString, WhisperPopup.WTNormal)
        return

    def whisperSCCustomTo(self, msgIndex, sendToId):
        messenger.send('wakeup')
        base.cr.ttsFriendsManager.d_whisperSCCustomTo(sendToId, msgIndex)

    def _isValidWhisperSource(self, source):
        return True

    def setWhisperSCCustomFrom(self, fromId, msgIndex):
        handle = base.cr.identifyAvatar(fromId)
        if handle == None:
            return
        if not self._isValidWhisperSource(handle):
            self.notify.warning('displayWhisper from non-toon %s' % fromId)
            return
        if base.localAvatar.isIgnored(fromId):
            return
        chatString = SCDecoders.decodeSCCustomMsg(msgIndex)
        if chatString:
            self.displayWhisper(fromId, chatString, WhisperPopup.WTNormal)

    def whisperSCEmoteTo(self, emoteId, sendToId):
        messenger.send('wakeup')
        base.cr.ttsFriendsManager.d_whisperSCEmoteTo(sendToId, emoteId)

    def setWhisperSCEmoteFrom(self, fromId, emoteId):
        handle = base.cr.identifyAvatar(fromId)
        if handle == None or base.localAvatar.isIgnored(fromId):
            return
        chatString = SCDecoders.decodeSCEmoteWhisperMsg(emoteId, handle.getName())
        if chatString:
            self.displayWhisper(fromId, chatString, WhisperPopup.WTEmote)
        return

    def setChatAbsolute(self, chatString, chatFlags, dialogue = None, interrupt = 1, quiet = 0):
        DistributedAvatar.DistributedAvatar.setChatAbsolute(self, chatString, chatFlags, dialogue, interrupt)
        if not quiet:
            pass

    def setTalk(self, chat):
        if not base.cr.chatAgent.verifyMessage(chat):
            return
        if base.localAvatar.isIgnored(self.doId):
            return
        if not self.understandable:
            chat = self.chatGarbler.garble(self, len(chat.split(' ')))
        elif base.whiteList and self.understandable < 2:
            chat = base.whiteList.processThroughAll(chat, self, self.chatGarbler)
        self.displayTalk(chat)

    def setTalkWhisper(self, avId, chat):
        if not base.cr.chatAgent.verifyMessage(chat):
            return
        if base.localAvatar.isIgnored(avId):
            return
        if not self.understandable:
            chat = self.chatGarbler.garble(self, len(chat.split(' ')))
        elif base.whiteList and self.understandable < 2:
            chat = base.whiteList.processThroughAll(chat, self.chatGarbler)
        self.displayTalkWhisper(avId, chat)

    def displayTalk(self, chat):
        print 'Talk: %s' % chat

    def displayTalkWhisper(self, avId, chat):
        print 'TalkWhisper from %s: %s' % (avId, chat)

    def b_setSC(self, msgIndex):
        self.setSC(msgIndex)
        self.d_setSC(msgIndex)

    def d_setSC(self, msgIndex):
        messenger.send('wakeup')
        self.sendUpdate('setSC', [msgIndex])

    def setSC(self, msgIndex):
        if base.localAvatar.isIgnored(self.doId):
            return
        chatString = SCDecoders.decodeSCStaticTextMsg(msgIndex)
        if chatString:
            self.setChatAbsolute(chatString, CFSpeech | CFQuicktalker | CFTimeout, quiet=1)

    def b_setSCCustom(self, msgIndex):
        self.setSCCustom(msgIndex)
        self.d_setSCCustom(msgIndex)

    def d_setSCCustom(self, msgIndex):
        messenger.send('wakeup')
        self.sendUpdate('setSCCustom', [msgIndex])

    def setSCCustom(self, msgIndex):
        if base.localAvatar.isIgnored(self.doId):
            return
        chatString = SCDecoders.decodeSCCustomMsg(msgIndex)
        if chatString:
            self.setChatAbsolute(chatString, CFSpeech | CFQuicktalker | CFTimeout)

    def b_setSCEmote(self, emoteId):
        self.b_setEmoteState(emoteId, animMultiplier=self.animMultiplier)

    def d_friendsNotify(self, avId, status):
        self.sendUpdate('friendsNotify', [avId, status])

    def friendsNotify(self, avId, status):
        avatar = base.cr.identifyFriend(avId)
        if avatar != None:
            if status == 1:
                self.setSystemMessage(avId, OTPLocalizer.WhisperNoLongerFriend % avatar.getName())
            elif status == 2:
                self.setSystemMessage(avId, OTPLocalizer.WhisperNowSpecialFriend % avatar.getName())
        return

    def d_teleportQuery(self, requesterId, sendToId = None):
        lastQuery = self.lastTeleportQuery
        currentQuery = time.time()

        if currentQuery - lastQuery < 0.1: # Oh boy! We found a skid!
            self.cr.stopReaderPollTask()
            self.cr.lostConnection()

        self.lastTeleportQuery = time.time()

        base.cr.ttsFriendsManager.d_teleportQuery(sendToId)

    def teleportQuery(self, requesterId):
        avatar = base.cr.identifyFriend(requesterId)

        if avatar is None:
            self.d_teleportResponse(self.doId, 0, 0, 0, 0, sendToId=requesterId)
        elif base.localAvatar.isIgnored(requesterId):
            self.d_teleportResponse(self.doId, 2, 0, 0, 0, sendToId=requesterId)
        elif hasattr(base, 'distributedParty') and ((base.distributedParty.partyInfo.isPrivate and requesterId not in base.distributedParty.inviteeIds) or base.distributedParty.isPartyEnding):
            self.d_teleportResponse(self.doId, 0, 0, 0, 0, sendToId=requesterId)
        elif self.__teleportAvailable and not self.ghostMode:
            self.setSystemMessage(requesterId, OTPLocalizer.WhisperComingToVisit % avatar.getName())
            messenger.send('teleportQuery', [avatar, self])
        else:
            self.setSystemMessage(requesterId, OTPLocalizer.WhisperFailedVisit % avatar.getName())
            self.d_teleportResponse(self.doId, 0, 0, 0, 0, sendToId=requesterId)

    def d_teleportResponse(self, avId, available, shardId, hoodId, zoneId, sendToId):
        teleportNotify.debug('sending teleportResponse%s' % ((avId, available,
            shardId, hoodId, zoneId, sendToId),)
        )

        base.cr.ttsFriendsManager.d_teleportResponse(sendToId, available,
            shardId, hoodId, zoneId
        )

    def teleportResponse(self, avId, available, shardId, hoodId, zoneId):
        teleportNotify.debug('received teleportResponse%s' % ((avId, available,
            shardId, hoodId, zoneId),)
        )

        messenger.send('teleportResponse', [avId, available, shardId, hoodId, zoneId])

    def d_teleportGiveup(self, requesterId, sendToId):
        teleportNotify.debug('sending teleportGiveup(%s) to %s' % (requesterId, sendToId))

        base.cr.ttsFriendsManager.d_teleportGiveup(sendToId)

    def teleportGiveup(self, requesterId):
        teleportNotify.debug('received teleportGiveup(%s)' % (requesterId,))
        avatar = base.cr.identifyAvatar(requesterId)

        if not self._isValidWhisperSource(avatar):
            self.notify.warning('teleportGiveup from non-toon %s' % requesterId)
            return

        if avatar is not None:
            self.setSystemMessage(requesterId,
                OTPLocalizer.WhisperGiveupVisit % avatar.getName()
            )

    def b_teleportGreeting(self, avId):
        if hasattr(self, 'ghostMode') and self.ghostMode:
            return
        self.d_teleportGreeting(avId)
        self.teleportGreeting(avId)

    def d_teleportGreeting(self, avId):
        self.sendUpdate('teleportGreeting', [avId])

    def teleportGreeting(self, avId):
        avatar = base.cr.getDo(avId)
        if isinstance(avatar, Avatar.Avatar):
            self.setChatAbsolute(OTPLocalizer.TeleportGreeting % avatar.getName(), CFSpeech | CFTimeout)
        elif avatar is not None:
            self.notify.warning('got teleportGreeting from %s referencing non-toon %s' % (self.doId, avId))
        return

    def setTeleportAvailable(self, available):
        self.__teleportAvailable = available

    def getTeleportAvailable(self):
        return self.__teleportAvailable

    def getFriendsList(self):
        return self.friendsList

    def setFriendsList(self, friendsList):
        self.friendsList = friendsList
        messenger.send('friendsListChanged')
        Avatar.reconsiderAllUnderstandable()

    def setDISLid(self, id):
        self.DISLid = id

    def setAdminAccess(self, access):
        self.adminAccess = access
        self.considerUnderstandable()

    def getAdminAccess(self):
        return self.adminAccess

    def isAdmin(self):
        return self.adminAccess >= MINIMUM_MAGICWORD_ACCESS

    def setAutoRun(self, value):
        self.autoRun = value

    def getAutoRun(self):
        return self.autoRun

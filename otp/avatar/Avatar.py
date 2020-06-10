from direct.actor.Actor import Actor
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import ClockDelta
from direct.interval.IntervalGlobal import *
from direct.showbase.PythonUtil import recordCreationStack
from panda3d.core import *
import random

from otp.ai import MagicWordManager
from otp.ai.MagicWordGlobal import *
from otp.avatar.ShadowCaster import ShadowCaster
from otp.chat import ChatUtil
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLocalizer
from otp.otpbase import OTPRender
from otp.nametag.Nametag import Nametag
from otp.nametag.NametagGroup import NametagGroup
from otp.nametag.NametagConstants import *

teleportNotify = DirectNotifyGlobal.directNotify.newCategory('Teleport')
teleportNotify.showTime = True
if config.GetBool('want-teleport-debug', 1):
    teleportNotify.setDebug(1)

def reconsiderAllUnderstandable():
    for av in Avatar.ActiveAvatars:
        av.considerUnderstandable()

class Avatar(Actor, ShadowCaster):
    notify = directNotify.newCategory('Avatar')
    ActiveAvatars = []

    def __init__(self, other = None):
        Actor.__init__(self, None, None, other, flattenable=0, setFinal=1)
        ShadowCaster.__init__(self)
        self.__font = OTPGlobals.getInterfaceFont()
        self.name = ''
        self.soundChatBubble = None
        self.avatarType = ''
        self.nametagNodePath = None
        self.__nameVisible = 1
        self.nametag = NametagGroup()
        self.nametag.setAvatar(self)
        self.nametag.setFont(OTPGlobals.getInterfaceFont())
        self.nametag.setSpeechFont(OTPGlobals.getInterfaceFont())
        self.nametag2dContents = Nametag.CName | Nametag.CSpeech
        self.nametag2dDist = Nametag.CName | Nametag.CSpeech
        self.nametag2dNormalContents = Nametag.CName | Nametag.CSpeech
        self.nametag3d = self.attachNewNode('nametag3d')
        self.nametag3d.setTag('cam', 'nametag')
        self.nametag3d.setLightOff()
        self.getGeomNode().showThrough(OTPRender.ShadowCameraBitmask)
        self.nametag3d.hide(OTPRender.ShadowCameraBitmask)
        self.collTube = None
        self.scale = 1.0
        self.height = 0.0
        self.style = None
        self.understandable = 1
        self.setPlayerType(NametagGroup.CCNormal)
        self.ghostMode = 0
        self.__chatParagraph = None
        self.__chatMessage = None
        self.__chatFlags = 0
        self.__chatPageNumber = None
        self.__chatAddressee = None
        self.__chatDialogueList = []
        self.__chatSet = 0
        self.__chatLocal = 0
        self.__currentDialogue = None
        self.wantAdminTag = True

    def delete(self):
        try:
            self.Avatar_deleted
        except:
            self.deleteNametag3d()
            Actor.cleanup(self)
            self.Avatar_deleted = 1
            del self.__font
            del self.style
            del self.soundChatBubble
            self.nametag.destroy()
            del self.nametag
            self.nametag3d.removeNode()
            ShadowCaster.delete(self)
            Actor.delete(self)

    def isLocal(self):
        return 0

    def isPet(self):
        return False

    def isProxy(self):
        return False

    def setPlayerType(self, playerType):
        self.playerType = playerType
        if not hasattr(self, 'nametag'):
            self.notify.warning('no nametag attributed, but would have been used.')
            return
        if self.isUnderstandable():
            self.nametag.setColorCode(self.playerType)
        else:
            self.nametag.setColorCode(NametagGroup.CCNonPlayer)
        self.setNametagName()

    def considerUnderstandable(self):
        if self.playerType in (NametagGroup.CCNormal, NametagGroup.CCSpeedChat):
            self.setPlayerType(NametagGroup.CCSpeedChat)
        if hasattr(base, 'localAvatar') and (self == base.localAvatar):
            self.understandable = 1
            self.setPlayerType(NametagGroup.CCNormal)
        elif self.playerType == NametagGroup.CCSuit:
            self.understandable = 1
            self.setPlayerType(NametagGroup.CCSuit)
        elif self.playerType not in (NametagGroup.CCNormal, NametagGroup.CCSpeedChat):
            self.understandable = 1
            self.setPlayerType(NametagGroup.CCNonPlayer)
        elif base.localAvatar.isTrueFriends(self.doId):
            self.understandable = 2
            self.setPlayerType(NametagGroup.CCNormal)
        elif base.cr.wantSpeedchatPlus():
            self.understandable = 1
            self.setPlayerType(NametagGroup.CCSpeedChat)
        else:
            self.understandable = 0
            self.setPlayerType(NametagGroup.CCSpeedChat)
        if base.cr.wantSpeedchatPlus() and hasattr(self, 'adminAccess') and self.isAdmin() and self != base.localAvatar:
            self.understandable = 2
        if not hasattr(self, 'nametag'):
            self.notify.warning('no nametag attributed, but would have been used')
        else:
            self.nametag.setColorCode(self.playerType)

    def isUnderstandable(self):
        return self.understandable

    def setDNAString(self, dnaString):
        pass

    def setDNA(self, dna):
        pass

    def getAvatarScale(self):
        return self.scale

    def setAvatarScale(self, scale):
        if self.scale != scale:
            self.scale = scale
            self.getGeomNode().setScale(scale)
            self.setHeight(self.height)

    def adjustNametag3d(self, parentScale = 1.0):
        self.nametag3d.setPos(0, 0, self.height + 0.5)

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height
        self.adjustNametag3d()
        if self.collTube:
            self.collTube.setPointB(0, 0, height - self.getRadius())
            if self.collNodePath:
                self.collNodePath.forceRecomputeBounds()

    def getRadius(self):
        return OTPGlobals.AvatarDefaultRadius

    def getName(self):
        return self.name

    def getType(self):
        return self.avatarType
    
    def setWantAdminTag(self, bool):
        self.wantAdminTag = bool
    
    def getWantAdminTag(self):
        return self.wantAdminTag

    def setName(self, name):
        if hasattr(self, 'isDisguised') and self.isDisguised:
            return

        self.name = name

        if hasattr(self, 'nametag'):
            self.setNametagName()

    def setDisplayName(self, str):
        if hasattr(self, 'isDisguised'):
            if self.isDisguised:
                return
        self.setNametagName(str)

    def setNametagName(self, name=None):
        if not name:
            name = self.name

        self.nametag.setName(name)

        if hasattr(self, 'adminAccess') and self.isAdmin() and self.getWantAdminTag():
            access = self.getAdminAccess()

            if access in OTPLocalizer.AccessToString:
                name += '\n\x01shadow\x01%s\x02' % OTPLocalizer.AccessToString[access]

        self.nametag.setDisplayName(name)

    def getFont(self):
        return self.__font

    def setFont(self, font):
        self.__font = font
        self.nametag.setFont(font)

    def getStyle(self):
        return self.style

    def setStyle(self, style):
        self.style = style

    def getDialogueArray(self):
        return None

    def playCurrentDialogue(self, dialogue, chatFlags, interrupt = 1):
        if interrupt and self.__currentDialogue is not None:
            self.__currentDialogue.stop()
        self.__currentDialogue = dialogue
        if dialogue:
            base.playSfx(dialogue, node=self)
        elif chatFlags & CFSpeech != 0 and self.nametag.getNumChatPages() > 0:
            self.playDialogueForString(self.nametag.getChat())
            if self.soundChatBubble != None:
                base.playSfx(self.soundChatBubble, node=self)

    def playDialogueForString(self, chatString):
        searchString = chatString.lower()
        if searchString.find(OTPLocalizer.DialogSpecial) >= 0:
            type = 'special'
        elif searchString.find(OTPLocalizer.DialogExclamation) >= 0:
            type = 'exclamation'
        elif searchString.find(OTPLocalizer.DialogQuestion) >= 0:
            type = 'question'
        elif random.randint(0, 1):
            type = 'statementA'
        else:
            type = 'statementB'
        stringLength = len(chatString)
        if stringLength <= OTPLocalizer.DialogLength1:
            length = 1
        elif stringLength <= OTPLocalizer.DialogLength2:
            length = 2
        elif stringLength <= OTPLocalizer.DialogLength3:
            length = 3
        else:
            length = 4
        self.playDialogue(type, length)

    def playDialogue(self, type, length):
        dialogueArray = self.getDialogueArray()
        if dialogueArray == None:
            return
        sfxIndex = None
        if type == 'statementA' or type == 'statementB':
            if length == 1:
                sfxIndex = 0
            elif length == 2:
                sfxIndex = 1
            elif length >= 3:
                sfxIndex = 2
        elif type == 'question':
            sfxIndex = 3
        elif type == 'exclamation':
            sfxIndex = 4
        elif type == 'special':
            sfxIndex = 5
        else:
            notify.error('unrecognized dialogue type: ', type)
        if sfxIndex != None and sfxIndex < len(dialogueArray) and dialogueArray[sfxIndex] != None:
            base.playSfx(dialogueArray[sfxIndex], node=self)
        return

    def getDialogueSfx(self, type, length):
        retval = None
        dialogueArray = self.getDialogueArray()
        if dialogueArray == None:
            return
        sfxIndex = None
        if type == 'statementA' or type == 'statementB':
            if length == 1:
                sfxIndex = 0
            elif length == 2:
                sfxIndex = 1
            elif length >= 3:
                sfxIndex = 2
        elif type == 'question':
            sfxIndex = 3
        elif type == 'exclamation':
            sfxIndex = 4
        elif type == 'special':
            sfxIndex = 5
        else:
            notify.error('unrecognized dialogue type: ', type)
        if sfxIndex != None and sfxIndex < len(dialogueArray) and dialogueArray[sfxIndex] != None:
            retval = dialogueArray[sfxIndex]
        return retval

    def setChatAbsolute(self, chatString, chatFlags, dialogue=None, interrupt=1):
        self.clearChat()
        self.nametag.setChat(chatString, chatFlags)
        self.playCurrentDialogue(dialogue, chatFlags, interrupt)

    def displayTalk(self, chatString):
        if not base.localAvatar.isIgnored(self.doId):
            self.clearChat()
            if ChatUtil.isThought(chatString):
                chatString = ChatUtil.removeThoughtPrefix(chatString)
                self.nametag.setChat(chatString, CFThought)
            else:
                self.nametag.setChat(chatString, CFSpeech | CFTimeout)

    def clearChat(self):
        self.nametag.clearChat()

    def getNameVisible(self):
        return self.__nameVisible

    def setNameVisible(self, bool):
        self.__nameVisible = bool
        if bool:
            self.showName()
        if not bool:
            self.hideName()

    def hideName(self):
        nametag3d = self.nametag.getNametag3d()
        nametag3d.setContents(Nametag.CSpeech | Nametag.CThought)

    def showName(self):
        if self.__nameVisible and (not self.ghostMode):
            nametag3d = self.nametag.getNametag3d()
            nametag3d.setContents(Nametag.CName | Nametag.CSpeech | Nametag.CThought)

    def hideNametag2d(self):
        nametag2d = self.nametag.getNametag2d()
        self.nametag2dContents = 0
        nametag2d.setContents(self.nametag2dContents & self.nametag2dDist)

    def showNametag2d(self):
        nametag2d = self.nametag.getNametag2d()
        self.nametag2dContents = self.nametag2dNormalContents
        if self.ghostMode:
            self.nametag2dContents = Nametag.CSpeech
        nametag2d.setContents(self.nametag2dContents & self.nametag2dDist)

    def hideNametag3d(self):
        nametag3d = self.nametag.getNametag3d()
        nametag3d.setContents(0)

    def showNametag3d(self):
        nametag3d = self.nametag.getNametag3d()
        if self.__nameVisible and (not self.ghostMode):
            nametag3d.setContents(Nametag.CName | Nametag.CSpeech | Nametag.CThought)
        else:
            nametag3d.setContents(0)

    def setPickable(self, flag):
        self.nametag.setActive(flag)

    def clickedNametag(self):
        MagicWordManager.lastClickedNametag = self
        if self.nametag.hasButton():
            self.advancePageNumber()
        elif self.nametag.isActive():
            messenger.send('clickedNametag', [self])

    def setPageChat(self, addressee, paragraph, message, quitButton,
                    extraChatFlags=None, dialogueList=[], pageButton=True):
        self.__chatAddressee = addressee
        self.__chatPageNumber = None
        self.__chatParagraph = paragraph
        self.__chatMessage = message
        if extraChatFlags is None:
            self.__chatFlags = CFSpeech
        else:
            self.__chatFlags = CFSpeech | extraChatFlags
        self.__chatDialogueList = dialogueList
        self.__chatSet = 0
        self.__chatLocal = 0
        self.__updatePageChat()
        if addressee == base.localAvatar.doId:
            if pageButton:
                self.__chatFlags |= CFPageButton
            if quitButton == None:
                self.__chatFlags |= CFNoQuitButton
            elif quitButton:
                self.__chatFlags |= CFQuitButton
            self.b_setPageNumber(self.__chatParagraph, 0)

    def setLocalPageChat(self, message, quitButton, extraChatFlags=None,
                         dialogueList=[]):
        self.__chatAddressee = base.localAvatar.doId
        self.__chatPageNumber = None
        self.__chatParagraph = None
        self.__chatMessage = message
        if extraChatFlags is None:
            self.__chatFlags = CFSpeech
        else:
            self.__chatFlags = CFSpeech | extraChatFlags
        self.__chatDialogueList = dialogueList
        self.__chatSet = 1
        self.__chatLocal = 1
        self.__chatFlags |= CFPageButton
        if quitButton == None:
            self.__chatFlags |= CFNoQuitButton
        elif quitButton:
            self.__chatFlags |= CFQuitButton
        if len(dialogueList) > 0:
            dialogue = dialogueList[0]
        else:
            dialogue = None
        self.clearChat()
        self.setChatAbsolute(message, self.__chatFlags, dialogue)
        self.setPageNumber(None, 0)

    def setPageNumber(self, paragraph, pageNumber, timestamp=None):
        if timestamp is None:
            elapsed = 0.0
        else:
            elapsed = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        self.__chatPageNumber = [paragraph, pageNumber]
        self.__updatePageChat()
        if hasattr(self, 'uniqueName'):
            if pageNumber >= 0:
                messenger.send(self.uniqueName('nextChatPage'), [pageNumber, elapsed])
            else:
                messenger.send(self.uniqueName('doneChatPage'), [elapsed])
        elif pageNumber >= 0:
            messenger.send('nextChatPage', [pageNumber, elapsed])
        else:
            messenger.send('doneChatPage', [elapsed])

    def advancePageNumber(self):
        if (self.__chatAddressee == base.localAvatar.doId) and (
            self.__chatPageNumber is not None) and (
            self.__chatPageNumber[0] == self.__chatParagraph):
            pageNumber = self.__chatPageNumber[1]
            if pageNumber >= 0:
                pageNumber += 1
                if pageNumber >= self.nametag.getNumChatPages():
                    pageNumber = -1
                if self.__chatLocal:
                    self.setPageNumber(self.__chatParagraph, pageNumber)
                else:
                    self.b_setPageNumber(self.__chatParagraph, pageNumber)

    def __updatePageChat(self):
        if (self.__chatPageNumber is not None) and (
            self.__chatPageNumber[0] == self.__chatParagraph):
            pageNumber = self.__chatPageNumber[1]
            if pageNumber >= 0:
                if not self.__chatSet:
                    if len(self.__chatDialogueList) > 0:
                        dialogue = self.__chatDialogueList[0]
                    else:
                        dialogue = None
                    self.setChatAbsolute(self.__chatMessage, self.__chatFlags, dialogue)
                    self.__chatSet = 1
                if pageNumber < self.nametag.getNumChatPages():
                    self.nametag.setPageNumber(pageNumber)
                    if pageNumber > 0:
                        if len(self.__chatDialogueList) > pageNumber:
                            dialogue = self.__chatDialogueList[pageNumber]
                        else:
                            dialogue = None
                        self.playCurrentDialogue(dialogue, self.__chatFlags)
                else:
                    self.clearChat()
            else:
                self.clearChat()

    def getAirborneHeight(self):
        height = self.getPos(self.shadowPlacer.shadowNodePath)
        return height.getZ() + 0.025

    def initializeNametag3d(self):
        self.deleteNametag3d()
        nametagNode = self.nametag.getNametag3d()
        self.nametagNodePath = self.nametag3d.attachNewNode(nametagNode)
        iconNodePath = self.nametag.getNameIcon()
        for cJoint in self.getNametagJoints():
            cJoint.clearNetTransforms()
            cJoint.addNetTransform(nametagNode)

    def deleteNametag3d(self):
        if self.nametagNodePath:
            self.nametagNodePath.removeNode()
            self.nametagNodePath = None

    def initializeBodyCollisions(self, collIdStr):
        self.collTube = CollisionTube(0, 0, 0.5, 0, 0, self.height - self.getRadius(), self.getRadius())
        self.collNode = CollisionNode(collIdStr)
        self.collNode.addSolid(self.collTube)
        self.collNodePath = self.attachNewNode(self.collNode)
        if self.ghostMode:
            self.collNode.setCollideMask(OTPGlobals.GhostBitmask)
        else:
            self.collNode.setCollideMask(OTPGlobals.WallBitmask)

    def stashBodyCollisions(self):
        if hasattr(self, 'collNodePath'):
            self.collNodePath.stash()

    def unstashBodyCollisions(self):
        if hasattr(self, 'collNodePath'):
            self.collNodePath.unstash()

    def disableBodyCollisions(self):
        if hasattr(self, 'collNodePath'):
            self.collNodePath.removeNode()
            del self.collNodePath
        self.collTube = None
        return

    def addActive(self):
        if base.wantNametags:
            try:
                Avatar.ActiveAvatars.remove(self)
            except ValueError:
                pass

            Avatar.ActiveAvatars.append(self)
            self.nametag.manage(base.marginManager)
            self.accept(self.nametag.getUniqueId(), self.clickedNametag)

    def removeActive(self):
        if base.wantNametags:
            try:
                Avatar.ActiveAvatars.remove(self)
            except ValueError:
                pass

            self.nametag.unmanage(base.marginManager)
            self.ignore(self.nametag.getUniqueId())

    def loop(self, animName, restart = 1, partName = None, fromFrame = None, toFrame = None):
        return Actor.loop(self, animName, restart, partName, fromFrame, toFrame)
    
    def createTalkSequence(self, speech, waitTime, name='talkSequence'):
        sequence = Sequence(name=name)

        for text in speech:
            sequence.append(Func(self.setChatAbsolute, text, CFSpeech))
            sequence.append(Wait(len(text.split(' '))))
            sequence.append(Func(self.clearChat))
            sequence.append(Wait(waitTime))

        return sequence

@magicWord(category=CATEGORY_COMMUNITY_MANAGER)
def target():
    """
    Returns the current Spellbook target.
    """
    return 'Your current target is: %s [avId: %s, access: %s]' % (spellbook.getTarget().getName(), spellbook.getTarget().doId, spellbook.getTarget().getAdminAccess())
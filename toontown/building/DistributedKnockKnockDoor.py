from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from panda3d.core import *

import DistributedAnimatedProp
from KnockKnockJokes import *
from toontown.distributed import DelayDelete
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from otp.nametag.NametagGroup import NametagGroup
from otp.nametag.NametagConstants import *
import random

class DistributedKnockKnockDoor(DistributedAnimatedProp.DistributedAnimatedProp):
    def __init__(self, cr):
        DistributedAnimatedProp.DistributedAnimatedProp.__init__(self, cr)

        self.fsm.setName('DistributedKnockKnockDoor')
        self.rimshot = None
        self.knockSfx = None

    def generate(self):
        DistributedAnimatedProp.DistributedAnimatedProp.generate(self)

        self.avatarTracks = []
        self.avatarId = 0

    def announceGenerate(self):
        DistributedAnimatedProp.DistributedAnimatedProp.announceGenerate(self)

        self.accept('exitKnockKnockDoorSphere_' + str(self.propId), self.exitTrigger)
        self.acceptAvatar()

    def disable(self):
        self.ignoreAll()

        DistributedAnimatedProp.DistributedAnimatedProp.disable(self)

    def delete(self):
        DistributedAnimatedProp.DistributedAnimatedProp.delete(self)

        if self.rimshot:
            self.rimshot = None
        if self.knockSfx:
            self.knockSfx = None

    def acceptAvatar(self):
        self.acceptOnce('enterKnockKnockDoorSphere_' + str(self.propId), self.enterTrigger)

    def setAvatarInteract(self, avatarId):
        DistributedAnimatedProp.DistributedAnimatedProp.setAvatarInteract(self, avatarId)

    def avatarExit(self, avatarId):
        if avatarId == self.avatarId:
            self.stopTracks()

    def knockKnockTrack(self, avatar, duration):
        if avatar is None:
            return
        self.rimshot = base.loadSfx('phase_5/audio/sfx/AA_heal_telljoke.ogg')
        self.knockSfx = base.loadSfx('phase_5/audio/sfx/GUI_knock_%s.ogg' % random.randint(1, 4))
        joke = KnockKnockJokes[self.propId % len(KnockKnockJokes)]
        place = base.cr.playGame.getPlace()
        doorName = TTLocalizer.DoorNametag
        self.nametag = None
        self.nametagNP = None
        doorNP = render.find('**/KnockKnockDoorSphere_' + str(self.propId) + ';+s')
        if doorNP.isEmpty():
            self.notify.warning('Could not find KnockKnockDoorSphere_%s' % self.propId)
            return
        self.nametag = NametagGroup()
        self.nametag.setAvatar(doorNP)
        self.nametag.setFont(ToontownGlobals.getToonFont())
        self.nametag.setSpeechFont(ToontownGlobals.getToonFont())
        self.nametag.setName(doorName)
        self.nametag.setActive(0)
        self.nametag.manage(base.marginManager)
        self.nametag.getNametag3d().setBillboardOffset(4)
        nametagNode = self.nametag.getNametag3d()
        self.nametagNP = render.attachNewNode(nametagNode)
        self.nametagNP.setName('knockKnockDoor_nt_' + str(self.propId))
        pos = doorNP.getBounds().getCenter()
        self.nametagNP.setPos(pos + Vec3(0, 0, avatar.getHeight() + 2))
        d = duration * 0.125
        track = Sequence(Parallel(Sequence(Wait(d * 0.5), SoundInterval(self.knockSfx)), Func(self.nametag.setChat, TTLocalizer.DoorKnockKnock, CFSpeech), Wait(d)), Func(avatar.setChatAbsolute, TTLocalizer.DoorWhosThere, CFSpeech | CFTimeout, openEnded=0), Wait(d), Func(self.nametag.setChat, joke[0], CFSpeech), Wait(d), Func(avatar.setChatAbsolute, joke[0] + TTLocalizer.DoorWhoAppendix, CFSpeech | CFTimeout, openEnded=0), Wait(d), Func(self.nametag.setChat, joke[1], CFSpeech))
        if avatar == base.localAvatar:
            track.append(Func(self.sendUpdate, 'requestToonup'))
        track.append(Parallel(SoundInterval(self.rimshot, startTime=2.0), Wait(d * 4)))
        track.append(Func(self.cleanupTrack))
        track.delayDelete = DelayDelete.DelayDelete(avatar, 'knockKnockTrack')
        return track

    def cleanupTrack(self):
        avatar = self.cr.doId2do.get(self.avatarId)
        if avatar:
            avatar.clearChat()
        if self.nametag:
            self.nametag.unmanage(base.marginManager)
            self.nametagNP.removeNode()
            self.nametag.destroy()
        self.nametag = None
        self.nametagNP = None

    def enterOff(self):
        DistributedAnimatedProp.DistributedAnimatedProp.enterOff(self)

    def exitOff(self):
        DistributedAnimatedProp.DistributedAnimatedProp.exitOff(self)

    def enterAttract(self, ts):
        DistributedAnimatedProp.DistributedAnimatedProp.enterAttract(self, ts)
        self.acceptAvatar()

    def exitAttract(self):
        DistributedAnimatedProp.DistributedAnimatedProp.exitAttract(self)

    def enterPlaying(self, ts):
        DistributedAnimatedProp.DistributedAnimatedProp.enterPlaying(self, ts)
        if self.avatarId:
            avatar = self.cr.doId2do.get(self.avatarId, None)
            track = self.knockKnockTrack(avatar, 8)
            if track != None:
                track.start(ts)
                self.avatarTracks.append(track)
        return

    def exitPlaying(self):
        DistributedAnimatedProp.DistributedAnimatedProp.exitPlaying(self)
        self.stopTracks()
    
    def stopTracks(self):
        for track in self.avatarTracks:
            track.pause()
            DelayDelete.cleanupDelayDeletes(track)

        self.cleanupTrack()
        self.avatarTracks = []
        self.avatarId = 0

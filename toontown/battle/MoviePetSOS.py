from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
import random

import BattleParticles
from BattleProps import *
from BattleSounds import *
import MovieCamera
import MovieUtil
from otp.nametag.NametagConstants import *
from toontown.pets import Pet, PetTricks
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownBattleGlobals


notify = DirectNotifyGlobal.directNotify.newCategory('MoviePetSOS')
soundFiles = ('AA_heal_tickle.ogg', 'AA_heal_telljoke.ogg', 'AA_heal_smooch.ogg', 'AA_heal_happydance.ogg', 'AA_heal_pixiedust.ogg', 'AA_heal_juggle.ogg')
offset = Point3(0, 4.0, 0)

def doPetSOSs(PetSOSs):
    if len(PetSOSs) == 0:
        return (None, None)
    track = Sequence()
    textTrack = Sequence()
    for p in PetSOSs:
        ival = __doPetSOS(p)
        if ival:
            track.append(ival)

    camDuration = track.getDuration()
    camTrack = MovieCamera.chooseHealShot(PetSOSs, camDuration)
    return (track, camTrack)


def __healToon(toon, hp, gender, callerToonId, ineffective = 0):
    notify.debug('healToon() - toon: %d hp: %d ineffective: %d' % (toon.doId, hp, ineffective))
    noLaughter = 0
    if ineffective == 1:
        if callerToonId == toon.doId:
            laughter = TTLocalizer.MoviePetSOSTrickFail
        else:
            noLaughter = 1
    else:
        maxDam = ToontownBattleGlobals.AvPropDamage[0][1][0][1]
        if callerToonId == toon.doId:
            if gender == 1:
                laughter = TTLocalizer.MoviePetSOSTrickSucceedBoy
            else:
                laughter = TTLocalizer.MoviePetSOSTrickSucceedGirl
        elif hp >= maxDam - 1:
            laughter = random.choice(TTLocalizer.MovieHealLaughterHits2)
        else:
            laughter = random.choice(TTLocalizer.MovieHealLaughterHits1)
    if not noLaughter:
        toon.setChatAbsolute(laughter, CFSpeech | CFTimeout)
    if hp > 0 and toon.hp != None:
        toon.toonUp(hp)
    else:
        notify.debug('__healToon() - toon: %d hp: %d' % (toon.doId, hp))


def __teleportIn(attack, pet, pos = Point3(0, 0, 0), hpr = Vec3(180.0, 0.0, 0.0)):
    callSfx = loader.loadSfx('phase_5.5/audio/sfx/call_pet.ogg')
    toon = attack['toon']
    seq = Sequence()
    
    seq.append(Func(toon.clearChat))
    seq.append(Func(callSfx.play))
    seq.append(ActorInterval(toon, 'callPet'))
    seq.append(Func(toon.loop, 'neutral'))
    seq.append(Func(pet.reparentTo, attack['battle']))
    seq.append(Func(pet.setPos, pos))
    seq.append(Func(pet.setHpr, hpr))
    seq.append(Func(pet.pose, 'reappear', 0))
    seq.append(pet.getTeleportInTrack())
    seq.append(Func(toon.setSC, 21200 + attack['level']))
    seq.append(Func(pet.loop, 'neutral'))
    seq.append(Func(loader.unloadSfx, callSfx))

    return seq


def __teleportOut(attack, pet):
    a = pet.getTeleportOutTrack()
    c = Func(pet.detachNode)
    d = Func(pet.delete)
    return Sequence(a, c)


def __doPetSOS(heal):
    petProxyId = heal['petId']
    pet = Pet.Pet()
    gender = 0
    if petProxyId in base.cr.doId2do:
        petProxy = base.cr.doId2do[petProxyId]
        if petProxy == None:
            return
        pet.setDNA(petProxy.style)
        pet.setName(petProxy.petName)
        gender = petProxy.gender
    else:
        pet.setDNA([-1, 0, 0, -1, 2, 0, 4, 0, 1])
        pet.setName(TTLocalizer.DefaultDoodleName)
    targets = heal['target']
    ineffective = heal['sidestep']
    level = heal['level']
    track = Sequence(__teleportIn(heal, pet))
    if ineffective:
        trickTrack = Parallel(Wait(1.0), Func(pet.loop, 'neutralSad'), Func(pet.showMood, 'confusion'))
    else:
        trickTrack = PetTricks.getTrickIval(pet, level)
    track.append(trickTrack)
    delay = 4.0
    first = 1
    targetTrack = Sequence()
    for target in targets:
        targetToon = target['toon']
        hp = target['hp']
        callerToonId = heal['toonId']
        reactIval = Func(__healToon, targetToon, hp, gender, callerToonId, ineffective)
        if first == 1:
            first = 0
        targetTrack.append(reactIval)

    mtrack = Parallel(Wait(2.0), targetTrack)
    track.append(mtrack)
    track.append(Sequence(Func(pet.clearMood)))
    track.append(__teleportOut(heal, pet))
    for target in targets:
        targetToon = target['toon']
        track.append(Func(targetToon.clearChat))

    track.append(Func(pet.delete))
    return track

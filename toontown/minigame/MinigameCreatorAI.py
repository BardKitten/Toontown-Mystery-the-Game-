import copy
import random
import time

import DistributedMinigameAI
import DistributedCannonGameAI
import DistributedCatchGameAI
import DistributedCogThiefGameAI
import DistributedDivingGameAI
import DistributedIceGameAI
import DistributedMazeGameAI
import DistributedMinigameTemplateAI
import DistributedPatternGameAI
import DistributedRaceGameAI
import DistributedRingGameAI
import DistributedTagGameAI
import DistributedTargetGameAI
import DistributedTugOfWarGameAI
import DistributedTwoDGameAI
import DistributedVineGameAI
from otp.ai.MagicWordGlobal import *
from toontown.toonbase import ToontownGlobals
from toontown.uberdog import TopToonsGlobals

simbase.forcedMinigameId = simbase.config.GetInt('force-minigame', 0)
RequestMinigame = {}
MinigameZoneRefs = {}

def createMinigame(air, playerArray, trolleyZone, minigameZone=None,
        previousGameId=ToontownGlobals.NoPreviousGameId, newbieIds=[]):
    if minigameZone is None:
        minigameZone = air.allocateZone()
    acquireMinigameZone(minigameZone)
    mgId = None
    mgDiff = None
    mgSzId = None
    for avId in playerArray:
        request = RequestMinigame.get(avId)
        if request is not None:
            mgId, mgKeep, mgDiff, mgSzId = request
            if not mgKeep:
                del RequestMinigame[avId]
            break
    if mgId is not None:
        pass
    elif simbase.forcedMinigameId:
        mgId = simbase.forcedMinigameId
    else:
        randomList = list(copy.copy(ToontownGlobals.MinigamePlayerMatrix[len(playerArray)]))
        if len(playerArray) > 1:
            randomList = list(copy.copy(ToontownGlobals.MinigameIDs))
        if previousGameId != ToontownGlobals.NoPreviousGameId:
            if randomList.count(previousGameId) != 0 and len(randomList) > 1:
                randomList.remove(previousGameId)
        mgId = random.choice(randomList)
    mgCtors = {
        ToontownGlobals.RaceGameId: DistributedRaceGameAI.DistributedRaceGameAI,
        ToontownGlobals.CannonGameId: DistributedCannonGameAI.DistributedCannonGameAI,
        ToontownGlobals.TagGameId: DistributedTagGameAI.DistributedTagGameAI,
        ToontownGlobals.PatternGameId: DistributedPatternGameAI.DistributedPatternGameAI,
        ToontownGlobals.RingGameId: DistributedRingGameAI.DistributedRingGameAI,
        ToontownGlobals.MazeGameId: DistributedMazeGameAI.DistributedMazeGameAI,
        ToontownGlobals.TugOfWarGameId: DistributedTugOfWarGameAI.DistributedTugOfWarGameAI,
        ToontownGlobals.CatchGameId: DistributedCatchGameAI.DistributedCatchGameAI,
        ToontownGlobals.DivingGameId: DistributedDivingGameAI.DistributedDivingGameAI,
        ToontownGlobals.TargetGameId: DistributedTargetGameAI.DistributedTargetGameAI,
        ToontownGlobals.MinigameTemplateId: DistributedMinigameTemplateAI.DistributedMinigameTemplateAI,
        ToontownGlobals.VineGameId: DistributedVineGameAI.DistributedVineGameAI,
        ToontownGlobals.IceGameId: DistributedIceGameAI.DistributedIceGameAI,
        ToontownGlobals.CogThiefGameId: DistributedCogThiefGameAI.DistributedCogThiefGameAI,
        ToontownGlobals.TwoDGameId: DistributedTwoDGameAI.DistributedTwoDGameAI
    }
    try:
        mg = mgCtors[mgId](air, mgId)
    except KeyError:
        raise Exception, 'unknown minigame ID: %s' % mgId
    mg.setExpectedAvatars(playerArray)
    mg.setNewbieIds(newbieIds)
    mg.setTrolleyZone(trolleyZone)
    mg.setDifficultyOverrides(mgDiff, mgSzId)
    mg.generateWithRequired(minigameZone)
    toons = []
    for doId in playerArray:
        toon = simbase.air.doId2do.get(doId)
        if toon is not None:
            toons.append(toon)
    for toon in toons:
        messenger.send('topToonsManager-event', [toon.doId, TopToonsGlobals.CAT_TROLLEY, 1])
    for toon in toons:
        simbase.air.questManager.toonPlayedMinigame(toon, toons)
    retVal = {}
    retVal['minigameZone'] = minigameZone
    retVal['minigameId'] = mgId
    return retVal


def acquireMinigameZone(zoneId):
    if zoneId not in MinigameZoneRefs:
        MinigameZoneRefs[zoneId] = 0
    MinigameZoneRefs[zoneId] += 1


def releaseMinigameZone(zoneId):
    MinigameZoneRefs[zoneId] -= 1
    if MinigameZoneRefs[zoneId] <= 0:
        del MinigameZoneRefs[zoneId]
        simbase.air.deallocateZone(zoneId)


@magicWord(category=CATEGORY_PROGRAMMER, types=[str, str])
def minigame(command, arg0=None):
    """
    A command set for Trolley minigames.
    """
    command = command.lower()
    invoker = spellbook.getInvoker()
    if (arg0 is None) and (command not in ('remove', 'abort')):
        return '~minigame %s takes exactly 1 argument (0 given)' % command
    elif arg0 and (command in ('remove', 'abort')):
        return '~minigame %s takes no arguments (1 given)' % command
    if command == 'request':
        for name in ToontownGlobals.MinigameNames:
            if arg0.lower() != name:
                continue
            name = ToontownGlobals.MinigameNames[name]
            RequestMinigame[invoker.doId] = (name, False, None, None)
            return 'Stored your request for minigame: ' + arg0
        return "Couldn't store your request for minigame: " + arg0
    if command == 'force':
        for name in ToontownGlobals.MinigameNames:
            if arg0.lower() != name:
                break
            name = ToontownGlobals.MinigameNames[name]
            RequestMinigame[invoker.doId] = (name, True, None, None)
            return 'Stored your force request for minigame: ' + arg0
        return "Couldn't store your force request for minigame: " + arg0
    if command == 'remove':
        if invoker.doId in RequestMinigame:
            del RequestMinigame[invoker.doId]
            return 'Your minigame request has been removed.'
        return 'You have no minigame requests!'
    if command == 'difficulty':
        if invoker.doId not in RequestMinigame:
            return 'You have no minigame requests!'
        try:
            arg0 = int(arg0)
        except:
            return 'Argument 0 must be of type: ' + str(int)
        request = RequestMinigame[invoker.doId]
        RequestMinigame[invoker.doId] = request[:2] + (arg0,) + request[3:]
        return 'Stored your request for the minigame difficulty: ' + str(arg0)
    if command == 'safezone':
        if invoker.doId not in RequestMinigame:
            return 'You have no minigame requests!'
        try:
            arg0 = int(arg0)
        except:
            return 'Argument 0 must be of type: ' + str(int)
        request = RequestMinigame[invoker.doId]
        RequestMinigame[invoker.doId] = request[:3] + (arg0,) + request[4:]
        return 'Stored your request for the minigame safezone: ' + str(arg0)
    if command == 'abort':
        for do in simbase.air.doId2do.values():
            if not isinstance(do, DistributedMinigameAI.DistributedMinigameAI):
                continue
            if invoker.doId not in do.avIdList:
                continue
            do.setGameAbort()
            return 'Skipped minigame!'
        return 'You are not currently in a minigame!'
    return 'Invalid command.'

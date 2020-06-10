from otp.ai.AIBaseGlobal import *
from direct.distributed.ClockDelta import *
from direct.distributed import DistributedObjectAI
import Level
from direct.directnotify import DirectNotifyGlobal
import EntityCreatorAI
from direct.showbase.PythonUtil import Functor, weightedChoice

class DistributedLevelAI(DistributedObjectAI.DistributedObjectAI, Level.Level):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLevelAI')

    def __init__(self, air, zoneId, entranceId, avIds):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        Level.Level.__init__(self)
        self.zoneId = zoneId
        self.entranceId = entranceId
        if len(avIds) <= 0 or len(avIds) > 4:
            self.notify.warning('How do we have this many avIds? avIds: %s' % avIds)
        self.avIdList = avIds
        self.numPlayers = len(self.avIdList)
        self.presentAvIds = list(self.avIdList)
        self.notify.debug('expecting avatars: %s' % str(self.avIdList))

    def setLevelSpec(self, levelSpec):
        self.levelSpec = levelSpec

    def generate(self, levelSpec = None):
        self.notify.debug('generate')
        DistributedObjectAI.DistributedObjectAI.generate(self)
        if levelSpec == None:
            levelSpec = self.levelSpec
        self.initializeLevel(levelSpec)
        self.sendUpdate('setZoneIds', [self.zoneIds])
        self.sendUpdate('setStartTimestamp', [self.startTimestamp])

    def getLevelZoneId(self):
        return self.zoneId

    def getAvIds(self):
        return self.avIdList

    def getEntranceId(self):
        return self.entranceId

    def getBattleCreditMultiplier(self):
        return 1.0

    def delete(self, deAllocZone = True):
        self.notify.debug('delete')
        self.destroyLevel()
        self.ignoreAll()
        if deAllocZone:
            self.air.deallocateZone(self.zoneId)
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def initializeLevel(self, levelSpec):
        self.startTime = globalClock.getRealTime()
        self.startTimestamp = globalClockDelta.localToNetworkTime(self.startTime, bits=32)
        lol = zip([1] * levelSpec.getNumScenarios(), range(levelSpec.getNumScenarios()))
        scenarioIndex = weightedChoice(lol)
        Level.Level.initializeLevel(self, self.doId, levelSpec, scenarioIndex)
        for avId in self.avIdList:
            self.acceptOnce(self.air.getAvatarExitEvent(avId), Functor(self.handleAvatarDisconnect, avId))

        self.allToonsGoneBarrier = self.beginBarrier('allToonsGone', self.avIdList, 3 * 24 * 60 * 60, self.allToonsGone)

    def handleAvatarDisconnect(self, avId):
        try:
            self.presentAvIds.remove(avId)
            DistributedLevelAI.notify.warning('av %s has disconnected' % avId)
        except:
            DistributedLevelAI.notify.warning('got disconnect for av %s, not in list' % avId)

        if not self.presentAvIds:
            self.allToonsGone([])

    def allToonsGone(self, toonsThatCleared):
        DistributedLevelAI.notify.info('allToonsGone')
        if hasattr(self, 'allToonsGoneBarrier'):
            self.ignoreBarrier(self.allToonsGoneBarrier)
            del self.allToonsGoneBarrier
        for avId in self.avIdList:
            self.ignore(self.air.getAvatarExitEvent(avId))

        self.requestDelete()

    def createEntityCreator(self):
        return EntityCreatorAI.EntityCreatorAI(level=self)

    def setOuch(self, penalty):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        self.notify.debug('setOuch %s' % penalty)
        if av and penalty > 0:
            av.takeDamage(penalty)
            if av.getHp() <= 0:
                av.inventory.zeroInv()
                av.d_setInventory(av.inventory.makeNetString())

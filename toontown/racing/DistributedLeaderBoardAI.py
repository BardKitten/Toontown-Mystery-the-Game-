from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.racing import RaceGlobals
import random, time

class DistributedLeaderBoardAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedLeaderBoardAI")

    def __init__(self, air, displays):
        DistributedObjectAI.__init__(self, air)
        self.displays = displays
        self.display = [0, 0, []]
        self.currentId = 0
        self.posHpr = (0, 0, 0, 0, 0, 0)

    def generateWithRequired(self, zoneId):
        DistributedObjectAI.generateWithRequired(self, zoneId)
        self.accept('goofyLeaderboardChange', self.__setDisplay)
        self.accept('goofyLeaderboardDisplay', self.__setDisplayRace)
        self.__updateDisplay()
        self.switchTask = taskMgr.doMethodLater(15, self.nextDisplay, 'leaderboardSwitchTask-%s' % random.random())

    def delete(self):
        DistributedObjectAI.delete(self)
        self.ignoreAll()
        taskMgr.remove(self.switchTask)

    def setPosHpr(self, x, y, z, h, p, r):
        self.posHpr = (x, y, z, h, p, r)

    def getPosHpr(self):
        return self.posHpr

    def getDisplay(self):
        return self.display

    def getDisplayName(self):
        return '%s, %s' % (self.display[0], self.display[1])

    def getMaxTimeDifference(self):
        return RaceGlobals.MaxTimeDifference[self.display[1]]

    def hasMaxTimeDifference(self):
        return self.display[1] in RaceGlobals.MaxTimeDifference

    def nextDisplay(self, task=None):
        self.__updateDisplay()
        self.currentId += 1

        if self.currentId >= len(self.displays):
            self.currentId = 0

        return Task.again

    def __setDisplayRace(self, race):
        self.currentId = race
        self.__updateDisplay()

    def __updateDisplay(self):
        race = self.displays[self.currentId]

        self.display = [race[0], race[1], []]
        self.__setDisplay()

    def __setDisplay(self):
        database = self.air.leaderboardMgr.getDatabase()
        displayName = self.getDisplayName()

        if not displayName in database:
            self.sendDisplayUpdate([])
            return

        displayEntry = database[displayName]

        if self.hasMaxTimeDifference():
            difference = time.time() - displayEntry[0]

            if difference >= self.getMaxTimeDifference():
                self.air.leaderboardMgr.clearRace(displayName)
                return

        self.sendDisplayUpdate(self.air.leaderboardMgr.trimList(displayEntry[1]))

    def sendDisplayUpdate(self, players):
        self.display[2] = players
        self.sendUpdate('setDisplay', self.display)

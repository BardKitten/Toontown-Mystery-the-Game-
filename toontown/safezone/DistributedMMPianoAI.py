from otp.ai.AIBase import *
from toontown.toonbase.ToontownGlobals import *
from direct.distributed.ClockDelta import *
from direct.distributed import DistributedObjectAI
from direct.task import Task
PianoSpeeds = [2, 4, 6, 8, 10, 12, 15, 20]
PianoMaxSpeed = PianoSpeeds[-1]
PianoSlowDownFactor = 0.7
PianoSlowDownInterval = 6.0
PianoSlowDownMinimum = 0.1

class DistributedMMPianoAI(DistributedObjectAI.DistributedObjectAI):

    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.spinStartTime = 0.0
        self.rpm = 0.0
        self.degreesPerSecond = (self.rpm / 60.0) * 360.0
        self.offset = 0.0
        self.direction = 1

    def requestSpeedUp(self):
        if self.rpm < PianoMaxSpeed:
            for speed in PianoSpeeds:
                if speed > self.rpm:
                    break

            self.updateSpeed(speed, self.direction)

        self.d_playSpeedUp(self.air.getAvatarIdFromSender())
        self.__slowDownLater()

    def requestChangeDirection(self):
        rpm = self.rpm
        if rpm == 0.0:
            rpm = PianoSpeeds[0]

        self.updateSpeed(rpm, -(self.direction))
        self.__slowDownLater()
        self.d_playChangeDirection(self.air.getAvatarIdFromSender())

    def d_setSpeed(self, rpm, offset, startTime):
        self.sendUpdate('setSpeed', [rpm, offset, globalClockDelta.localToNetworkTime(startTime)])

    def d_playSpeedUp(self, avId):
        self.sendUpdate('playSpeedUp', [avId])

    def d_playChangeDirection(self, avId):
        self.sendUpdate('playChangeDirection', [avId])

    def updateSpeed(self, rpm, direction):
        now = globalClock.getFrameTime()
        heading = self.degreesPerSecond * (now - self.spinStartTime) + self.offset
        self.rpm = rpm
        self.direction = direction
        self.degreesPerSecond = (rpm / 60.0) * 360.0 * direction
        self.offset = heading % 360.0
        self.spinStartTime = now
        self.d_setSpeed(self.rpm * self.direction, self.offset, self.spinStartTime)

    def __slowDownLater(self):
        taskName = self.uniqueName('slowDown')
        taskMgr.remove(taskName)
        taskMgr.doMethodLater(PianoSlowDownInterval, self.__slowDown, taskName)

    def __slowDown(self, task):
        rpm = self.rpm * PianoSlowDownFactor
        if rpm < PianoSlowDownMinimum:
            self.updateSpeed(0.0, self.direction)
        else:
            self.updateSpeed(rpm, self.direction)
            self.__slowDownLater()
        return Task.done

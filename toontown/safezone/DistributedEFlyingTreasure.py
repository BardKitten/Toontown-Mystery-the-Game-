from DistributedTreasure import DistributedTreasure
import math, random

class DistributedEFlyingTreasure(DistributedTreasure):

    def __init__(self, cr):
        DistributedTreasure.__init__(self, cr)
        self.scale = 2
        self.delT = math.pi * 2.0 * random.random()
        self.shadow = 0

    def disable(self):
        DistributedTreasure.disable(self)
        taskMgr.remove(self.taskName('flying-treasure'))

    def setPosition(self, x, y, z):
        DistributedTreasure.setPosition(self, x, y, z)
        self.initPos = self.nodePath.getPos()
        taskMgr.add(self.animateTask, self.taskName('flying-treasure'))

    def animateTask(self, task):
        pos = self.initPos
        t = 0.5 * math.pi * globalClock.getFrameTime()
        dZ = 5.0 * math.sin(t + self.delT)
        self.nodePath.setPos(pos[0], pos[1], pos[2] + dZ)
        return task.cont

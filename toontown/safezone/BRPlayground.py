from direct.task.Task import Task
from toontown.safezone import Playground
import random

class BRPlayground(Playground.Playground):
    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)
        taskMgr.doMethodLater(1, self.__windTask, 'BR-wind')

    def exit(self):
        Playground.Playground.exit(self)
        taskMgr.remove('BR-wind')

    def __windTask(self, task):
        base.playSfx(random.choice(self.loader.windSound))
        time = random.random() * 8.0 + 1
        taskMgr.doMethodLater(time, self.__windTask, 'BR-wind')
        return Task.done

import gc
import math
import sys
import time

from direct.directnotify.DirectNotifyGlobal import *
from direct.interval.IntervalManager import ivalMgr
from direct.showbase import EventManager
from direct.showbase import PythonUtil
from direct.showbase.BulletinBoardGlobal import *
from direct.showbase.EventManagerGlobal import *
from direct.showbase.JobManagerGlobal import *
from direct.showbase.MessengerGlobal import *
from direct.showbase.PythonUtil import *
from direct.task import Task
from direct.task.TaskManagerGlobal import *
from otp.otpbase import BackupManager
from panda3d.core import *


class AIBase:
    notify = directNotify.newCategory('AIBase')

    def __init__(self):
        self.config = getConfigShowbase()
        __builtins__['__dev__'] = self.config.GetBool('want-dev', 0)
        if self.config.GetBool('use-vfs', 1):
            vfs = VirtualFileSystem.getGlobalPtr()
        else:
            vfs = None
        self.wantTk = self.config.GetBool('want-tk', 0)
        self.AISleep = self.config.GetFloat('ai-sleep', 0.04)
        self.AIRunningNetYield = self.config.GetBool('ai-running-net-yield', 0)
        self.AIForceSleep = self.config.GetBool('ai-force-sleep', 0)
        self.eventMgr = eventMgr
        self.messenger = messenger
        self.bboard = bulletinBoard
        self.taskMgr = taskMgr
        Task.TaskManager.taskTimerVerbose = self.config.GetBool('task-timer-verbose', 0)
        Task.TaskManager.extendedExceptions = self.config.GetBool('extended-exceptions', 0)
        self.sfxManagerList = None
        self.musicManager = None
        self.jobMgr = jobMgr
        self.hidden = NodePath('hidden')
        self.graphicsEngine = GraphicsEngine()
        globalClock = ClockObject.getGlobalClock()
        self.trueClock = TrueClock.getGlobalPtr()
        globalClock.setRealTime(self.trueClock.getShortTime())
        globalClock.setAverageFrameRateInterval(30.0)
        globalClock.tick()
        taskMgr.globalClock = globalClock
        __builtins__['ostream'] = Notify.out()
        __builtins__['globalClock'] = globalClock
        __builtins__['vfs'] = vfs
        __builtins__['hidden'] = self.hidden
        PythonUtil.recordFunctorCreationStacks()
        self.wantStats = self.config.GetBool('want-pstats', 0)
        Task.TaskManager.pStatsTasks = self.config.GetBool('pstats-tasks', 0)
        taskMgr.resumeFunc = PStatClient.resumeAfterPause
        wantFakeTextures = self.config.GetBool('want-fake-textures-ai', 1)
        if wantFakeTextures:
            loadPrcFileData('aibase', 'textures-header-only 1')
        self.wantPets = self.config.GetBool('want-pets', 1)
        if self.wantPets:
            from toontown.pets import PetConstants
            self.petMoodTimescale = self.config.GetFloat('pet-mood-timescale', 1.0)
            self.petMoodDriftPeriod = self.config.GetFloat('pet-mood-drift-period', PetConstants.MoodDriftPeriod)
            self.petThinkPeriod = self.config.GetFloat('pet-think-period', PetConstants.ThinkPeriod)
            self.petMovePeriod = self.config.GetFloat('pet-move-period', PetConstants.MovePeriod)
            self.petPosBroadcastPeriod = self.config.GetFloat('pet-pos-broadcast-period', PetConstants.PosBroadcastPeriod)
        self.wantBingo = self.config.GetBool('want-fish-bingo', 1)
        self.wantKarts = self.config.GetBool('want-karts', 1)
        self.backups = BackupManager.BackupManager(
            filepath=self.config.GetString('backups-filepath', 'dependencies/backups/'),
            extension=self.config.GetString('backups-extension', '.json'))
        self.createStats()
        self.restart()

    def createStats(self, hostname = None, port = None):
        if not self.wantStats:
            return False
        if PStatClient.isConnected():
            PStatClient.disconnect()
        if hostname is None:
            hostname = ''
        if port is None:
            port = -1
        PStatClient.connect(hostname, port)
        return PStatClient.isConnected()

    def __sleepCycleTask(self, task):
        time.sleep(self.AISleep)
        return Task.cont

    def __resetPrevTransform(self, state):
        PandaNode.resetAllPrevTransform()
        return Task.cont

    def __ivalLoop(self, state):
        ivalMgr.step()
        return Task.cont

    def __igLoop(self, state):
        self.graphicsEngine.renderFrame()
        return Task.cont

    def shutdown(self):
        self.taskMgr.remove('ivalLoop')
        self.taskMgr.remove('igLoop')
        self.taskMgr.remove('aiSleep')
        self.eventMgr.shutdown()

    def restart(self):
        self.shutdown()
        self.taskMgr.add(self.__resetPrevTransform, 'resetPrevTransform', priority=-51)
        self.taskMgr.add(self.__ivalLoop, 'ivalLoop', priority=20)
        self.taskMgr.add(self.__igLoop, 'igLoop', priority=50)
        if self.config.GetBool('garbage-collect-states', 1):
            self.taskMgr.add(self.__garbageCollectStates, 'garbageCollectStates', priority=46)
        if self.AISleep >= 0 and (not self.AIRunningNetYield or self.AIForceSleep):
            self.taskMgr.add(self.__sleepCycleTask, 'aiSleep', priority=55)
        self.eventMgr.restart()
    
    def __garbageCollectStates(self, state):
        TransformState.garbageCollect()
        RenderState.garbageCollect()
        return Task.cont

    def getRepository(self):
        return self.air

    def run(self):
        self.taskMgr.run()

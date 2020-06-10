from panda3d.core import *
from direct.task.Task import Task
from toontown.battle import BattleParticles
import colorsys

def createSnow(geom):
    snow = BattleParticles.loadParticleFile('snowdisk.ptf')
    snow.setPos(0, 0, 5)
    snowRender = geom.attachNewNode('snowRender')
    snowRender.setDepthWrite(0)
    snowRender.setBin('fixed', 1)

    return snow, snowRender

def startUnderwaterFog():
    if not base.wantFog:
        return

    stopUnderwaterFog()
    taskMgr.add(__updateUnderwaterFog, 'underwaterFog')

def stopUnderwaterFog():
    taskMgr.remove('underwaterFog')

def __updateUnderwaterFog(task):
    fog = base.cr.playGame.hood.fog if hasattr(base.cr.playGame.hood, 'fog') else base.cr.playGame.place.fog
    saturation = min(max((base.localAvatar.getZ() / -12.3), 0.51), 1)
    fog.setColor(*colorsys.hsv_to_rgb(0.616, saturation, 0.5))
    return task.cont

def cloudSkyTrack(task):
    task.h += globalClock.getDt() * 0.25

    if task.cloud1.isEmpty() or task.cloud2.isEmpty():
        return

    task.cloud1.setH(task.h)
    task.cloud2.setH(-task.h * 0.8)
    return task.cont

def startCloudSky(hood, parent=camera, effects=CompassEffect.PRot | CompassEffect.PZ):
    hood.sky.reparentTo(parent)
    hood.sky.setDepthTest(0)
    hood.sky.setDepthWrite(0)
    hood.sky.setBin('background', 100)
    hood.sky.find('**/Sky').reparentTo(hood.sky, -1)
    hood.sky.reparentTo(parent)
    hood.sky.setZ(0.0)
    hood.sky.setHpr(0.0, 0.0, 0.0)

    ce = CompassEffect.make(NodePath(), effects)

    hood.sky.node().setEffect(ce)
    skyTrackTask = Task(hood.skyTrack)
    skyTrackTask.h = 0
    skyTrackTask.cloud1 = hood.sky.find('**/cloud1')
    skyTrackTask.cloud2 = hood.sky.find('**/cloud2')

    if not skyTrackTask.cloud1.isEmpty() and not skyTrackTask.cloud2.isEmpty():
        taskMgr.add(skyTrackTask, 'skyTrack')
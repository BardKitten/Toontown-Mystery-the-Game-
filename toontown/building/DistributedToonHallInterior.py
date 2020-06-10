from direct.actor import Actor
from direct.interval.IntervalGlobal import *
from direct.showbase import Audio3DManager
from otp.ai.MagicWordGlobal import *
from toontown.dna.DNAParser import *
from toontown.hood import ZoneUtil
from toontown.toon import DistributedNPCToonBase
from DistributedToonInterior import DistributedToonInterior
import ToonInteriorColors, random

class DistributedToonHallInterior(DistributedToonInterior):

    def setup(self):
        self.dnaStore = base.cr.playGame.dnaStore
        self.randomGenerator = random.Random()
        self.randomGenerator.seed(self.zoneId)
        interior = self.randomDNAItem('TI_hall', self.dnaStore.findNode)
        self.interior = interior.copyTo(render)
        hoodId = ZoneUtil.getCanonicalHoodId(self.zoneId)
        self.colors = ToonInteriorColors.colors[hoodId]
        self.replaceRandomInModel(self.interior)
        doorModelName = 'door_double_round_ul'
        if doorModelName[-1:] == 'r':
            doorModelName = doorModelName[:-1] + 'l'
        else:
            doorModelName = doorModelName[:-1] + 'r'
        door = self.dnaStore.findNode(doorModelName)
        door_origin = render.find('**/door_origin;+s')
        doorNP = door.copyTo(door_origin)
        door_origin.setScale(0.8, 0.8, 0.8)
        door_origin.setPos(door_origin, 0, -0.025, 0)
        color = self.randomGenerator.choice(self.colors['TI_door'])
        setupDoor(doorNP, self.interior, door_origin, self.dnaStore, str(self.block), color)
        doorFrame = doorNP.find('door_*_flat')
        doorFrame.wrtReparentTo(self.interior)
        doorFrame.setColor(color)
        del self.colors
        del self.dnaStore
        del self.randomGenerator
        self.interior.flattenMedium()
        for npcToon in self.cr.doFindAllInstances(DistributedNPCToonBase.DistributedNPCToonBase):
            npcToon.initToonState()

        self.createSillyMeter()

    def createSillyMeter(self):
        ropes = loader.loadModel('phase_4/models/modules/tt_m_ara_int_ropes')
        ropes.reparentTo(self.interior)
        self.sillyMeter = Actor.Actor('phase_4/models/props/tt_a_ara_ttc_sillyMeter_default', {'arrowTube': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_arrowFluid',
         'phaseOne': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseOne',
         'phaseTwo': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseTwo',
         'phaseThree': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseThree',
         'phaseFour': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseFour',
         'phaseFourToFive': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseFourToFive',
         'phaseFive': 'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseFive'})
        self.sillyMeter.reparentTo(self.interior)
        self.smPhase1 = self.sillyMeter.find('**/stage1')
        self.smPhase2 = self.sillyMeter.find('**/stage2')
        self.smPhase3 = self.sillyMeter.find('**/stage3')
        self.smPhase4 = self.sillyMeter.find('**/stage4')
        self.smPhase2.hide()
        self.smPhase3.hide()
        self.smPhase4.hide()
        thermometerLocator = self.sillyMeter.findAllMatches('**/uvj_progressBar')[1]
        thermometerMesh = self.sillyMeter.find('**/tube')
        thermometerMesh.setTexProjector(thermometerMesh.findTextureStage('default'), thermometerLocator, self.sillyMeter)
        self.sillyMeter.flattenMedium()
        self.sillyMeter.makeSubpart('arrow', ['uvj_progressBar*', 'def_springA'])
        self.sillyMeter.makeSubpart('meter', ['def_pivot'], ['uvj_progressBar*', 'def_springA'])
        self.audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)
        self.phase1Sfx = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseOne.ogg')
        self.phase1Sfx.setLoop(True)
        self.phase2Sfx = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseTwo.ogg')
        self.phase2Sfx.setLoop(True)
        self.phase3Sfx = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseThree.ogg')
        self.phase3Sfx.setLoop(True)
        self.phase4Sfx = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseFour.ogg')
        self.phase4Sfx.setLoop(True)
        self.phase4To5Sfx = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseFourToFive.ogg')
        self.phase4To5Sfx.setLoop(False)
        self.phase5Sfx = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseFive.ogg')
        self.phase5Sfx.setLoop(True)
        self.arrowSfx = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterArrow.ogg')
        self.arrowSfx.setLoop(False)
        self.audio3d.setDropOffFactor(0.1)

        self.startSillyMeter(config.GetInt('silly-meter-phase', 12))

    def startSillyMeter(self, phase):
        self.stopSillyMeter()

        if hasattr(self, 'enterPhase%s' % phase):
            getattr(self, 'enterPhase%s' % phase)()
            self.phase = phase

    def stopSillyMeter(self):
        if hasattr(self, 'phase') and hasattr(self, 'exitPhase%s' % self.phase):
            getattr(self, 'exitPhase%s' % self.phase)()

    def enterPhase0(self):
        self.animSeq = Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=1, endFrame=30), Sequence(Func(self.phase1Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase1Sfx, self.sillyMeter)))
        self.animSeq.start()
        self.sillyMeter.loop('phaseOne', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase0(self):
        self.animSeq.finish()
        del self.animSeq
        self.audio3d.detachSound(self.phase1Sfx)
        self.phase1Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase1(self):
        self.audio3d.attachSoundToObject(self.phase1Sfx, self.sillyMeter)
        self.animSeq = Sequence(Sequence(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', constrainedLoop=0, startFrame=31, endFrame=42), Func(self.arrowSfx.play)), Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=42, endFrame=71), Sequence(Func(self.phase1Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase1Sfx, self.sillyMeter))))
        self.animSeq.start()
        self.sillyMeter.loop('phaseOne', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase1(self):
        self.audio3d.detachSound(self.phase1Sfx)
        self.phase1Sfx.stop()
        self.animSeq.finish()
        del self.animSeq
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase2(self):
        self.animSeq = Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=42, endFrame=71), Sequence(Func(self.phase1Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase1Sfx, self.sillyMeter)))
        self.animSeq.start()
        self.smPhase2.show()
        self.sillyMeter.loop('phaseOne', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase2(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.audio3d.detachSound(self.phase1Sfx)
        self.phase1Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase3(self):
        self.animSeq = Sequence(Sequence(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', constrainedLoop=0, startFrame=72, endFrame=83), Func(self.arrowSfx.play)), Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=83, endFrame=112), Sequence(Func(self.phase1Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase1Sfx, self.sillyMeter))))
        self.animSeq.start()
        self.smPhase2.show()
        self.sillyMeter.loop('phaseOne', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase3(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.audio3d.detachSound(self.phase1Sfx)
        self.phase1Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase4(self):
        self.animSeq = Sequence(Sequence(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', constrainedLoop=0, startFrame=113, endFrame=124), Func(self.arrowSfx.play)), Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=124, endFrame=153), Sequence(Func(self.phase1Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase1Sfx, self.sillyMeter))))
        self.animSeq.start()
        self.smPhase2.show()
        self.sillyMeter.loop('phaseOne', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase4(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.audio3d.detachSound(self.phase1Sfx)
        self.phase1Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase5(self):
        self.animSeq = Sequence(Sequence(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', constrainedLoop=0, startFrame=154, endFrame=165), Func(self.arrowSfx.play)), Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=165, endFrame=194), Sequence(Func(self.phase2Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase2Sfx, self.sillyMeter))))
        self.animSeq.start()
        self.smPhase2.show()
        self.sillyMeter.loop('phaseTwo', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase5(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.audio3d.detachSound(self.phase2Sfx)
        self.phase2Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase6(self):
        self.animSeq = Sequence(Sequence(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', constrainedLoop=0, startFrame=195, endFrame=206), Func(self.arrowSfx.play)), Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=206, endFrame=235), Sequence(Func(self.phase2Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase2Sfx, self.sillyMeter))))
        self.animSeq.start()
        self.smPhase2.show()
        self.sillyMeter.loop('phaseTwo', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase6(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.audio3d.detachSound(self.phase2Sfx)
        self.phase2Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase7(self):
        self.animSeq = Sequence(Sequence(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', constrainedLoop=0, startFrame=236, endFrame=247), Func(self.arrowSfx.play)), Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=247, endFrame=276), Sequence(Func(self.phase3Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase3Sfx, self.sillyMeter))))
        self.animSeq.start()
        self.smPhase2.show()
        self.smPhase3.show()
        self.sillyMeter.loop('phaseThree', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase7(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.smPhase3.hide()
        self.audio3d.detachSound(self.phase3Sfx)
        self.phase3Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase8(self):
        self.animSeq = Sequence(Sequence(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', constrainedLoop=0, startFrame=277, endFrame=288), Func(self.arrowSfx.play)), Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=288, endFrame=317), Sequence(Func(self.phase3Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase3Sfx, self.sillyMeter))))
        self.animSeq.start()
        self.smPhase2.show()
        self.smPhase3.show()
        self.sillyMeter.loop('phaseThree', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase8(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.smPhase3.hide()
        self.audio3d.detachSound(self.phase3Sfx)
        self.phase3Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase9(self):
        self.animSeq = Sequence(Sequence(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', constrainedLoop=0, startFrame=318, endFrame=329), Func(self.arrowSfx.play)), Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=329, endFrame=358), Sequence(Func(self.phase3Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase3Sfx, self.sillyMeter))))
        self.animSeq.start()
        self.smPhase2.show()
        self.smPhase3.show()
        self.sillyMeter.loop('phaseThree', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase9(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.smPhase3.hide()
        self.audio3d.detachSound(self.phase3Sfx)
        self.phase3Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase10(self):
        self.animSeq = Sequence(Sequence(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', constrainedLoop=0, startFrame=359, endFrame=370), Func(self.arrowSfx.play)), Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=370, endFrame=399), Sequence(Func(self.phase4Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase4Sfx, self.sillyMeter))))
        self.animSeq.start()
        self.smPhase2.show()
        self.smPhase3.show()
        self.smPhase4.show()
        self.sillyMeter.loop('phaseFour', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase10(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.smPhase3.hide()
        self.smPhase4.hide()
        self.audio3d.detachSound(self.phase4Sfx)
        self.phase4Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase11(self):
        self.animSeq = Sequence(Sequence(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', constrainedLoop=0, startFrame=400, endFrame=411), Func(self.arrowSfx.play)), Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=411, endFrame=440), Sequence(Func(self.phase4Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase4Sfx, self.sillyMeter))))
        self.animSeq.start()
        self.smPhase2.show()
        self.smPhase3.show()
        self.smPhase4.show()
        self.sillyMeter.loop('phaseFour', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase11(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.smPhase3.hide()
        self.smPhase4.hide()
        self.audio3d.detachSound(self.phase4Sfx)
        self.phase4Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase12(self):
        self.animSeq = Sequence(Sequence(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', constrainedLoop=0, startFrame=441, endFrame=452), Func(self.arrowSfx.play)), Parallel(ActorInterval(self.sillyMeter, 'arrowTube', partName='arrow', duration=604800, constrainedLoop=1, startFrame=452, endFrame=481), Sequence(Func(self.phase4Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase4Sfx, self.sillyMeter))))
        self.animSeq.start()
        self.smPhase2.show()
        self.smPhase3.show()
        self.smPhase4.show()
        self.sillyMeter.loop('phaseFour', partName='meter')
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase12(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.smPhase3.hide()
        self.smPhase4.hide()
        self.audio3d.detachSound(self.phase4Sfx)
        self.phase4Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase13(self):
        self.animSeq = Sequence(Parallel(Func(self.phase4To5Sfx.play), ActorInterval(self.sillyMeter, 'phaseFourToFive', constrainedLoop=0, startFrame=1, endFrame=120)), Parallel(ActorInterval(self.sillyMeter, 'phaseFive', duration=604800, constrainedLoop=1, startFrame=1, endFrame=48), Sequence(Func(self.phase5Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase5Sfx, self.sillyMeter))))
        self.animSeq.start()
        self.smPhase2.show()
        self.smPhase3.show()
        self.smPhase4.show()
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase13(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.smPhase3.hide()
        self.smPhase4.hide()
        self.audio3d.detachSound(self.phase5Sfx)
        self.phase5Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterPhase14(self):
        self.animSeq = Parallel(ActorInterval(self.sillyMeter, 'phaseFive', duration=604800, constrainedLoop=1, startFrame=1, endFrame=48), Sequence(Func(self.phase5Sfx.play), Func(self.audio3d.attachSoundToObject, self.phase5Sfx, self.sillyMeter)))
        self.animSeq.start()
        self.smPhase2.show()
        self.smPhase3.show()
        self.smPhase4.show()
        self.accept('SillyMeterPhase', self.startSillyMeter)

    def exitPhase14(self):
        self.animSeq.finish()
        del self.animSeq
        self.smPhase2.hide()
        self.smPhase3.hide()
        self.smPhase4.hide()
        self.audio3d.detachSound(self.phase5Sfx)
        self.phase5Sfx.stop()
        self.sillyMeter.stop()
        self.ignore('SillyMeterPhase')

    def enterOff(self):
        self.ignore('SillyMeterPhase')
        if hasattr(self, 'sillyMeter'):
            del self.sillyMeter
        if hasattr(self, 'smPhase1'):
            del self.smPhase1
        if hasattr(self, 'smPhase2'):
            del self.smPhase2
        if hasattr(self, 'smPhase3'):
            del self.smPhase3
        if hasattr(self, 'smPhase4'):
            del self.smPhase4
        self.cleanUpSounds()

    def exitOff(self):
        pass

    def cleanUpSounds(self):

        def __cleanUpSound__(soundFile):
            if soundFile.status() == soundFile.PLAYING:
                soundFile.setLoop(False)
                soundFile.stop()

        if hasattr(self, 'audio3d'):
            self.audio3d.disable()
            del self.audio3d
        if hasattr(self, 'phase1Sfx'):
            __cleanUpSound__(self.phase1Sfx)
            del self.phase1Sfx
        if hasattr(self, 'phase2Sfx'):
            __cleanUpSound__(self.phase2Sfx)
            del self.phase2Sfx
        if hasattr(self, 'phase3Sfx'):
            __cleanUpSound__(self.phase3Sfx)
            del self.phase3Sfx
        if hasattr(self, 'phase4Sfx'):
            __cleanUpSound__(self.phase4Sfx)
            del self.phase4Sfx
        if hasattr(self, 'phase4To5Sfx'):
            __cleanUpSound__(self.phase4To5Sfx)
            del self.phase4To5Sfx
        if hasattr(self, 'phase5Sfx'):
            __cleanUpSound__(self.phase5Sfx)
            del self.phase5Sfx
        if hasattr(self, 'arrowSfx'):
            __cleanUpSound__(self.arrowSfx)
            del self.arrowSfx

    def disable(self):
        self.ignoreAll()
        self.stopSillyMeter()
        self.enterOff()
        DistributedToonInterior.disable(self)

    def delete(self):
        DistributedToonInterior.delete(self)

@magicWord(category=CATEGORY_CREATIVE, types=[int])
def sillyPhase(phase):
    """
    Set the silly meter phase.
    """

    if phase < -1 or phase > 14:
        return 'Phase number must be between 0 and 14!'

    messenger.send('SillyMeterPhase', [phase])
    return 'Successfully set the silly meter phase!'

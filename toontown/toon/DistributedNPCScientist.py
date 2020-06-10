from toontown.toonbase import TTLocalizer
from DistributedNPCToonBase import DistributedNPCToonBase

class DistributedNPCScientist(DistributedNPCToonBase):

    def getCollSphereRadius(self):
        return 2.5

    def initPos(self):
        self.setHpr(180, 0, 0)
        self.setScale(1.0)

    def handleCollisionSphereEnter(self, collEntry):
        self.nametag3d.setDepthTest(0)
        self.nametag3d.setBin('fixed', 0)

    def setModelHand(self, path):
        model = loader.loadModel(path)

        for hand in self.getRightHands():
            placeholder = hand.attachNewNode('RightHandObj')
            placeholder.setH(180)
            placeholder.setScale(render, 1.0)
            placeholder.setPos(0, 0, 0.1)
            model.instanceTo(placeholder)

    def generateToon(self):
        DistributedNPCToonBase.generateToon(self)
        self.setupToonNodes()
        self.setModelHand('phase_4/models/props/tt_m_prp_acs_%s' % ('sillyReader' if self.style.getAnimal() == 'duck' else 'clipboard'))
        self.startSequence(config.GetInt('silly-meter-phase', 12))
        self.accept('SillyMeterPhase', self.startSequence)

    def startLookAround(self):
        pass

    def startSequence(self, phase):
        if not self.style.getAnimal() == 'horse':
            return

        if phase < 4:
            dialogue = TTLocalizer.ScientistPhase1Dialogue
        elif phase < 8:
            dialogue = TTLocalizer.ScientistPhase2Dialogue
        elif phase < 12:
            dialogue = TTLocalizer.ScientistPhase3Dialogue
        elif phase == 12:
            dialogue = TTLocalizer.ScientistPhase4Dialogue
        elif phase == 13:
            dialogue = TTLocalizer.ScientistPhase5Dialogue
        else:
            dialogue = TTLocalizer.ScientistPhase6Dialogue

        self.stopSequence()
        self.sequence = self.createTalkSequence(dialogue, 1)
        self.sequence.loop(0)

    def stopSequence(self):
        if hasattr(self, 'sequence'):
            self.sequence.pause()
            del self.sequence

    def disable(self):
        self.stopSequence()
        self.ignore('SillyMeterPhase')
        DistributedNPCToonBase.disable(self)

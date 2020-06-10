import DistributedNPCToonBaseAI, random

Animation = random.choice(["ScientistPlay", "ScientistWork", "ScientistLessWork", "ScientistJealous"])

class DistributedNPCScientistAI(DistributedNPCToonBaseAI.DistributedNPCToonBaseAI):

    def getStartAnimState(self):
        return 'ScientistEmcee' if self.npcId == 2020 else Animation

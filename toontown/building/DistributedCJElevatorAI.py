from ElevatorConstants import *
import DistributedBossElevatorAI

class DistributedCJElevatorAI(DistributedBossElevatorAI.DistributedBossElevatorAI):

    def __init__(self, air, bldg, zone):
        DistributedBossElevatorAI.DistributedBossElevatorAI.__init__(self, air, bldg, zone)
        self.type = ELEVATOR_CJ
        self.countdownTime = ElevatorData[self.type]['countdown']

from ElevatorConstants import *
import DistributedBossElevatorAI

class DistributedBBElevatorAI(DistributedBossElevatorAI.DistributedBossElevatorAI):

    def __init__(self, air, bldg, zone):
        DistributedBossElevatorAI.DistributedBossElevatorAI.__init__(self, air, bldg, zone)
        self.type = ELEVATOR_BB
        self.countdownTime = ElevatorData[self.type]['countdown']
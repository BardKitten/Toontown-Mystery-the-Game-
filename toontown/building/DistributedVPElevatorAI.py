from ElevatorConstants import *
import DistributedBossElevatorAI

class DistributedVPElevatorAI(DistributedBossElevatorAI.DistributedBossElevatorAI):

    def __init__(self, air, bldg, zone):
        DistributedBossElevatorAI.DistributedBossElevatorAI.__init__(self, air, bldg, zone)
        self.type = ELEVATOR_VP
        self.countdownTime = ElevatorData[self.type]['countdown']

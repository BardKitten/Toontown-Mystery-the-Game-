from otp.ai.AIBaseGlobal import *
from direct.distributed.ClockDelta import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
import DistributedCogHQDoorAI
from direct.fsm import State
from toontown.toonbase import ToontownGlobals
import CogDisguiseGlobals
from toontown.building import FADoorCodes
from toontown.building import DoorTypes

class DistributedCogHQExteriorDoorAI(DistributedCogHQDoorAI.DistributedCogHQDoorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCogHQExteriorDoorAI')

    def __init__(self, air, blockNumber, doorType, destinationZone, doorIndex = 0, lockValue = FADoorCodes.SB_DISGUISE_INCOMPLETE, swing = 3):
        DistributedCogHQDoorAI.DistributedCogHQDoorAI.__init__(self, air, blockNumber, doorType, destinationZone, doorIndex, lockValue, swing)

    def requestEnter(self):
        avId = self.air.getAvatarIdFromSender()
        dept = ToontownGlobals.cogHQZoneId2deptIndex(self.destinationZone)
        av = self.air.doId2do.get(avId)
        if av:
            if self.doorType == DoorTypes.EXT_COGHQ and self.isLockedDoor():
                parts = av.getCogParts()
                if CogDisguiseGlobals.isSuitComplete(parts, dept):
                    allowed = 1
                else:
                    allowed = 0
            else:
                allowed = 1
            if not allowed:
                self.sendReject(avId, self.isLockedDoor())
            else:
                print("********\nRequesting Lobby GUI...\n********")
                self.sendUpdate('selectLobby', [avId])

    def confirmEntrance(self, avId, status):
        if status:
            print("********\nAvatar Heading to Lobby...\n********")
            self.enqueueAvatarIdEnter(avId)
            self.sendUpdateToAvatarId(avId, 'setOtherZoneIdAndDoId', [self.destinationZone, self.otherDoor.getDoId()])
        else:
            print("********\nAvatar Canceled Entrance.\n********")
            self.sendReject(avId, 0)

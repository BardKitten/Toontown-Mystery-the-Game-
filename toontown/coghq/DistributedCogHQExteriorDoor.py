from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
import DistributedCogHQDoor
from toontown.hood import ZoneUtil
from BossLobbyGui import BossLobbyGui

class DistributedCogHQExteriorDoor(DistributedCogHQDoor.DistributedCogHQDoor):

    def __init__(self, cr):
        DistributedCogHQDoor.DistributedCogHQDoor.__init__(self, cr)
        self.lobbyGui = None

    def selectLobby(self, avId):
        print("********\nCreating Lobby GUI...\n********")
        self.lobbyGui = BossLobbyGui(self.sendConfirmation, avId)
        self.lobbyGui.loadFrame(0)

    def sendConfirmation(self, avId, status):
        self.lobbyGui.destroy()
        self.lobbyGui = None
        print("********\nGUI Complete.\nSending Confirmation...\n********")
        self.sendUpdate('confirmEntrance', [avId, status])

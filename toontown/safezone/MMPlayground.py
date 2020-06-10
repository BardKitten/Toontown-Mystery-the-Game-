from direct.fsm import ClassicFSM, State
from toontown.safezone import Playground
from toontown.toonbase import ToontownGlobals
import random

class MMPlayground(Playground.Playground):
    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        self.activityFsm = ClassicFSM.ClassicFSM('Activity', [State.State('off', self.enterOff, self.exitOff, ['OnPiano']), State.State('OnPiano', self.enterOnPiano, self.exitOnPiano, ['off'])], 'off', 'off')
        self.activityFsm.enterInitialState()

    def enterOff(self):
        return None

    def exitOff(self):
        return None

    def enterOnPiano(self):
        base.localAvatar.b_setParent(ToontownGlobals.SPMinniesPiano)

    def exitOnPiano(self):
        base.localAvatar.b_setParent(ToontownGlobals.SPRender)

from direct.gui.DirectGui import DirectButton, DirectFrame, DGG
from direct.task.Task import Task
from otp.otpbase import OTPLocalizer
from toontown.toonbase import ToontownGlobals, TTLocalizer, ToontownTimer
import LaffMeter, LaffRestockGlobals

class LaffShopGui(DirectFrame):

    def __init__(self):
        DirectFrame.__init__(self, parent=aspect2d, relief=None, geom=DGG.getDefaultDialogGeom(), geom_color=ToontownGlobals.GlobalDialogColor, geom_scale=(1.33, 1, 1.3), pos=(0, 0, 0), text='', text_scale=0.07, text_pos=(0, 0.475))
        self.initialiseoptions(LaffShopGui)
        
        self.additionalLaff = 0
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(aspect2d)
        self.timer.posInTopRightCorner()
        self.timer.countdown(LaffRestockGlobals.TIMER_SECONDS, self.__cancel, [LaffRestockGlobals.TIMER_END])
        self.setupButtons()
        self.bindButtons()
        self.laffMeter = LaffMeter.LaffMeter(base.localAvatar.style, base.localAvatar.getHp(), base.localAvatar.getMaxHp())
        self.laffMeter.reparentTo(self)
        self.laffMeter.setPos(0, 0, 0.065)
        self.laffMeter.setScale(0.13)
        self.__updateLaffMeter(1)

    def setupButtons(self):
        buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        arrowGui = loader.loadModel('phase_3/models/gui/create_a_toon_gui')
        arrowImageList = (arrowGui.find('**/CrtATn_R_Arrow_UP'), arrowGui.find('**/CrtATn_R_Arrow_DN'), arrowGui.find('**/CrtATn_R_Arrow_RLVR'), arrowGui.find('**/CrtATn_R_Arrow_UP'))

        self.cancelButton = DirectButton(parent=self, relief=None, image=(buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), pos=(-0.2, 0, -0.5), text=OTPLocalizer.lCancel, text_scale=0.06, text_pos=(0, -0.1), command=self.__cancel, extraArgs=[LaffRestockGlobals.USER_CANCEL])
        self.okButton = DirectButton(parent=self, relief=None, image=(buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr')), pos=(0.2, 0, -0.5), text=OTPLocalizer.lOK, text_scale=0.06, text_pos=(0, -0.1), command=self.__restock)
        self.upArrow = DirectButton(parent=self, relief=None, image=arrowImageList, image_scale=(1, 1, 1), image3_color=Vec4(0.6, 0.6, 0.6, 0.25), pos=(0.2, 0, -0.265))
        self.downArrow = DirectButton(parent=self, relief=None, image=arrowImageList, image_scale=(-1, 1, 1), image3_color=Vec4(0.6, 0.6, 0.6, 0.25), pos=(-0.2, 0, -0.265))

        buttons.removeNode()
        arrowGui.removeNode()

    def bindButtons(self):
        self.downArrow.bind(DGG.B1PRESS, self.__taskUpdate, extraArgs=[-1])
        self.downArrow.bind(DGG.B1RELEASE, self.__taskDone)
        self.upArrow.bind(DGG.B1PRESS, self.__taskUpdate, extraArgs=[1])
        self.upArrow.bind(DGG.B1RELEASE, self.__taskDone)

    def destroy(self):
        self.ignoreAll()

        if self.timer:
            self.timer.destroy()

        taskMgr.remove(self.taskName('runLaffCounter'))
        DirectFrame.destroy(self)

    def __cancel(self, state):
        self.destroy()
        messenger.send('laffShopDone', [state, 0])

    def __restock(self):
        self.destroy()
        messenger.send('laffShopDone', [LaffRestockGlobals.RESTOCK, self.additionalLaff])

    def __updateLaffMeter(self, amount):
        self.additionalLaff += amount
        hitLimit = 0
        newLaff = base.localAvatar.getHp() + self.additionalLaff

        if (newLaff - 1) <= base.localAvatar.getHp():
            self.downArrow['state'] = DGG.DISABLED
            hitLimit = 1
        else:
            self.downArrow['state'] = DGG.NORMAL

        if newLaff >= base.localAvatar.getMaxHp():
            self.upArrow['state'] = DGG.DISABLED
            hitLimit = 1
        else:
            self.upArrow['state'] = DGG.NORMAL

        cost = self.additionalLaff * ToontownGlobals.CostPerLaffRestock
        self['text'] = TTLocalizer.RestockAskMessage % (self.additionalLaff, cost)

        if cost > base.localAvatar.getTotalMoney():
            self.okButton['state'] = DGG.DISABLED
            self['text'] += TTLocalizer.RestockNoMoneyGuiMessage
        else:
            self.okButton['state'] = DGG.NORMAL

        self.laffMeter.hp = newLaff
        self.laffMeter.start()

        return hitLimit

    def __runTask(self, task):
        if task.time - task.prevTime < task.delayTime:
            return Task.cont
        else:
            task.delayTime = max(0.05, task.delayTime * 0.75)
            task.prevTime = task.time
            hitLimit = self.__updateLaffMeter(task.delta)

            return Task.done if hitLimit else Task.cont

    def __taskDone(self, event):
        messenger.send('wakeup')
        taskMgr.remove(self.taskName('runLaffCounter'))

    def __taskUpdate(self, delta, event):
        messenger.send('wakeup')

        task = Task(self.__runTask)
        task.delayTime = 0.4
        task.prevTime = 0.0
        task.delta = delta
        hitLimit = self.__updateLaffMeter(delta)

        if not hitLimit:
            taskMgr.add(task, self.taskName('runLaffCounter'))
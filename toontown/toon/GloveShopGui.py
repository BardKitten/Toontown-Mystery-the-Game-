from direct.gui.DirectGui import DirectButton, DirectLabel, DGG
from direct.task.Task import Task
from toontown.toon import ToonDNA
from toontown.toonbase import ToontownGlobals, TTLocalizer, ToontownTimer
import GloveNPCGlobals, time

class GloveShopGui:

    def __init__(self):
        self.index = 0
        self.id = time.time()
        self.lastGlove = base.localAvatar.style.gloveColor
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(aspect2d)
        self.timer.posInTopRightCorner()
        self.timer.countdown(GloveNPCGlobals.TIMER_SECONDS, self.__exit, [GloveNPCGlobals.TIMER_END])
        self.setupButtons()
        self.bindButtons()
        self.__updateIndex(0)

    def setupButtons(self):
        gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        arrowImage = (gui.find('**/tt_t_gui_mat_shuffleArrowUp'), gui.find('**/tt_t_gui_mat_shuffleArrowDown'))
        buttonImage = (gui.find('**/tt_t_gui_mat_shuffleUp'), gui.find('**/tt_t_gui_mat_shuffleDown'))

        self.title = DirectLabel(aspect2d, relief=None, text=TTLocalizer.GloveGuiTitle,
                     text_fg=(0, 1, 0, 1), text_scale=0.15, text_font=ToontownGlobals.getSignFont(),
                     pos=(0, 0, -0.30), text_shadow=(1, 1, 1, 1))

        self.notice = DirectLabel(aspect2d, relief=None, text='', text_fg=(1, 0, 0, 1), text_scale=0.11,
                      text_font=ToontownGlobals.getSignFont(), pos=(0, 0, -0.45), text_shadow=(1, 1, 1, 1))

        self.color = DirectLabel(aspect2d, relief=None, text='', text_scale=0.11, text_font=ToontownGlobals.getSignFont(),
                     pos=(0, 0, -0.70), text_shadow=(1, 1, 1, 1))

        self.buyButton = DirectButton(aspect2d, relief=None, image=buttonImage, text=TTLocalizer.GloveGuiBuy,
                         text_font=ToontownGlobals.getInterfaceFont(), text_scale=0.11, text_pos=(0, -0.02),
                         pos=(-0.60, 0, -0.90), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), command=self.__exit, extraArgs=[GloveNPCGlobals.CHANGE])

        self.cancelButton = DirectButton(aspect2d, relief=None, image=buttonImage, text=TTLocalizer.lCancel,
                            text_font=ToontownGlobals.getInterfaceFont(), text_scale=0.11, text_pos=(0, -0.02),
                            pos=(0.60, 0, -0.90), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), command=self.__exit, extraArgs=[GloveNPCGlobals.USER_CANCEL])

        self.downArrow = DirectButton(aspect2d, relief=None, image=arrowImage, pos=(-0.60, 0, -0.66))
        self.upArrow = DirectButton(aspect2d, relief=None, image=arrowImage, pos=(0.60, 0, -0.66), scale=-1)

        gui.removeNode()

    def bindButtons(self):
        self.downArrow.bind(DGG.B1PRESS, self.__taskUpdate, extraArgs=[-1])
        self.downArrow.bind(DGG.B1RELEASE, self.__taskDone)
        self.upArrow.bind(DGG.B1PRESS, self.__taskUpdate, extraArgs=[1])
        self.upArrow.bind(DGG.B1RELEASE, self.__taskDone)

    def destroy(self):
        if self.timer:
            self.timer.destroy()

        if not hasattr(self, 'title'):
            return

        # TODO: DirectDialog-ify
        self.title.destroy()
        self.notice.destroy()
        self.color.destroy()
        self.buyButton.destroy()
        self.cancelButton.destroy()
        self.downArrow.destroy()
        self.upArrow.destroy()
        del self.title
        del self.notice
        del self.color
        del self.buyButton
        del self.cancelButton
        del self.downArrow
        del self.upArrow

        taskMgr.remove('runGloveCounter-%s' % self.id)

    def setClientGlove(self, color):
        dna = base.localAvatar.style

        dna.gloveColor = color
        base.localAvatar.setDNA(dna)

    def __exit(self, state):
        self.destroy()
        self.setClientGlove(self.lastGlove)
        messenger.send('gloveShopDone', [state, self.index if state == GloveNPCGlobals.CHANGE else 0])

    def __updateIndex(self, offset):
        self.index += offset
        hitLimit = 0
        color = ToonDNA.allColorsList[self.index]

        if self.index <= 0:
            self.downArrow['state'] = DGG.DISABLED
            hitLimit = 1
        else:
            self.downArrow['state'] = DGG.NORMAL

        if (self.index + 1) >= len(TTLocalizer.NumToColor):
            self.upArrow['state'] = DGG.DISABLED
            hitLimit = 1
        else:
            self.upArrow['state'] = DGG.NORMAL
        
        if self.lastGlove == color:
            self.buyButton['state'] = DGG.DISABLED
            self.notice['text'] = TTLocalizer.GloveGuiSameColor
        else:
            self.buyButton['state'] = DGG.NORMAL
            self.notice['text'] = TTLocalizer.GloveGuiNotice % ToontownGlobals.GloveCost

        self.color['text'] = TTLocalizer.NumToColor[self.index]
        self.color['text_fg'] = color
        self.setClientGlove(color)
        return hitLimit

    def __runTask(self, task):
        if task.time - task.prevTime < task.delayTime:
            return Task.cont
        else:
            task.delayTime = max(0.05, task.delayTime * 0.75)
            task.prevTime = task.time
            hitLimit = self.__updateIndex(task.delta)

            return Task.done if hitLimit else Task.cont

    def __taskDone(self, event):
        messenger.send('wakeup')
        taskMgr.remove('runGloveCounter-%s' % self.id)

    def __taskUpdate(self, delta, event):
        messenger.send('wakeup')

        task = Task(self.__runTask)
        task.delayTime = 0.4
        task.prevTime = 0.0
        task.delta = delta
        hitLimit = self.__updateIndex(delta)

        if not hitLimit:
            taskMgr.add(task, 'runGloveCounter-%s' % self.id)

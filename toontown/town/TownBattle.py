from toontown.toonbase.ToontownBattleGlobals import *
import types
from direct.fsm import StateData
from direct.fsm import ClassicFSM, State
from direct.fsm import State
import TownBattleAttackPanel
import TownBattleWaitPanel
import TownBattleChooseAvatarPanel
import TownBattleSOSPanel
import TownBattleSOSPetSearchPanel
import TownBattleSOSPetInfoPanel
import TownBattleToonPanel
import TownBattleCogPanel
from toontown.toontowngui import TTDialog
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import BattleBase
from direct.showbase import PythonUtil
from toontown.toonbase import TTLocalizer, ToontownGlobals, ToontownTimer
from toontown.pets import PetConstants
from direct.gui.DirectGui import *
from toontown.battle import FireCogPanel

class TownBattle(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownBattle')
    evenPos = (0.75,
     0.25,
     -0.25,
     -0.75)
    oddPos = (0.5, 0, -0.5)

    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.numCogs = 1
        self.creditLevel = None
        self.luredIndices = []
        self.trappedIndices = []
        self.numToons = 1
        self.toons = []
        self.localNum = 0
        self.time = 0
        self.bldg = 0
        self.track = -1
        self.level = -1
        self.target = 0
        self.toonAttacks = [(-1, 0, 0)] * 4
        self.fsm = ClassicFSM.ClassicFSM('TownBattle', [
            State.State('Off',
                self.enterOff,
                self.exitOff,
                ['Attack']),
            State.State('Attack',
                self.enterAttack,
                self.exitAttack,
                ['ChooseCog',
                 'ChooseToon',
                 'AttackWait',
                 'Run',
                 'Fire',
                 'SOS']),
            State.State('ChooseCog',
                self.enterChooseCog,
                self.exitChooseCog,
                ['AttackWait',
                 'Attack']),
            State.State('AttackWait',
                self.enterAttackWait,
                self.exitAttackWait,
                ['ChooseCog',
                 'ChooseToon',
                 'Attack']),
            State.State('ChooseToon',
                self.enterChooseToon,
                self.exitChooseToon,
                ['AttackWait',
                 'Attack']),
            State.State('Run',
                self.enterRun,
                self.exitRun,
                ['Attack']),
            State.State('SOS',
                self.enterSOS,
                self.exitSOS,
                ['Attack',
                 'AttackWait',
                 'SOSPetSearch',
                 'SOSPetInfo']),
            State.State('SOSPetSearch',
                self.enterSOSPetSearch,
                self.exitSOSPetSearch,
                ['SOS',
                 'SOSPetInfo']),
            State.State('SOSPetInfo',
                self.enterSOSPetInfo,
                self.exitSOSPetInfo,
                ['SOS',
                 'AttackWait']),
            State.State('Fire',
                self.enterFire,
                self.exitFire,
                ['Attack',
                 'AttackWait'])],
            'Off', 'Off')
        self.runPanel = TTDialog.TTDialog(dialogName='TownBattleRunPanel', text=TTLocalizer.TownBattleRun, style=TTDialog.TwoChoice, command=self.__handleRunPanelDone)
        self.runPanel.hide()
        self.attackPanelDoneEvent = 'attack-panel-done'
        self.attackPanel = TownBattleAttackPanel.TownBattleAttackPanel(self.attackPanelDoneEvent)
        self.waitPanelDoneEvent = 'wait-panel-done'
        self.waitPanel = TownBattleWaitPanel.TownBattleWaitPanel(self.waitPanelDoneEvent)
        self.chooseCogPanelDoneEvent = 'choose-cog-panel-done'
        self.chooseCogPanel = TownBattleChooseAvatarPanel.TownBattleChooseAvatarPanel(self.chooseCogPanelDoneEvent, 0)
        self.chooseToonPanelDoneEvent = 'choose-toon-panel-done'
        self.chooseToonPanel = TownBattleChooseAvatarPanel.TownBattleChooseAvatarPanel(self.chooseToonPanelDoneEvent, 1)
        self.SOSPanelDoneEvent = 'SOS-panel-done'
        self.SOSPanel = TownBattleSOSPanel.TownBattleSOSPanel(self.SOSPanelDoneEvent)
        self.SOSPetSearchPanelDoneEvent = 'SOSPetSearch-panel-done'
        self.SOSPetSearchPanel = TownBattleSOSPetSearchPanel.TownBattleSOSPetSearchPanel(self.SOSPetSearchPanelDoneEvent)
        self.SOSPetInfoPanelDoneEvent = 'SOSPetInfo-panel-done'
        self.SOSPetInfoPanel = TownBattleSOSPetInfoPanel.TownBattleSOSPetInfoPanel(self.SOSPetInfoPanelDoneEvent)
        self.fireCogPanelDoneEvent = 'fire-cog-panel-done'
        self.FireCogPanel = FireCogPanel.FireCogPanel(self.fireCogPanelDoneEvent)
        self.rolloverFrame = DirectFrame(aspect2d, relief=None, geom=DGG.getDefaultDialogGeom(), geom_color=(0.6, 1.0, 0.4, 1), geom_scale=(0.5, 0.3, 0.2), text_scale=0.05, text_pos=(0, 0.0125), text='', text_fg=(0, 0, 0, 1), pos=(0.4, 0, 0))
        self.rolloverFrame.setBin('gui-popup', 0)
        self.rolloverFrame.hide()
        self.suitGui = loader.loadModel('phase_3.5/models/gui/suit_detail_panel')
        self.suitGui.find('**/avatar_panel/shadow').setColor(1, 1, 1, 0.5)
        self.toonPanels = [TownBattleToonPanel.TownBattleToonPanel(self) for i in xrange(4)]
        self.cogPanels = [TownBattleCogPanel.TownBattleCogPanel(self) for i in xrange(4)]
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.posInTopRightCorner()
        self.timer.setScale(0.4)
        self.timer.hide()

    def cleanup(self):
        self.ignore(self.attackPanelDoneEvent)
        self.unload()
        del self.fsm
        self.runPanel.cleanup()
        del self.runPanel
        del self.attackPanel
        del self.waitPanel
        del self.chooseCogPanel
        del self.chooseToonPanel
        del self.SOSPanel
        del self.FireCogPanel
        del self.SOSPetSearchPanel
        del self.SOSPetInfoPanel
        del self.rolloverFrame

        for panel in self.toonPanels + self.cogPanels:
            panel.cleanup()

        del self.toonPanels
        del self.cogPanels
        self.timer.destroy()
        self.suitGui.removeNode()
        del self.suitGui
        del self.timer
        del self.toons

    def enter(self, event, parentFSMState, bldg = 0, creditMultiplier = 1, tutorialFlag = 0):
        self.parentFSMState = parentFSMState
        self.parentFSMState.addChild(self.fsm)
        if not self.isLoaded:
            self.load()
        self.battleEvent = event
        self.fsm.enterInitialState()
        base.localAvatar.laffMeter.start()
        self.numToons = 1
        self.numCogs = 1
        self.toons = [base.localAvatar.doId]
        self.toonPanels[0].setLaffMeter(base.localAvatar)
        self.bldg = bldg
        self.creditLevel = None
        self.creditMultiplier = creditMultiplier
        self.tutorialFlag = tutorialFlag
        base.localAvatar.inventory.setBattleCreditMultiplier(self.creditMultiplier)
        base.localAvatar.inventory.setActivateMode('battle', heal=0, bldg=bldg, tutorialFlag=tutorialFlag)
        self.SOSPanel.bldg = bldg

    def exit(self):
        base.localAvatar.laffMeter.stop()
        self.parentFSMState.removeChild(self.fsm)
        del self.parentFSMState
        base.localAvatar.inventory.setBattleCreditMultiplier(1)

    def load(self):
        if self.isLoaded:
            return
        self.attackPanel.load()
        self.waitPanel.load()
        self.chooseCogPanel.load()
        self.chooseToonPanel.load()
        self.SOSPanel.load()
        if hasattr(base, 'wantPets') and base.wantPets:
            self.SOSPetSearchPanel.load()
            self.SOSPetInfoPanel.load()
        self.isLoaded = 1

    def unload(self):
        if not self.isLoaded:
            return
        self.attackPanel.unload()
        self.waitPanel.unload()
        self.chooseCogPanel.unload()
        self.chooseToonPanel.unload()
        self.FireCogPanel.unload()
        self.SOSPanel.unload()
        if hasattr(base, 'wantPets') and base.wantPets:
            self.SOSPetSearchPanel.unload()
            self.SOSPetInfoPanel.unload()
        self.isLoaded = 0

    def setState(self, state):
        if hasattr(self, 'fsm'):
            self.fsm.request(state)

    def updateTimer(self, time):
        self.time = time
        self.timer.setTime(time)
        return None
    
    def showRolloverFrame(self, parent, type, text, extra=None):
        dict = TTLocalizer.BattleHoverAttributes[type]

        for key, value in dict.iteritems():
            if key == 'pos':
                self.rolloverFrame.setPos(value)
            elif key == 'suit':
                if value:
                    self.rolloverFrame['text_font'] = ToontownGlobals.getSuitFont()
                    self.rolloverFrame['geom'] = self.suitGui.find('**/avatar_panel')
                else:
                    self.rolloverFrame['text_font'] = ToontownGlobals.getInterfaceFont()
                    self.rolloverFrame['geom'] = DGG.getDefaultDialogGeom()
            else:
                self.rolloverFrame[key] = value

        self.rolloverFrame.reparentTo(parent)
        self.rolloverFrame.show()
        self.rolloverFrame['text'] = text
    
    def hideRolloverFrame(self, extra=None):
        self.rolloverFrame.hide()
    
    def isAttackDangerous(self, hp):
        for panel in self.toonPanels:
            if panel.hasAvatar() and panel.avatar.getHp() <= hp:
                return True

    def __enterPanels(self, num, localNum):
        self.notify.debug('enterPanels() num: %d localNum: %d' % (num, localNum))
        for toonPanel in self.toonPanels:
            toonPanel.hide()
            toonPanel.setPos(0, 0, -0.9)
        
        self.positionPanels(num, self.toonPanels)

    def __enterCogPanels(self, num):
        for cogPanel in self.cogPanels:
            cogPanel.hide()
            cogPanel.updateHealthBar()
            cogPanel.updateRolloverBind()
            cogPanel.setPos(0, 0, 0.62)
        
        self.positionPanels(num, self.cogPanels)
    
    def positionPanels(self, num, panels):
        pos = self.evenPos if num % 2 == 0 else self.oddPos

        for i, panel in enumerate(panels):
            if num > i:
                panel.setX(pos[i if num >= 3 else i + 1])
                panel.show()

    def updateChosenAttacks(self, battleIndices, tracks, levels, targets):
        self.notify.debug('updateChosenAttacks bi=%s tracks=%s levels=%s targets=%s' % (battleIndices,
         tracks,
         levels,
         targets))
        for i in xrange(4):
            if battleIndices[i] == -1:
                pass
            else:
                if tracks[i] == BattleBase.NO_ATTACK:
                    numTargets = 0
                    target = -2
                elif tracks[i] == BattleBase.PASS_ATTACK:
                    numTargets = 0
                    target = -2
                elif tracks[i] == BattleBase.NPCSOS:
                    numTargets = 0
                    target = targets[i]
                elif tracks[i] == BattleBase.SOS or tracks[i] == BattleBase.PETSOS:
                    numTargets = 0
                    target = -2
                elif tracks[i] == HEAL_TRACK:
                    numTargets = self.numToons
                    if self.__isGroupHeal(levels[i]):
                        target = -2
                    else:
                        target = targets[i]
                else:
                    numTargets = self.numCogs
                    if self.__isGroupAttack(tracks[i], levels[i]):
                        target = -1
                    else:
                        target = targets[i]
                        if target == -1:
                            numTargets = None
                self.toonPanels[battleIndices[i]].setValues(battleIndices[i], tracks[i], levels[i], numTargets, target, self.localNum)

    def chooseDefaultTarget(self):
        if self.track > -1:
            response = {}
            response['mode'] = 'Attack'
            response['track'] = self.track
            response['level'] = self.level
            response['target'] = self.target
            messenger.send(self.battleEvent, [response])
            return 1
        return 0

    def updateLaffMeter(self, toonNum, hp):
        self.toonPanels[toonNum].updateLaffMeter(hp)

    def enterOff(self):
        if self.isLoaded:
            for panel in self.toonPanels + self.cogPanels:
                panel.hide()

        self.toonAttacks = [(-1, 0, 0)] * 4
        self.target = 0

        if hasattr(self, 'timer'):
            self.timer.hide()

    def exitOff(self):
        if self.isLoaded:
            self.__enterPanels(self.numToons, self.localNum)
            if settings['cogInterface']:
                self.__enterCogPanels(self.numCogs)
        self.timer.show()
        self.track = -1
        self.level = -1
        self.target = 0

    def enterAttack(self):
        self.attackPanel.enter()
        self.accept(self.attackPanelDoneEvent, self.__handleAttackPanelDone)

    def exitAttack(self):
        self.ignore(self.attackPanelDoneEvent)
        self.attackPanel.exit()

    def __handleAttackPanelDone(self, doneStatus):
        self.notify.debug('doneStatus: %s' % doneStatus)
        mode = doneStatus['mode']
        if mode == 'Inventory':
            self.track = doneStatus['track']
            self.level = doneStatus['level']
            self.toonPanels[self.localNum].setValues(self.localNum, self.track, self.level)
            if self.track == HEAL_TRACK:
                if self.__isGroupHeal(self.level):
                    response = {}
                    response['mode'] = 'Attack'
                    response['track'] = self.track
                    response['level'] = self.level
                    response['target'] = self.target
                    messenger.send(self.battleEvent, [response])
                    self.fsm.request('AttackWait')
                elif self.numToons == 3 or self.numToons == 4:
                    self.fsm.request('ChooseToon')
                elif self.numToons == 2:
                    response = {}
                    response['mode'] = 'Attack'
                    response['track'] = self.track
                    response['level'] = self.level
                    if self.localNum == 0:
                        response['target'] = 1
                    elif self.localNum == 1:
                        response['target'] = 0
                    else:
                        self.notify.error('Bad localNum value: %s' % self.localNum)
                    messenger.send(self.battleEvent, [response])
                    self.fsm.request('AttackWait')
                else:
                    self.notify.error('Heal was chosen when number of toons is %s' % self.numToons)
            elif self.__isCogChoiceNecessary():
                self.notify.debug('choice needed')
                self.fsm.request('ChooseCog')
                response = {}
                response['mode'] = 'Attack'
                response['track'] = self.track
                response['level'] = self.level
                response['target'] = -1
                messenger.send(self.battleEvent, [response])
            else:
                self.notify.debug('no choice needed')
                self.fsm.request('AttackWait')
                response = {}
                response['mode'] = 'Attack'
                response['track'] = self.track
                response['level'] = self.level
                response['target'] = 0
                messenger.send(self.battleEvent, [response])
        elif mode == 'Run':
            self.fsm.request('Run')
        elif mode == 'SOS':
            self.fsm.request('SOS')
        elif mode == 'Fire':
            self.fsm.request('Fire')
        elif mode == 'Pass':
            response = {}
            response['mode'] = 'Pass'
            response['id'] = -1
            messenger.send(self.battleEvent, [response])
            self.fsm.request('AttackWait')
        else:
            self.notify.warning('unknown mode: %s' % mode)

    def checkHealTrapLure(self):
        self.notify.debug('numToons: %s, numCogs: %s, lured: %s, trapped: %s' % (self.numToons,
         self.numCogs,
         self.luredIndices,
         self.trappedIndices))
        if len(PythonUtil.union(self.trappedIndices, self.luredIndices)) == self.numCogs:
            canTrap = 0
        else:
            canTrap = 1
        if len(self.luredIndices) == self.numCogs:
            canLure = 0
            canTrap = 0
        else:
            canLure = 1
        if self.numToons == 1:
            canHeal = 0
        else:
            canHeal = 1
        return (canHeal, canTrap, canLure)

    def adjustCogsAndToons(self, cogs, luredIndices, trappedIndices, toons):
        numCogs = len(cogs)
        self.notify.debug('adjustCogsAndToons() numCogs: %s self.numCogs: %s' % (numCogs, self.numCogs))
        self.notify.debug('adjustCogsAndToons() luredIndices: %s self.luredIndices: %s' % (luredIndices, self.luredIndices))
        self.notify.debug('adjustCogsAndToons() trappedIndices: %s self.trappedIndices: %s' % (trappedIndices, self.trappedIndices))
        toonIds = [toon.doId for toon in toons]
        self.notify.debug('adjustCogsAndToons() toonIds: %s self.toons: %s' % (toonIds, self.toons))
        maxSuitLevel = 0
        for cog in cogs:
            maxSuitLevel = max(maxSuitLevel, cog.getActualLevel())

        creditLevel = maxSuitLevel
        resetActivateMode = numCogs != self.numCogs or creditLevel != self.creditLevel or luredIndices != self.luredIndices or trappedIndices != self.trappedIndices or toonIds != self.toons
        self.notify.debug('adjustCogsAndToons() resetActivateMode: %s' % resetActivateMode)
        self.numCogs = numCogs
        self.creditLevel = creditLevel
        self.luredIndices = luredIndices
        self.trappedIndices = trappedIndices
        self.toons = toonIds
        self.numToons = len(toons)
        self.localNum = toons.index(base.localAvatar)
        currStateName = self.fsm.getCurrentState().getName()
        
        if settings['cogInterface']:
            self.__enterCogPanels(self.numCogs)

            for i in xrange(len(cogs)):
                self.cogPanels[i].setSuit(cogs[i])
        
        if resetActivateMode:
            self.__enterPanels(self.numToons, self.localNum)
            for i in xrange(len(toons)):
                self.toonPanels[i].setLaffMeter(toons[i])

            if currStateName == 'ChooseCog':
                self.chooseCogPanel.adjustCogs(self.numCogs, self.luredIndices, self.trappedIndices, self.track)
            elif currStateName == 'ChooseToon':
                self.chooseToonPanel.adjustToons(self.numToons, self.localNum)
            canHeal, canTrap, canLure = self.checkHealTrapLure()
            base.localAvatar.inventory.setBattleCreditMultiplier(self.creditMultiplier)
            base.localAvatar.inventory.setActivateMode('battle', heal=canHeal, trap=canTrap, lure=canLure, bldg=self.bldg, creditLevel=self.creditLevel, tutorialFlag=self.tutorialFlag)

    def enterChooseCog(self):
        self.cog = 0
        self.chooseCogPanel.enter(self.numCogs, luredIndices=self.luredIndices, trappedIndices=self.trappedIndices, track=self.track)
        self.accept(self.chooseCogPanelDoneEvent, self.__handleChooseCogPanelDone)

    def exitChooseCog(self):
        self.ignore(self.chooseCogPanelDoneEvent)
        self.chooseCogPanel.exit()

    def __handleChooseCogPanelDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'Back':
            self.fsm.request('Attack')
        elif mode == 'Avatar':
            self.cog = doneStatus['avatar']
            self.target = self.cog
            self.fsm.request('AttackWait')
            response = {}
            response['mode'] = 'Attack'
            response['track'] = self.track
            response['level'] = self.level
            response['target'] = self.cog
            messenger.send(self.battleEvent, [response])
        else:
            self.notify.warning('unknown mode: %s' % mode)

    def enterAttackWait(self, chosenToon = -1):
        self.accept(self.waitPanelDoneEvent, self.__handleAttackWaitBack)
        self.waitPanel.enter(self.numToons)

    def exitAttackWait(self):
        self.waitPanel.exit()
        self.ignore(self.waitPanelDoneEvent)

    def __handleAttackWaitBack(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'Back':
            if self.track == HEAL_TRACK:
                self.fsm.request('Attack')
            elif self.track == BattleBase.NO_ATTACK:
                self.fsm.request('Attack')
            elif self.__isCogChoiceNecessary():
                self.fsm.request('ChooseCog')
            else:
                self.fsm.request('Attack')
            response = {}
            response['mode'] = 'UnAttack'
            messenger.send(self.battleEvent, [response])
        else:
            self.notify.error('unknown mode: %s' % mode)

    def enterChooseToon(self):
        self.toon = 0
        self.chooseToonPanel.enter(self.numToons, localNum=self.localNum)
        self.accept(self.chooseToonPanelDoneEvent, self.__handleChooseToonPanelDone)

    def exitChooseToon(self):
        self.ignore(self.chooseToonPanelDoneEvent)
        self.chooseToonPanel.exit()

    def __handleChooseToonPanelDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'Back':
            self.fsm.request('Attack')
        elif mode == 'Avatar':
            self.toon = doneStatus['avatar']
            self.target = self.toon
            self.fsm.request('AttackWait', [self.toon])
            response = {}
            response['mode'] = 'Attack'
            response['track'] = self.track
            response['level'] = self.level
            response['target'] = self.toon
            messenger.send(self.battleEvent, [response])
        else:
            self.notify.warning('unknown mode: %s' % mode)

    def enterRun(self):
        self.runPanel.show()

    def exitRun(self):
        self.runPanel.hide()

    def __handleRunPanelDone(self, doneStatus):
        if doneStatus == DGG.DIALOG_OK:
            response = {}
            response['mode'] = 'Run'
            messenger.send(self.battleEvent, [response])
        else:
            self.fsm.request('Attack')

    def enterFire(self):
        canHeal, canTrap, canLure = self.checkHealTrapLure()
        self.FireCogPanel.enter(self.numCogs, luredIndices=self.luredIndices, trappedIndices=self.trappedIndices, track=self.track)
        self.accept(self.fireCogPanelDoneEvent, self.__handleCogFireDone)

    def exitFire(self):
        self.ignore(self.fireCogPanelDoneEvent)
        self.FireCogPanel.exit()

    def __handleCogFireDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'Back':
            self.fsm.request('Attack')
        elif mode == 'Avatar':
            self.cog = doneStatus['avatar']
            self.target = self.cog
            self.fsm.request('AttackWait')
            response = {}
            response['mode'] = 'Fire'
            response['target'] = self.cog
            messenger.send(self.battleEvent, [response])
        else:
            self.notify.warning('unknown mode: %s' % mode)

    def enterSOS(self):
        canHeal, canTrap, canLure = self.checkHealTrapLure()
        self.SOSPanel.enter(canLure, canTrap)
        self.accept(self.SOSPanelDoneEvent, self.__handleSOSPanelDone)

    def exitSOS(self):
        self.ignore(self.SOSPanelDoneEvent)
        self.SOSPanel.exit()

    def __handleSOSPanelDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'Friend':
            doId = doneStatus['friend']
            response = {}
            response['mode'] = 'SOS'
            response['id'] = doId
            messenger.send(self.battleEvent, [response])
            self.fsm.request('AttackWait')
        elif mode == 'Pet':
            self.petId = doneStatus['petId']
            self.petName = doneStatus['petName']
            self.fsm.request('SOSPetSearch')
        elif mode == 'NPCFriend':
            doId = doneStatus['friend']
            response = {}
            response['mode'] = 'NPCSOS'
            response['id'] = doId
            messenger.send(self.battleEvent, [response])
            self.fsm.request('AttackWait')
        elif mode == 'Back':
            self.fsm.request('Attack')

    def enterSOSPetSearch(self):
        response = {}
        response['mode'] = 'PETSOSINFO'
        response['id'] = self.petId
        self.SOSPetSearchPanel.enter(self.petId, self.petName)
        self.proxyGenerateMessage = 'petProxy-%d-generated' % self.petId
        self.accept(self.proxyGenerateMessage, self.__handleProxyGenerated)
        self.accept(self.SOSPetSearchPanelDoneEvent, self.__handleSOSPetSearchPanelDone)
        messenger.send(self.battleEvent, [response])

    def exitSOSPetSearch(self):
        self.ignore(self.proxyGenerateMessage)
        self.ignore(self.SOSPetSearchPanelDoneEvent)
        self.SOSPetSearchPanel.exit()

    def __handleSOSPetSearchPanelDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'Back':
            self.fsm.request('SOS')
        else:
            self.notify.error('invalid mode in handleSOSPetSearchPanelDone')

    def __handleProxyGenerated(self):
        self.fsm.request('SOSPetInfo')

    def enterSOSPetInfo(self):
        self.SOSPetInfoPanel.enter(self.petId)
        self.accept(self.SOSPetInfoPanelDoneEvent, self.__handleSOSPetInfoPanelDone)

    def exitSOSPetInfo(self):
        self.ignore(self.SOSPetInfoPanelDoneEvent)
        self.SOSPetInfoPanel.exit()

    def __handleSOSPetInfoPanelDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'OK':
            response = {}
            response['mode'] = 'PETSOS'
            response['id'] = self.petId
            response['trickId'] = doneStatus['trickId']
            messenger.send(self.battleEvent, [response])
            self.fsm.request('AttackWait')
            bboard.post(PetConstants.OurPetsMoodChangedKey, True)
        elif mode == 'Back':
            self.fsm.request('SOS')

    def __isCogChoiceNecessary(self):
        return self.numCogs > 1 and not self.__isGroupAttack(self.track, self.level)

    def __isGroupAttack(self, trackNum, levelNum):
        return BattleBase.attackAffectsGroup(trackNum, levelNum)

    def __isGroupHeal(self, levelNum):
        return self.__isGroupAttack(HEAL_TRACK, levelNum)

from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from direct.task.Task import Task
from panda3d.core import *
from toontown.distributed import ToontownDistrictStats
from toontown.hood import ZoneUtil
from toontown.shtiker import ShtikerPage
from toontown.coghq import CogDisguiseGlobals
from toontown.suit import SuitDNA
from toontown.suit import Suit
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.toontowngui import TTDialog


ICON_COLORS = (Vec4(0.863, 0.776, 0.769, 1.0), Vec4(0.749, 0.776, 0.824, 1.0),
               Vec4(0.749, 0.769, 0.749, 1.0), Vec4(0.843, 0.745, 0.745, 1.0))

POP_COLORS = (Vec4(0.4, 0.4, 1.0, 1.0), Vec4(0.4, 1.0, 0.4, 1.0),
              Vec4(1.0, 0.4, 0.4, 1.0))

def compareShardTuples(a, b):
    if a[1] < b[1]:
        return -1
    elif b[1] < a[1]:
        return 1
    else:
        return 0

def setupInvasionMarkerAny(node):
    pass

def setupInvasionMarker(node, invasionStatus):
    if node.find('**/*invasion-marker'):
        return

    markerNode = node.attachNewNode('invasion-marker')

    if invasionStatus == 5:
        setupInvasionMarkerAny(markerNode)
        return

    icons = loader.loadModel('phase_3/models/gui/cog_icons')
    iconStatus = invasionStatus - 1

    if iconStatus in SuitDNA.suitDeptModelPaths:
        icon = icons.find(SuitDNA.suitDeptModelPaths[iconStatus]).copyTo(markerNode)

    icons.removeNode()

    icon.setColor(ICON_COLORS[iconStatus])
    icon.setPos(0.50, 0, 0.0125)
    icon.setScale(0.0535)

def removeInvasionMarker(node):
    markerNode = node.find('**/*invasion-marker')

    if not markerNode.isEmpty():
        markerNode.removeNode()


class ShardPage(ShtikerPage.ShtikerPage):
    notify = DirectNotifyGlobal.directNotify.newCategory('ShardPage')

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.shardButtonMap = {}
        self.shardButtons = []
        self.scrollList = None
        self.currentBTP = None
        self.currentBTL = None
        self.currentBTR = None
        self.currentBTI = None
        self.currentO = None
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.9, 1, 1)
        self.textDisabledColor = Vec4(0.4, 0.8, 0.4, 1)
        self.ShardInfoUpdateInterval = 5.0
        self.lowPop = config.GetInt('shard-low-pop', 150)
        self.midPop = config.GetInt('shard-mid-pop', 300)
        self.highPop = -1
        self.showPop = config.GetBool('show-population', 0)
        self.showTotalPop = config.GetBool('show-total-population', 0)
        self.noTeleport = config.GetBool('shard-page-disable', 0)
        self.shardGroups = []
        self.shardText = []
        self.groupDialog = None

    def load(self):
        matchGui = loader.loadModel('phase_3.5/models/gui/matching_game_gui')
        main_text_scale = 0.06
        title_text_scale = 0.12
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.ShardPageTitle, text_scale=title_text_scale, textMayChange=0, pos=(0, 0, 0.6))
        helpText_ycoord = 0.403
        self.helpText = DirectLabel(parent=self, relief=None, text='', text_scale=main_text_scale, text_wordwrap=12, text_align=TextNode.ALeft, textMayChange=1, pos=(0.058, 0, helpText_ycoord))
        shardPop_ycoord = helpText_ycoord - 0.523
        totalPop_ycoord = shardPop_ycoord - 0.44
        self.districtInfo = NodePath('Selected-Shard-Info')
        self.districtInfo.reparentTo(self)
        self.preferredButton = DirectButton(parent=self, relief=None, image=matchGui.find('**/minnieCircle'), pos=(0.1, 0, -0.575), scale=0.35, text=TTLocalizer.ShardPagePreferred, text_scale=0.11, text_pos=(0, -0.2), command=self.setPreferredShard)
        self.totalPopulationText = DirectLabel(parent=self.districtInfo, relief=None, text=TTLocalizer.ShardPagePopulationTotal % 1, text_scale=main_text_scale, text_wordwrap=8, textMayChange=1, text_align=TextNode.ACenter, pos=(0.4247, 0, totalPop_ycoord))
        if self.showTotalPop:
            self.totalPopulationText.show()
        else:
            self.totalPopulationText.hide()
        self.gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        self.listXorigin = -0.02
        self.listFrameSizeX = 0.67
        self.listZorigin = -0.96
        self.listFrameSizeZ = 1.04
        self.arrowButtonScale = 1.3
        self.itemFrameXorigin = -0.247
        self.itemFrameZorigin = 0.365
        self.buttonXstart = self.itemFrameXorigin + 0.293
        self.regenerateScrollList()
        scrollTitle = DirectFrame(parent=self.scrollList, text=TTLocalizer.ShardPageScrollTitle, text_scale=main_text_scale, text_align=TextNode.ACenter, relief=None, pos=(self.buttonXstart, 0, self.itemFrameZorigin + 0.127))
        matchGui.removeNode()

    def firstLoadShard(self, buttonTuple):
        curShardTuples = base.cr.listActiveShards()
        curShardTuples.sort(compareShardTuples)
        actualShardId = base.localAvatar.defaultShard
        for i in xrange(len(curShardTuples)):
            shardId, name, pop, invasionStatus, groupAvCount = curShardTuples[i]
            if shardId == actualShardId:
                self.currentBTP = buttonTuple[0]
                self.currentBTL = buttonTuple[1]
                self.currentBTR = buttonTuple[2]
                self.currentBTI = buttonTuple[3]
                self.currentO = [pop, name, shardId]
                self.currentBTL['state'] = DGG.DISABLED
                self.currentBTR['state'] = DGG.DISABLED
                self.reloadRightBrain(pop, name, groupAvCount, shardId, buttonTuple)

    def unload(self):
        self.gui.removeNode()
        del self.title
        self.scrollList.destroy()
        del self.scrollList
        del self.shardButtons
        taskMgr.remove('ShardPageUpdateTask-doLater')

        ShtikerPage.ShtikerPage.unload(self)

    def regenerateScrollList(self):
        selectedIndex = 0

        if self.scrollList:
            selectedIndex = self.scrollList.getSelectedIndex()
            for button in self.shardButtons:
                button.detachNode()
            self.scrollList.destroy()
            self.scrollList = None

        self.scrollList = DirectScrolledList(parent=self, relief=None, pos=(-0.51, 0, 0), incButton_image=(self.gui.find('**/FndsLst_ScrollUp'),
         self.gui.find('**/FndsLst_ScrollDN'),
         self.gui.find('**/FndsLst_ScrollUp_Rllvr'),
         self.gui.find('**/FndsLst_ScrollUp')), incButton_relief=None, incButton_scale=(self.arrowButtonScale, self.arrowButtonScale, -self.arrowButtonScale), incButton_pos=(self.buttonXstart + 0.005, 0, self.itemFrameZorigin - 1.000), incButton_image3_color=Vec4(1, 1, 1, 0.2), decButton_image=(self.gui.find('**/FndsLst_ScrollUp'),
         self.gui.find('**/FndsLst_ScrollDN'),
         self.gui.find('**/FndsLst_ScrollUp_Rllvr'),
         self.gui.find('**/FndsLst_ScrollUp')), decButton_relief=None, decButton_scale=(self.arrowButtonScale, self.arrowButtonScale, self.arrowButtonScale), decButton_pos=(self.buttonXstart, 0.0025, self.itemFrameZorigin + 0.130), decButton_image3_color=Vec4(1, 1, 1, 0.2), itemFrame_pos=(self.itemFrameXorigin, 0, self.itemFrameZorigin), itemFrame_scale=1.0, itemFrame_relief=DGG.SUNKEN, itemFrame_frameSize=(self.listXorigin,
         self.listXorigin + self.listFrameSizeX,
         self.listZorigin,
         self.listZorigin + self.listFrameSizeZ), itemFrame_frameColor=(0.85, 0.95, 1, 1), itemFrame_borderWidth=(0.01, 0.01), numItemsVisible=15, forceHeight=0.065, items=self.shardButtons)
        self.scrollList.scrollTo(selectedIndex)

    def askForShardInfoUpdate(self, task = None):
        ToontownDistrictStats.refresh('shardInfoUpdated')
        taskMgr.doMethodLater(self.ShardInfoUpdateInterval, self.askForShardInfoUpdate, 'ShardPageUpdateTask-doLater')
        return Task.done

    def makeShardButton(self, shardId, groupAvCount, shardName, shardPop):
        shardButtonParent = DirectFrame()
        shardButtonL = DirectButton(parent=shardButtonParent, relief=None, text=shardName, text_scale=0.06, text_align=TextNode.ALeft, text_fg=Vec4(0, 0, 0, 1), text3_fg=self.textDisabledColor, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, textMayChange=0, command=self.reloadRightBrain)
        popText = str(shardPop)
        if popText is None:
            popText = ''
        model = loader.loadModel('phase_3.5/models/gui/matching_game_gui')
        button = model.find('**/minnieCircle')

        shardButtonR = DirectButton(parent=shardButtonParent, relief=None,
                                    image=button,
                                    image_scale=(0.3, 1, 0.3),
                                    image2_scale=(0.35, 1, 0.35),
                                    image_color=self.getPopColor(shardPop),
                                    pos=(0.58, 0, 0.0125),
                                    text=popText,
                                    text_scale=0.06,
                                    text_align=TextNode.ARight,
                                    text_pos=(-0.14, -0.0165), text_fg=Vec4(0, 0, 0, 1), text3_fg=self.textDisabledColor, text1_bg=self.textRolloverColor, text2_bg=self.textRolloverColor, textMayChange=1, command=self.reloadRightBrain)
        model.removeNode()
        button.removeNode()

        invasionMarker = NodePath('InvasionMarker-%s' % shardId)
        invasionMarker.reparentTo(shardButtonParent)

        buttonTuple = (shardButtonParent, shardButtonR, shardButtonL, invasionMarker)
        shardButtonL['extraArgs'] = extraArgs=[shardPop, shardName, groupAvCount, shardId, buttonTuple]
        shardButtonR['extraArgs'] = extraArgs=[shardPop, shardName, groupAvCount, shardId, buttonTuple]

        return buttonTuple

    def makeGroupButton(self, shardId, group, population):
        groupButtonParent = DirectFrame()
        groupButtonL = DirectButton(parent=groupButtonParent, relief=None, text=TTLocalizer.GlobalStreetNames[group][-1], text_pos=(0.0, -0.0225), text_scale=0.048, text_align=TextNode.ALeft, text_fg=Vec4(0, 0, 0, 1), text3_fg=self.textDisabledColor, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, command=self.joinGroup, extraArgs=[group, shardId])

        groupButtonR = DirectButton(parent=groupButtonParent, relief=None,
                                    pos=(0.58, 0, -0.0125),
                                    text=str(population),
                                    text_scale=0.055,
                                    text_align=TextNode.ACenter,
                                    command=self.joinGroup,
                                    extraArgs=[group, shardId],
                                    text_pos=(-0.00575, -0.0125), text_fg=Vec4(0, 0, 0, 1), text3_fg=Vec4(0, 0, 0, 1), text1_bg=self.textRolloverColor, text2_bg=self.textRolloverColor)

        return (groupButtonParent, groupButtonL, groupButtonR)
    
    def joinGroup(self, group, shardId):
        canonicalHoodId = ZoneUtil.getCanonicalHoodId(group)
        shardName = base.cr.activeDistrictMap[shardId].name
        hoodName = TTLocalizer.GlobalStreetNames[canonicalHoodId]
        teleportAccess = base.localAvatar.hasTeleportAccess(canonicalHoodId)

        if teleportAccess:
            message = TTLocalizer.GroupAskAccess
        elif base.localAvatar.defaultShard == shardId:
            self.acceptOnce('groupDialogDone', self.cleanupGroupDialog)
            self.groupDialog = TTDialog.TTGlobalDialog(style=TTDialog.Acknowledge, text=TTLocalizer.GroupAskNoAccessSame % (hoodName[0], hoodName[-1]), doneEvent='groupDialogDone')
            self.groupDialog.show()
            return
        else:
            message = TTLocalizer.GroupAskNoAccess
        
        self.acceptOnce('groupDialogDone', self.__handleGroupDialog, extraArgs=[canonicalHoodId if teleportAccess else base.localAvatar.lastHood, shardId])
        self.groupDialog = TTDialog.TTGlobalDialog(style=TTDialog.TwoChoice, text=message % (hoodName[0], hoodName[-1], shardName), doneEvent='groupDialogDone')
        self.groupDialog.show()
    
    def cleanupGroupDialog(self):
        self.ignore('groupDialogDone')
        self.groupDialog.cleanup()
        del self.groupDialog
    
    def __handleGroupDialog(self, canonicalHoodId, shardId):
        response = self.groupDialog.doneStatus
        self.cleanupGroupDialog()

        if response == 'ok':
            self.requestTeleport(canonicalHoodId, shardId)

    def removeRightBrain(self):
        self.districtInfo.find('**/*district-info').removeNode()

    def reloadRightBrain(self, shardPop, shardName, groupAvCount, shardId, buttonTuple):
        self.currentRightBrain = (shardPop, shardName, shardId, buttonTuple)
        if self.districtInfo.find('**/*district-info'):
            self.removeRightBrain()
        if self.currentBTL:
            self.currentBTL['state'] = DGG.NORMAL
        if self.currentBTR:
            self.currentBTR['state'] = DGG.NORMAL
        popText = self.getPopText(shardPop)
        districtInfoNode = self.districtInfo.attachNewNode('district-info')
        self.districtStatusLabel = DirectLabel(parent=districtInfoNode, relief=None, pos=(0.4247, 0, 0.45), text=popText, text_scale=0.09, text_fg=Vec4(0, 0, 0, 1), textMayChange=1)
        pText = TTLocalizer.ShardPageShardTitle % (shardName, str(shardPop))
        self.populationStatusLabel = DirectLabel(parent=districtInfoNode, relief=None, pos=(0.4247, 0, 0.38), text=pText, text_scale=0.04, text_fg=Vec4(0, 0, 0, 1), textMayChange=1)
        tText = TTLocalizer.ShardPageTeleport % shardName
        tImage = loader.loadModel('phase_4/models/gui/purchase_gui')
        tImage.setSz(1.35)
        self.shardTeleportButton = DirectButton(parent=districtInfoNode, relief=None, pos=(0.4247, 0, 0.25), image=(tImage.find('**/PurchScrn_BTN_UP'), tImage.find('**/PurchScrn_BTN_DN'), tImage.find('**/PurchScrn_BTN_RLVR')), text=tText, text_scale=0.065, text_pos=(0.0, 0.015), text_fg=Vec4(0, 0, 0, 1), textMayChange=1, command=self.choseShard, extraArgs=[shardId])

        self.currentBTP = buttonTuple[0]
        self.currentBTL = buttonTuple[1]
        self.currentBTR = buttonTuple[2]
        self.currentBTI = buttonTuple[3]
        self.currentO = [shardPop, shardName, shardId]
        self.currentBTL['state'] = DGG.DISABLED
        self.currentBTR['state'] = DGG.DISABLED
        self.preferredButton.setColor((0, 1, 0, 1) if settings.get('preferredShard') == shardName else (1, 0, 0, 1))

        if shardId == base.localAvatar.defaultShard:
            self.shardTeleportButton['state'] = DGG.DISABLED

        for button in self.shardGroups + self.shardText:
            button.removeNode()
        
        self.shardGroups = []
        self.shardText = []

        for i, group in enumerate(ToontownGlobals.GROUP_ZONES):
            btuple = self.makeGroupButton(shardId, group, groupAvCount[i])
            if ZoneUtil.getCanonicalHoodId(base.localAvatar.zoneId) == ZoneUtil.getCanonicalHoodId(group):
                btuple[1]['state'] = DGG.DISABLED
                btuple[2]['state'] = DGG.DISABLED
            self.shardGroups.append(btuple[0])
            self.shardText.append(btuple[2])

        buttonImage = (self.gui.find('**/FndsLst_ScrollUp'), self.gui.find('**/FndsLst_ScrollDN'), self.gui.find('**/FndsLst_ScrollUp_Rllvr'), self.gui.find('**/FndsLst_ScrollUp'))
        self.districtGroups = DirectScrolledList(parent=districtInfoNode, relief=None,
                                                 pos=(0.38, 0, -0.34),
                                                 incButton_image=buttonImage,
                                                 incButton_relief=None,
                                                 incButton_scale=(self.arrowButtonScale,
                                                                  self.arrowButtonScale,
                                                                  -self.arrowButtonScale),
                                                 incButton_pos=(self.buttonXstart + 0.005, 0, -0.125),
                                                 incButton_image3_color=Vec4(1, 1, 1, 0.2),
                                                 decButton_image=buttonImage,
                                                 decButton_relief=None,
                                                 decButton_scale=(self.arrowButtonScale,
                                                                  self.arrowButtonScale,
                                                                  self.arrowButtonScale),
                                                 decButton_pos=(self.buttonXstart, 0.0025, 0.445),
                                                 decButton_image3_color=Vec4(1, 1, 1, 0.2),
                                                 itemFrame_pos=(self.itemFrameXorigin, 0, self.itemFrameZorigin),
                                                 itemFrame_scale=1.0,
                                                 itemFrame_relief=DGG.SUNKEN,
                                                 itemFrame_frameSize=(self.listXorigin,
                                                                      (self.listXorigin + self.listFrameSizeX),
                                                                      self.listZorigin/2.1,
                                                                      (self.listZorigin + self.listFrameSizeZ)/2.1),
                                                 itemFrame_frameColor=(0.85, 0.95, 1, 1),
                                                 itemFrame_borderWidth=(0.01, 0.01),
                                                 numItemsVisible=7,
                                                 forceHeight=0.065,
                                                 items=self.shardGroups)

    def getPopColor(self, pop):
        if pop <= self.lowPop:
            newColor = POP_COLORS[0]
        elif pop <= self.midPop:
            newColor = POP_COLORS[1]
        else:
            newColor = POP_COLORS[2]
        return newColor

    def getPopText(self, pop):
        if pop <= self.lowPop:
            popText = TTLocalizer.ShardPageLow
        elif pop <= self.midPop:
            popText = TTLocalizer.ShardPageMed
        else:
            popText = TTLocalizer.ShardPageHigh
        return popText

    def getPopChoiceHandler(self, pop):
        if pop <= self.midPop:
            if self.noTeleport and not self.showPop:
                handler = self.shardChoiceReject
            else:
                handler = self.choseShard
        elif self.showPop:
            handler = self.choseShard
        else:
            if localAvatar.isAdmin():
                handler = self.choseShard
            else:
                handler = self.shardChoiceReject
        return handler

    def getCurrentZoneId(self):
        try:
            zoneId = base.cr.playGame.getPlace().getZoneId()
        except:
            zoneId = None
        return zoneId

    def createSuitHead(self, suitName):
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit(suitName)
        suit = Suit.Suit()
        suit.setDNA(suitDNA)
        headParts = suit.getHeadParts()
        head = hidden.attachNewNode('head')
        for part in headParts:
            copyPart = part.copyTo(head)
            copyPart.setDepthTest(1)
            copyPart.setDepthWrite(1)
        self.fitGeometry(head, fFlip=1)
        suit.delete()
        suit = None
        return head

    def updateScrollList(self):
        curShardTuples = base.cr.listActiveShards()
        curShardTuples.sort(compareShardTuples)

        actualShardId = base.localAvatar.defaultShard
        actualShardName = None
        anyChanges = 0
        totalPop = 0
        currentMap = {}
        self.shardButtons = []

        for i in xrange(len(curShardTuples)):

            shardId, name, pop, invasionStatus, groupAvCount = curShardTuples[i]

            if shardId == actualShardId:
                actualShardName = name

            totalPop += pop
            currentMap[shardId] = 1
            buttonTuple = self.shardButtonMap.get(shardId)

            if buttonTuple == None:
                buttonTuple = self.makeShardButton(shardId, groupAvCount, name, pop)
                self.shardButtonMap[shardId] = buttonTuple
                anyChanges = 1
            else:
                buttonTuple[1]['image_color'] = self.getPopColor(pop)
                buttonTuple[1]['text'] = str(pop)
                buttonTuple[1]['command'] = self.reloadRightBrain
                buttonTuple[1]['extraArgs'] = [pop, name, groupAvCount, shardId, buttonTuple]
                buttonTuple[2]['command'] = self.reloadRightBrain
                buttonTuple[2]['extraArgs'] = [pop, name, groupAvCount, shardId, buttonTuple]
            
            for i, button in enumerate(self.shardText):
                button['text'] = str(groupAvCount[i])

            self.shardButtons.append(buttonTuple[0])

            if invasionStatus:
                setupInvasionMarker(buttonTuple[3], invasionStatus)
            else:
                removeInvasionMarker(buttonTuple[3])

        for shardId, buttonTuple in self.shardButtonMap.items():

            if shardId not in currentMap:
                buttonTuple[3].removeNode()
                buttonTuple[0].destroy()
                del self.shardButtonMap[shardId]
                anyChanges = 1

        if anyChanges:
            self.regenerateScrollList()

        self.totalPopulationText['text'] = TTLocalizer.ShardPagePopulationTotal % totalPop
        helpText = TTLocalizer.ShardPageHelpIntro

        if actualShardName:
            helpText += TTLocalizer.ShardPageHelpWhere % actualShardName

        if not self.book.safeMode:
            helpText += TTLocalizer.ShardPageHelpMove

    def enter(self):
        self.askForShardInfoUpdate()
        self.updateScrollList()
        currentShardId = base.localAvatar.defaultShard
        buttonTuple = self.shardButtonMap.get(currentShardId)
        if buttonTuple:
            i = self.shardButtons.index(buttonTuple[0])
            self.scrollList.scrollTo(i, centered=1)
            self.firstLoadShard(buttonTuple)
        ShtikerPage.ShtikerPage.enter(self)
        self.accept('shardInfoUpdated', self.updateScrollList)

    def exit(self):
        for shardId, buttonTuple in self.shardButtonMap.items():
            buttonTuple[1]['state'] = DGG.NORMAL
            buttonTuple[2]['state'] = DGG.NORMAL
        self.ignore('shardInfoUpdated')
        self.ignore('ShardPageConfirmDone')
        taskMgr.remove('ShardPageUpdateTask-doLater')
        ShtikerPage.ShtikerPage.exit(self)

    def shardChoiceReject(self, shardId):
        self.confirm = TTDialog.TTGlobalDialog(doneEvent='ShardPageConfirmDone', message=TTLocalizer.ShardPageChoiceReject, style=TTDialog.Acknowledge)
        self.confirm.show()
        self.accept('ShardPageConfirmDone', self.__handleConfirm)

    def __handleConfirm(self):
        self.ignore('ShardPageConfirmDone')
        self.confirm.cleanup()
        del self.confirm

    def choseShard(self, shardId):
        if not base.localAvatar.defaultShard == shardId:
            self.requestTeleport(base.localAvatar.lastHood, shardId)
        
    def requestTeleport(self, hood, shardId):
        canonicalHoodId = ZoneUtil.getCanonicalHoodId(hood)

        try:
            place = base.cr.playGame.getPlace()
        except:
            try:
                place = base.cr.playGame.hood.loader.place
            except:
                place = base.cr.playGame.hood.place

        place.requestTeleport(canonicalHoodId, canonicalHoodId, shardId, -1)
    
    def setPreferredShard(self):
        if settings.get('preferredShard', '') == self.currentO[1]:
            self.preferredButton.setColor(1, 0, 0, 1)
            del settings['preferredShard']
        else:
            self.preferredButton.setColor(0, 1, 0, 1)
            settings['preferredShard'] = self.currentO[1]
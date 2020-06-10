from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer, ToontownGlobals, ToontownBattleGlobals
import NPCToons, ToonDNA, ToonHead

def createNPCToonHead(NPCID, dimension = 0.5):
    NPCInfo = NPCToons.NPCToonDict[NPCID]
    dnaList = NPCInfo[2]
    gender = NPCInfo[3]
    if dnaList == 'r':
        dnaList = NPCToons.getRandomDNA(NPCID, gender)
    dna = ToonDNA.ToonDNA()
    dna.newToonFromProperties(*dnaList)
    head = ToonHead.ToonHead()
    head.setupHead(dna, forGui=1)
    fitGeometry(head, fFlip=1, dimension=dimension)
    return head

def fitGeometry(geom, fFlip = 0, dimension = 0.5):
    p1 = Point3()
    p2 = Point3()
    geom.calcTightBounds(p1, p2)
    if fFlip:
        t = p1[0]
        p1.setX(-p2[0])
        p2.setX(-t)
    d = p2 - p1
    biggest = max(d[0], d[2])
    s = dimension / biggest
    mid = (p1 + d / 2.0) * s
    geomXform = hidden.attachNewNode('geomXform')
    for child in geom.getChildren():
        child.reparentTo(geomXform)

    geomXform.setPosHprScale(-mid[0], -mid[1] + 1, -mid[2], 180, 0, 0, s, s, s)
    geomXform.reparentTo(geom)

class NPCFriendPanel(DirectFrame):

    def __init__(self, parent = aspect2d, callable = False, **kw):
        optiondefs = (('relief', None, None), ('doneEvent', None, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent=parent)
        self.callable = callable
        self.cardList = []
        self.friendDict = {}
        self.pos = 0
        self.updateLayout()
        self.initialiseoptions(NPCFriendPanel)

        gui = loader.loadModel('phase_3.5/models/gui/battle_gui')
        buttonImage = (gui.find('**/PckMn_BackBtn'), gui.find('**/PckMn_BackBtn_Dn'), gui.find('**/PckMn_BackBtn_Rlvr'))
        self.leftArrow = DirectButton(parent=self, relief=None, image=buttonImage, pos=(-6.8, 0, 0), scale=3.8, command=self.addPageIndex, extraArgs=[-1])
        self.rightArrow = DirectButton(parent=self, relief=None, image=buttonImage, pos=(6.8, 0, 0), scale=-3.8, command=self.addPageIndex, extraArgs=[1])
        gui.removeNode()

        self.leftArrow.hide()

    def addPageIndex(self, index):
        self.pos += (16 * index)

        if self.pos > 0:
            self.leftArrow.show()
        else:
            self.leftArrow.hide()

        self.update()

    def update(self):
        friendList = sorted(self.friendDict.keys(), reverse=True, key=lambda id: NPCToons.getNPCTrackLevelHpRarity(id)[3])
        cardNum = 0

        for i in xrange(self.pos, self.pos + 16):
            card = self.cardList[cardNum]

            if len(friendList) > i:
                npcId = friendList[i]
                card.update(npcId, self.friendDict[npcId], self.callable)
                self.rightArrow.show()
            else:
                card.update(None, 0, self.callable)
                self.rightArrow.hide()

            cardNum += 1

    def updateLayout(self):
        for card in self.cardList:
            card.destroy()

        self.cardList = []
        xOffset = -5.2
        yOffset = 3.5
        count = 0

        for i in xrange(16):
            card = NPCFriendCard(parent=self, doneEvent=self['doneEvent'])
            self.cardList.append(card)
            card.setPos(xOffset, 1, yOffset)
            card.setScale(0.75)
            xOffset += 3.5
            count += 1

            if count % 4 == 0:
                xOffset = -5.25
                yOffset += -2.45

    def setFriends(self, friends):
        self.friendDict = friends

class NPCFriendCard(DirectFrame):
    normalTextColor = (0.3, 0.25, 0.2, 1)
    maxRarity = 5
    sosTracks = ToontownBattleGlobals.Tracks + ToontownBattleGlobals.NPCTracks

    def __init__(self, parent = aspect2dp, **kw):
        optiondefs = (('NPCID', 'Uninitialized', None), ('relief', None, None), ('doneEvent', None, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent=parent)
        self.initialiseoptions(NPCFriendCard)
        cardModel = loader.loadModel('phase_3.5/models/gui/playingCard')
        self.front = DirectFrame(parent=self, relief=None, image=cardModel.find('**/card_front'))
        self.front.hide()
        self.back = DirectFrame(parent=self, relief=None, image=cardModel.find('**/card_back'))
        self.sosTypeInfo = DirectLabel(parent=self.front, relief=None, text='', text_font=ToontownGlobals.getMinnieFont(), text_fg=self.normalTextColor, text_scale=0.35, text_align=TextNode.ACenter, text_wordwrap=16.0, pos=(0, 0, 1.15))
        self.NPCHead = None
        self.NPCName = DirectLabel(parent=self.front, relief=None, text='', text_fg=self.normalTextColor, text_scale=0.4, text_align=TextNode.ACenter, text_wordwrap=8.0, pos=(0, 0, -0.45))
        buttonModels = loader.loadModel('phase_3.5/models/gui/inventory_gui')
        upButton = buttonModels.find('**/InventoryButtonUp')
        downButton = buttonModels.find('**/InventoryButtonDown')
        rolloverButton = buttonModels.find('**/InventoryButtonRollover')
        self.sosCallButton = DirectButton(parent=self.front, relief=None, text=TTLocalizer.NPCCallButtonLabel, text_fg=self.normalTextColor, text_scale=0.28, text_align=TextNode.ACenter, image=(upButton,
         downButton,
         rolloverButton,
         upButton), image_color=(1.0, 0.2, 0.2, 1), image0_color=Vec4(1.0, 0.4, 0.4, 1), image3_color=Vec4(1.0, 0.4, 0.4, 0.4), image_scale=(4.4, 1, 3.6), image_pos=Vec3(0, 0, 0.08), pos=(-1.15, 0, -0.9), scale=1.25, command=self.__chooseNPCFriend)
        self.sosCallButton.hide()
        self.sosCountInfo = DirectLabel(parent=self.front, relief=None, text='', text_fg=self.normalTextColor, text_scale=0.75, text_align=TextNode.ALeft, textMayChange=1, pos=(0.0, 0, -1.0))
        star = loader.loadModel('phase_3.5/models/gui/name_star')
        self.rarityStars = []

        for i in xrange(self.maxRarity):
            label = DirectLabel(parent=self.front, relief=None, image=star, image_scale=0.2, image_color=Vec4(0.502, 0.251, 0.251, 1.0), pos=(1.1 - i * 0.24, 0, -1.2))
            label.hide()
            self.rarityStars.append(label)

    def __chooseNPCFriend(self):
        if self['NPCID'] and self['doneEvent']:
            doneStatus = {}
            doneStatus['mode'] = 'NPCFriend'
            doneStatus['friend'] = self['NPCID']
            messenger.send(self['doneEvent'], [doneStatus])

    def destroy(self):
        if self.NPCHead:
            self.NPCHead.detachNode()
            self.NPCHead.delete()

        DirectFrame.destroy(self)

    def update(self, NPCID, count = 0, fCallable = 0):
        oldNPCID = self['NPCID']
        self['NPCID'] = NPCID

        if NPCID != oldNPCID:
            if self.NPCHead:
                self.NPCHead.detachNode()
                self.NPCHead.delete()
            if NPCID is None:
                self.showBack()
                return

            self.front.show()
            self.back.hide()
            self.NPCName['text'] = TTLocalizer.NPCToonNames[NPCID]
            self.NPCHead = createNPCToonHead(NPCID, dimension=1.2)
            self.NPCHead.reparentTo(self.front)
            self.NPCHead.setZ(0.45)
            track, level, hp, rarity = NPCToons.getNPCTrackLevelHpRarity(NPCID)
            sosText = self.sosTracks[track]

            if track == ToontownBattleGlobals.NPC_RESTOCK_GAGS:
                if level == -1:
                    sosText += ' All'
                else:
                    sosText += ' ' + self.sosTracks[level]
            sosText = TextEncoder.upper(sosText)
            self.sosTypeInfo['text'] = sosText

            for i in xrange(self.maxRarity):
                if i < rarity:
                    self.rarityStars[i].show()
                else:
                    self.rarityStars[i].hide()

        if fCallable:
            self.sosCallButton.show()
            self.sosCountInfo.setPos(-0.4, 0, -0.9)
            self.sosCountInfo['text_scale'] = 0.4
            self.sosCountInfo['text_align'] = TextNode.ALeft
        else:
            self.sosCallButton.hide()
            self.sosCountInfo.setPos(0, 0, -0.9)
            self.sosCountInfo['text_scale'] = 0.5
            self.sosCountInfo['text_align'] = TextNode.ACenter
        if count > 0:
            countText = TTLocalizer.NPCFriendPanelRemaining % count
            self.sosCallButton['state'] = DGG.NORMAL
        else:
            countText = TTLocalizer.NPCFriendUnavailable
            self.sosCallButton['state'] = DGG.DISABLED
        self.sosCountInfo['text'] = countText
        return

    def showFront(self):
        self.front.show()
        self.back.hide()

    def showBack(self):
        self.front.hide()
        self.back.show()

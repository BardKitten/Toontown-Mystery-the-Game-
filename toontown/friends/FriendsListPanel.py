from panda3d.core import *
from direct.gui.DirectGui import *
from direct.fsm import StateData
from toontown.toon import ToonAvatarPanel
from toontown.friends import ToontownFriendSecret
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from otp.nametag.NametagGroup import *
from otp.nametag.NametagConstants import *
from otp.otpbase import OTPGlobals
FLPPets = 1
FLPOnline = 2
FLPAll = 3
globalFriendsList = None

def determineFriendName(friendId):
    handle = base.cr.identifyFriend(friendId)

    return handle.getName() if handle else ''

def compareFriends(f1, f2):
    name1 = determineFriendName(f1)
    name2 = determineFriendName(f2)
    if name1 > name2:
        return 1
    elif name1 == name2:
        return 0
    else:
        return -1

def showFriendsList():
    global globalFriendsList
    if globalFriendsList == None:
        globalFriendsList = FriendsListPanel()
    globalFriendsList.enter()
    return

def hideFriendsList():
    if globalFriendsList != None:
        globalFriendsList.exit()
    return

def showFriendsListTutorial():
    global globalFriendsList
    if globalFriendsList == None:
        globalFriendsList = FriendsListPanel()
    globalFriendsList.enter()
    globalFriendsList.closeCommand = globalFriendsList.close['command']
    globalFriendsList.close['command'] = None
    return

def hideFriendsListTutorial():
    if globalFriendsList != None:
        if hasattr(globalFriendsList, 'closeCommand'):
            globalFriendsList.close['command'] = globalFriendsList.closeCommand
        globalFriendsList.exit()
    return

def isFriendsListShown():
    if globalFriendsList != None:
        return globalFriendsList.isEntered
    return 0

def unloadFriendsList():
    global globalFriendsList
    if globalFriendsList != None:
        globalFriendsList.unload()
        globalFriendsList = None
    return

class FriendsListPanel(DirectFrame, StateData.StateData):

    def __init__(self):
        self.leftmostPanel = FLPPets
        self.rightmostPanel = FLPAll
        DirectFrame.__init__(self, relief=None)
        self.listScrollIndex = [0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0]
        self.initialiseoptions(FriendsListPanel)
        StateData.StateData.__init__(self, 'friends-list-done')
        self.friends = {}
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.9, 1, 1)
        self.textDisabledColor = Vec4(0.4, 0.8, 0.4, 1)
        self.panelType = FLPOnline

    def load(self):
        if self.isLoaded == 1:
            return None
        self.isLoaded = 1
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        auxGui = loader.loadModel('phase_3.5/models/gui/avatar_panel_gui')
        self.title = DirectLabel(parent=self, relief=None, text='', text_scale=TTLocalizer.FLPtitle, text_fg=(0, 0.1, 0.4, 1), pos=(0.007, 0.0, 0.2))
        background_image = gui.find('**/FriendsBox_Open')
        self['image'] = background_image
        self.reparentTo(base.a2dTopRight)
        self.setPos(-0.233, 0, -0.46)
        self.scrollList = DirectScrolledList(parent=self, relief=None, incButton_image=(gui.find('**/FndsLst_ScrollUp'),
         gui.find('**/FndsLst_ScrollDN'),
         gui.find('**/FndsLst_ScrollUp_Rllvr'),
         gui.find('**/FndsLst_ScrollUp')), incButton_relief=None, incButton_pos=(0.0, 0.0, -0.316), incButton_image3_color=Vec4(0.6, 0.6, 0.6, 0.6), incButton_scale=(1.0, 1.0, -1.0), decButton_image=(gui.find('**/FndsLst_ScrollUp'),
         gui.find('**/FndsLst_ScrollDN'),
         gui.find('**/FndsLst_ScrollUp_Rllvr'),
         gui.find('**/FndsLst_ScrollUp')), decButton_relief=None, decButton_pos=(0.0, 0.0, 0.117), decButton_image3_color=Vec4(0.6, 0.6, 0.6, 0.6), itemFrame_pos=(-0.17, 0.0, 0.06), itemFrame_relief=None, numItemsVisible=8, items=[])
        clipper = PlaneNode('clipper')
        clipper.setPlane(Plane(Vec3(-1, 0, 0), Point3(0.2, 0, 0)))
        clipNP = self.scrollList.attachNewNode(clipper)
        self.scrollList.setClipPlane(clipNP)
        self.close = DirectButton(parent=self, relief=None, image=(auxGui.find('**/CloseBtn_UP'), auxGui.find('**/CloseBtn_DN'), auxGui.find('**/CloseBtn_Rllvr')), pos=(0.01, 0, -0.38), command=self.__close)
        self.left = DirectButton(parent=self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), image3_color=Vec4(0.6, 0.6, 0.6, 0.6), pos=(-0.15, 0.0, -0.38), scale=(-1.0, 1.0, 1.0), command=self.__left)
        self.right = DirectButton(parent=self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), image3_color=Vec4(0.6, 0.6, 0.6, 0.6), pos=(0.17, 0, -0.38), command=self.__right)
        self.newFriend = DirectButton(parent=self, relief=None, pos=(-0.14, 0.0, 0.14), image=(auxGui.find('**/Frnds_Btn_UP'), auxGui.find('**/Frnds_Btn_DN'), auxGui.find('**/Frnds_Btn_RLVR')), text=('', TTLocalizer.FriendsListPanelNewFriend, TTLocalizer.FriendsListPanelNewFriend), text_scale=TTLocalizer.FLPnewFriend, text_fg=(0, 0, 0, 1), text_bg=(1, 1, 1, 1), text_pos=(0.1, -0.085), textMayChange=0, command=self.__newFriend)
        self.trueFriends = DirectButton(parent=self, relief=None, pos=TTLocalizer.FLPtruefriendsPos, image=(auxGui.find('**/ChtBx_ChtBtn_UP'), auxGui.find('**/ChtBx_ChtBtn_DN'), auxGui.find('**/ChtBx_ChtBtn_RLVR')), text=('',
         TTLocalizer.FriendsListPanelTrueFriends,
         TTLocalizer.FriendsListPanelTrueFriends,
         ''), text_scale=TTLocalizer.FLPtruefriends, text_fg=(0, 0, 0, 1), text_bg=(1, 1, 1, 1), text_pos=(-0.04, -0.085), textMayChange=0, command=self.__trueFriends)
        gui.removeNode()
        auxGui.removeNode()

    def unload(self):
        if self.isLoaded == 0:
            return None
        self.isLoaded = 0
        self.exit()
        del self.title
        del self.scrollList
        del self.close
        del self.left
        del self.right
        del self.friends
        DirectFrame.destroy(self)

    def makeFriendButton(self, avId, color):
        handle = base.cr.identifyFriend(avId)

        if not handle:
            base.cr.fillUpFriendsMap()
            return

        return DirectButton(relief=None, text=handle.getName(), text_scale=0.04, text_align=TextNode.ALeft, text_fg=color, text_shadow=None, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, text_font=ToontownGlobals.getToonFont(), textMayChange=0, command=self.__choseFriend, extraArgs=[avId])

    def enter(self):
        if self.isEntered == 1:
            return None
        self.isEntered = 1
        if self.isLoaded == 0:
            self.load()
        base.localAvatar.obscureFriendsListButton(1)
        if ToonAvatarPanel.ToonAvatarPanel.currentAvatarPanel:
            ToonAvatarPanel.ToonAvatarPanel.currentAvatarPanel.cleanup()
            ToonAvatarPanel.ToonAvatarPanel.currentAvatarPanel = None
        self.__updateScrollList()
        self.__updateTitle()
        self.__updateArrows()
        self.show()
        self.accept('friendOnline', self.__friendOnline)
        self.accept('friendOffline', self.__friendOffline)
        self.accept('friendsListChanged', self.__friendsListChanged)
        self.accept('friendsMapComplete', self.__friendsListChanged)
        return

    def exit(self):
        if self.isEntered == 0:
            return None
        self.isEntered = 0
        self.listScrollIndex[self.panelType] = self.scrollList.index
        self.hide()
        base.cr.cleanPetsFromFriendsMap()
        self.ignore('friendOnline')
        self.ignore('friendOffline')
        self.ignore('friendsListChanged')
        self.ignore('friendsMapComplete')
        base.localAvatar.obscureFriendsListButton(-1)
        messenger.send(self.doneEvent)
        return None

    def __close(self):
        messenger.send('wakeup')
        self.exit()

    def __left(self):
        messenger.send('wakeup')
        self.listScrollIndex[self.panelType] = self.scrollList.index
        if self.panelType > self.leftmostPanel:
            self.panelType -= 1
        self.__updateScrollList()
        self.__updateTitle()
        self.__updateArrows()

    def __right(self):
        messenger.send('wakeup')
        self.listScrollIndex[self.panelType] = self.scrollList.index
        if self.panelType < self.rightmostPanel:
            self.panelType += 1
        self.__updateScrollList()
        self.__updateTitle()
        self.__updateArrows()

    def __trueFriends(self):
        messenger.send('wakeup')
        ToontownFriendSecret.showFriendSecret()

    def __newFriend(self):
        messenger.send('wakeup')
        messenger.send('friendAvatar', [None, None, None])

    def __choseFriend(self, friendId):
        messenger.send('wakeup')
        handle = base.cr.identifyFriend(friendId)
        if handle != None:
            messenger.send('clickedNametag', [handle])

    def createButtons(self, avIds, nametag):
        avIds.sort(compareFriends)

        for avId in avIds:
            if avId not in self.friends:
                button = self.makeFriendButton(avId, nametag)

                if button:
                    self.scrollList.addItem(button, refresh=0)
                    self.friends[avId] = button

    def __updateScrollList(self):
        petFriends = []
        trueFriends = []
        friends = []

        if self.panelType == FLPAll or self.panelType == FLPOnline:
            if base.wantPets and base.localAvatar.hasPet():
                petFriends.insert(0, base.localAvatar.getPetId())

            for friendId in base.localAvatar.friendsList:
                if self.panelType != FLPOnline or base.cr.isFriendOnline(friendId):
                    handle = base.cr.identifyFriend(friendId)

                    if not handle:
                        base.cr.fillUpFriendsMap()
                        return

                    if base.localAvatar.isTrueFriends(friendId):
                        trueFriends.insert(0, friendId)
                    else:
                        friends.insert(0, friendId)
        elif self.panelType == FLPPets and base.wantPets:
            for avId, av in base.cr.doId2do.items():
                from toontown.pets import DistributedPet
                if isinstance(av, DistributedPet.DistributedPet):
                    petFriends.append(avId)

        for friendId in self.friends.keys():
            friendButton = self.friends[friendId]
            self.scrollList.removeItem(friendButton, refresh=0)
            friendButton.destroy()
            del self.friends[friendId]

        self.createButtons(petFriends, NAMETAG_COLORS[CCNonPlayer][0][0])
        self.createButtons(trueFriends, NAMETAG_COLORS[CCNormal][0][0])
        self.createButtons(friends, NAMETAG_COLORS[CCSpeedChat][0][0])

        self.scrollList.index = self.listScrollIndex[self.panelType]
        self.scrollList.refresh()

    def __updateTitle(self):
        if self.panelType == FLPOnline:
            self.title['text'] = TTLocalizer.FriendsListPanelOnlineFriends
        elif self.panelType == FLPAll:
            self.title['text'] = TTLocalizer.FriendsListPanelAllFriends
        else:
            self.title['text'] = TTLocalizer.FriendsListPanelPets
        self.title.resetFrameSize()

    def __updateArrows(self):
        if self.panelType == self.leftmostPanel:
            self.left['state'] = 'inactive'
        else:
            self.left['state'] = 'normal'
        if self.panelType == self.rightmostPanel:
            self.right['state'] = 'inactive'
        else:
            self.right['state'] = 'normal'

    def __friendOnline(self, doId):
        if self.panelType == FLPOnline:
            self.__updateScrollList()

    def __friendOffline(self, doId):
        if self.panelType == FLPOnline:
            self.__updateScrollList()

    def __friendsListChanged(self, arg1 = None, arg2 = None):
        self.__updateScrollList()

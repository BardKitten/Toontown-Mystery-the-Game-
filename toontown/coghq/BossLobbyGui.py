from panda3d.core import *
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

class BossLobbyGui(DirectFrame):

    class InitialFrame(DirectFrame):
        frame = 0

        class LobbySelection(DirectButton):

            def __init__(self, parent, **kw):
                optiondefs = (
                    ('relief', None, None),
                    ('image_scale', 0.55, None),
                    ('text_pos', (0.3, -0.0225), None),
                    ('text_scale', 0.075, None),
                )
                self.defineoptions(kw, optiondefs)
                DirectButton.__init__(self, relief=None)
                self.initialiseoptions(BossLobbyGui.InitialFrame.LobbySelection)

        def __init__(self, parent, callback, **kw):
            optiondefs = (
                ('relief', None, None),
                ('state', DGG.NORMAL, None),
                ('image', DGG.getDefaultDialogGeom(), None),
                ('image_scale', (1.0, 1.0, 0.75), None),
                ('image_color', ToontownGlobals.GlobalDialogColor, None),
                ('pos', (0, 0, 0), None),
            )
            self.defineoptions(kw, optiondefs)
            DirectFrame.__init__(self, relief=None)
            self.initialiseoptions(BossLobbyGui.InitialFrame)
            self.callback = callback
            self.selection = -1
            self.load()

        def destroy(self):
            if hasattr(self, 'title') and self.title:
                self.title.destroy()
                del self.title
            if hasattr(self, 'buttons') and len(self.buttons):
                for button in self.buttons:
                    button.destroy()
                del self.buttons
            if hasattr(self, 'okButton') and self.okButton:
                self.okButton.destroy()
                del self.okButton
            if hasattr(self, 'cancelButton') and self.cancelButton:
                self.cancelButton.destroy()
                del self.cancelButton
            DirectFrame.destroy(self)

        def load(self):
            empty = loader.loadModel("phase_3.5/models/gui/matching_game_gui.bam")
            buttons = loader.loadModel("phase_3/models/gui/dialog_box_buttons_gui")
            self.emptyList = (empty.find("**/minnieCircle"), empty.find("**/minnieCircle"), empty.find("**/minnieCircle"))
            okImageList = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            cancelImageList = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
            empty.removeNode()
            buttons.removeNode()
            self.title = DirectLabel(parent=self, relief=None, text="Select a Lobby", textMayChange=1, text_scale=0.1, pos=(0, 0, 0.25))
            self.okButton = DirectButton(parent=self, relief=None, image=okImageList, pos=(-0.1, 0, -0.275), command=self.nextFrame, extraArgs=[True])
            self.cancelButton = DirectButton(parent=self, relief=None, image=cancelImageList, pos=(0.1, 0, -0.275), command=self.nextFrame, extraArgs=[False])
            self.buttons = []
            public = BossLobbyGui.InitialFrame.LobbySelection(self, image=self.emptyList, pos=(-0.35, 0, 0.075), text="Public", command=self.setSelection, extraArgs=[0])
            private = BossLobbyGui.InitialFrame.LobbySelection(self, image=self.emptyList, pos=(-0.3475, 0, -0.075), text="Private", command=self.setSelection, extraArgs=[1])
            self.buttons.extend([
                public,
                private
            ])

        def setSelection(self, buttonId):
            newSelection = self.buttons[buttonId]
            if newSelection:
                for button in self.buttons:
                    button.setColor(1, 1, 1, 1)
                newSelection.setColor(0, 1, 0, 1)
            self.selection = buttonId

        def getSelection(self):
            return self.selection

        def nextFrame(self, status):
            if status and self.getSelection() >= 0:
                options = {
                    'lobbyType': self.getSelection()
                }
                self.callback(self.frame + 1, options)
            else:
                self.callback(-1)

    class SecondaryFrame(DirectFrame):
        frame = 1

        class LobbyList(DirectScrolledList):

            def __init__(self, parent, **kw):
                buttons = loader.loadModel("phase_3/models/gui/tt_m_gui_mat_mainGui")
                arrowGui = (buttons.find('**/tt_t_gui_mat_arrowUp'), buttons.find('**/tt_t_gui_mat_arrowDown'), buttons.find('**/tt_t_gui_mat_arrowDisabled'))
                buttons.removeNode()
                optiondefs = (
                    ('relief', None, None),
                    ('pos', (-0.375, 0, -0.045), None),
                    ('numItemsVisible', 4, None),
                    ('forceHeight', 0.12, None),
                    ('itemFrame_relief', DGG.SUNKEN, None),
                    ('itemFrame_pos', (0, 0, 0), None),
                    ('itemFrame_scale', 1.0, None),
                    ('itemFrame_borderWidth', (0.015, 0.015), None),
                    ('itemFrame_frameSize', (-0.325, 0.225, -0.325, 0.2), None),
                    ('itemFrame_frameColor', (0.85, 0.95, 1, 1), None),
                    ('decButton_image', arrowGui, None),
                    ('decButton_relief', None, None),
                    ('decButton_pos', (0.31, 0, 0.025), None),
                    ('decButton_hpr', (0, 0, -90), None),
                    ('decButton_scale', 0.5, None),
                    ('incButton_image', arrowGui, None),
                    ('incButton_relief', None, None),
                    ('incButton_pos', (0.31, 0, -0.175), None),
                    ('incButton_hpr', (0, 0, 90), None),
                    ('incButton_scale', 0.5, None),
                )
                self.defineoptions(kw, optiondefs)
                DirectScrolledList.__init__(self, relief=None)
                self.initialiseoptions(BossLobbyGui.SecondaryFrame.LobbyList)

        class LobbyListItem(DirectFrame):

            def __init__(self, parent, itemText, callback, **kw):
                optiondefs = (
                    ('relief', None, None),
                    ('frameColor', (0.85, 0.95, 1, 1), None),
                    ('frameSize', (-0.31, 0.21, 0.055, 0.185), None),
                )
                self.defineoptions(kw, optiondefs)
                DirectFrame.__init__(self, relief=None)
                self.initialiseoptions(BossLobbyGui.SecondaryFrame.LobbyListItem)
                self.button = DirectButton(
                    parent=self,
                    relief=None,
                    text=itemText,
                    text_align=TextNode.ALeft,
                    text_fg=Vec4(0, 0, 0, 1),
                    text3_fg=(0.4, 0.8, 0.4, 1),
                    text1_bg=(1, 1, 0, 1),
                    text2_bg=(0.5, 0.9, 1, 1),
                    pos=(-0.28, 0, 0.105),
                    scale=0.065,
                    command=callback,
                    extraArgs=[itemText],
                )

            def destroy(self):
                if hasattr(self, 'button') and self.button:
                    self.button.destroy()
                DirectFrame.destroy(self)

        class LobbyEntry(DirectEntry):

            def __init__(self, parent, **kw):
                optiondefs = (
                    ('relief', DGG.SUNKEN, None),
                    ('borderWidth', (0.25, 0.25), None),
                    ('pos', (-0.675, 0, 0.285), None),
                    ('scale', (0.05, 0.055, 0.055), None),
                    ('numLines', 1, None),
                    ('focus', 1, None),
                    ('frameColor', (0.85, 0.95, 1, 1), None),
                )
                self.defineoptions(kw, optiondefs)
                DirectEntry.__init__(self, relief=None)
                self.initialiseoptions(BossLobbyGui.SecondaryFrame.LobbyEntry)

        def __init__(self, parent, callback, **kw):
            optiondefs = (
                ('relief', None, None),
                ('state', DGG.NORMAL, None),
                ('image', DGG.getDefaultDialogGeom(), None),
                ('image_scale', (1.6, 1.0, 1.3), None),
                ('image_color', ToontownGlobals.GlobalDialogColor, None),
                ('pos', (0, 0, 0), None),
            )
            self.defineoptions(kw, optiondefs)
            DirectFrame.__init__(self, relief=None)
            self.initialiseoptions(BossLobbyGui.SecondaryFrame)
            self.callback = callback
            self.items = []
            self.selection = None
            self.friendsOnly = False
            self.laffLimit = False
            self.lobbyName = None
            self.isCreating = False
            self.load()

        def destroy(self):
            if hasattr(self, 'titleLeft') and self.titleLeft:
                self.titleLeft.destroy()
                del self.titleLeft
            if hasattr(self, 'lobbies') and self.lobbies:
                self.lobbies.destroy()
                del self.lobbies
            if hasattr(self, 'entry') and self.entry:
                self.entry.destroy()
                del self.entry
            if hasattr(self, 'cancelButton') and self.cancelButton:
                self.cancelButton.destroy()
                del self.cancelButton
            if hasattr(self, 'nextButton') and self.nextButton:
                self.nextButton.destroy()
                del self.nextButton
            if hasattr(self, 'nameLabel') and self.nameLabel:
                self.nameLabel.destroy()
                del self.nameLabel
            if hasattr(self, 'nameEntry') and self.nameEntry:
                self.nameEntry.destroy()
                del self.nameEntry
            if hasattr(self, 'friendLabel') and self.friendLabel:
                self.friendLabel.destroy()
                del self.friendLabel
            if hasattr(self, 'friendCheckbox') and self.friendCheckbox:
                self.friendCheckbox.destroy()
                del self.friendCheckbox
            if hasattr(self, 'laffLabel') and self.laffLabel:
                self.laffLabel.destroy()
                del self.laffLabel
            if hasattr(self, 'laffCheckbox') and self.laffCheckbox:
                self.laffCheckbox.destroy()
                del self.laffCheckbox
            DirectFrame.destroy(self)

        def load(self):
            empty = loader.loadModel("phase_3.5/models/gui/matching_game_gui.bam")
            buttons = loader.loadModel("phase_3/models/gui/tt_m_gui_mat_mainGui")
            cancelImageList = (buttons.find('**/tt_t_gui_mat_closeUp'), buttons.find('**/tt_t_gui_mat_closeDown'), buttons.find('**/tt_t_gui_mat_closeDown'))
            nextImageList = (buttons.find('**/tt_t_gui_mat_nextUp'), buttons.find('**/tt_t_gui_mat_nextDown'), buttons.find('**/tt_t_gui_mat_nextDown'))
            emptyList = (empty.find("**/minnieCircle"), empty.find("**/minnieCircle"), empty.find("**/minnieCircle"))
            empty.removeNode()
            buttons.removeNode()

            self.titleLeft = DirectLabel(parent=self, relief=None, text="Select a Lobby", textMayChange=1, text_scale=0.08, pos=(-0.435, 0, 0.475))
            self.titleRight = DirectLabel(parent=self, relief=None, text="Create a Lobby", textMayChange=1, text_scale=0.08, pos=(0.39, 0, 0.475))

            self.lobbies = BossLobbyGui.SecondaryFrame.LobbyList(self)
            self.entry = BossLobbyGui.SecondaryFrame.LobbyEntry(self, command=self.loadItemsToList)

            self.items = [
                "Loudrob",
                "Jake",
                "Voltage",
                "Daniel",
                "Mel",
            ]

            self.nameLabel = DirectLabel(parent=self, relief=None, text="Name:", text_scale=0.06, pos=(0.125, 0, 0.285))
            self.nameEntry = BossLobbyGui.SecondaryFrame.LobbyEntry(self, command=self.setLobbyName, pos=(0.27, 0, 0.285), width=9)

            self.friendLabel = DirectLabel(parent=self, relief=None, text="Friends Only?", text_scale=0.06, pos=(0.221, 0, 0.085))
            self.friendCheckbox = DirectButton(parent=self, relief=None, image=emptyList, pos=(0.62, 0, 0.095), scale=0.55, color=(1, 0, 0, 1), command=self.toggleFriendsOnly)

            self.laffLabel = DirectLabel(parent=self, relief=None, text="70+ Laff Only?", text_scale=0.06, pos=(0.251, 0, -0.115))
            self.laffCheckbox = DirectButton(parent=self, relief=None, image=emptyList, pos=(0.62, 0, -0.105), scale=0.55, color=(1, 0, 0, 1), command=self.toggleLaffLimit)

            self.cancelButton = DirectButton(parent=self, relief=None, image=cancelImageList, pos=(-0.65, 0, -0.535), scale=0.57, command=self.nextFrame, extraArgs=[False])
            self.nextButton = DirectButton(parent=self, relief=None, image=nextImageList, pos=(0.65, 0, -0.535), scale=0.3, command=self.nextFrame, extraArgs=[True])

        def loadItemsToList(self, entryText):
            if hasattr(self, 'lobbies') and self.lobbies:
                self.lobbies.destroy()
            self.lobbies = BossLobbyGui.SecondaryFrame.LobbyList(self)
            toAdd = []
            for i in self.items:
                if i.lower().startswith(entryText.lower()):
                    toAdd.append(i)
            for i in sorted(toAdd):
                newItem = BossLobbyGui.SecondaryFrame.LobbyListItem(self, i, self.setSelection)
                self.lobbies.addItem(newItem)

        def setSelection(self, selection):
            self.selection = selection

        def getSelection(self):
            return self.selection

        def toggleFriendsOnly(self):
            if self.friendsOnly:
                self.friendsOnly = False
                self.friendCheckbox.setColor(1, 0, 0, 1)
            else:
                self.friendsOnly = True
                self.friendCheckbox.setColor(0, 1, 0, 1)

        def getFriendsOnly(self):
            return self.friendsOnly

        def toggleLaffLimit(self):
            if self.laffLimit:
                self.laffLimit = False
                self.laffCheckbox.setColor(1, 0, 0, 1)
            else:
                self.laffLimit = True
                self.laffCheckbox.setColor(0, 1, 0, 1)

        def getLaffLimit(self):
            return self.laffLimit

        def setLobbyName(self, name):
            self.isCreating = bool(name)
            self.lobbyName = name

        def getLobbyName(self):
            return self.lobbyName

        def nextFrame(self, status):
            if status:
                if self.getSelection():
                    options = {
                        'selected': self.getSelection()
                    }
                    self.callback(self.frame + 1, options)
                elif self.isCreating:
                    options = {
                        'name': self.lobbyName,
                        'friends': self.getFriendsOnly(),
                        'laff': self.getLaffLimit(),
                    }
                    self.callback(self.frame + 1, options)
                else:
                    self.callback(-1)
            else:
                self.callback(-1)

    def __init__(self, callback, av):
        DirectFrame.__init__(self)
        self.callback = callback
        self.avatar = av
        self.frame = None

    def destroy(self):
        if hasattr(self, 'frame') and self.frame:
            self.frame.destroy()
            del self.frame
        DirectFrame.destroy(self)

    def loadFrame(self, frameNum, args={}):
        if hasattr(self, 'frame') and self.frame:
            self.frame.destroy()
        if frameNum == -1:
            self.callback(self.avatar, False)
        elif frameNum == 0:
            self.frame = BossLobbyGui.InitialFrame(self, self.loadFrame)
        elif frameNum == 1 and args.get('lobbyType') is not None:
            lobby = args.get('lobbyType')
            if lobby == 0:
                self.callback(self.avatar, True)
            elif lobby == 1:
                self.frame = BossLobbyGui.SecondaryFrame(self, self.loadFrame)
        elif frameNum == 2:
            selection = args.get('selected')
            name = args.get('name')
            if selection:
                self.callback(self.avatar, True)
            elif name:
                friendsOnly = args.get('friends')
                laffLimit = args.get('laff')
                self.callback(self.avatar, True)
            else:
                self.callback(self.avatar, False)

# The following is made for use with the GUI editor.
GUI_EDITOR = """
from toontown.coghq.BossLobbyGui import BossLobbyGui

test = BossLobbyGui(None, None)
test.loadFrame(1, {'lobbyType': 1})
"""

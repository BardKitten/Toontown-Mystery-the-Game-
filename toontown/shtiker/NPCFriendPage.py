import ShtikerPage
from direct.gui.DirectGui import *
from panda3d.core import *
from toontown.toon import NPCFriendPanel
from toontown.toonbase import TTLocalizer

class NPCFriendPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    def load(self):
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.NPCFriendPageTitle, text_scale=0.12, textMayChange=0, pos=(0, 0, 0.6))
        self.friendPanel = NPCFriendPanel.NPCFriendPanel(parent=self, callable=False)
        self.friendPanel.setScale(0.1225)
        self.friendPanel.setZ(-0.03)
        return

    def unload(self):
        ShtikerPage.ShtikerPage.unload(self)
        del self.title
        del self.friendPanel

    def updatePage(self):
        self.friendPanel.setFriends(base.localAvatar.NPCFriendsDict)
        self.friendPanel.update()

    def enter(self):
        self.updatePage()
        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)

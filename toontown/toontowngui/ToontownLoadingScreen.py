from pandac.PandaModules import *
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.hood import ZoneUtil
import random

LOADING_SCREEN_SORT_INDEX = 4000

class ToontownLoadingScreen:

    def __init__(self):
        self.__expectedCount = 0
        self.__count = 0
        self.textures = [(loader.loadTexture('phase_3.5/maps/loading/toon.jpg'), ToontownGlobals.getInterfaceFont(), (0, 0, 0.5, 1)),
         (loader.loadTexture('phase_3.5/maps/loading/cog.jpg'), ToontownGlobals.getSuitFont(), (1.0, 1.0, 1.0, 1)),
         (loader.loadTexture('phase_3.5/maps/loading/default.jpg'), ToontownGlobals.getInterfaceFont(), (0, 0, 0.5, 1))
        ]
        self.gui = loader.loadModel('phase_3/models/gui/progress-background.bam')
        self.title = DirectLabel(guiId='ToontownLoadingScreenTitle', parent=self.gui, relief=None, pos=(base.a2dRight/5, 0, 0.235), text='', textMayChange=1, text_scale=0.08, text_fg=(0, 0, 0.5, 1), text_align=TextNode.ALeft, text_font=ToontownGlobals.getInterfaceFont())
        self.tip = DirectLabel(guiId='ToontownLoadingScreenTip', parent=self.gui, relief=None, pos=(0, 0, 0.045), text='', textMayChange=1, text_scale=0.05, text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), text_align=TextNode.ACenter)
        self.waitBar = DirectWaitBar(guiId='ToontownLoadingScreenWaitBar', parent=self.gui, frameSize=(base.a2dLeft+(base.a2dRight/4.95), base.a2dRight-(base.a2dRight/4.95), -0.03, 0.03), pos=(0, 0, 0.15), text='')
        logoScale = 0.5625  # Scale for our locked aspect ratio (2:1).
        self.logo = OnscreenImage(
            image='phase_3/maps/toontown-logo.png',
            scale=(logoScale * 2.0, 1, logoScale))
        self.logo.reparentTo(hidden)
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        scale = self.logo.getScale()
        self.logo.setPos(0, 0, -scale[2])

    def destroy(self):
        self.tip.destroy()
        self.title.destroy()
        self.gui.removeNode()
        self.logo.removeNode()

    def getTip(self, tipCategory):
        return TTLocalizer.TipTitle + ' ' + random.choice(TTLocalizer.TipDict.get(tipCategory))

    def begin(self, range, label, gui, tipCategory, zoneId):
        info = self.textures[ZoneUtil.isCogHQZone(zoneId) if zoneId else 2]
        self.waitBar['range'] = range
        self.title['text'] = label
        self.__count = 0
        self.__expectedCount = range
        if gui:
            self.waitBar['frameSize'] = (base.a2dLeft+(base.a2dRight/4.95), base.a2dRight-(base.a2dRight/4.95), -0.03, 0.03)
            self.title['text_font'] = info[1]
            self.title['text_fg'] = info[2]
            self.title.reparentTo(base.a2dpBottomLeft, LOADING_SCREEN_SORT_INDEX)
            self.title.setPos(base.a2dRight/5, 0, 0.235)
            self.tip['text'] = self.getTip(tipCategory)
            self.gui.setPos(0, -0.1, 0)
            self.gui.reparentTo(aspect2d, LOADING_SCREEN_SORT_INDEX)
            self.gui.setTexture(info[0], 1)
            self.logo.reparentTo(base.a2dpTopCenter, LOADING_SCREEN_SORT_INDEX)
        else:
            self.title.reparentTo(base.a2dpBottomLeft, LOADING_SCREEN_SORT_INDEX)
            self.gui.reparentTo(hidden)
            self.logo.reparentTo(hidden)
        self.tip.reparentTo(base.a2dpBottomCenter, LOADING_SCREEN_SORT_INDEX)
        self.waitBar.reparentTo(base.a2dpBottomCenter, LOADING_SCREEN_SORT_INDEX)
        self.waitBar.update(self.__count)

    def end(self):
        self.waitBar.finish()
        self.waitBar.reparentTo(self.gui)
        self.title.reparentTo(self.gui)
        self.tip.reparentTo(self.gui)
        self.gui.reparentTo(hidden)
        self.logo.reparentTo(hidden)
        return (self.__expectedCount, self.__count)

    def abort(self):
        self.gui.reparentTo(hidden)

    def tick(self):
        self.__count = self.__count + 1
        self.waitBar.update(self.__count)
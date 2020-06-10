from direct.gui.DirectGui import *
from otp.otpbase import OTPLocalizer
from toontown.catalog import CatalogFurnitureItem
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.toontowngui import TTDialog
from DistributedFurnitureItem import DistributedFurnitureItem
import glob, ntpath, os, time

class DistributedTV(DistributedFurnitureItem):

    def __init__(self, cr):
        DistributedFurnitureItem.__init__(self, cr)
        self.dialog = None
        self.screen = None
        self.sound = None
        self.accept('exitingStoppedState', self.destroyGui)
    
    def loadModel(self, animate=1):
        model = DistributedFurnitureItem.loadModel(self)

        if animate:
            pos = CatalogFurnitureItem.TvToPosScale[self.item.furnitureType]
            self.screen = NodePath(CardMaker('tv-screen').generate())

            model.find('**/toonTownBugTV_screen').hide()
            self.screen.reparentTo(model)
            self.screen.setScale(*pos[1])
            self.screen.setPos(*pos[0])
            self.resetScreen()

        cSphere = CollisionSphere(0.0, -1.5, 1.0, 1.575)
        cSphere.setTangible(0)
        colNode = CollisionNode('TV-%s' % self.doId)
        colNode.addSolid(cSphere)
        cSpherePath = model.attachNewNode(colNode)
        cSpherePath.setCollideMask(ToontownGlobals.WallBitmask)
        self.accept('enterTV-%s' % self.doId, self.__enterSphere)
        return model
    
    def disable(self):
        self.ignoreAll()
        self.destroyGui()
        self.destroySound()
        DistributedFurnitureItem.disable(self)
    
    def setVideo(self, video, time):
        if (not video) or (not time):
            return

        self.destroySound()
        self.startVideo(os.path.join('user', os.path.join('videos', video)), time)
    
    def getPack(self, name):
        for pack in TTLocalizer.TVPacks:
            if pack.lower() in name:
                return pack

        return None
    
    def destroySound(self):
        if self.sound:
            self.sound.stop()
            self.sound = None
    
    def destroyGui(self, arg=None):
        if self.dialog:
            self.dialog.destroy()
            self.dialog = None
        
    def destroyGuiAndWalk(self, arg=None):
        self.destroyGui()
        base.cr.playGame.getPlace().setState('walk')
    
    def cutOff(self, string):
        return string if len(string) < 24 else '%s...' % string[:24]
    
    def resetScreen(self):
        self.screen.setTextureOff(TextureStage.getDefault())
        self.screen.setColor(0.3, 0.3, 0.3, 1.0)
    
    def startVideo(self, video, startTime):
        if not os.path.exists(video):
            pack = self.getPack(video)
            base.localAvatar.setSystemMessage(0, TTLocalizer.TVUnknownVideoPack % pack if pack else TTLocalizer.TVUnknownVideo)
            self.resetScreen()
            return
        
        start = time.time() - startTime
        movie = loader.loadTexture(video)
        self.sound = loader.loadSfx(video)
        length = self.sound.length()
        
        if start >= length:
            start -= int(start / length) * length
        
        movie.synchronizeTo(self.sound)
        self.screen.setColor(1, 1, 1, 1)
        self.screen.setTexture(movie)
        self.screen.setTexScale(TextureStage.getDefault(), movie.getTexScale())
        self.sound.setTime(start)
        self.sound.setLoop(True)
        self.sound.play()
    
    def __enterSphere(self, collisionEntry):
        if base.localAvatar.doId != self.furnitureMgr.ownerId:
            return

        videos = []
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        buttonImage = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp'))
        base.cr.playGame.getPlace().setState('stopped')
        self.dialog = DirectFrame(relief=None, geom=DGG.getDefaultDialogGeom(), geom_color=ToontownGlobals.GlobalDialogColor, geom_scale=(1.33, 1, 1.4),
                                  pos=(0, 0, 0), text=TTLocalizer.TVChooseVideo, text_scale=0.07, text_pos=(0, 0.575))

        for file in sorted(glob.glob('user/videos/*.mp4')):
            filename = ntpath.basename(file)
            videos.append(DirectButton(relief=None, text=self.cutOff(filename[:-4]), text_pos=(0.0, -0.0225), text_scale=0.048, text_align=TextNode.ALeft, text_fg=(0, 0, 0, 1), text3_fg=(0.4, 0.8, 0.4, 1), text1_bg=(0.5, 0.9, 1, 1), text2_bg=(1, 1, 0, 1), command=self.chooseVideo, extraArgs=[filename]))
            
        scrollList = DirectScrolledList(parent=self.dialog, relief=None, pos=(-0.05, 0, 0), incButton_image=buttonImage, incButton_relief=None, incButton_scale=(1.3, 1.3, -1.3),
                                        incButton_pos=(0.045, 0, -0.4), incButton_image3_color=(1, 1, 1, 0.2), decButton_image=buttonImage, decButton_relief=None,
                                        decButton_scale=1.3, decButton_pos=(0.045, 0, 0.5), decButton_image3_color=(1, 1, 1, 0.2), itemFrame_pos=(-0.247, 0, 0.365),
                                        itemFrame_scale=1.0, itemFrame_relief=DGG.SUNKEN, itemFrame_frameSize=(-0.02, 0.6, -0.7,  0.08), itemFrame_frameColor=(0.85, 0.95, 1, 1),
                                        itemFrame_borderWidth=(0.01, 0.01), numItemsVisible=10, forceHeight=0.065, items=videos)
        cancelButton = DirectButton(parent=self.dialog, relief=None, image=(buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), pos=(0, 0, -0.55), text=OTPLocalizer.lCancel, text_scale=0.06, text_pos=(0, -0.1), command=self.destroyGuiAndWalk)

        gui.removeNode()
        buttons.removeNode()
    
    def chooseVideo(self, video):
        self.destroyGuiAndWalk()
        self.sendUpdate('requestVideo', [video])
    
    def showDialog(self, text):
        base.cr.playGame.getPlace().setState('stopped')
        self.dialog = TTDialog.TTDialog(style=TTDialog.Acknowledge, text=text, text_wordwrap=15, fadeScreen=1, command=self.destroyGuiAndWalk)
    
    def requestVideoResponse(self, response):
        if response == ToontownGlobals.TV_NOT_OWNER:
            self.showDialog(TTLocalizer.TVNotOwner)
        elif response == ToontownGlobals.TV_INVALID_VIDEO:
            self.showDialog(TTLocalizer.TVInvalidVideo)
        elif response == ToontownGlobals.TV_OK:
            self.showDialog(TTLocalizer.TVOK)
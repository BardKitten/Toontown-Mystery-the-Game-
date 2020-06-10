from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from toontown.catalog import CatalogFurnitureItem
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.toontowngui import TTDialog
from DistributedFurnitureItem import DistributedFurnitureItem

class DistributedChair(DistributedFurnitureItem):

    def __init__(self, cr):
        DistributedFurnitureItem.__init__(self, cr)
        self.dialog = None
        self.exitButton = None
        self.avId = ToontownGlobals.CHAIR_NONE
        self.accept('exitingStoppedState', self.destroyGui)
    
    def loadModel(self):
        model = DistributedFurnitureItem.loadModel(self)
        cSphere = CollisionSphere(0.0, self.getChair()[3], 1.0, 1.575)
        cSphere.setTangible(0)
        colNode = CollisionNode('Chair-%s' % self.doId)
        colNode.addSolid(cSphere)
        cSpherePath = model.attachNewNode(colNode)
        cSpherePath.setCollideMask(ToontownGlobals.WallBitmask)
        self.accept('enterChair-%s' % self.doId, self.__enterSphere)
        return model
    
    def disable(self):
        av = base.cr.doId2do.get(self.avId)

        if av:
            self.resetAvatar(av)

        self.ignoreAll()
        DistributedFurnitureItem.disable(self)
    
    def getChair(self):
        return CatalogFurnitureItem.ChairToPosHpr[self.item.furnitureType]
    
    def destroyGui(self):
        if self.exitButton:
            self.exitButton.destroy()
            self.exitButton = None
        
        if self.dialog:
            self.dialog.destroy()
            self.dialog = None
    
    def setupGui(self):
        castGui = loader.loadModel('phase_4/models/gui/fishingGui')
        self.exitButton = DirectButton(parent=base.a2dBottomRight, relief=None, text=('', TTLocalizer.FishingExit, TTLocalizer.FishingExit), text_align=TextNode.ACenter, text_scale=0.1, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(0.0, -0.12), pos=(-0.158, 0, 0.14), image=(castGui.find('**/exit_buttonUp'), castGui.find('**/exit_buttonDown'), castGui.find('**/exit_buttonRollover')), command=self.sendUpdate, extraArgs=['requestSit', [ToontownGlobals.CHAIR_STOP]])
        castGui.removeNode()

        base.localAvatar.stopSleepWatch()
        base.localAvatar.startSleepWatch(self.__handleFallingAsleep)

    def resetAvatar(self, av):
        av.loop('neutral')
        av.setPos(av.getPos(render))
        av.getGeomNode().setHpr(0, 0, 0)
        av.setH(self.getH() + self.getChair()[1][0])
        av.reparentTo(render)
        
        if av == base.localAvatar:
            base.localAvatar.setPreventCameraDisable(False)
            base.cr.playGame.getPlace().setState('walk')

    def setAvId(self, avId):
        if avId == ToontownGlobals.CHAIR_NONE:
            self.avId = avId
            return

        chair = self.getChair()
        av = base.cr.doId2do.get(avId)
        
        if not av:
            return

        sitStartDuration = av.getDuration('sit-start')
        sequence = Sequence(Func(av.loop, 'walk'), av.getGeomNode().hprInterval(0.25, chair[1]), Parallel(Sequence(Wait(sitStartDuration * 0.25), av.posInterval(sitStartDuration * 0.25, chair[0])), ActorInterval(av, 'sit-start')), Func(av.setAnimState, 'Sit', 1.0))

        av.setPosHpr(chair[2], (0, 0, 0))
        av.reparentTo(self)

        if av == base.localAvatar:
            base.cr.playGame.getPlace().setState('walk')
            base.localAvatar.setPreventCameraDisable(True)
            base.cr.playGame.getPlace().setState('stopped')
            sequence.append(Func(self.setupGui))

        sequence.start()
        self.avId = avId
    
    def setStatus(self, status):
        av = base.cr.doId2do.get(self.avId)

        if not av:
            return
        
        if status == ToontownGlobals.CHAIR_UNEXPECTED_EXIT:
            self.resetAvatar(av)
        else:
            sitStartDuration = av.getDuration('sit-start')
            self.destroyGui()
            Sequence(Parallel(ActorInterval(av, 'sit-start', startTime=sitStartDuration, endTime=0.0), Sequence(Wait(sitStartDuration * 0.25), av.posInterval(sitStartDuration * 0.25, self.getChair()[2]))), Func(self.resetAvatar, av)).start()

    def resetAvatar(self, av):
        av.loop('neutral')
        av.setPos(av.getPos(render))
        av.getGeomNode().setHpr(0, 0, 0)
        av.setH(self.getH() + self.getChair()[1][0])
        av.reparentTo(render)
        
        if av == base.localAvatar:
            base.localAvatar.setPreventCameraDisable(False)
            base.cr.playGame.getPlace().setState('walk')
            self.destroyGui()
    
    def __enterSphere(self, collisionEntry):
        if self.avId in base.cr.doId2do:
            return
        
        base.cr.playGame.getPlace().setState('stopped')
        self.dialog = TTDialog.TTDialog(style=TTDialog.TwoChoice, text=TTLocalizer.ChairAskToUse, fadeScreen=1, command=self.__handleDialogResponse)
    
    def __handleDialogResponse(self, response):
        self.destroyGui()
        
        if response < 0:
            base.cr.playGame.getPlace().setState('walk')
            return
        
        self.sendUpdate('requestSit', [ToontownGlobals.CHAIR_START])
    
    def __handleFallingAsleep(self, arg):
        self.sendUpdate('requestSit', [ToontownGlobals.CHAIR_STOP])
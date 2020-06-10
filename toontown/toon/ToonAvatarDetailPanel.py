from panda3d.core import *
from toontown.toonbase.ToontownGlobals import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase import DirectObject
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
import DistributedToon
from toontown.friends import FriendInviter
import ToonTeleportPanel
from toontown.toonbase import TTLocalizer, ToontownGlobals
from toontown.hood import ZoneUtil
from toontown.toonbase.ToontownBattleGlobals import Tracks, Levels, getAvPropDamage
import Toon, NPCFriendPanel
globalAvatarDetail = None

def showAvatarDetail(avId, avName):
    global globalAvatarDetail
    if globalAvatarDetail != None:
        globalAvatarDetail.cleanup()
        globalAvatarDetail = None
    globalAvatarDetail = ToonAvatarDetailPanel(avId, avName)


def hideAvatarDetail():
    global globalAvatarDetail
    if globalAvatarDetail != None:
        globalAvatarDetail.cleanup()
        globalAvatarDetail = None
    return


def unloadAvatarDetail():
    global globalAvatarDetail
    if globalAvatarDetail != None:
        globalAvatarDetail.cleanup()
        globalAvatarDetail = None
    return


class ToonAvatarDetailPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonAvatarDetailPanel')

    def __init__(self, avId, avName, parent = base.a2dTopRight, **kw):
        buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        gui = loader.loadModel('phase_3.5/models/gui/avatar_panel_gui')
        sosGui = loader.loadModel('phase_3.5/models/gui/playingCard')
        detailPanel = gui.find('**/avatarInfoPanel')
        textScale = 0.095
        textWrap = 16.4
        optiondefs = (('pos', (-0.79, 0.0, -0.47), None),
         ('scale', 0.5, None),
         ('relief', None, None),
         ('image', detailPanel, None),
         ('image_color', GlobalDialogColor, None),
         ('text', '', None),
         ('text_wordwrap', textWrap, None),
         ('text_scale', textScale, None),
         ('text_pos', (-0.125, 0.775), None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.dataText = DirectLabel(self, text='', text_scale=0.09, text_align=TextNode.ALeft, text_wordwrap=15, relief=None, pos=(-0.85, 0.0, 0.645))
        self.avId = avId
        self.avName = avName
        self.avatar = None
        self.createdAvatar = None
        self.fsm = ClassicFSM.ClassicFSM('ToonAvatarDetailPanel', [State.State('off', self.enterOff, self.exitOff, ['begin']),
         State.State('begin', self.enterBegin, self.exitBegin, ['query', 'data', 'off']),
         State.State('query', self.enterQuery, self.exitQuery, ['data', 'invalid', 'off']),
         State.State('data', self.enterData, self.exitData, ['off']),
         State.State('invalid', self.enterInvalid, self.exitInvalid, ['off'])], 'off', 'off')
        ToonTeleportPanel.hideTeleportPanel()
        FriendInviter.hideFriendInviter()
        self.bCancel = DirectButton(self, image=(buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), image_scale=1.1, relief=None, text=TTLocalizer.AvatarDetailPanelCancel, text_scale=TTLocalizer.TADPbCancel, text_pos=(0.12, -0.01), pos=TTLocalizer.TADPbCancelPos, scale=2.0, command=self.__handleCancel)
        self.bCancel.hide()
        self.sosButton = DirectButton(self, relief=None, image=sosGui.find('**/card_back'), scale=0.05, pos=(0.3, 0, -0.76), text=('', TTLocalizer.DetailPanelSOS, TTLocalizer.DetailPanelSOS, ''), text_fg=(1, 1, 0.5, 1), text_shadow=(0, 0, 0, 1), text_scale=2, text_pos=(0, -3.4), text_align=TextNode.ACenter, state=DGG.NORMAL, command=self.__toggleSOSGui)
        self.sosButton.hide()
        self.sosFrame = DirectFrame(self, relief=None, image=DGG.getDefaultDialogGeom(), image_scale=(2.6, 1, 1.87), image_color=ToontownGlobals.GlobalDialogColor, pos=(0.2, 0, 0.8))
        self.sosFrame.setBin('background', 10)
        self.sosFrame.setScale(0.5)
        self.sosPage = NPCFriendPanel.NPCFriendPanel(parent=self.sosFrame, callable=False)
        self.sosPage.setScale(0.18)
        self.sosPage.setPos(0, 0, 0.05)
        self.initialiseoptions(ToonAvatarDetailPanel)
        self.fsm.enterInitialState()
        self.fsm.request('begin')
        buttons.removeNode()
        gui.removeNode()
        sosGui.removeNode()

    def cleanup(self):
        if self.fsm:
            self.fsm.request('off')
            self.fsm = None
            base.cr.cancelAvatarDetailsRequest(self.avatar)
        if self.createdAvatar:
            self.avatar.delete()
            self.createdAvatar = None
        self.destroy()

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterBegin(self):
        myId = base.localAvatar.doId
        self['text'] = self.avName
        if self.avId == myId:
            self.avatar = base.localAvatar
            self.createdAvatar = 0
            self.fsm.request('data')
        else:
            self.fsm.request('query')

    def exitBegin(self):
        pass

    def enterQuery(self):
        self.dataText['text'] = TTLocalizer.AvatarDetailPanelLookup % self.avName
        self.sosButton.hide()
        self.bCancel.show()
        self.avatar = base.cr.doId2do.get(self.avId)
        if self.avatar != None and not self.avatar.ghostMode:
            self.createdAvatar = 0
        else:
            self.avatar = DistributedToon.DistributedToon(base.cr)
            self.createdAvatar = 1
            self.avatar.doId = self.avId
            self.avatar.forceAllowDelayDelete()
        base.cr.getAvatarDetails(self.avatar, self.__handleAvatarDetails, 'DistributedToon')
        return

    def exitQuery(self):
        self.bCancel.hide()

    def enterData(self):
        self.bCancel['text'] = TTLocalizer.AvatarDetailPanelClose
        self.bCancel.show()
        self.__showData()

    def exitData(self):
        self.bCancel.hide()

    def enterInvalid(self):
        self.dataText['text'] = TTLocalizer.AvatarDetailPanelFailedLookup % self.avName

    def exitInvalid(self):
        self.bCancel.hide()

    def __handleCancel(self):
        unloadAvatarDetail()

    def __handleAvatarDetails(self, gotData, avatar, dclass):
        if not self.fsm or avatar != self.avatar:
            self.notify.warning('Ignoring unexpected request for avatar %s' % avatar.doId)
            return
        if gotData:
            self.fsm.request('data')
        else:
            self.fsm.request('invalid')

    def __showData(self):
        av = self.avatar
        online = 1
        if base.cr.isFriend(self.avId):
            online = base.cr.isFriendOnline(self.avId)
        identifier = int(str(self.avId)[1:])

        if online:
            shardName = base.cr.getShardName(av.defaultShard)
            hoodName = base.cr.hoodMgr.getFullnameFromId(av.lastHood)
            text = TTLocalizer.AvatarDetailPanelOnline % {'district': shardName, 'location': hoodName, 'identifier': identifier}
        else:
            text = TTLocalizer.AvatarDetailPanelOffline % {'identifier': identifier}
        self.dataText['text'] = text
        self.sosButton.show()
        self.__addToonModel()
        self.__updateTrackInfo()
        self.__updateTrophyInfo()
        self.__updateLaffInfo()
        self.__updateSOSPage()

    def __addToonModel(self):
        toon = Toon.Toon()
        toon.setDNA(self.avatar.style)
        toon.reparentTo(self)
        toon.setPos(0.45, 0, 0.3)
        toon.setH(180)
        toon.setScale(0.11)
        toon.loop('neutral')
        toon.setDepthWrite(True)
        toon.setDepthTest(True)
    
    def __updateLaffInfo(self):
        avatar = self.avatar
        messenger.send('updateLaffMeter', [avatar, avatar.hp, avatar.maxHp])

    def __updateTrackInfo(self):
        xOffset = -0.501814
        xSpacing = 0.1835
        yOffset = 0.1
        ySpacing = -0.115
        inventory = self.avatar.inventory
        self.inventoryFrame = DirectFrame(parent=self, relief=None)
        inventoryModels = loader.loadModel('phase_3.5/models/gui/inventory_gui')
        rolloverFrame = DirectFrame(parent=self.inventoryFrame, relief=None, geom=DGG.getDefaultDialogGeom(), geom_color=(0, 0.5, 1, 1), geom_scale=(0.5, 0.3, 0.2), text_scale=0.05, text_pos=(0, 0.0125), text='', text_fg=(1, 1, 1, 1))
        rolloverFrame.setBin('gui-popup', 0)
        rolloverFrame.hide()
        buttonModel = inventoryModels.find('**/InventoryButtonUp')
        for track in xrange(0, len(Tracks)):
            DirectLabel(parent=self.inventoryFrame, relief=None, text=TextEncoder.upper(TTLocalizer.BattleGlobalTracks[track]), text_scale=TTLocalizer.TADPtrackLabel, text_align=TextNode.ALeft, pos=(-0.9, 0, TTLocalizer.TADtrackLabelPosZ + track * ySpacing))
            if self.avatar.hasTrackAccess(track):
                curExp, nextExp = inventory.getCurAndNextExpValues(track)
                for item in xrange(0, len(Levels[track])):
                    level = Levels[track][item]
                    if curExp >= level:
                        numItems = inventory.numItem(track, item)
                        organic = self.avatar.checkGagBonus(track, item)
                        if numItems == 0:
                            image_color = Vec4(0.5, 0.5, 0.5, 1)
                            geom_color = Vec4(0.2, 0.2, 0.2, 0.5)
                        elif organic:
                            image_color = Vec4(0, 0.8, 0.4, 1)
                            geom_color = None
                        else:
                            image_color = Vec4(0, 0.6, 1, 1)
                            geom_color = None
                        pos = (xOffset + item * xSpacing, 0, yOffset + track * ySpacing)
                        label = DirectLabel(parent=self.inventoryFrame, image=buttonModel, image_scale=(0.92, 1, 1), image_color=image_color, geom=inventory.invModels[track][item], geom_color=geom_color, geom_scale=0.6, relief=None, pos=pos, state=DGG.NORMAL)
                        label.bind(DGG.ENTER, self.showInfo, extraArgs=[rolloverFrame, track, int(getAvPropDamage(track, item, curExp, organic)), numItems, (pos[0] + 0.37, pos[1], pos[2])])
                        label.bind(DGG.EXIT, self.hideInfo, extraArgs=[rolloverFrame])
                    else:
                        break
    
    def showInfo(self, frame, track, damage, numItems, pos, extra):
        frame.setPos(*pos)
        frame.show()
        frame['text'] = TTLocalizer.GagPopup % (self.avatar.inventory.getToonupDmgStr(track, 0), damage, numItems)

    def hideInfo(self, frame, extra):
        frame.hide()

    def __updateTrophyInfo(self):
        if self.createdAvatar:
            return
        if self.avatar.trophyScore >= TrophyStarLevels[2]:
            color = TrophyStarColors[2]
        elif self.avatar.trophyScore >= TrophyStarLevels[1]:
            color = TrophyStarColors[1]
        elif self.avatar.trophyScore >= TrophyStarLevels[0]:
            color = TrophyStarColors[0]
        else:
            color = None
        if color:
            gui = loader.loadModel('phase_3.5/models/gui/avatar_panel_gui')
            star = gui.find('**/avatarStar')
            self.star = DirectLabel(parent=self, image=star, image_color=color, pos=(0.610165, 0, -0.760678), scale=0.9, relief=None)
            gui.removeNode()
    
    def __updateSOSPage(self):
        self.sosPage.setFriends(self.avatar.NPCFriendsDict)
        self.sosPage.update()
    
    def __toggleSOSGui(self):
        self.sosButton['state'] = DGG.DISABLED

        if self.sosFrame.getScale() == 0.5:
            pos = (-0.4, 0, -1.88)
            scale = 1.0
        else:
            pos = (0, 0, 0.05)
            scale = 0.5
            self.sosFrame.setBin('background', 10)
        
        Sequence(
            Parallel(
                self.sosFrame.posInterval(1.0, pos, blendType='easeOut'),
                self.sosFrame.scaleInterval(1.0, scale, blendType='easeOut')
            ),
            Func(self.__enableSOSButton)
        ).start()
    
    def __enableSOSButton(self):
        try:
            self.sosButton['state'] = DGG.NORMAL

            if self.sosFrame.getScale() == 1.0:
                self.sosFrame.clearBin()
        except:
            pass
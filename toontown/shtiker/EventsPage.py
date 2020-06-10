import urllib
from pandac.PandaModules import Vec4, Vec3, TextNode
from direct.task.Task import Task
from direct.gui.DirectGui import DirectFrame, DirectLabel, DirectButton, DirectScrolledList, DirectCheckButton
from direct.gui import DirectGuiGlobals
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPLocalizer
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.toontowngui import TTDialog
from toontown.parties import PartyGlobals
from toontown.parties import PartyUtils
from toontown.parties.CalendarGuiMonth import CalendarGuiMonth
from toontown.parties.PartyUtils import getPartyActivityIcon
from toontown.parties.Party import Party
from toontown.parties.ServerTimeGui import ServerTimeGui
import ShtikerPage
EventsPage_Host = 0
EventsPage_Invited = 1
EventsPage_Calendar = 2

class EventsPage(ShtikerPage.ShtikerPage):
    notify = DirectNotifyGlobal.directNotify.newCategory('EventsPage')

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.mode = EventsPage_Calendar
        self.setMode(self.mode)
        self.noTeleport = config.GetBool('Parties-page-disable', 0)
        self.isPrivate = True
        self.hostedPartyInfo = None
        return

    def load(self):
        self.scrollButtonGui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        self.hostingGui = loader.loadModel('phase_4/models/parties/schtickerbookHostingGUI')
        self.invitationGui = loader.loadModel('phase_4/models/parties/schtickerbookInvitationGUI')
        self.activityIconsModel = loader.loadModel('phase_4/models/parties/eventSignIcons')
        self.decorationModels = loader.loadModel('phase_4/models/parties/partyDecorations')
        self.loadTabs()
        self.loadHostingTab()
        self.loadInvitationsTab()
        self.loadCalendarTab()
        self.titleLabel = DirectLabel(parent=self, relief=None, text=TTLocalizer.EventsPageHostTabTitle, text_scale=TTLocalizer.EPtitleLabel, textMayChange=True, pos=self.hostingGui.find('**/myNextParty_text_locator').getPos())
        return

    def loadTabs(self):
        normalColor = (1.0, 1.0, 1.0, 1.0)
        clickColor = (0.8, 0.8, 0.0, 1.0)
        rolloverColor = (0.15, 0.82, 1.0, 1.0)
        diabledColor = (1.0, 0.98, 0.15, 1.0)
        gui = loader.loadModel('phase_3.5/models/gui/fishingBook')
        self.hostTab = DirectButton(parent=self, relief=None, text=TTLocalizer.EventsPageHostTabName, text_scale=TTLocalizer.EPhostTab, text_align=TextNode.ACenter, text_pos=(0.12, 0.0), image=gui.find('**/tabs/polySurface1'), image_pos=(0.55, 1, -0.91), image_hpr=(0, 0, -90), image_scale=(0.033, 0.033, 0.035), image_color=normalColor, image1_color=clickColor, image2_color=rolloverColor, image3_color=diabledColor, text_fg=Vec4(0.2, 0.1, 0, 1), command=self.setMode, extraArgs=[EventsPage_Host], pos=(-0.13, 0, 0.775))
        self.invitedTab = DirectButton(parent=self, relief=None, text=TTLocalizer.EventsPageInvitedTabName, text_scale=TTLocalizer.EPinvitedTab, text_pos=(0.12, 0.0), text_align=TextNode.ACenter, image=gui.find('**/tabs/polySurface2'), image_pos=(0.12, 1, -0.91), image_hpr=(0, 0, -90), image_scale=(0.033, 0.033, 0.035), image_color=normalColor, image1_color=clickColor, image2_color=rolloverColor, image3_color=diabledColor, text_fg=Vec4(0.2, 0.1, 0, 1), command=self.setMode, extraArgs=[EventsPage_Invited], pos=(0.28, 0, 0.775))
        self.calendarTab = DirectButton(parent=self, relief=None, text=TTLocalizer.EventsPageCalendarTabName, text_scale=TTLocalizer.EPcalendarTab, text_pos=(0.12, 0.0), text_align=TextNode.ACenter, image=gui.find('**/tabs/polySurface2'), image_pos=(0.12, 1, -0.91), image_hpr=(0, 0, -90), image_scale=(0.033, 0.033, 0.035), image_color=normalColor, image1_color=clickColor, image2_color=rolloverColor, image3_color=diabledColor, text_fg=Vec4(0.2, 0.1, 0, 1), command=self.setMode, extraArgs=[EventsPage_Calendar], pos=(-0.55, 0, 0.775))
        return

    def loadHostingTab(self):
        self.hostedPartyDisplay = self.attachNewNode('Hosting')
        self.hostedPartyDisplay.setPos(0.0, 0.0, 0.04)
        self.hostingBackgroundFlat = DirectFrame(parent=self.hostedPartyDisplay, relief=None, geom=self.hostingGui.find('**/background_flat'))
        self.hostingGuestList, self.hostingGuestLabel = self.createListAndLabel(self.hostedPartyDisplay, self.hostingGui, 'guests', 7)
        self.hostingActivityList, self.hostingActivityLabel = self.createListAndLabel(self.hostedPartyDisplay, self.hostingGui, 'activities', 1)
        self.hostingDecorationList, self.hostingDecorationLabel = self.createListAndLabel(self.hostedPartyDisplay, self.hostingGui, 'decorations', 1)
        self.hostingDateLabel = DirectLabel(parent=self.hostedPartyDisplay, relief=None, text='', scale=TTLocalizer.EPhostingDateLabel, text_align=TextNode.ACenter, text_wordwrap=10, textMayChange=True, pos=self.hostingGui.find('**/date_locator').getPos())
        pos = self.hostingGui.find('**/cancel_text_locator').getPos()
        self.hostingCancelButton = DirectButton(parent=self.hostedPartyDisplay, relief=None, geom=(self.hostingGui.find('**/cancelPartyButton_up'),
         self.hostingGui.find('**/cancelPartyButton_down'),
         self.hostingGui.find('**/cancelPartyButton_rollover'),
         self.hostingGui.find('**/cancelPartyButton_inactive')), text=TTLocalizer.EventsPageHostTabCancelButton, text_scale=TTLocalizer.EPhostingCancelButton, text_pos=(pos[0], pos[2]), command=self.__doCancelParty)
        pos = self.hostingGui.find('**/startParty_text_locator').getPos()
        self.partyGoButton = DirectButton(parent=self.hostedPartyDisplay, relief=None, geom=(self.hostingGui.find('**/startPartyButton_up'),
         self.hostingGui.find('**/startPartyButton_down'),
         self.hostingGui.find('**/startPartyButton_rollover'),
         self.hostingGui.find('**/startPartyButton_inactive')), text=TTLocalizer.EventsPageGoButton, text_scale=TTLocalizer.EPpartyGoButton, text_pos=(pos[0], pos[2]), textMayChange=True, command=self._startParty)
        self.publicPrivateLabel = DirectLabel(parent=self.hostedPartyDisplay, relief=None, text=TTLocalizer.EventsPageHostTabPublicPrivateLabel, text_scale=TTLocalizer.EPpublicPrivateLabel, text_align=TextNode.ACenter, pos=self.hostingGui.find('**/thisPartyIs_text_locator').getPos())
        pos = self.hostingGui.find('**/public_text_locator').getPos()
        checkedImage = self.hostingGui.find('**/checked_button')
        uncheckedImage = self.hostingGui.find('**/unchecked_button')
        self.publicButton = DirectCheckButton(parent=self.hostedPartyDisplay, relief=None, scale=0.1, boxBorder=0.08, boxImage=(uncheckedImage, checkedImage, None), boxImageScale=10, boxRelief=None, text=TTLocalizer.EventsPageHostTabToggleToPublic, text_align=TextNode.ALeft, text_scale=TTLocalizer.EPpublicButton, pos=pos, command=self.__changePublicPrivate, indicator_pos=(-0.7, 0, 0.2))
        pos = self.hostingGui.find('**/private_text_locator').getPos()
        self.privateButton = DirectCheckButton(parent=self.hostedPartyDisplay, relief=None, scale=0.1, boxBorder=0.08, boxImage=(uncheckedImage, checkedImage, None), boxImageScale=10, boxRelief=None, text=TTLocalizer.EventsPageHostTabToggleToPrivate, text_align=TextNode.ALeft, text_scale=TTLocalizer.EPprivateButton, pos=pos, command=self.__changePublicPrivate, indicator_pos=(-0.7, 0, 0.2))
        self.confirmCancelPartyEvent = 'confirmCancelPartyEvent'
        self.accept(self.confirmCancelPartyEvent, self.confirmCancelOfParty)
        self.confirmCancelPartyGui = TTDialog.TTGlobalDialog(dialogName=self.uniqueName('confirmCancelPartyGui'), doneEvent=self.confirmCancelPartyEvent, message=TTLocalizer.EventsPageConfirmCancel % int(PartyGlobals.PartyRefundPercentage * 100.0), style=TTDialog.YesNo, okButtonText=OTPLocalizer.DialogYes, cancelButtonText=OTPLocalizer.DialogNo)
        self.confirmCancelPartyGui.doneStatus = ''
        self.confirmCancelPartyGui.hide()
        self.confirmTooLatePartyEvent = 'confirmTooLatePartyEvent'
        self.accept(self.confirmTooLatePartyEvent, self.confirmTooLateParty)
        self.confirmTooLatePartyGui = TTDialog.TTGlobalDialog(dialogName=self.uniqueName('confirmTooLatePartyGui'), doneEvent=self.confirmTooLatePartyEvent, message=TTLocalizer.EventsPageTooLateToStart, style=TTDialog.Acknowledge)
        self.confirmTooLatePartyGui.hide()
        self.confirmPublicPrivateChangeEvent = 'confirmPublicPrivateChangeEvent'
        self.accept(self.confirmPublicPrivateChangeEvent, self.confirmPublicPrivateChange)
        self.confirmPublicPrivateGui = TTDialog.TTGlobalDialog(dialogName=self.uniqueName('confirmPublicPrivateGui'), doneEvent=self.confirmPublicPrivateChangeEvent, message=TTLocalizer.EventsPagePublicPrivateNoGo, style=TTDialog.Acknowledge)
        self.confirmPublicPrivateGui.hide()
        self.cancelPartyResultGuiEvent = 'cancelPartyResultGuiEvent'
        self.accept(self.cancelPartyResultGuiEvent, self.cancelPartyResultGuiCommand)
        self.cancelPartyResultGui = TTDialog.TTGlobalDialog(dialogName=self.uniqueName('cancelPartyResultGui'), doneEvent=self.cancelPartyResultGuiEvent, message=TTLocalizer.EventsPageCancelPartyResultOk % 0, style=TTDialog.Acknowledge)
        self.cancelPartyResultGui.doneStatus = ''
        self.cancelPartyResultGui.hide()
        self.__setPublicPrivateButton()
        return

    def loadInvitationsTab(self):
        self.invitationDisplay = self.attachNewNode('invitations')
        self.invitationDisplay.setPos(0.0, 0.0, 0.04)
        self.invitationBackgroundFlat = DirectFrame(parent=self.invitationDisplay, relief=None, geom=self.invitationGui.find('**/background_flat'))
        self.invitationPartiesFlat = DirectFrame(parent=self.invitationDisplay, relief=None, geom=self.invitationGui.find('**/parties_background'))
        self.invitationActivtiesFlat = DirectFrame(parent=self.invitationDisplay, relief=None, geom=self.invitationGui.find('**/activities_background'))
        self.invitationPartyList, self.invitationPartyLabel = self.createListAndLabel(self.invitationDisplay, self.invitationGui, 'parties', 7, 'ButtonDown', 'ButtonUp', 'Text_locator')
        self.invitationActivityList, self.invitationActivityLabel = self.createListAndLabel(self.invitationDisplay, self.invitationGui, 'activities', 1, 'ButtonDown', 'ButtonUp', 'Text_locator')
        pos = self.invitationGui.find('**/startText_locator').getPos()
        self.invitePartyGoButton = DirectButton(parent=self.invitationDisplay, relief=None, geom=(self.invitationGui.find('**/startButton_up'),
         self.invitationGui.find('**/startButton_down'),
         self.invitationGui.find('**/startButton_rollover'),
         self.invitationGui.find('**/startButton_inactive')), text=TTLocalizer.EventsPageInviteGoButton, text_scale=TTLocalizer.EPinvitePartyGoButton, text_pos=(pos[0], pos[2]), textMayChange=True, command=self._inviteStartParty)
        self.invitationDateTimeLabel = DirectLabel(parent=self.invitationDisplay, relief=None, text='', textMayChange=True, text_scale=0.07, pos=(0, 0, -0.65))
        return

    def loadCalendarTab(self):
        self.calendarDisplay = self.attachNewNode('calendar')
        self.toontownTimeLabel = DirectLabel(parent=self.calendarDisplay, pos=(0.175, 0, -0.69), text_align=TextNode.ARight, relief=None, text=TTLocalizer.EventsPageToontownTimeIs, text_scale=0.065, text_font=ToontownGlobals.getMinnieFont(), text_fg=(255 / 255.0,
         146 / 255.0,
         113 / 255.0,
         1), textMayChange=0)
        self.calendarGuiMonth = None # To be set upon tab's first opening.
        pos = (0.35, 0, -0.69)
        self.toontownTimeGui = ServerTimeGui(self.calendarDisplay, pos)
        return

    def getGuestItem(self, name, inviteStatus):
        label = DirectLabel(relief=None, text=name, text_scale=0.045, text_align=TextNode.ALeft, textMayChange=True)
        dot = DirectFrame(relief=None, geom=self.hostingGui.find('**/questionMark'), pos=(0.5, 0.0, 0.01))
        if inviteStatus == PartyGlobals.InviteStatus.Accepted:
            dot['geom'] = (self.hostingGui.find('**/checkmark'),)
        elif inviteStatus == PartyGlobals.InviteStatus.Rejected:
            dot['geom'] = (self.hostingGui.find('**/x'),)
        PartyUtils.truncateTextOfLabelBasedOnWidth(label, name, PartyGlobals.EventsPageGuestNameMaxWidth)
        dot.reparentTo(label)
        return label

    def getActivityItem(self, activityBase, count = 1):
        activityName = TTLocalizer.PartyActivityNameDict[activityBase.activityId]['generic']
        if count == 1:
            textForActivity = activityName
        else:
            textForActivity = '%s x %d' % (activityName, count)
        iconString = PartyGlobals.ActivityIds.getString(activityBase.activityId)
        geom = getPartyActivityIcon(self.activityIconsModel, iconString)
        label = DirectLabel(relief=None, geom=geom, geom_scale=0.38, geom_pos=Vec3(0.0, 0.0, -0.17), text=textForActivity, text_scale=TTLocalizer.EPactivityItemLabel, text_align=TextNode.ACenter, text_pos=(-0.01, -0.43), text_wordwrap=7.0)
        return label

    def getDecorationItem(self, decorBase, count = 1):
        decorationName = TTLocalizer.PartyDecorationNameDict[decorBase.decorId]['editor']
        if count == 1:
            textForDecoration = decorationName
        else:
            textForDecoration = decorationName + ' x ' + str(count)
        assetName = PartyGlobals.DecorationIds.getString(decorBase.decorId)
        label = DirectLabel(relief=None, geom=self.decorationModels.find('**/partyDecoration_%s' % assetName), text=textForDecoration, text_scale=TTLocalizer.EPdecorationItemLabel, text_align=TextNode.ACenter, text_pos=(-0.01, -0.43), text_wordwrap=7.0)
        label['geom_scale'] = (2.6, 0.01, 0.05)
        label['geom_pos'] = (0.0, 0.0, -0.33)
        return label

    def getToonNameFromAvId(self, avId):
        result = TTLocalizer.EventsPageUnknownToon
        sender = base.cr.identifyAvatar(avId)
        if sender:
            result = sender.getName()
        return result

    def loadInvitations(self):
        EventsPage.notify.debug('loadInvitations')
        self.selectedInvitationItem = None
        self.invitationPartyList.removeAndDestroyAllItems()
        self.invitationActivityList.removeAndDestroyAllItems()
        self.invitePartyGoButton['state'] = DirectGuiGlobals.DISABLED
        for partyInfo in base.localAvatar.partiesInvitedTo:
            if partyInfo.status == PartyGlobals.PartyStatus.Cancelled or partyInfo.status == PartyGlobals.PartyStatus.Finished:
                continue
            inviteInfo = None
            for inviteInfo in base.localAvatar.invites:
                if partyInfo.partyId == inviteInfo.partyId:
                    break

            if inviteInfo is None:
                EventsPage.notify.error('No invitation info for party id %d' % partyInfo.partyId)
                return
            if inviteInfo.status == PartyGlobals.InviteStatus.NotRead:
                continue
            hostName = self.getToonNameFromAvId(partyInfo.hostId)
            item = DirectButton(relief=None, text=hostName, text_align=TextNode.ALeft, text_bg=Vec4(0.0, 0.0, 0.0, 0.0), text_scale=0.045, textMayChange=True, command=self.invitePartyClicked)
            PartyUtils.truncateTextOfLabelBasedOnWidth(item, hostName, PartyGlobals.EventsPageHostNameMaxWidth)
            item['extraArgs'] = [item]
            item.setPythonTag('activityIds', partyInfo.getActivityIds())
            item.setPythonTag('partyStatus', partyInfo.status)
            item.setPythonTag('hostId', partyInfo.hostId)
            item.setPythonTag('startTime', partyInfo.startTime)
            self.invitationPartyList.addItem(item)

        return

    def invitePartyClicked(self, item):
        if item.getPythonTag('partyStatus') == PartyGlobals.PartyStatus.Started:
            self.invitePartyGoButton['state'] = DirectGuiGlobals.NORMAL
        else:
            self.invitePartyGoButton['state'] = DirectGuiGlobals.DISABLED
        if self.selectedInvitationItem is not None:
            self.selectedInvitationItem['state'] = DirectGuiGlobals.NORMAL
            self.selectedInvitationItem['text_bg'] = Vec4(0.0, 0.0, 0.0, 0.0)
        self.selectedInvitationItem = item
        self.selectedInvitationItem['state'] = DirectGuiGlobals.DISABLED
        self.selectedInvitationItem['text_bg'] = Vec4(1.0, 1.0, 0.0, 1.0)
        self.fillInviteActivityList(item.getPythonTag('activityIds'))
        startTime = item.getPythonTag('startTime')
        self.invitationDateTimeLabel['text'] = TTLocalizer.EventsPageInvitedTabTime % (PartyUtils.formatDate(startTime.year, startTime.month, startTime.day), PartyUtils.formatTime(startTime.hour, startTime.minute))
        return

    def fillInviteActivityList(self, activityIds):
        self.invitationActivityList.removeAndDestroyAllItems()
        countDict = {}
        for actId in activityIds:
            if actId not in countDict:
                countDict[actId] = 1
            else:
                countDict[actId] += 1

        for activityId in countDict:
            if countDict[activityId] == 1:
                textOfActivity = TTLocalizer.PartyActivityNameDict[activityId]['generic']
            else:
                textOfActivity = TTLocalizer.PartyActivityNameDict[activityId]['generic'] + ' x ' + str(countDict[activityId])
            geom = getPartyActivityIcon(self.activityIconsModel, PartyGlobals.ActivityIds.getString(activityId))
            item = DirectLabel(relief=None, text=textOfActivity, text_align=TextNode.ACenter, text_scale=0.05, text_pos=(0.0, -0.15), geom_scale=0.3, geom_pos=Vec3(0.0, 0.0, 0.07), geom=geom)
            self.invitationActivityList.addItem(item)

        return

    def _inviteStartParty(self):
        if self.selectedInvitationItem is None:
            self.invitePartyGoButton['state'] = DirectGuiGlobals.DISABLED
            return
        self.doneStatus = {'mode': 'startparty',
         'firstStart': False,
         'hostId': self.selectedInvitationItem.getPythonTag('hostId')}
        messenger.send(self.doneEvent)
        return

    def loadHostedPartyInfo(self):
        self.unloadGuests()
        self.unloadActivities()
        self.unloadDecorations()
        self.hostedPartyInfo = None
        self.confirmCancelPartyGui.doneStatus = ''
        self.confirmCancelPartyGui.hide()
        self.cancelPartyResultGui.doneStatus = ''
        self.cancelPartyResultGui.hide()
        if base.localAvatar.hostedParties is not None and len(base.localAvatar.hostedParties) > 0:
            for partyInfo in base.localAvatar.hostedParties:
                if partyInfo.status == PartyGlobals.PartyStatus.Pending or partyInfo.status == PartyGlobals.PartyStatus.CanStart or partyInfo.status == PartyGlobals.PartyStatus.NeverStarted or partyInfo.status == PartyGlobals.PartyStatus.Started:
                    self.hostedPartyInfo = partyInfo
                    self.loadGuests()
                    self.loadActivities()
                    self.loadDecorations()
                    self.hostingDateLabel['text'] = TTLocalizer.EventsPageHostTabDateTimeLabel % (PartyUtils.formatDate(partyInfo.startTime.year, partyInfo.startTime.month, partyInfo.startTime.day), PartyUtils.formatTime(partyInfo.startTime.hour, partyInfo.startTime.minute))
                    self.isPrivate = partyInfo.isPrivate
                    self.__setPublicPrivateButton()
                    if partyInfo.status == PartyGlobals.PartyStatus.CanStart:
                        self.partyGoButton['state'] = DirectGuiGlobals.NORMAL
                        self.partyGoButton['text'] = (TTLocalizer.EventsPageGoButton,)
                    elif partyInfo.status == PartyGlobals.PartyStatus.Started:
                        place = base.cr.playGame.getPlace()
                        if isinstance(place, Party):
                            if hasattr(base, 'distributedParty'):
                                if base.distributedParty.partyInfo.hostId == base.localAvatar.doId:
                                    self.partyGoButton['state'] = DirectGuiGlobals.DISABLED
                                else:
                                    self.partyGoButton['state'] = DirectGuiGlobals.NORMAL
                            else:
                                self.partyGoButton['state'] = DirectGuiGlobals.NORMAL
                                self.notify.warning('base.distributedParty is not defined when base.cr.playGame.getPlace is party. This should never happen.')
                        else:
                            self.partyGoButton['state'] = DirectGuiGlobals.NORMAL
                        self.partyGoButton['text'] = (TTLocalizer.EventsPageGoBackButton,)
                    else:
                        self.partyGoButton['text'] = (TTLocalizer.EventsPageGoButton,)
                        self.partyGoButton['state'] = DirectGuiGlobals.DISABLED
                    if partyInfo.status not in (PartyGlobals.PartyStatus.Pending, PartyGlobals.PartyStatus.CanStart):
                        self.hostingCancelButton['state'] = DirectGuiGlobals.DISABLED
                    else:
                        self.hostingCancelButton['state'] = DirectGuiGlobals.NORMAL
                    self.hostingDateLabel.show()
                    self.hostedPartyDisplay.show()
                    return

        self.hostingDateLabel['text'] = TTLocalizer.EventsPageHostingTabNoParty
        self.hostingCancelButton['state'] = DirectGuiGlobals.DISABLED
        self.partyGoButton['state'] = DirectGuiGlobals.DISABLED
        self.publicButton['state'] = DirectGuiGlobals.DISABLED
        self.privateButton['state'] = DirectGuiGlobals.DISABLED
        self.hostedPartyDisplay.show()
        return

    def checkCanStartHostedParty(self):
        result = True
        if self.hostedPartyInfo.endTime < base.cr.toontownTimeManager.getCurServerDateTime() and self.hostedPartyInfo.status == PartyGlobals.PartyStatus.CanStart:
            result = False
            self.confirmTooLatePartyGui.show()
        return result

    def confirmTooLateParty(self):
        if hasattr(self, 'confirmTooLatePartyGui'):
            self.confirmTooLatePartyGui.hide()

    def confirmPublicPrivateChange(self):
        if hasattr(self, 'confirmPublicPrivateGui'):
            self.confirmPublicPrivateGui.hide()

    def _startParty(self):
        if not self.checkCanStartHostedParty():
            return
        if self.hostedPartyInfo.status == PartyGlobals.PartyStatus.CanStart:
            firstStart = True
        else:
            firstStart = False
        self.doneStatus = {'mode': 'startparty',
         'firstStart': firstStart,
         'hostId': None}
        messenger.send(self.doneEvent)
        return

    def loadGuests(self):
        for partyReplyInfoBase in base.localAvatar.partyReplyInfoBases:
            if partyReplyInfoBase.partyId == self.hostedPartyInfo.partyId:
                for singleReply in partyReplyInfoBase.replies:
                    toonName = self.getToonNameFromAvId(singleReply.inviteeId)
                    self.hostingGuestList.addItem(self.getGuestItem(toonName, singleReply.status))

    def loadActivities(self):
        countDict = {}
        for activityBase in self.hostedPartyInfo.activityList:
            if activityBase.activityId not in countDict:
                countDict[activityBase.activityId] = 1
            else:
                countDict[activityBase.activityId] += 1

        idsUsed = []
        for activityBase in self.hostedPartyInfo.activityList:
            if activityBase.activityId not in idsUsed:
                idsUsed.append(activityBase.activityId)
                count = countDict[activityBase.activityId]
                self.hostingActivityList.addItem(self.getActivityItem(activityBase, count))

    def loadDecorations(self):
        countDict = {}
        for decorBase in self.hostedPartyInfo.decors:
            if decorBase.decorId not in countDict:
                countDict[decorBase.decorId] = 1
            else:
                countDict[decorBase.decorId] += 1

        idsUsed = []
        for decorBase in self.hostedPartyInfo.decors:
            if decorBase.decorId not in idsUsed:
                count = countDict[decorBase.decorId]
                self.hostingDecorationList.addItem(self.getDecorationItem(decorBase, count))
                idsUsed.append(decorBase.decorId)

    def unloadGuests(self):
        self.hostingGuestList.removeAndDestroyAllItems()

    def unloadActivities(self):
        self.hostingActivityList.removeAndDestroyAllItems()

    def unloadDecorations(self):
        self.hostingDecorationList.removeAndDestroyAllItems()

    def unload(self):
        self.scrollButtonGui.removeNode()
        self.hostingGui.removeNode()
        self.invitationGui.removeNode()
        self.activityIconsModel.removeNode()
        self.decorationModels.removeNode()
        del self.titleLabel
        self.hostingGuestList.removeAndDestroyAllItems()
        self.hostingGuestList.destroy()
        del self.hostingGuestList
        self.hostingActivityList.removeAndDestroyAllItems()
        self.hostingActivityList.destroy()
        del self.hostingActivityList
        self.hostingDecorationList.removeAndDestroyAllItems()
        self.hostingDecorationList.destroy()
        del self.hostingDecorationList
        self.invitationPartyList.removeAndDestroyAllItems()
        self.invitationPartyList.destroy()
        del self.invitationPartyList
        self.invitationActivityList.removeAndDestroyAllItems()
        self.invitationActivityList.destroy()
        del self.invitationActivityList
        self.confirmCancelPartyGui.cleanup()
        del self.confirmCancelPartyGui
        self.confirmTooLatePartyGui.cleanup()
        del self.confirmTooLatePartyGui
        self.confirmPublicPrivateGui.cleanup()
        del self.confirmPublicPrivateGui
        self.ignore('changePartyPrivateResponseReceived')
        taskMgr.remove('changePartyPrivateResponseReceivedTimeOut')
        self.cancelPartyResultGui.cleanup()
        del self.cancelPartyResultGui
        self.ignore(self.confirmCancelPartyEvent)
        self.ignore(self.cancelPartyResultGuiEvent)
        self.avatar = None
        self.hostingCancelButton.destroy()
        del self.hostingCancelButton
        self.partyGoButton.destroy()
        del self.partyGoButton
        self.publicButton.destroy()
        del self.publicButton
        self.privateButton.destroy()
        del self.privateButton
        self.invitePartyGoButton.destroy()
        del self.invitePartyGoButton
        self.hostTab.destroy()
        self.invitedTab.destroy()
        self.calendarTab.destroy()
        if self.calendarGuiMonth:
            self.calendarGuiMonth.destroy()
        self.toontownTimeGui.destroy()
        taskMgr.remove('EventsPageUpdateTask-doLater')
        ShtikerPage.ShtikerPage.unload(self)
        return

    def enter(self):
        self.updatePage()
        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        self.unloadGuests()
        self.unloadActivities()
        self.unloadDecorations()

    def __handleConfirm(self):
        self.ignore('confirmDone')
        self.confirm.cleanup()
        del self.confirm

    def createListAndLabel(self, parent, gui, typeString, itemsVisible, downString = 'DownArrow', upString = 'UpArrow', textString = '_text_locator'):
        list = DirectScrolledList(parent=parent, relief=None, incButton_image=(gui.find('**/%s%s_up' % (typeString, downString)),
         gui.find('**/%s%s_down' % (typeString, downString)),
         gui.find('**/%s%s_rollover' % (typeString, downString)),
         gui.find('**/%s%s_inactive' % (typeString, downString))), incButton_relief=None, decButton_image=(gui.find('**/%s%s_up' % (typeString, upString)),
         gui.find('**/%s%s_down' % (typeString, upString)),
         gui.find('**/%s%s_rollover' % (typeString, upString)),
         gui.find('**/%s%s_inactive' % (typeString, upString))), decButton_relief=None, itemFrame_pos=gui.find('**/%s_locator' % typeString).getPos(), itemFrame_relief=None, numItemsVisible=itemsVisible, forceHeight=0.07)
        strings = {'guests': TTLocalizer.EventsPageHostingTabGuestListTitle,
         'activities': TTLocalizer.EventsPageHostingTabActivityListTitle,
         'decorations': TTLocalizer.EventsPageHostingTabDecorationsListTitle,
         'parties': TTLocalizer.EventsPageHostingTabPartiesListTitle}
        label = DirectLabel(parent=parent, relief=None, text=strings[typeString], text_scale=TTLocalizer.EPcreateListAndLabel, pos=gui.find('**/%s%s' % (typeString, textString)).getPos())
        return (list, label)

    def setMode(self, mode, updateAnyways = 0):
        messenger.send('wakeup')
        if updateAnyways == False:
            if self.mode == mode:
                return
            else:
                self.mode = mode
        self.show()
        self.updatePage()

    def getMode(self):
        return self.mode

    def updatePage(self):
        if self.mode == EventsPage_Host:
            self.hostTab['state'] = DirectGuiGlobals.DISABLED
            self.invitedTab['state'] = DirectGuiGlobals.NORMAL
            self.calendarTab['state'] = DirectGuiGlobals.NORMAL
            self.invitationDisplay.hide()
            self.hostedPartyDisplay.show()
            self.calendarDisplay.hide()
            self.loadHostedPartyInfo()
            if self.hostedPartyInfo is None:
                self.titleLabel['text'] = TTLocalizer.EventsPageHostTabTitleNoParties
            else:
                self.titleLabel['text'] = TTLocalizer.EventsPageHostTabTitle
        elif self.mode == EventsPage_Invited:
            self.titleLabel['text'] = TTLocalizer.EventsPageInvitedTabTitle
            self.hostTab['state'] = DirectGuiGlobals.NORMAL
            self.invitedTab['state'] = DirectGuiGlobals.DISABLED
            self.calendarTab['state'] = DirectGuiGlobals.NORMAL
            self.hostedPartyDisplay.hide()
            self.invitationDisplay.show()
            self.calendarDisplay.hide()
            self.loadInvitations()
        elif self.mode == EventsPage_Calendar:
            self.titleLabel['text'] = ''
            self.hostTab['state'] = DirectGuiGlobals.NORMAL
            self.invitedTab['state'] = DirectGuiGlobals.NORMAL
            self.calendarTab['state'] = DirectGuiGlobals.DISABLED
            self.hostedPartyDisplay.hide()
            self.invitationDisplay.hide()
            self.calendarDisplay.show()
            if not self.calendarGuiMonth:
                curServerDate = base.cr.toontownTimeManager.getCurServerDateTime()
                self.calendarGuiMonth = CalendarGuiMonth(self.calendarDisplay, curServerDate, onlyFutureMonthsClickable=True)
            self.calendarGuiMonth.changeMonth(0)
        return

    def __setPublicPrivateButton(self):
        if self.isPrivate:
            self.privateButton['indicatorValue'] = True
            self.publicButton['indicatorValue'] = False
            self.privateButton['state'] = DirectGuiGlobals.DISABLED
            self.publicButton['state'] = DirectGuiGlobals.NORMAL
        else:
            self.privateButton['indicatorValue'] = False
            self.publicButton['indicatorValue'] = True
            self.privateButton['state'] = DirectGuiGlobals.NORMAL
            self.publicButton['state'] = DirectGuiGlobals.DISABLED

    def __changePublicPrivate(self, indicator):
        self.__setPublicPrivateButton()
        self.confirmPublicPrivateGui['text'] = TTLocalizer.EventsPagePublicPrivateChange
        self.confirmPublicPrivateGui.buttonList[0].hide()
        self.confirmPublicPrivateGui.show()
        base.cr.partyManager.sendChangePrivateRequest(self.hostedPartyInfo.partyId, not self.isPrivate)
        self.accept('changePartyPrivateResponseReceived', self.changePartyPrivateResponseReceived)
        taskMgr.doMethodLater(5.0, self.changePartyPrivateResponseReceived, 'changePartyPrivateResponseReceivedTimeOut', [0, 0, PartyGlobals.ChangePartyFieldErrorCode.DatabaseError])

    def changePartyPrivateResponseReceived(self, partyId, newPrivateStatus, errorCode):
        EventsPage.notify.debug('changePartyPrivateResponseReceived called with partyId = %d, newPrivateStatus = %d, errorCode = %d' % (partyId, newPrivateStatus, errorCode))
        taskMgr.remove('changePartyPrivateResponseReceivedTimeOut')
        self.ignore('changePartyPrivateResponseReceived')
        if errorCode == PartyGlobals.ChangePartyFieldErrorCode.AllOk:
            self.isPrivate = newPrivateStatus
            self.confirmPublicPrivateGui.hide()
        else:
            self.confirmPublicPrivateGui.buttonList[0].show()
            if errorCode == PartyGlobals.ChangePartyFieldErrorCode.AlreadyStarted:
                self.confirmPublicPrivateGui['text'] = TTLocalizer.EventsPagePublicPrivateAlreadyStarted
            else:
                self.confirmPublicPrivateGui['text'] = TTLocalizer.EventsPagePublicPrivateNoGo
        self.__setPublicPrivateButton()

    def __doCancelParty(self):
        if self.hostedPartyInfo:
            if self.hostedPartyInfo.status == PartyGlobals.PartyStatus.Pending or self.hostedPartyInfo.status == PartyGlobals.PartyStatus.CanStart or self.hostedPartyInfo.status == PartyGlobals.PartyStatus.NeverStarted:
                self.hostingCancelButton['state'] = DirectGuiGlobals.DISABLED
                self.confirmCancelPartyGui.show()

    def confirmCancelOfParty(self):
        self.confirmCancelPartyGui.hide()
        if self.confirmCancelPartyGui.doneStatus == 'ok':
            base.cr.partyManager.sendChangePartyStatusRequest(self.hostedPartyInfo.partyId, PartyGlobals.PartyStatus.Cancelled)
            self.accept('changePartyStatusResponseReceived', self.changePartyStatusResponseReceived)
        else:
            self.hostingCancelButton['state'] = DirectGuiGlobals.NORMAL

    def changePartyStatusResponseReceived(self, partyId, newPartyStatus, errorCode, beansRefunded):
        EventsPage.notify.debug('changePartyStatusResponseReceived called with partyId = %d, newPartyStatus = %d, errorCode = %d' % (partyId, newPartyStatus, errorCode))
        if errorCode == PartyGlobals.ChangePartyFieldErrorCode.AllOk:
            if newPartyStatus == PartyGlobals.PartyStatus.Cancelled:
                self.loadHostedPartyInfo()
                self.cancelPartyResultGui['text'] = TTLocalizer.EventsPageCancelPartyResultOk % beansRefunded
                self.cancelPartyResultGui.show()
        elif errorCode == PartyGlobals.ChangePartyFieldErrorCode.AlreadyRefunded and newPartyStatus == PartyGlobals.PartyStatus.NeverStarted:
            self.loadHostedPartyInfo()
            self.cancelPartyResultGui['text'] = TTLocalizer.EventsPageCancelPartyAlreadyRefunded
            self.cancelPartyResultGui.show()
        else:
            self.cancelPartyResultGui['text'] = TTLocalizer.EventsPageCancelPartyResultError
            self.cancelPartyResultGui.show()
            self.hostingCancelButton['state'] = DirectGuiGlobals.NORMAL

    def cancelPartyResultGuiCommand(self):
        self.cancelPartyResultGui.hide()

    def updateToontownTime(self):
        self.toontownTimeGui.updateTime()

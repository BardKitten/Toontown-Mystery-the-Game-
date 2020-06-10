from pandac.PandaModules import TextNode, PlaneNode, Plane
from direct.gui.DirectGui import DirectFrame, DirectLabel, DirectButton, DirectScrolledList, DGG
from direct.gui import DirectGuiGlobals
from toontown.ai import HolidayGlobals
from toontown.toonbase import TTLocalizer, ToontownGlobals
from toontown.parties.PartyInfo import PartyInfo
from toontown.parties import PartyGlobals
import datetime

def myStrftime(myTime):
    result = ''
    result = myTime.strftime('%I')
    if result[0] == '0':
        result = result[1:]
    result += myTime.strftime(':%M %p')
    return result

class CalendarGuiDay(DirectFrame):
    ScrollListTextSize = 0.03

    def __init__(self, parent, myDate, startDate, dayClickCallback = None, onlyFutureDaysClickable = False):
        self.origParent = parent
        self.startDate = startDate
        self.myDate = myDate
        self.dayClickCallback = dayClickCallback
        self.onlyFutureDaysClickable = onlyFutureDaysClickable
        DirectFrame.__init__(self, parent=parent)
        self.filter = ToontownGlobals.CalendarFilterShowAll
        self.load()
        self.createGuiObjects()
        self.update()

    def load(self):
        dayAsset = loader.loadModel('phase_4/models/parties/tt_m_gui_sbk_calendar_box')
        dayAsset.reparentTo(self)
        self.dayButtonLocator = self.find('**/loc_origin')
        self.numberLocator = self.find('**/loc_number')
        self.scrollLocator = self.find('**/loc_topLeftList')
        self.selectedLocator = self.find('**/loc_origin')
        self.todayBox = self.find('**/boxToday')
        self.todayBox.hide()
        self.selectedFrame = self.find('**/boxHover')
        self.selectedFrame.hide()
        self.defaultBox = self.find('**/boxBlank')
        self.scrollBottomRightLocator = self.find('**/loc_bottomRightList')
        self.scrollDownLocator = self.find('**/loc_scrollDown')
        self.scrollUpLocator = self.find('**/loc_scrollUp')

    def createGuiObjects(self):
        self.dayButton = DirectButton(parent=self.dayButtonLocator, image=self.selectedFrame, relief=None, command=self.__clickedOnDay, pressEffect=1, rolloverSound=None, clickSound=None)
        self.numberWidget = DirectLabel(parent=self.numberLocator, relief=None, text=str(self.myDate.day), text_scale=0.04, text_align=TextNode.ACenter, text_font=ToontownGlobals.getInterfaceFont(), text_fg=(110 / 255.0, 126 / 255.0, 255 / 255.0, 1))
        self.listXorigin = 0
        self.listFrameSizeX = self.scrollBottomRightLocator.getX() - self.scrollLocator.getX()
        self.scrollHeight = self.scrollLocator.getZ() - self.scrollBottomRightLocator.getZ()
        self.listZorigin = self.scrollBottomRightLocator.getZ()
        self.listFrameSizeZ = self.scrollLocator.getZ() - self.scrollBottomRightLocator.getZ()
        self.arrowButtonXScale = 1
        self.arrowButtonZScale = 1
        self.itemFrameXorigin = 0
        self.itemFrameZorigin = 0
        self.buttonXstart = self.itemFrameXorigin + 0.21
        self.gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        buttonOffSet = -0.01
        incButtonPos = (0.0, 0, 0)
        decButtonPos = (0.0, 0, 0)
        itemFrameMinZ = self.listZorigin
        itemFrameMaxZ = self.listZorigin + self.listFrameSizeZ
        arrowUp = self.find('**/downScroll_up')
        arrowDown = self.find('**/downScroll_down')
        arrowHover = self.find('**/downScroll_hover')
        self.scrollList = DirectScrolledList(parent=self.scrollLocator, relief=None, pos=(0, 0, 0), incButton_image=(arrowUp,
         arrowDown,
         arrowHover,
         arrowUp), incButton_relief=None, incButton_scale=(self.arrowButtonXScale, 1, self.arrowButtonZScale), incButton_pos=incButtonPos, incButton_image3_color=(1, 1, 1, 0.2), decButton_image=(arrowUp,
         arrowDown,
         arrowHover,
         arrowUp), decButton_relief=None, decButton_scale=(self.arrowButtonXScale, 1, -self.arrowButtonZScale), decButton_pos=decButtonPos, decButton_image3_color=(1, 1, 1, 0.2), itemFrame_pos=(self.itemFrameXorigin, 0, -0.03), numItemsVisible=4, incButtonCallback=self.scrollButtonPressed, decButtonCallback=self.scrollButtonPressed)
        itemFrameParent = self.scrollList.itemFrame.getParent()
        self.scrollList.incButton.reparentTo(self.scrollDownLocator)
        self.scrollList.decButton.reparentTo(self.scrollUpLocator)
        arrowUp.removeNode()
        arrowDown.removeNode()
        arrowHover.removeNode()
        clipper = PlaneNode('clipper')
        clipper.setPlane(Plane((-1, 0, 0), (0.23, 0, 0)))
        clipNP = self.scrollList.component('itemFrame').attachNewNode(clipper)
        self.scrollList.component('itemFrame').setClipPlane(clipNP)

    def scrollButtonPressed(self):
        self.__clickedOnDay()

    def adjustForMonth(self):
        curServerDate = base.cr.toontownTimeManager.getCurServerDateTime()
        if self.onlyFutureDaysClickable:
            if self.myDate.year < curServerDate.year or self.myDate.year == curServerDate.year and self.myDate.month < curServerDate.month or self.myDate.year == curServerDate.year and self.myDate.month == curServerDate.month and self.myDate.day < curServerDate.day:
                self.numberWidget.setColorScale(0.5, 0.5, 0.5, 0.5)
                self.numberWidget['state'] = DirectGuiGlobals.DISABLED
            else:
                self.numberWidget.setColorScale(1, 1, 1, 1)
        if self.myDate.month != self.startDate.month:
            self.setColorScale(0.75, 0.75, 0.75, 1.0)
            if self.dayClickCallback is not None:
                self.numberWidget['state'] = DirectGuiGlobals.DISABLED
        else:
            self.setColorScale(1, 1, 1, 1)
        if self.myDate.date() == curServerDate.date():
            self.defaultBox.hide()
            self.todayBox.show()
        else:
            self.defaultBox.show()
            self.todayBox.hide()

    def destroy(self):
        if self.dayClickCallback is not None:
            self.numberWidget.destroy()
        self.dayClickCallback = None
        try:
            for item in self.scrollList['items']:
                if hasattr(item, 'description') and item.description and hasattr(item.description, 'destroy'):
                    item.unbind(DGG.ENTER)
                    item.unbind(DGG.EXIT)
                    item.description.destroy()

        except e:
            pass

        self.scrollList.removeAndDestroyAllItems()
        self.scrollList.destroy()
        self.dayButton.destroy()
        DirectFrame.destroy(self)

    def updateArrowButtons(self):
        numItems = 0
        try:
            numItems = len(self.scrollList['items'])
        except e:
            numItems = 0

        if numItems <= self.scrollList.numItemsVisible:
            self.scrollList.incButton.hide()
            self.scrollList.decButton.hide()
        else:
            self.scrollList.incButton.show()
            self.scrollList.decButton.show()

    def collectTimedEvents(self):
        if self.filter == ToontownGlobals.CalendarFilterShowAll or self.filter == ToontownGlobals.CalendarFilterShowOnlyParties:
            for party in localAvatar.partiesInvitedTo:
                if party.startTime.date() == self.myDate.date():
                    self.addPartyToScrollList(party)

            for party in localAvatar.hostedParties:
                if party.startTime.date() == self.myDate.date():
                    self.addPartyToScrollList(party)

        if self.filter == ToontownGlobals.CalendarFilterShowAll or self.filter == ToontownGlobals.CalendarFilterShowOnlyHolidays:
            for id, holiday in HolidayGlobals.Holidays.iteritems():
                title, description = TTLocalizer.HolidayNamesInCalendar[id]

                if 'weekDay' in holiday:
                    if self.myDate.weekday() == holiday['weekDay']:
                        self.addTitleAndDescToScrollList(title, description)
                elif 'startMonth' in holiday or 'startDay' in holiday:
                    startDate = HolidayGlobals.getStartDate(holiday, self.myDate)
                    endDate = HolidayGlobals.getEndDate(holiday, self.myDate)

                    if self.isDateMatch(self.myDate, startDate):
                        if self.isDateMatch(startDate, endDate):
                            description = '%s. %s' % (title, description)
                        else:
                            description = '%s. %s %s %s' % (title, description, TTLocalizer.CalendarEndsAt, endDate.strftime('%b %d'))

                        self.addTitleAndDescToScrollList(title, description)
                    elif self.isDateMatch(self.myDate, endDate):
                        title = '%s %s' % (TTLocalizer.CalendarEndOf, title)
                        description = '%s. %s %s' % (title, TTLocalizer.CalendarStartedOn, startDate.strftime('%b %d'))

                        self.addTitleAndDescToScrollList(title, description)

    def isDateMatch(self, date1, date2):
        return date1.day == date2.day and date1.month == date2.month

    def addTitleAndDescToScrollList(self, title, desc):
        textSize = self.ScrollListTextSize
        descTextSize = 0.05
        newItem = DirectButton(relief=None, text=title, text_scale=textSize, text_align=TextNode.ALeft, rolloverSound=None, clickSound=None, pressEffect=0, command=self.__clickedOnScrollItem)
        scrollItemHeight = newItem.getHeight()
        descUnderItemZAdjust = scrollItemHeight * descTextSize / textSize
        descUnderItemZAdjust = max(0.0534, descUnderItemZAdjust)
        descUnderItemZAdjust = -descUnderItemZAdjust
        descZAdjust = descUnderItemZAdjust
        newItem.description = DirectLabel(parent=newItem, pos=(0.115, 0, descZAdjust), text='', text_wordwrap=15, pad=(0.02, 0.02), text_scale=descTextSize, text_align=TextNode.ACenter, textMayChange=0)
        newItem.description.checkedHeight = False
        newItem.description.setBin('gui-popup', 0)
        newItem.description.hide()
        newItem.bind(DGG.ENTER, self.enteredTextItem, extraArgs=[newItem, desc, descUnderItemZAdjust])
        newItem.bind(DGG.EXIT, self.exitedTextItem, extraArgs=[newItem])
        self.scrollList.addItem(newItem)

    def exitedTextItem(self, newItem, mousepos):
        newItem.description.hide()

    def enteredTextItem(self, newItem, descText, descUnderItemZAdjust, mousePos):
        if not newItem.description.checkedHeight:
            newItem.description.checkedHeight = True
            newItem.description['text'] = descText
            bounds = newItem.description.getBounds()
            descHeight = newItem.description.getHeight()
            scrollItemHeight = newItem.getHeight()
            descOverItemZAdjust = descHeight - scrollItemHeight / 2.0
            descZPos = self.getPos(aspect2d)[2] + descUnderItemZAdjust - descHeight
            if descZPos < -1.0:
                newItem.description.setZ(descOverItemZAdjust)
            descWidth = newItem.description.getWidth()
            brightFrame = loader.loadModel('phase_4/models/parties/tt_m_gui_sbk_calendar_popUp_bg')
            newItem.description['geom'] = brightFrame
            newItem.description['geom_scale'] = (descWidth, 1, descHeight)
            descGeomZ = (bounds[2] - bounds[3]) / 2.0
            descGeomZ += bounds[3]
            newItem.description['geom_pos'] = (0, 0, descGeomZ)
        newItem.description.show()

    def addPartyToScrollList(self, party):
        textSize = self.ScrollListTextSize
        descTextSize = 0.05
        partyTitle = myStrftime(party.startTime)
        partyTitle = partyTitle + ' ' + TTLocalizer.EventsPageCalendarTabParty
        textSize = self.ScrollListTextSize
        descTextSize = 0.05
        newItem = DirectButton(relief=None, text=partyTitle, text_scale=textSize, text_align=TextNode.ALeft, rolloverSound=None, clickSound=None, pressEffect=0, command=self.__clickedOnScrollItem)
        scrollItemHeight = newItem.getHeight()
        descUnderItemZAdjust = scrollItemHeight * descTextSize / textSize
        descUnderItemZAdjust = max(0.0534, descUnderItemZAdjust)
        descUnderItemZAdjust = -descUnderItemZAdjust
        descZAdjust = descUnderItemZAdjust
        self.scrollList.addItem(newItem)
        newItem.description = MiniInviteVisual(newItem, party)
        newItem.description.setBin('gui-popup', 0)
        newItem.description.hide()
        newItem.bind(DGG.ENTER, self.enteredTextItem, extraArgs=[newItem, newItem.description, descUnderItemZAdjust])
        newItem.bind(DGG.EXIT, self.exitedTextItem, extraArgs=[newItem])

    def __clickedOnScrollItem(self):
        self.__clickedOnDay()

    def __clickedOnDay(self):
        acceptClick = True
        if self.onlyFutureDaysClickable:
            curServerDate = base.cr.toontownTimeManager.getCurServerDateTime()
            if self.myDate.date() < curServerDate.date():
                acceptClick = False
        if not acceptClick:
            return
        if self.dayClickCallback:
            self.dayClickCallback(self)
        messenger.send('clickedOnDay', [self.myDate.date()])

    def updateSelected(self, selected):
        multiplier = 1.1
        if selected:
            self.selectedFrame.show()
            self.setScale(multiplier)
            self.setPos(-0.01, 0, 0.01)
            grandParent = self.origParent.getParent()
            self.origParent.reparentTo(grandParent)
        else:
            self.selectedFrame.hide()
            self.setScale(1.0)
            self.setPos(0, 0, 0)

    def changeDate(self, startDate, myDate):
        self.startDate = startDate
        self.myDate = myDate
        self.scrollList.removeAndDestroyAllItems()
        self.update()

    def update(self):
        self.numberWidget['text'] = str(self.myDate.day)
        self.adjustForMonth()
        self.collectTimedEvents()
        self.updateArrowButtons()

    def changeFilter(self, filter):
        oldFilter = self.filter
        self.filter = filter
        if self.filter != oldFilter:
            self.scrollList.removeAndDestroyAllItems()
            self.update()

class MiniInviteVisual(DirectFrame):

    def __init__(self, parent, partyInfo):
        DirectFrame.__init__(self, parent, pos=(0.1, 0, -0.018))
        self.checkedHeight = True
        self.partyInfo = partyInfo
        self.parent = parent
        self.inviteBackgrounds = loader.loadModel('phase_4/models/parties/partyStickerbook')
        backgrounds = ['calendar_popup_birthday',
         'calendar_popup_fun',
         'calendar_popup_cupcake',
         'tt_t_gui_sbk_calendar_popup_racing',
         'tt_t_gui_sbk_calendar_popup_valentine1',
         'tt_t_gui_sbk_calendar_popup_victoryParty',
         'tt_t_gui_sbk_calendar_popup_winter1']
        self.background = DirectFrame(parent=self, relief=None, geom=self.inviteBackgrounds.find('**/%s' % backgrounds[self.partyInfo.inviteTheme]), scale=(0.7, 1.0, 0.23), pos=(0.0, 0.0, -0.1))
        self.whosePartyLabel = DirectLabel(parent=self, relief=None, pos=(0.07, 0.0, -0.04), text=' ', text_scale=0.04, text_wordwrap=8, textMayChange=True)
        self.whenTextLabel = DirectLabel(parent=self, relief=None, text=' ', pos=(0.07, 0.0, -0.13), text_scale=0.04, textMayChange=True)
        self.partyStatusLabel = DirectLabel(parent=self, relief=None, text=' ', pos=(0.07, 0.0, -0.175), text_scale=0.04, textMayChange=True)

    def show(self):
        self.reparentTo(self.parent)
        self.setPos(0.1, 0, -0.018)
        newParent = self.parent.getParent().getParent()
        self.wrtReparentTo(newParent)
        if self.whosePartyLabel['text'] == ' ':
            host = base.cr.identifyAvatar(self.partyInfo.hostId)
            if host:
                name = host.getName()
                self.whosePartyLabel['text'] = name
        if self.whenTextLabel['text'] == ' ':
            time = myStrftime(self.partyInfo.startTime)
            self.whenTextLabel['text'] = time
        if self.partyStatusLabel['text'] == ' ':
            if self.partyInfo.status == PartyGlobals.PartyStatus.Cancelled:
                self.partyStatusLabel['text'] = TTLocalizer.CalendarPartyCancelled
            elif self.partyInfo.status == PartyGlobals.PartyStatus.Finished:
                self.partyStatusLabel['text'] = TTLocalizer.CalendarPartyFinished
            elif self.partyInfo.status == PartyGlobals.PartyStatus.Started:
                self.partyStatusLabel['text'] = TTLocalizer.CalendarPartyGo
            elif self.partyInfo.status == PartyGlobals.PartyStatus.NeverStarted:
                self.partyStatusLabel['text'] = TTLocalizer.CalendarPartyNeverStarted
            else:
                self.partyStatusLabel['text'] = TTLocalizer.CalendarPartyGetReady
        DirectFrame.show(self)

    def destroy(self):
        del self.checkedHeight
        del self.partyInfo
        del self.parent
        del self.background
        del self.whosePartyLabel
        del self.whenTextLabel
        del self.partyStatusLabel
        DirectFrame.destroy(self)

from direct.distributed.DistributedObject import DistributedObject
from otp.speedchat import SpeedChatGlobals
import HolidayGlobals, time

class DistributedEffectMgr(DistributedObject):

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.nextTime = 0

    def delete(self):
        self.ignoreAll()
        DistributedObject.delete(self)

    def setHoliday(self, holiday):
        self.holiday = holiday
        self.accept(SpeedChatGlobals.SCStaticTextMsgEvent, self.__saidPhrase)

    def __saidPhrase(self, phraseId):
        if not self.cr.newsManager.isHolidayRunning(self.holiday):
            return

        currentTime = time.time()

        if self.nextTime > currentTime:
            return

        holidayInfo = HolidayGlobals.getHoliday(self.holiday)

        if 'speedchatIndexes' not in holidayInfo or phraseId not in holidayInfo['speedchatIndexes']:
            return

        if 'effectDelay' in holidayInfo:
            self.nextTime = currentTime + holidayInfo['effectDelay']

        self.sendUpdate('requestEffect')

    def effectDone(self, amount):
        holidayInfo = HolidayGlobals.getHoliday(self.holiday)

        self.cr.newsManager.broadcastHoliday(holidayInfo, 'effectMessage')

        if 'scavengerHunt' in holidayInfo:
            type = holidayInfo['scavengerHunt']

            if type == HolidayGlobals.TRICK_OR_TREAT:
                base.localAvatar.trickOrTreatTargetMet(amount)
            elif type == HolidayGlobals.WINTER_CAROLING:
                base.localAvatar.winterCarolingTargetMet(amount)

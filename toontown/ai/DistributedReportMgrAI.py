from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.uberdog.ClientServicesManagerUD import executeHttpRequestAndLog
import ReportGlobals, threading, time

# TODO: FIX

'''
THREADING.TIMER CAUSES CONTROL C NOT TO WORK, AND FOR THE AI NOT TO DIE
'''

class DistributedReportMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedReportMgrAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.reports = []
        self.interval = config.GetInt('report-interval', 600)
        #self.scheduleReport()

    #def scheduleReport(self):
    #    threading.Timer(self.interval, self.sendAllReports).start()

    def sendReport(self, avId, category):
        if not ReportGlobals.isValidCategoryName(category) or not len(str(avId)) == 9:
            return

        reporter = self.air.doId2do.get(self.air.getAvatarIdFromSender())

        if not reporter or reporter.isReported(avId):
            return

        timestamp = int(round(time.time() * 1000))
        self.reports.append('%s|%s|%s|%s' % (timestamp, reporter.doId, avId, category))

    def sendAllReports(self):
        #self.scheduleReport()

        if not self.reports or config.GetString('accountdb-type', 'developer') != 'remote':
            return

        executeHttpRequestAndLog('report', reports=','.join(self.reports))
        self.reports = []

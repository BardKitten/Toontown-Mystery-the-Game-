from direct.directnotify import DirectNotifyGlobal
import FactoryInterior

class MegaCorpInterior(FactoryInterior.FactoryInterior):
    notify = DirectNotifyGlobal.directNotify.newCategory('FactoryInterior')

    def __init__(self, loader, parentFSM, doneEvent):
        FactoryInterior.FactoryInterior.__init__(self, loader, parentFSM, doneEvent)
        self.zoneId = ToontownGlobals.SellbotMegaCorpInt

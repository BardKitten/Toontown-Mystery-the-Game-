from direct.directnotify import DirectNotifyGlobal
import DistributedFactoryAI

class DistributedMegaCorpAI(DistributedFactoryAI.DistributedFactoryAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBrutalFactoryAI')

    def __init__(self, air, factoryId, zoneId, entranceId, avIds):
        DistributedFactoryAI.DistributedFactoryAI.__init__(self, air, factoryId, zoneId, entranceId, avIds)

from direct.directnotify.DirectNotifyGlobal import *
import cPickle

from otp.ai.AIBaseGlobal import *
from toontown.building import DistributedBuildingAI
from toontown.building import GagshopBuildingAI
from toontown.building import HQBuildingAI
from toontown.building import KartShopBuildingAI
from toontown.building import PetshopBuildingAI
from toontown.hood import ZoneUtil


class DistributedBuildingMgrAI:
    notify = directNotify.newCategory('DistributedBuildingMgrAI')

    def __init__(self, air, branchId, dnaStore, trophyMgr):
        self.air = air
        self.branchId = branchId
        self.canonicalBranchId = ZoneUtil.getCanonicalZoneId(self.branchId)
        self.dnaStore = dnaStore
        self.trophyMgr = trophyMgr
        self.__buildings = {}
        self.tableName = 'buildings_%s' % self.branchId
        self.findAllLandmarkBuildings()

    def cleanup(self):
        for building in self.__buildings.values():
            building.cleanup()
        self.__buildings = {}

    def isValidBlockNumber(self, blockNumber):
        return blockNumber in self.__buildings

    def isSuitBlock(self, blockNumber):
        if not self.isValidBlockNumber(blockNumber):
            return False
        return self.__buildings[blockNumber].isSuitBlock()

    def getSuitBlocks(self):
        blocks = []
        for blockNumber, building in self.__buildings.items():
            if building.isSuitBlock():
                blocks.append(blockNumber)
        return blocks

    def getEstablishedSuitBlocks(self):
        blocks = []
        for blockNumber, building in self.__buildings.items():
            if building.isEstablishedSuitBlock():
                blocks.append(blockNumber)
        return blocks

    def getToonBlocks(self):
        blocks = []
        for blockNumber, building in self.__buildings.items():
            if isinstance(building, HQBuildingAI.HQBuildingAI):
                continue
            if isinstance(building, GagshopBuildingAI.GagshopBuildingAI):
                continue
            if isinstance(building, PetshopBuildingAI.PetshopBuildingAI):
                continue
            if isinstance(building, KartShopBuildingAI.KartShopBuildingAI):
                continue
            if not building.isSuitBlock():
                blocks.append(blockNumber)
        return blocks

    def getBuildings(self):
        return self.__buildings.values()

    def getFrontDoorPoint(self, blockNumber):
        if self.isValidBlockNumber(blockNumber):
            return self.__buildings[blockNumber].getFrontDoorPoint()

    def getBuildingTrack(self, blockNumber):
        if self.isValidBlockNumber(blockNumber):
            return self.__buildings[blockNumber].track

    def getBuilding(self, blockNumber):
        if self.isValidBlockNumber(blockNumber):
            return self.__buildings[blockNumber]

    def setFrontDoorPoint(self, blockNumber, point):
        if self.isValidBlockNumber(blockNumber):
            return self.__buildings[blockNumber].setFrontDoorPoint(point)

    def getDNABlockLists(self):
        blocks = []
        hqBlocks = []
        gagshopBlocks = []
        petshopBlocks = []
        kartshopBlocks = []
        for i in xrange(self.dnaStore.getNumBlockNumbers()):
            blockNumber = self.dnaStore.getBlockNumberAt(i)
            buildingType = self.dnaStore.getBlockBuildingType(blockNumber)
            if buildingType == 'hq':
                hqBlocks.append(blockNumber)
            elif buildingType == 'gagshop':
                gagshopBlocks.append(blockNumber)
            elif buildingType == 'petshop':
                if self.air.wantPets:
                    petshopBlocks.append(blockNumber)
            elif buildingType == 'kartshop':
                kartshopBlocks.append(blockNumber)
            else:
                blocks.append(blockNumber)
        return (blocks, hqBlocks, gagshopBlocks, petshopBlocks, kartshopBlocks)

    def findAllLandmarkBuildings(self):
        buildings = self.load()
        (blocks, hqBlocks, gagshopBlocks, petshopBlocks, kartshopBlocks) = self.getDNABlockLists()
        for blockNumber in blocks:
            self.newBuilding(blockNumber, buildings.get(blockNumber, None))
        for blockNumber in hqBlocks:
            self.newHQBuilding(blockNumber)
        for blockNumber in gagshopBlocks:
            self.newGagshopBuilding(blockNumber)
        for block in petshopBlocks:
            self.newPetshopBuilding(block)
        for block in kartshopBlocks:
            self.newKartShopBuilding(block)

    def newBuilding(self, blockNumber, blockData = None):
        building = DistributedBuildingAI.DistributedBuildingAI(self.air, blockNumber, self.branchId, self.trophyMgr)
        building.generateWithRequired(self.branchId)
        if blockData:
            building.track = blockData.get('track', 'c')
            building.realTrack = blockData.get('track', 'c')
            building.difficulty = int(blockData.get('difficulty', 1))
            building.numFloors = int(blockData.get('numFloors', 1))
            building.numFloors = max(1, min(5, building.numFloors))
            building.becameSuitTime = blockData.get('becameSuitTime', time.time())
            if blockData['state'] == 'suit':
                building.setState('suit')
            elif blockData['state'] == 'cogdo':
                if simbase.air.wantCogdominiums:
                    building.setState('cogdo')
            else:
                building.setState('toon')
        else:
            building.setState('toon')
        self.__buildings[blockNumber] = building
        return building

    def newHQBuilding(self, blockNumber):
        dnaStore = self.air.dnaStoreMap[self.canonicalBranchId]
        exteriorZoneId = dnaStore.getZoneFromBlockNumber(blockNumber)
        interiorZoneId = (self.branchId - (self.branchId%100)) + 500 + blockNumber
        building = HQBuildingAI.HQBuildingAI(
            self.air, exteriorZoneId, interiorZoneId, blockNumber)
        self.__buildings[blockNumber] = building
        return building

    def newGagshopBuilding(self, blockNumber):
        dnaStore = self.air.dnaStoreMap[self.canonicalBranchId]
        exteriorZoneId = dnaStore.getZoneFromBlockNumber(blockNumber)
        interiorZoneId = (self.branchId - (self.branchId%100)) + 500 + blockNumber
        building = GagshopBuildingAI.GagshopBuildingAI(
            self.air, exteriorZoneId, interiorZoneId, blockNumber)
        self.__buildings[blockNumber] = building
        return building

    def newPetshopBuilding(self, blockNumber):
        dnaStore = self.air.dnaStoreMap[self.canonicalBranchId]
        exteriorZoneId = dnaStore.getZoneFromBlockNumber(blockNumber)
        interiorZoneId = (self.branchId - (self.branchId%100)) + 500 + blockNumber
        building = PetshopBuildingAI.PetshopBuildingAI(
            self.air, exteriorZoneId, interiorZoneId, blockNumber)
        self.__buildings[blockNumber] = building
        return building

    def newKartShopBuilding(self, blockNumber):
        dnaStore = self.air.dnaStoreMap[self.canonicalBranchId]
        exteriorZoneId = dnaStore.getZoneFromBlockNumber(blockNumber)
        interiorZoneId = (self.branchId - (self.branchId%100)) + 500 + blockNumber
        building = KartShopBuildingAI.KartShopBuildingAI(
            self.air, exteriorZoneId, interiorZoneId, blockNumber)
        self.__buildings[blockNumber] = building
        return building

    def save(self):
        if self.air.dbConn:
            buildings = []
            for i in self.__buildings.values():
                if isinstance(i, HQBuildingAI.HQBuildingAI):
                    continue
                buildings.append(i.getPickleData())

            street = {'ai': self.air.districtId, 'branch': self.branchId}
            try:
                self.air.dbGlobalCursor.streets.update(street,
                                                        {'$setOnInsert': street,
                                                        '$set': {'buildings': buildings}},
                                                        upsert=True)
            except: # Something happened to our DB, but we can reconnect and retry.
                taskMgr.doMethodLater(config.GetInt('mongodb-retry-time', 2), self.save, 'retrySave', extraArgs=[])
        
        else:
            self.saveDev()
            
    def saveDev(self):
        backups = {}
        for blockNumber in self.getSuitBlocks():
            building = self.getBuilding(blockNumber)
            backups[blockNumber] = building.getPickleData()
        simbase.backups.save('block-info', (self.air.districtId, self.branchId), backups)
        
    def load(self):
        if self.air.dbConn:
            blocks = {}

            # Ensure that toontown.streets is indexed. Doing this at loading time
            # is a fine way to make sure that we won't upset players with a
            # lagspike while we wait for the backend to handle the index request.
            self.air.dbGlobalCursor.streets.ensure_index([('ai', 1),
                                                        ('branch', 1)])

            street = {'ai': self.air.districtId, 'branch': self.branchId}
            try:
                doc = self.air.dbGlobalCursor.streets.find_one(street)
            except: # We're failing over - normally we'd wait to retry, but this is on AI startup so we might want to retry (or refactor the bldgMgr so we can sanely retry).
                return blocks

            if not doc:
                return blocks

            for building in doc.get('buildings', []):
                blocks[int(building['block'])] = building

            return blocks
        
        else:
            blocks = simbase.backups.load('block-info', (self.air.districtId, self.branchId), default={})
            return blocks
            

   

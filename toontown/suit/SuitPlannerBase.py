from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import *
from toontown.hood import ZoneUtil, HoodUtil
from toontown.toonbase import ToontownGlobals, ToontownBattleGlobals
from toontown.building import SuitBuildingGlobals
from toontown.dna.DNAParser import *

class SuitPlannerBase:
    notify = directNotify.newCategory('SuitPlannerBase')
    SuitHoodInfo = [[2100,
      3,
      15,
      30,
      99,
      100,
      5,
      (30,
       50,
       80,
       80,
       100,
       100),
      (50,
       50,
       0,
       0),
      (1, 2, 3, 4, 5),
      []],
     [2200,
      3,
      15,
      30,
      99,
      100,
      5,
      (30,
       50,
       80,
       80,
       100,
       100),
      (0,
       0,
       50,
       50),
      (1, 2, 3, 4, 5),
      []],
     [2300,
      3,
      15,
      30,
      99,
      100,
      5,
      (1,
       30,
       50,
       80,
       80,
       100),
      (25,
       25,
       25,
       25),
      (3, 4, 5),
      []],
     [1100,
      1,
      5,
      0,
      99,
      100,
      5,
      (1,
       100,
       100,
       100,
       100,
       100),
      (50,
       0,
       0,
       50),
      (3, 4, 5, 6),
      []],
     [1200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       100,
       100,
       100,
       100,
       100),
      (0,
       0,
       95,
       5),
      (3,
	   4,
       5,
       6),
      []],
     [1300,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       100,
       100,
       100,
       100,
       100),
      (0,
       0,
       20,
       80),
      (4,
       5,
       6),
      []],
     [3100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       100,
       100,
       100,
       100,
       100),
      (95,
       0,
       5,
       0),
      (6, 7, 8, 9),
      []],
     [3200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       100,
       100,
       100,
       100,
       100),
      (0,
       0,
       50,
       50),
      (7, 8, 9),
      []],
     [3300,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       100,
       100,
       100,
       100,
       100),
      (0,
       100,
       0,
       0),
      (7, 8, 9, 10),
      []],
     [4100,
      1,
      5,
      0,
      99,
      100,
      4,
      (100,
       100,
       100,
       100,
       100,
       100),
      (50,
       0,
       50,
       0),
      (5, 6, 7, 8),
      []],
     [4200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       100,
       100,
       100,
       100,
       100),
      (15,
       75,
       0,
       10),
      (5,
       6,
       7,
       8),
      []],
     [4300,
      1,
      5,
      0,
      99,
      100,
      4,
      (100,
       100,
       100,
       100,
       100,
       100),
      (15,
       0,
       0,
       85),
      (6,
       7,
       8),
      []],
     [5100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       100,
       100,
       100,
       100,
       100),
      (40,
       0,
       50,
       10),
      (4, 5, 6, 7),
      []],
     [5200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       100,
       100,
       100,
       100,
       100),
      (0,
       0,
       80,
       20),
      (4,
       5,
       6,
       7),
      []],
     [5300,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       5,
       5,
       90),
      (6,
       7,
       8),
      []],
     [9100,
      1,
      5,
      0,
      99,
      100,
      4,
      (100,
       100,
       100,
       100,
       100,
       100),
      (50,
       50,
       0,
       0),
      (7,
       8,
	   9,
       10),
      []],
     [9200,
      1,
      5,
      0,
      99,
      100,
      4,
      (100,
       100,
       100,
       100,
       100,
       100),
      (0,
       0,
       50,
       50),
      (8,
       9,
       10),
      []],
     [10000,
      20,
      30,
      0,
      0,
      0,
      4,
      (100,
       100,
       100,
       100,
       100,
       100),
      (100,
       0,
       0,
       0),
      (11, 12, 13, 14),
      []],
     [11000,
      3,
      15,
      0,
      0,
      0,
      4,
      (100,
       100,
       100,
       100,
       100,
       100),
      (0,
       0,
       0,
       100),
      (6, 7, 8),
      []],
     [11200,
      10,
      20,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       0,
       100),
      (9, 10, 11, 12, 13),
      []],
     [12000,
      10,
      20,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       100,
       0),
      (8, 9, 10),
      []],
     [13000,
      10,
      20,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       100,
       0,
       0),
      (9, 10, 11, 12),
      []]]
    SUIT_HOOD_INFO_ZONE = 0
    SUIT_HOOD_INFO_MIN = 1
    SUIT_HOOD_INFO_MAX = 2
    SUIT_HOOD_INFO_BMIN = 3
    SUIT_HOOD_INFO_BMAX = 4
    SUIT_HOOD_INFO_BWEIGHT = 5
    SUIT_HOOD_INFO_SMAX = 6
    SUIT_HOOD_INFO_JCHANCE = 7
    SUIT_HOOD_INFO_TRACK = 8
    SUIT_HOOD_INFO_LVL = 9
    SUIT_HOOD_INFO_HEIGHTS = 10
    TOTAL_BWEIGHT = 0
    TOTAL_BWEIGHT_PER_TRACK = [0,
     0,
     0,
     0]
    TOTAL_BWEIGHT_PER_HEIGHT = [0,
     0,
     0,
     0,
     0]
    for currHoodInfo in SuitHoodInfo:
        weight = currHoodInfo[SUIT_HOOD_INFO_BWEIGHT]
        tracks = currHoodInfo[SUIT_HOOD_INFO_TRACK]
        levels = currHoodInfo[SUIT_HOOD_INFO_LVL]
        heights = [0,
         0,
         0,
         0,
         0]
        for level in levels:
            minFloors, maxFloors = SuitBuildingGlobals.SuitBuildingInfo[level - 1][0]
            for i in xrange(minFloors - 1, maxFloors):
                heights[i] += 1

        currHoodInfo[SUIT_HOOD_INFO_HEIGHTS] = heights
        TOTAL_BWEIGHT += weight
        TOTAL_BWEIGHT_PER_TRACK[0] += weight * tracks[0]
        TOTAL_BWEIGHT_PER_TRACK[1] += weight * tracks[1]
        TOTAL_BWEIGHT_PER_TRACK[2] += weight * tracks[2]
        TOTAL_BWEIGHT_PER_TRACK[3] += weight * tracks[3]
        TOTAL_BWEIGHT_PER_HEIGHT[0] += weight * heights[0]
        TOTAL_BWEIGHT_PER_HEIGHT[1] += weight * heights[1]
        TOTAL_BWEIGHT_PER_HEIGHT[2] += weight * heights[2]
        TOTAL_BWEIGHT_PER_HEIGHT[3] += weight * heights[3]
        TOTAL_BWEIGHT_PER_HEIGHT[4] += weight * heights[4]

    def __init__(self):
        self.suitWalkSpeed = ToontownGlobals.SuitWalkSpeed
        self.dnaStore = None
        self.pointIndexes = {}
        return

    def delete(self):
        del self.dnaStore

    def setupDNA(self):
        if self.dnaStore:
            return None
        self.dnaStore = DNAStorage()
        dnaFileName = self.genDNAFileName()
        loadDNAFileAI(self.dnaStore, dnaFileName)
        self.initDNAInfo()

    def genDNAFileName(self):
        zoneId = ZoneUtil.getCanonicalZoneId(self.getZoneId())
        hoodId = ZoneUtil.getCanonicalHoodId(zoneId)
        hood = ToontownGlobals.dnaMap[hoodId]
        phase = ToontownGlobals.streetPhaseMap[hoodId]
        if hoodId == zoneId:
            zoneId = 'sz'
        return 'phase_%s/dna/%s_%s.pdna' % (phase, hood, zoneId)

    def getZoneId(self):
        return self.zoneId

    def setZoneId(self, zoneId):
        self.notify.debug('setting zone id for suit planner')
        self.zoneId = zoneId
        self.setupDNA()

    def extractGroupName(self, groupFullName):
        return groupFullName.split(':', 1)[0]

    def initDNAInfo(self):
        numGraphs = self.dnaStore.discoverContinuity()
        if numGraphs != 1:
            self.notify.info('zone %s has %s disconnected suit paths.' % (self.zoneId, numGraphs))
        self.battlePosDict = {}
        self.cellToGagBonusDict = {}

        for i in xrange(self.dnaStore.getNumDNAVisGroupsAI()):
            vg = self.dnaStore.getDNAVisGroupAI(i)
            zoneId = int(self.extractGroupName(vg.getName()))

            if vg.getNumBattleCells() == 1:
                battleCell = vg.getBattleCell(0)
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
            elif vg.getNumBattleCells() > 1:
                self.notify.warning('multiple battle cells for zone: %d' % zoneId)
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()

            if True:
                for i in xrange(vg.getNumChildren()):
                    childDnaGroup = vg.at(i)

                    if isinstance(childDnaGroup, DNAInteractiveProp):
                        self.notify.debug('got interactive prop %s' % childDnaGroup)
                        battleCellId = childDnaGroup.getCellId()

                        if battleCellId == -1:
                            self.notify.warning('interactive prop %s  at %s not associated with a a battle' % (childDnaGroup, zoneId))

                        elif battleCellId == 0:
                            if zoneId in self.cellToGagBonusDict:
                                self.notify.error('FIXME battle cell at zone %s has two props %s %s linked to it' % (zoneId, self.cellToGagBonusDict[zoneId], childDnaGroup))
                            else:
                                name = childDnaGroup.getName()
                                propType = HoodUtil.calcPropType(name)
                                if propType in ToontownBattleGlobals.PropTypeToTrackBonus:
                                    trackBonus = ToontownBattleGlobals.PropTypeToTrackBonus[propType]
                                    self.cellToGagBonusDict[zoneId] = trackBonus

        self.dnaStore.resetDNAGroups()
        self.dnaStore.resetDNAVisGroups()
        self.dnaStore.resetDNAVisGroupsAI()
        self.streetPointList = []
        self.frontdoorPointList = []
        self.sidedoorPointList = []
        self.cogHQDoorPointList = []
        numPoints = self.dnaStore.getNumSuitPoints()
        for i in xrange(numPoints):
            point = self.dnaStore.getSuitPointAtIndex(i)
            if point.getPointType() == DNASuitPoint.FRONT_DOOR_POINT:
                self.frontdoorPointList.append(point)
            elif point.getPointType() == DNASuitPoint.SIDE_DOOR_POINT:
                self.sidedoorPointList.append(point)
            elif (point.getPointType() == DNASuitPoint.COGHQ_IN_POINT) or (point.getPointType() == DNASuitPoint.COGHQ_OUT_POINT):
                self.cogHQDoorPointList.append(point)
            else:
                self.streetPointList.append(point)
            self.pointIndexes[point.getIndex()] = point

    def performPathTest(self):
        if not self.notify.getDebug():
            return None
        startAndEnd = self.pickPath()
        if not startAndEnd:
            return None
        startPoint = startAndEnd[0]
        endPoint = startAndEnd[1]
        path = self.dnaStore.getSuitPath(startPoint, endPoint)
        numPathPoints = path.getNumPoints()
        for i in xrange(numPathPoints - 1):
            zone = self.dnaStore.getSuitEdgeZone(path.getPointIndex(i), path.getPointIndex(i + 1))
            travelTime = self.dnaStore.getSuitEdgeTravelTime(path.getPointIndex(i), path.getPointIndex(i + 1), self.suitWalkSpeed)
            self.notify.debug('edge from point ' + `i` + ' to point ' + `(i + 1)` + ' is in zone: ' + `zone` + ' and will take ' + `travelTime` + ' seconds to walk.')

    def genPath(self, startPoint, endPoint, minPathLen, maxPathLen):
        return self.dnaStore.getSuitPath(startPoint, endPoint, minPathLen, maxPathLen)

    def getDnaStore(self):
        return self.dnaStore

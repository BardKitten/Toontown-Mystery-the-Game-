from pandac import PandaModules as PM
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.PythonUtil import list2dict, uniqueElements
import LevelConstants, types

class LevelSpec:
    notify = DirectNotifyGlobal.directNotify.newCategory('LevelSpec')
    SystemEntIds = (LevelConstants.UberZoneEntId, LevelConstants.LevelMgrEntId)

    def __init__(self, spec = None, scenario = 0):
        newSpec = 0
        if type(spec) is types.ModuleType:
            self.specDict = spec.levelSpec
        elif type(spec) is types.DictType:
            self.specDict = spec
        self.entId2specDict = {}
        self.entId2specDict.update(list2dict(self.getGlobalEntIds(), value=self.privGetGlobalEntityDict()))
        for i in xrange(self.getNumScenarios()):
            self.entId2specDict.update(list2dict(self.getScenarioEntIds(i), value=self.privGetScenarioEntityDict(i)))

        self.setScenario(scenario)

    def destroy(self):
        del self.specDict
        del self.entId2specDict
        del self.scenario
        if hasattr(self, 'level'):
            del self.level

    def getNumScenarios(self):
        return len(self.specDict['scenarios'])

    def setScenario(self, scenario):
        self.scenario = scenario

    def getScenario(self):
        return self.scenario

    def getGlobalEntIds(self):
        return self.privGetGlobalEntityDict().keys()

    def getScenarioEntIds(self, scenario = None):
        if scenario is None:
            scenario = self.scenario
        return self.privGetScenarioEntityDict(scenario).keys()

    def getAllEntIds(self):
        return self.getGlobalEntIds() + self.getScenarioEntIds()

    def getAllEntIdsFromAllScenarios(self):
        entIds = self.getGlobalEntIds()
        for scenario in xrange(self.getNumScenarios()):
            entIds.extend(self.getScenarioEntIds(scenario))

        return entIds

    def getEntitySpec(self, entId):
        specDict = self.entId2specDict[entId]
        return specDict[entId]

    def getEntityType(self, entId):
        return self.getEntitySpec(entId)['type']

    def getEntityZoneEntId(self, entId):
        spec = self.getEntitySpec(entId)
        type = spec['type']
        if type == 'zone':
            return entId
        return self.getEntityZoneEntId(spec['parentEntId'])

    def getEntType2ids(self, entIds):
        entType2ids = {}
        for entId in entIds:
            type = self.getEntityType(entId)
            entType2ids.setdefault(type, [])
            entType2ids[type].append(entId)

        return entType2ids

    def privGetGlobalEntityDict(self):
        return self.specDict['globalEntities']

    def privGetScenarioEntityDict(self, scenario):
        return self.specDict['scenarios'][scenario]

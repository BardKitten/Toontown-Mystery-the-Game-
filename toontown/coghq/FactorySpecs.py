from toontown.toonbase import ToontownGlobals
import SellbotLegFactorySpec
import SellbotLegFactoryCogs
import LawbotLegFactorySpec
import LawbotLegFactoryCogs

def getFactorySpecModule(factoryId):
    return FactorySpecModules[factoryId]


def getCogSpecModule(factoryId):
    return CogSpecModules[factoryId]


FactorySpecModules = {ToontownGlobals.SellbotFactoryInt: SellbotLegFactorySpec,
 ToontownGlobals.LawbotOfficeInt: LawbotLegFactorySpec}
CogSpecModules = {ToontownGlobals.SellbotFactoryInt: SellbotLegFactoryCogs,
 ToontownGlobals.LawbotOfficeInt: LawbotLegFactoryCogs}

if config.GetBool('want-brutal-factory', True):
    import SellbotMegaCorpLegSpec
    import SellbotMegaCorpLegCogs
    FactorySpecModules[ToontownGlobals.SellbotMegaCorpInt] = SellbotMegaCorpLegSpec
    CogSpecModules[ToontownGlobals.SellbotMegaCorpInt] = SellbotMegaCorpLegCogs

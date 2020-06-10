from toontown.coghq import CogDisguiseGlobals
from toontown.suit import SuitDNA

class CogSuitManagerAI:

    def recoverPart(self, toon, factoryType, suitTrack):
        if suitTrack not in SuitDNA.suitDepts:
            return

        recoveredParts = [0, 0, 0, 0]
        parts = toon.getCogParts()
        suitTrack = SuitDNA.suitDepts.index(suitTrack)

        if CogDisguiseGlobals.isSuitComplete(parts, suitTrack):
            return recoveredParts

        recoveredParts[suitTrack] = toon.giveGenericCogPart(factoryType, suitTrack)
        return recoveredParts

    def removeParts(self, toon, suitDept):
        parts = toon.getCogParts()

        if CogDisguiseGlobals.isSuitComplete(parts, suitDept):
            toon.loseCogParts(suitDept)

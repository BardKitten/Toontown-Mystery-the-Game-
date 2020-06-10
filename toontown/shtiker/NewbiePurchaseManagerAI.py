import PurchaseManagerAI

class NewbiePurchaseManagerAI(PurchaseManagerAI.PurchaseManagerAI):

    def __init__(self, air, newbieId, avArray, mpArray, previousMinigameId, trolleyZone):
        self.ownedNewbieId = newbieId
        newbieList = []
        PurchaseManagerAI.PurchaseManagerAI.__init__(self, air, avArray, mpArray, previousMinigameId, trolleyZone, newbieList)

    def startCountdown(self):
        pass

    def getOwnedNewbieId(self):
        return self.ownedNewbieId

    def getInvolvedAvIds(self):
        return [self.ownedNewbieId]

    def handlePlayerLeaving(self, avId):
        toon = self.air.doId2do.get(avId)
        if toon:
            self.air.questManager.toonRodeTrolleyFirstTime(toon)

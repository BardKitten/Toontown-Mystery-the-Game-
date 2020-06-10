from DistributedNPCToonBaseAI import DistributedNPCToonBaseAI

class DistributedNPCClerkAI(DistributedNPCToonBaseAI):

    def setInventory(self, inventory, money):
        av = self.air.doId2do.get(self.air.getAvatarIdFromSender())

        if not av:
            return

        av.b_setMoney(money if av.inventory.validatePurchase(av.inventory.makeFromNetString(inventory), av.getMoney(), money) else av.getMoney())
        av.d_setInventory(av.inventory.makeNetString())
    
    def setState(self, avId, state):
        self.sendUpdate('setState', [self.air.getAvatarIdFromSender(), state])
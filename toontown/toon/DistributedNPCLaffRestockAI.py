from toontown.toonbase import ToontownGlobals
import LaffRestockGlobals, DistributedNPCToonBaseAI

class DistributedNPCLaffRestockAI(DistributedNPCToonBaseAI.DistributedNPCToonBaseAI):

    def restock(self, laff):
        av = simbase.air.doId2do.get(self.air.getAvatarIdFromSender())

        if not av:
            return

        newLaff = av.getHp() + laff

        if newLaff > av.getMaxHp():
            self.sendUpdate('restockResult', [LaffRestockGlobals.FULL_LAFF])
            return
        elif laff <= 0 or newLaff <= av.getHp():
            self.sendUpdate('restockResult', [LaffRestockGlobals.LESS_LAFF])
            return

        cost = laff * ToontownGlobals.CostPerLaffRestock

        if cost > av.getTotalMoney():
            self.sendUpdate('restockResult', [LaffRestockGlobals.NOT_ENOUGH_MONEY])
            return

        av.takeMoney(cost)
        av.toonUp(laff)
        self.sendUpdate('restockResult', [LaffRestockGlobals.RESTOCK_SUCCESSFUL])
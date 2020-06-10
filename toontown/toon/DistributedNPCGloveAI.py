from toontown.toonbase import ToontownGlobals
import DistributedNPCToonBaseAI, GloveNPCGlobals, ToonDNA

class DistributedNPCGloveAI(DistributedNPCToonBaseAI.DistributedNPCToonBaseAI):

    def changeGlove(self, color):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)

        if av is None or not hasattr(av, 'dna'):
            return
        elif len(ToonDNA.allColorsList) <= color:
            self.sendUpdate('changeGloveResult', [avId, GloveNPCGlobals.INVALID_COLOR])
            return
        elif av.dna.gloveColor == color:
            self.sendUpdate('changeGloveResult', [avId, GloveNPCGlobals.SAME_COLOR])
            return
        elif av.getTotalMoney() < ToontownGlobals.GloveCost:
            self.sendUpdate('changeGloveResult', [avId, GloveNPCGlobals.NOT_ENOUGH_MONEY])
            return

        av.takeMoney(ToontownGlobals.GloveCost)
        newDNA = ToonDNA.ToonDNA()
        newDNA.makeFromNetString(av.getDNAString())
        newDNA.gloveColor = ToonDNA.allColorsList[color]
        taskMgr.doMethodLater(1.0, lambda task: av.b_setDNAString(newDNA.makeNetString()), 'transform-%d' % avId)
        self.sendUpdate('changeGloveResult', [avId, GloveNPCGlobals.CHANGE_SUCCESSFUL])

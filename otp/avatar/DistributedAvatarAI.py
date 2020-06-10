from otp.ai.AIBaseGlobal import *
from otp.otpbase import OTPGlobals
from direct.distributed import DistributedNodeAI

class DistributedAvatarAI(DistributedNodeAI.DistributedNodeAI):

    def __init__(self, air):
        DistributedNodeAI.DistributedNodeAI.__init__(self, air)
        self.hp = 0
        self.maxHp = 0

    def b_setName(self, name):
        self.setName(name)
        self.d_setName(name)

    def d_setName(self, name):
        self.sendUpdate('setName', [name])

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def b_setMaxHp(self, maxHp):
        self.d_setMaxHp(maxHp)
        self.setMaxHp(maxHp)

    def d_setMaxHp(self, maxHp):
        self.sendUpdate('setMaxHp', [maxHp])

    def setMaxHp(self, maxHp):
        self.maxHp = maxHp

    def getMaxHp(self):
        return self.maxHp

    def b_setHp(self, hp):
        self.d_setHp(hp)
        self.setHp(hp)

    def d_setHp(self, hp):
        self.sendUpdate('setHp', [hp])

    def setHp(self, hp):
        self.hp = hp

    def getHp(self):
        return self.hp

    def toonUp(self, num):
        if self.hp >= self.maxHp:
            return
        self.hp = min(self.hp + num, self.maxHp)
        self.b_setHp(self.hp)

    def getRadius(self):
        return OTPGlobals.AvatarDefaultRadius

    def checkAvOnShard(self, avId):
        self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), 'confirmAvOnShard', [avId, avId in self.air.doId2do])

    def setParentStr(self, parentToken):
        if parentToken:
            senderId = self.air.getAvatarIdFromSender()
            self.air.writeServerEvent('Admin chat warning', senderId, 'using setParentStr to send "%s"' % parentToken)
            self.notify.warning('Admin chat warning: %s using setParentStr to send "%s"' % (senderId, parentToken))
        DistributedNodeAI.DistributedNodeAI.setParentStr(self, parentToken)

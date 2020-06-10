from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.level.DistributedLevel import DistributedLevel
from otp.level import LevelConstants
from otp.level.LevelSpec import LevelSpec
from toontown.cogdominium.DistCogdoGame import DistCogdoGame
from toontown.cogdominium.CogdoEntityCreator import CogdoEntityCreator

class DistCogdoLevelGame(DistCogdoGame, DistributedLevel):
    notify = directNotify.newCategory('DistCogdoLevelGame')

    def __init__(self, cr):
        DistributedLevel.__init__(self, cr)
        DistCogdoGame.__init__(self, cr)

    def generate(self):
        DistributedLevel.generate(self)
        DistCogdoGame.generate(self)

    def announceGenerate(self):
        DistributedLevel.announceGenerate(self)
        DistCogdoGame.announceGenerate(self)

    def createEntityCreator(self):
        return CogdoEntityCreator(level=self)

    def levelAnnounceGenerate(self):
        self.notify.debug('levelAnnounceGenerate')
        DistributedLevel.levelAnnounceGenerate(self)
        DistributedLevel.initializeLevel(self, LevelSpec(self.getSpec()))

    def initVisibility(self):
        levelMgr = self.getEntity(LevelConstants.LevelMgrEntId)
        levelMgr.geom.reparentTo(render)
        DistributedLevel.initVisibility(self)

    def placeLocalToon(self):
        DistributedLevel.placeLocalToon(self, moveLocalAvatar=False)

    def disable(self):
        DistCogdoGame.disable(self)
        DistributedLevel.disable(self)

    def delete(self):
        DistCogdoGame.delete(self)
        DistributedLevel.delete(self)

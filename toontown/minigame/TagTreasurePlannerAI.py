from direct.directnotify import DirectNotifyGlobal
from toontown.safezone import RegenTreasurePlannerAI

class TagTreasurePlannerAI(RegenTreasurePlannerAI.RegenTreasurePlannerAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('TagTreasurePlannerAI')

    def __init__(self, zoneId, game, callback, treasureType, spawnPoints):
        self.numPlayers = 0
        self.game = game
        self.spawnPoints = spawnPoints
        RegenTreasurePlannerAI.RegenTreasurePlannerAI.__init__(self, zoneId, treasureType, 'TagTreasurePlanner-' + str(zoneId), 3, 6, callback)

    def initSpawnPoints(self):
        return self.spawnPoints

    def validAvatar(self, treasure, av):
        return av.doId != self.game.itAvId

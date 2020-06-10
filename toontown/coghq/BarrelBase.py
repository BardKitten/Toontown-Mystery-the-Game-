import random

class BarrelBase:

    def getRng(self):
        return random.Random(self.entId * self.level.doId)

    def getRewardPerGrab(self):
        if not hasattr(self, '_reward'):
            if self.rewardPerGrabMax > self.rewardPerGrab:
                self._reward = self.getRng().randrange(self.rewardPerGrab, self.rewardPerGrabMax + 1)
            else:
                self._reward = self.rewardPerGrab
        return self._reward

    def getGagLevel(self):
        if not hasattr(self, '_gagLevel'):
            if self.gagLevelMax > self.gagLevel:
                self._gagLevel = self.getRng().randrange(self.gagLevel, self.gagLevelMax + 1)
            else:
                self._gagLevel = self.gagLevel
        return self._gagLevel

    def getGagTrack(self):
        if not hasattr(self, '_gagTrack'):
            if self.gagTrack == 'random':
                tracks = (0, 1, 2, 3, 4, 4, 5, 5, 6)
                self._gagTrack = self.getRng().choice(tracks)
            else:
                self._gagTrack = self.gagTrack
        return self._gagTrack

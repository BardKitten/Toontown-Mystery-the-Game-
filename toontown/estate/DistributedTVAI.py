from toontown.toonbase import ToontownGlobals
from DistributedFurnitureItemAI import DistributedFurnitureItemAI
import time

class DistributedTVAI(DistributedFurnitureItemAI):

    def __init__(self, air, furnitureMgr, item):
        DistributedFurnitureItemAI.__init__(self, air, furnitureMgr, item)
        self.video = ['', 0]
    
    def d_setVideo(self, video):
        self.sendUpdate('setVideo', video)
    
    def getVideo(self):
        return self.video
    
    def requestVideo(self, video):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        
        if not av:
            return
        elif self.furnitureMgr.ownerId != avId:
            self.sendUpdateToAvatarId(avId, 'requestVideoResponse', [ToontownGlobals.TV_NOT_OWNER])
            return
        elif not video.endswith('.mp4'):
            self.sendUpdateToAvatarId(avId, 'requestVideoResponse', [ToontownGlobals.TV_INVALID_VIDEO])
            return

        self.video = [video, int(time.time())]
        self.d_setVideo(self.video)
        self.sendUpdateToAvatarId(avId, 'requestVideoResponse', [ToontownGlobals.TV_OK])
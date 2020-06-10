from toontown.catalog import CatalogAccessoryItem, CatalogClothingItem, CatalogNametagItem, CatalogEmoteItem
from toontown.catalog.CatalogAccessoryItemGlobals import *
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.toon import ToonDNA
from toontown.quest import Quests
from DistributedFurnitureItemAI import DistributedFurnitureItemAI
import random, time

class DistributedChairAI(DistributedFurnitureItemAI):
    
    def __init__(self, air, furnitureMgr, itemType):
        DistributedFurnitureItemAI.__init__(self, air, furnitureMgr, itemType)
        self.avId = ToontownGlobals.CHAIR_NONE
    
    def destroy(self):
        self.ignoreAll()
        DistributedFurnitureItemAI.destroy(self)
    
    def b_setAvId(self, avId):
        self.avId = avId
        self.sendUpdate('setAvId', [avId])
    
    def b_resetAvId(self):
        self.b_setAvId(ToontownGlobals.CHAIR_NONE)
    
    def b_resetAvWithAnim(self, reason):
        self.sendUpdate('setStatus', [reason])
        self.b_resetAvId()
    
    def getAvId(self):
        return self.avId
    
    def getSitResponse(self):
        return ToontownGlobals.CHAIR_NONE
    
    def requestSit(self, requestCode):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        
        if not av:
            return

        if requestCode == ToontownGlobals.CHAIR_START:
            if self.avId in self.air.doId2do:
                return

            self.b_setAvId(avId)
            self.acceptOnce(self.air.getAvatarExitEvent(avId), self.__handleUnexpectedExit)
        elif requestCode == ToontownGlobals.CHAIR_STOP:
            if self.avId != avId:
                return
            
            self.b_resetAvWithAnim(ToontownGlobals.CHAIR_EXIT)
            self.ignoreAll()
    
    def __handleUnexpectedExit(self):
        self.b_resetAvWithAnim(ToontownGlobals.CHAIR_UNEXPECTED_EXIT)
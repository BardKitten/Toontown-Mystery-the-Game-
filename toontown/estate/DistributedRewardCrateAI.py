from toontown.catalog import CatalogAccessoryItem, CatalogClothingItem, CatalogNametagItem, CatalogEmoteItem
from toontown.catalog.CatalogAccessoryItemGlobals import *
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.toon import ToonDNA
from toontown.quest import Quests
from DistributedFurnitureItemAI import DistributedFurnitureItemAI
import random, time

RANDOM_PRIZES = [ToontownGlobals.CRATE_BEANS] * 10 + [ToontownGlobals.CRATE_BUFFS] * 5 + [ToontownGlobals.CRATE_NAMETAGS] * 10 + [ToontownGlobals.CRATE_EMOTES] * 10 + [ToontownGlobals.CRATE_CLOTHING] * 30 + [ToontownGlobals.CRATE_ACCESSORIES] * 35

class DistributedRewardCrateAI(DistributedFurnitureItemAI):
    
    def requestKeyUsage(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        
        if not av:
            return
        
        if avId != self.furnitureMgr.ownerId:
            self.sendUpdateToAvatarId(avId, 'useKeyResponse', [ToontownGlobals.CRATE_NOT_OWNER, 0])
            return
        elif not av.getCrateKeys():
            self.sendUpdateToAvatarId(avId, 'useKeyResponse', [ToontownGlobals.CRATE_NO_KEYS, 0])
            return

        av.removeCrateKeys(1)
        self.choosePrize(av)
        
        if not config.GetBool('dont-destroy-crate', False):
            self.furnitureMgr.deleteItemFromRoom(self.doId, False)
    
    def choosePrize(self, av, tryNumber = 0):
        if tryNumber == 10:
            self.giveBeans(av)
            return

        prizeType = random.choice(RANDOM_PRIZES)

        if prizeType == ToontownGlobals.CRATE_BEANS:
            self.giveBeans(av)
        elif prizeType == ToontownGlobals.CRATE_BUFFS:
            buffId = random.choice(Quests.BuffRewardIds)
            buff = Quests.RewardDict[buffId]
            
            buff[0](buffId, buff[1:]).sendRewardAI(av)
            self.sendUpdateToAvatarId(av.doId, 'useKeyResponse', [ToontownGlobals.CRATE_BUFFS, buffId])
        elif prizeType == ToontownGlobals.CRATE_NAMETAGS:
            allNametags = xrange(len(TTLocalizer.NametagFonts))
            playerNametags = av.nametagStyles
            remainingNametags = [nametag for nametag in allNametags if nametag not in playerNametags]

            if not remainingNametags:
                self.choosePrize(av, tryNumber + 1)
                return
            
            nametag = random.choice(remainingNametags)
            item = CatalogNametagItem.CatalogNametagItem(nametag, 0)
            
            if item.reachedPurchaseLimit(av):
                return

            av.addToDeliverySchedule(item)
            self.sendUpdateToAvatarId(av.doId, 'useKeyResponse', [ToontownGlobals.CRATE_NAMETAGS, 0])
        elif prizeType == ToontownGlobals.CRATE_EMOTES:
            playerEmotes = av.emoteAccess
            remainingEmotes = [i for i, access in enumerate(playerEmotes) if (not access) and access not in (17, 18, 19)]

            if not remainingEmotes:
                self.choosePrize(av, tryNumber + 1)
                return

            emote = random.choice(remainingEmotes)
            item = CatalogEmoteItem.CatalogEmoteItem(emote, 0)
            
            if item.reachedPurchaseLimit(av):
                self.choosePrize(av, tryNumber + 1)
                return

            av.addToDeliverySchedule(item)
            self.sendUpdateToAvatarId(av.doId, 'useKeyResponse', [ToontownGlobals.CRATE_EMOTES, 0])
        elif prizeType == ToontownGlobals.CRATE_CLOTHING:
            clothing = CatalogClothingItem.ClothingTypes.keys()
            random.shuffle(clothing)
            
            for id in clothing:
                item = CatalogClothingItem.CatalogClothingItem(id, 0)
                
                if not item.notOfferedTo(av) and not item.reachedPurchaseLimit(av):
                    av.addToDeliverySchedule(item)
                    self.sendUpdateToAvatarId(av.doId, 'useKeyResponse', [ToontownGlobals.CRATE_CLOTHING, 0])
                    return
        elif prizeType == ToontownGlobals.CRATE_ACCESSORIES:
            accessories = AccessoryTypes.keys()
            random.shuffle(accessories)
            
            for id in accessories:
                item = CatalogAccessoryItem.CatalogAccessoryItem(id, 0)
                
                if not item.reachedPurchaseLimit(av):
                    av.addToDeliverySchedule(item)
                    self.sendUpdateToAvatarId(av.doId, 'useKeyResponse', [ToontownGlobals.CRATE_ACCESSORIES, 0])
                    return
                
    def giveBeans(self, av):
        beans = random.randint(1, 15) * 100

        av.addMoney(beans)
        self.sendUpdateToAvatarId(av.doId, 'useKeyResponse', [ToontownGlobals.CRATE_BEANS, beans])
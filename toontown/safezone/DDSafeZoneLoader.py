from toontown.safezone import SafeZoneLoader, DDPlayground
from toontown.toon import NPCToons
from toontown.toonbase import TTLocalizer
import random

class DDSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DDPlayground.DDPlayground
        self.musicFile = 'phase_6/audio/bgm/DD_nbrhood.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/DD_SZ_activity.ogg'
        self.dnaFile = 'phase_6/dna/donalds_dock_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_DD_sz.pdna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.seagullSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_Seagull.ogg')
        self.underwaterSound = base.loadSfx('phase_4/audio/sfx/AV_ambient_water.ogg')
        self.swimSound = base.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.ogg')
        self.submergeSound = base.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.ogg')
        self.boat = self.geom.find('**/donalds_boat')
        self.dockSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_dockcreak.ogg')
        self.foghornSound = base.loadSfx('phase_5/audio/sfx/SZ_DD_foghorn.ogg')
        self.bellSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_shipbell.ogg')
        self.waterSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_waterlap.ogg')

        if not self.boat.isEmpty():
            wheel = self.boat.find('**/wheel')

            if not wheel.isEmpty():
                wheel.hide()

            self.boat.stash()
            self.donald = NPCToons.createLocalNPC(7011)

            self.donald.setPos(0, -1, 3.95)
            self.donald.reparentTo(self.boat)
            self.donald.setHat(48, 0, 0)
            self.donald.hideShadow()

            random.shuffle(TTLocalizer.DonaldChatter)
            self.donaldSpeech = self.donald.createTalkSequence(TTLocalizer.DonaldChatter, 15)
            self.donaldSpeech.loop(0)

        water = self.geom.find('**/water')

        water.setColorScale(1, 1, 1, 0.7)
        water.setTransparency(1)

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)

        if hasattr(self, 'donald'):
            self.donaldSpeech.pause()
            self.donald.delete()
            del self.donaldSpeech
            del self.donald

        del self.seagullSound
        del self.underwaterSound
        del self.swimSound
        del self.dockSound
        del self.foghornSound
        del self.bellSound
        del self.waterSound
        del self.submergeSound
        del self.boat

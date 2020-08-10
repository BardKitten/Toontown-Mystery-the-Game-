from ToontownGlobals import *
import math
import TTLocalizer

BattleCamFaceOffFov = 30.0
BattleCamFaceOffPos = Point3(0, -10, 4)
BattleCamDefaultPos = Point3(0, -8.6, 16.5)
BattleCamDefaultHpr = Vec3(0, -61, 0)
BattleCamDefaultFov = 80.0
BattleCamMenuFov = 65.0
BattleCamJoinPos = Point3(0, -12, 13)
BattleCamJoinHpr = Vec3(0, -45, 0)
SkipMovie = 0
BaseHp = 70
Tracks = TTLocalizer.BattleGlobalTracks
NPCTracks = TTLocalizer.BattleGlobalNPCTracks
TrackColors = (
 (211 / 255.0, 148 / 255.0, 255 / 255.0),
 (249 / 255.0, 255 / 255.0, 93 / 255.0),
 (79 / 255.0, 190 / 255.0, 76 / 255.0),
 (93 / 255.0, 108 / 255.0, 239 / 255.0),
 (255 / 255.0, 145 / 255.0, 66 / 255.0),
 (255 / 255.0, 65 / 255.0, 199 / 255.0),
 (67 / 255.0, 243 / 255.0, 255 / 255.0)
)
HEAL_TRACK = 0
TRAP_TRACK = 1
LURE_TRACK = 2
SOUND_TRACK = 3
THROW_TRACK = 4
SQUIRT_TRACK = 5
DROP_TRACK = 6
NPC_RESTOCK_GAGS = 7
NPC_TOONS_HIT = 8
NPC_COGS_MISS = 9
MIN_TRACK_INDEX = 0
MAX_TRACK_INDEX = 6
MIN_LEVEL_INDEX = 0
MAX_LEVEL_INDEX = 6
LAST_REGULAR_GAG_LEVEL = 5
UBER_GAG_LEVEL_INDEX = 6
NUM_GAG_TRACKS = 7
PropTypeToTrackBonus = {AnimPropTypes.Hydrant: SQUIRT_TRACK,
 AnimPropTypes.Mailbox: THROW_TRACK,
 AnimPropTypes.Trashcan: HEAL_TRACK}
Levels = [
 [0, 20, 150, 1500, 5000, 10000, 20000],
 [0, 20, 150, 1500, 5000, 10000, 20000],
 [0, 20, 150, 1500, 5000, 10000, 20000],
 [0, 20, 150, 1500, 5000, 10000, 20000],
 [0, 20, 150, 1500, 5000, 10000, 20000],
 [0, 20, 150, 1500, 5000, 10000, 20000],
 [0, 20, 150, 1500, 5000, 10000, 20000]
]
regMaxSkill = 20000
UberSkill = 1000
MaxSkill = UberSkill + regMaxSkill
ExperienceCap = 1750


MaxToonAcc = 95
StartingLevel = 0
CarryLimits = (
 (5, 0, 0, 0, 0, 0, 0),
 (10, 5, 0, 0, 0, 0, 0),
 (15, 10, 5, 0, 0, 0, 0),
 (20, 15, 10, 5, 0, 0, 0),
 (25, 20, 15, 10, 3, 0, 0),
 (30, 25, 20, 15, 5, 2, 0),
 (30, 25, 20, 15, 7, 3, 1)
)
MaxProps = ((15, 40), (30, 60), (75, 80))
DLF_SKELECOG = 1
DLF_FOREMAN = 2
DLF_BOSS = 4
DLF_SUPERVISOR = 8
DLF_VIRTUAL = 16
DLF_REVIVES = 32
pieNames = ['tart', 'fruitpie-slice', 'creampie-slice', 'fruitpie', 'creampie', 'birthday-cake', 'wedding-cake', 'lawbook']
AvProps = (
 ('feather', 'bullhorn', 'lipstick', 'bamboocane', 'pixiedust', 'baton', 'baton'),
 ('banana', 'rake', 'marbles', 'quicksand', 'trapdoor', 'tnt', 'traintrack'),
 ('1dollar', 'smmagnet', '5dollar', 'bigmagnet', '10dollar', 'hypnogogs', 'hypnogogs'),
 ('bikehorn', 'whistle', 'bugle', 'aoogah', 'elephant', 'foghorn', 'singing'),
 ('cupcake', 'fruitpieslice', 'creampieslice', 'fruitpie', 'creampie', 'cake', 'cake'),
 ('flower', 'waterglass', 'waterballoon', 'bottle', 'firehose', 'stormcloud', 'stormcloud'),
 ('flowerpot', 'sandbag', 'anvil', 'weight', 'safe', 'piano', 'piano')
)
AvPropsNew = (
 ('inventory_feather', 'inventory_megaphone', 'inventory_lipstick', 'inventory_bamboo_cane', 'inventory_pixiedust', 'inventory_juggling_cubes', 'inventory_ladder'),
 ('inventory_bannana_peel', 'inventory_rake', 'inventory_marbles', 'inventory_quicksand_icon', 'inventory_trapdoor', 'inventory_tnt', 'inventory_traintracks'),
 ('inventory_1dollarbill', 'inventory_small_magnet', 'inventory_5dollarbill', 'inventory_big_magnet', 'inventory_10dollarbill', 'inventory_hypno_goggles', 'inventory_screen'),
 ('inventory_bikehorn', 'inventory_whistle', 'inventory_bugle', 'inventory_aoogah', 'inventory_elephant', 'inventory_fog_horn', 'inventory_opera_singer'),
 ('inventory_tart', 'inventory_fruit_pie_slice', 'inventory_cream_pie_slice', 'inventory_fruitpie', 'inventory_creampie', 'inventory_cake', 'inventory_wedding'),
 ('inventory_squirt_flower', 'inventory_glass_of_water', 'inventory_water_gun', 'inventory_seltzer_bottle', 'inventory_firehose', 'inventory_storm_cloud', 'inventory_geyser'),
 ('inventory_flower_pot', 'inventory_sandbag', 'inventory_anvil', 'inventory_weight', 'inventory_safe_box', 'inventory_piano', 'inventory_ship')
)
AvPropStrings = TTLocalizer.BattleGlobalAvPropStrings
AvPropStringsSingular = TTLocalizer.BattleGlobalAvPropStringsSingular
AvPropStringsPlural = TTLocalizer.BattleGlobalAvPropStringsPlural
AvPropAccuracy = (
 (60, 60, 60, 60, 60, 60, 60),
 (0, 0, 0, 0, 0, 0, 0),
 (60, 65, 70, 75, 80, 85, 90),
 (95, 95, 95, 95, 95, 95, 95),
 (80, 80, 80, 80, 80, 80, 80),
 (90, 90, 90, 90, 90, 90, 90),
 (60, 60, 60, 60, 60, 60, 60)
)
AvLureBonusAccuracy = (75, 70, 75, 80, 85, 90, 95)
AvTrackAccStrings = TTLocalizer.BattleGlobalAvTrackAccStrings
AvPropDamage = (
 ( # Toon-up
  ((6, 7), (Levels[0][0], Levels[0][1])),
  ((12, 15), (Levels[0][1], Levels[0][2])),
  ((18, 24), (Levels[0][2], Levels[0][3])),
  ((30, 35), (Levels[0][3], Levels[0][4])),
  ((45, 55), (Levels[0][4], Levels[0][5])),
  ((60, 100), (Levels[0][5], Levels[0][6])),
  ((150, 150), (Levels[0][6], MaxSkill))
 ),
 ( # Trap
  ((18, 25), (Levels[1][0], Levels[1][1])),
  ((28, 35), (Levels[1][1], Levels[1][2])),
  ((45, 65), (Levels[1][2], Levels[1][3])),
  ((90, 110), (Levels[1][3], Levels[1][4])),
  ((125, 195), (Levels[1][4], Levels[1][5])),
  ((180, 320), (Levels[1][5], Levels[1][6])),
  ((365, 365), (Levels[1][6], MaxSkill))
 ),
 ( # Lure
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0))
 ),
 ( # Sound
  ((4, 6), (Levels[3][0], Levels[3][1])),
  ((9, 12), (Levels[3][1], Levels[3][2])),
  ((15, 18), (Levels[3][2], Levels[3][3])),
  ((22, 26), (Levels[3][3], Levels[3][4])),
  ((30, 35), (Levels[3][4], Levels[3][5])),
  ((55, 90), (Levels[3][5], Levels[3][6])),
  ((115, 115), (Levels[3][6], MaxSkill))
 ),
 ( # Throw
  ((8, 11), (Levels[4][0], Levels[4][1])),
  ((13, 16), (Levels[4][1], Levels[4][2])),
  ((20, 25), (Levels[4][2], Levels[4][3])),
  ((36, 45), (Levels[4][3], Levels[4][4])),
  ((50, 70), (Levels[4][4], Levels[4][5])),
  ((80, 135), (Levels[4][5], Levels[4][6])),
  ((185, 185), (Levels[4][6], MaxSkill))
 ),
 ( # Squirt
  ((6, 8), (Levels[5][0], Levels[5][1])),
  ((11, 14), (Levels[5][1], Levels[5][2])),
  ((17, 22), (Levels[5][2], Levels[5][3])),
  ((31, 38), (Levels[5][3], Levels[5][4])),
  ((45, 55), (Levels[5][4], Levels[5][5])),
  ((75, 115), (Levels[5][5], Levels[5][6])),
  ((150, 150), (Levels[5][6], MaxSkill))
 ),
 ( # Drop
  ((12, 15), (Levels[6][0], Levels[6][1])),
  ((20, 25), (Levels[6][1], Levels[6][2])),
  ((40, 45), (Levels[6][2], Levels[6][3])),
  ((65, 85), (Levels[6][3], Levels[6][4])),
  ((95, 140), (Levels[6][4], Levels[6][5])),
  ((150, 240), (Levels[6][5], Levels[6][6])),
  ((300, 300), (Levels[6][6], MaxSkill))
 )
)
ATK_SINGLE_TARGET = 0
ATK_GROUP_TARGET = 1
AvPropTargetCat = (
 (ATK_SINGLE_TARGET, ATK_GROUP_TARGET, ATK_SINGLE_TARGET, ATK_GROUP_TARGET, ATK_SINGLE_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET),
 (ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET),
 (ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET),
 (ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_GROUP_TARGET)
)
AvPropTarget = (0, 3, 0, 2, 3, 3, 3)
NumRoundsLured = [2, 3, 4, 5, 6, 7, 10]

def getAvPropDamage(attackTrack, attackLevel, exp, organicBonus = False, propBonus = False, propAndOrganicBonusStack = False):
    if attackTrack == LURE_TRACK:
        return NumRoundsLured[attackLevel]
    minD = AvPropDamage[attackTrack][attackLevel][0][0]
    maxD = AvPropDamage[attackTrack][attackLevel][0][1]
    minE = AvPropDamage[attackTrack][attackLevel][1][0]
    maxE = AvPropDamage[attackTrack][attackLevel][1][1]
    expVal = min(exp, maxE)
    expPerHp = float(maxE - minE + 1) / float(maxD - minD + 1)
    damage = math.floor((expVal - minE) / expPerHp) + minD
    if damage <= 0:
        damage = minD
    if propAndOrganicBonusStack:
        originalDamage = damage
        if organicBonus:
            damage += getDamageBonus(originalDamage)
        if propBonus:
            damage += getDamageBonus(originalDamage)
    elif organicBonus or propBonus:
        damage += getDamageBonus(damage)
    return damage


def getDamageBonus(normal):
    bonus = int(normal * 0.25)
    if bonus < 1 and normal > 1:
        bonus = 1
    return bonus


def isGroup(track, level):
    return AvPropTargetCat[AvPropTarget[track]][level]


def getCreditMultiplier(floorIndex):
    return 1 + floorIndex * 1.5


def getFactoryCreditMultiplier(factoryId):
    if factoryId == SellbotMegaCorpInt:
        return 4.0
    return 3.0


def getFactoryMeritMultiplier(factoryId):
    return 4.0


def getMintCreditMultiplier(mintId):
    return {CashbotMintIntA: 5.0,
     CashbotMintIntB: 6.5,
     CashbotMintIntC: 8.0}.get(mintId, 2.0)


def getStageCreditMultiplier(stageId):
    return {LawbotStageIntA: 5.0,
	LawbotStageIntB: 5.5,
	LawbotStageIntC: 7.0,
	LawbotStageIntD: 8.5}.get(stageId, 8.5)


def getCountryClubCreditMultiplier(countryClubId):
    return {BossbotCountryClubIntA: 6.0,
     BossbotCountryClubIntB: 7.5,
     BossbotCountryClubIntC: 9.0}.get(countryClubId, 2.0)


def getBossBattleCreditMultiplier(battleNumber):
    return 3 + battleNumber


def getInvasionMultiplier():
    return 4.0


def getMoreXpHolidayMultiplier():
    return 6.0


def encodeUber(trackList):
    bitField = 0
    for trackIndex in xrange(len(trackList)):
        if trackList[trackIndex] > 0:
            bitField += pow(2, trackIndex)

    return bitField


def decodeUber(flagMask):
    if flagMask == 0:
        return []
    maxPower = 16
    workNumber = flagMask
    workPower = maxPower
    trackList = []
    while workPower >= 0:
        if workNumber >= pow(2, workPower):
            workNumber -= pow(2, workPower)
            trackList.insert(0, 1)
        else:
            trackList.insert(0, 0)
        workPower -= 1

    endList = len(trackList)
    foundOne = 0
    while not foundOne:
        if trackList[endList - 1] == 0:
            trackList.pop(endList - 1)
            endList -= 1
        else:
            foundOne = 1

    return trackList


def getUberFlag(flagMask, index):
    decode = decodeUber(flagMask)
    if index >= len(decode):
        return 0
    else:
        return decode[index]


def getUberFlagSafe(flagMask, index):
    if flagMask == 'unknown' or flagMask < 0:
        return -1
    else:
        return getUberFlag(flagMask, index)

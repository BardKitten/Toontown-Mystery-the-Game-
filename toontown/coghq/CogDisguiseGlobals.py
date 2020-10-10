from toontown.suit import SuitDNA
import types
from toontown.toonbase import TTLocalizer
from direct.showbase import PythonUtil
from otp.otpbase import OTPGlobals
PartsPerSuit = (17,
 14,
 12,
 10)
PartsPerSuitBitmasks = (131071,
 130175,
 56447,
 56411)
AllBits = 131071
MinPartLoss = 2
MaxPartLoss = 4
MeritsPerLevel = ((100,
  200,
  300,
  400,
  1000),
 (300,
  460,
  650,
  900,
  2000),
 (650,
  850,
  1150,
  1500,
  3500),
 (1000,
  1400,
  2000,
  2750,
  5000),
 (1750,
  2500,
  3350,
  4500,
  8500),
 (3000,
  3750,
  4500,
  5500,
  6500,
  8000,
  15000),
 (4000,
  5000,
  6000,
  7500,
  9500,
  11500,
  15000,
  18500,
  30000),
 (7500,
  9000,
  11000,
  13500,
  16500,
  20000,
  24000,
  28000,
  32000,
  36000,
  40000,
  45000,
  50000,
  55000,
  60000,
  65000,
  100000,
  0),
 (60,
  100,
  150,
  250,
  650),
 (150,
  250,
  380,
  500,
  1000),
 (300,
  450,
  650,
  950,
  2000),
 (700,
  900,
  1250,
  1600,
  3500),
 (1300,
  1560,
  1850,
  2250,
  4500),
 (1800,
  2200,
  2650,
  3100,
  3750,
  4500,
  10000),
 (3000,
  3500,
  4000,
  4500,
  5100,
  5800,
  7000,
  15000),
 (4500,
  5200,
  6050,
  6850,
  7620,
  8500,
  9500,
  10500,
  12000,
  13500,
  15000,
  17500,
  20000,
  25000,
  30000,
  35000,
  75000,
  0),
 (50,
  70,
  100,
  135,
  350),
 (75,
  125,
  185,
  250,
  550),
 (150,
  250,
  350,
  475,
  1000),
 (300,
  425,
  550,
  800,
  1850),
 (500,
  650,
  800,
  1150,
  2500),
 (750,
  950,
  1150,
  1400,
  1650,
  2000,
  5000),
 (1200,
  1600,
  2000,
  2400,
  2800,
  3350,
  3900,
  9000),
 (2400,
  3000,
  3800,
  4650,
  5500,
  6500,
  7500,
  8550,
  10000,
  11550,
  13500,
  16000,
  19000,
  22000,
  25000,
  27500,
  55000,
  0),
 (35,
  45,
  60,
  80,
  250),
 (50,
  70,
  100,
  160,
  445),
 (120,
  170,
  240,
  330,
  750),
 (210,
  290,
  390,
  510,
  1235),
 (350,
  480,
  630,
  800,
  2000),
 (650,
  800,
  950,
  1125,
  1300,
  1560,
  3500),
 (930,
  1200,
  1500,
  1800,
  2150,
  2500,
  2800,
  6500),
 (1750,
  2100,
  2500,
  2900,
  3350,
  3800,
  4200,
  4600,
  5000,
  5500,
  6000,
  6550,
  7050,
  7650,
  8300,
  9000,
  20000,
  0))
leftLegUpper = 1
leftLegLower = 2
leftLegFoot = 4
rightLegUpper = 8
rightLegLower = 16
rightLegFoot = 32
torsoLeftShoulder = 64
torsoRightShoulder = 128
torsoChest = 256
torsoHealthMeter = 512
torsoPelvis = 1024
leftArmUpper = 2048
leftArmLower = 4096
leftArmHand = 8192
rightArmUpper = 16384
rightArmLower = 32768
rightArmHand = 65536
upperTorso = torsoLeftShoulder
leftLegIndex = 0
rightLegIndex = 1
torsoIndex = 2
leftArmIndex = 3
rightArmIndex = 4
PartsQueryShifts = (leftLegUpper,
 rightLegUpper,
 torsoLeftShoulder,
 leftArmUpper,
 rightArmUpper)
PartsQueryMasks = (leftLegFoot + leftLegLower + leftLegUpper,
 rightLegFoot + rightLegLower + rightLegUpper,
 torsoPelvis + torsoHealthMeter + torsoChest + torsoRightShoulder + torsoLeftShoulder,
 leftArmHand + leftArmLower + leftArmUpper,
 rightArmHand + rightArmLower + rightArmUpper)
PartNameStrings = TTLocalizer.CogPartNames
SimplePartNameStrings = TTLocalizer.CogPartNamesSimple
PartsQueryNames = ({1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[2],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[5],
  64: PartNameStrings[6],
  128: PartNameStrings[7],
  256: PartNameStrings[8],
  512: PartNameStrings[9],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[13],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[16]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[2],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[5],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[13],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[16]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[2],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[5],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[1],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[4],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]})
suitTypes = PythonUtil.Enum(('NoSuit', 'NoMerits', 'FullSuit'))

def getNextPart(parts, partIndex, dept):
    dept = dept2deptIndex(dept)
    needMask = PartsPerSuitBitmasks[dept] & PartsQueryMasks[partIndex]
    haveMask = parts[dept] & PartsQueryMasks[partIndex]
    nextPart = ~needMask | haveMask
    nextPart = nextPart ^ nextPart + 1
    nextPart = nextPart + 1 >> 1
    return nextPart


def getPartName(partArray):
    index = 0
    for part in partArray:
        if part:
            return PartsQueryNames[index][part]
        index += 1


def isSuitComplete(parts, dept):
    dept = dept2deptIndex(dept)
    for p in xrange(len(PartsQueryMasks)):
        if getNextPart(parts, p, dept):
            return 0

    return 1

def getTotalMerits(toon, index):
    from toontown.battle import SuitBattleGlobals
    cogIndex = toon.cogTypes[index] + SuitDNA.suitsPerDept * index
    cogTypeStr = SuitDNA.suitHeadTypes[cogIndex]
    cogBaseLevel = SuitBattleGlobals.SuitAttributes[cogTypeStr]['level']
    cogLevel = toon.cogLevels[index] - cogBaseLevel
    cogLevel = max(min(cogLevel, len(MeritsPerLevel[cogIndex]) - 1), 0)
    return MeritsPerLevel[cogIndex][cogLevel]


def getTotalParts(bitString, shiftWidth = 32):
    sum = 0
    for shift in xrange(0, shiftWidth):
        sum = sum + (bitString >> shift & 1)

    return sum


def asBitstring(number):
    array = []
    shift = 0
    if number == 0:
        array.insert(0, '0')
    while pow(2, shift) <= number:
        if number >> shift & 1:
            array.insert(0, '1')
        else:
            array.insert(0, '0')
        shift += 1

    str = ''
    for i in xrange(0, len(array)):
        str = str + array[i]

    return str


def asNumber(bitstring):
    num = 0
    for i in xrange(0, len(bitstring)):
        if bitstring[i] == '1':
            num += pow(2, len(bitstring) - 1 - i)

    return num


def dept2deptIndex(dept):
    if type(dept) == types.StringType:
        dept = SuitDNA.suitDepts.index(dept)
    return dept

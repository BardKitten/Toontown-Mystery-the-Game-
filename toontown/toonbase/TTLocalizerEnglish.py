from toontown.toonbase.TTLocalizerEnglishProperty import *
from toontown.catalog import CatalogAccessoryItemGlobals
from otp.otpbase import OTPLocalizer as OL
import random
OL.SpeedChatStaticText = OL.SpeedChatStaticTextToontown.copy()
for key in OL.SpeedChatStaticTextCommon.iterkeys():
    OL.SpeedChatStaticText[key] = OL.SpeedChatStaticTextCommon[key]

commitmantst = 'kptmptest - removable'
InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'
ToonFont = 'phase_3/models/fonts/ImpressBT.ttf'
SuitFont = 'phase_3/models/fonts/vtRemingtonPortable.ttf'
SignFont = 'phase_3/models/fonts/MickeyFont'
MinnieFont = 'phase_3/models/fonts/MinnieFont'
ChalkFont = 'phase_3/models/fonts/Chawp.ttf'
BuildingNametagFont = 'phase_3/models/fonts/MickeyFont'
BuildingNametagShadow = None
NametagFonts = (
    'phase_3/models/fonts/ImpressBT.ttf',
    'phase_3/models/fonts/AnimGothic.bam',
    'phase_3/models/fonts/Aftershock.bam',
    'phase_3/models/fonts/JiggeryPokery.bam',
    'phase_3/models/fonts/Ironwork.bam',
    'phase_3/models/fonts/HastyPudding.bam',
    'phase_3/models/fonts/Comedy.bam',
    'phase_3/models/fonts/Humanist.bam',
    'phase_3/models/fonts/Portago.bam',
    'phase_3/models/fonts/Musicals.bam',
    'phase_3/models/fonts/Scurlock.bam',
    'phase_3/models/fonts/Danger.bam',
    'phase_3/models/fonts/Alie.bam',
    'phase_3/models/fonts/OysterBar.bam',
    'phase_3/models/fonts/RedDogSaloon.bam',
    'phase_3/models/fonts/PBN.ttf',
    'phase_3/models/fonts/SomethingStrange.ttf',
    'phase_3/models/fonts/DinosaursAreAlive.ttf'
)
NametagFontNames = (
    'Basic',
    'Plain',
    'Shivering',
    'Wonky',
    'Fancy',
    'Silly',
    'Zany',
    'Practical',
    'Nautical',
    'Whimsical',
    'Spooky',
    'Action',
    'Poetic',
    'Boardwalk',
    'Western',
    'Pixelated',
    'Metal',
    'Dinosaurs'
)
NametagLabel = ' Nametag'
ScreenshotPath = 'user/screenshots/'
Flippy = 'Miss Marma'
lTheBrrrgh = 'Freezing Area'
lDaisyGardens = 'Daisy Gardens'
lDonaldsDock = "Donald's Dock"
lDonaldsDreamland = "Donald's Dreamland"
lMinniesMelodyland = "Minnie's Melodyland"
lToontownCentral = 'Toontown Playground'
lToonHQ = 'Toon HQ'
lSellbotHQ = 'Fashionbot HQ'
lGoofySpeedway = 'Goofy Speedway'
lOutdoorZone = "Chip 'n Dale's Acorn Acres"
lGolfZone = "Chip 'n Dale's MiniGolf"
lPartyHood = 'Party Grounds'
GlobalStreetNames = {20000: ('to', 'on', 'Tutorial Terrace'),
 1000: ('to the', 'in the', 'Playground'),
 1100: ('to', 'on', 'Barnacle World'),
 1200: ('to', 'on', 'Seaweed Area'),
 1300: ('to', 'on', 'Light Boat Area'),
 2000: ('to the', 'in the', 'Playground'),
 2100: ('to', 'on', 'Daisy Gardens Intro'),
 2200: ('to', 'on', 'Mickeys Travel Street'),
 2300: ('to', 'on', 'Punch Place'),
 3000: ('to the', 'in the', 'Playground'),
 3100: ('to', 'on', 'Lil Oldmans Lane'),
 3200: ('to', 'on', 'Minnies Lane'),
 3300: ('to', 'on', 'Defenderbot Law Lane'),
 4000: ('to the', 'in the', 'Playground'),
 4100: ('to', 'on', 'Music Lane'),
 4200: ('to', 'on', 'Loud Lane'),
 4300: ('to', 'on', 'Quiet Lane'),
 5000: ('to the', 'in the', 'Playground'),
 5100: ('to', 'on', 'Flower Lane'),
 5200: ('to', 'on', 'Tree Lane'),
 5300: ('to', 'on', 'Danger Lane'),
 9000: ('to the', 'in the', 'Playground'),
 9100: ('to', 'on', 'Quiet Lane'),
 9200: ('to', 'on', 'ZZZ Street'),
 9300: ('to', 'on', 'Bed Lane'),
 10000: ('to the', 'in the', 'Pizza CourtHouse'),
 10100: ("to the', 'in the', 'Pizzabot HQ"),
 10200: ("to', 'in', 'Darth Noah's Lair"),
 10500: ('to', 'in', 'Easy Three'),
 10600: ('to', 'in', 'Medium Six'),
 10700: ('to', 'in', 'Hard Nine'),
 11000: ('to the', 'in the', 'Fashionbot Courtyard'),
 11100: ('to the', 'in the', 'Fashionbot Lobby'),
 11200: ('to the', 'in the', 'Fashionbot Factory'),
 11500: ('to the', 'in the', 'Fashionbot Factory'),
 11600: ('to the', 'in the', 'Fashionbot Hard Mode'),
 12000: ('to the', 'in the', 'Carebot Medical Area'),
 12100: ('to the', 'in the', 'Carebot Vault'),
 12500: ('to the', 'in the', 'Carebot Waiting Vault'),
 12600: ('to the', 'in the', 'Carebot Interior'),
 12700: ('to the', 'in the', 'Carebot Final Room'),
 13000: ('to the', 'in the', 'Courtbot Court Room'),
 13100: ('to the', 'in the', 'Law Room'),
 13200: ('to the', 'in the', "Court Room"),
 13300: ('to the', 'in the', 'Warehouse'),
 13400: ('to the', 'in the', 'Judge Office'),
 13500: ('to the', 'in the', 'Jail'),
 13600: ('to the', 'in the', 'Law Enforcers Room')}
DonaldsDock = ('to', 'in', lDonaldsDock)
ToontownCentral = ('to', 'in', lToontownCentral)
TheBrrrgh = ('to', 'in', lTheBrrrgh)
MinniesMelodyland = ('to', 'in', lMinniesMelodyland)
DaisyGardens = ('to', 'in', lDaisyGardens)
OutdoorZone = ('to', 'in', lOutdoorZone)
FunnyFarm = ('to the', 'in the', 'Funny Farm')
GoofySpeedway = ('to', 'in', lGoofySpeedway)
DonaldsDreamland = ('to', 'in', lDonaldsDreamland)
BossbotHQ = ('to', 'in', 'Castle HQ')
SellbotHQ = ('to', 'in', 'Fashionbot HQ')
CashbotHQ = ('to', 'in', 'Medical HQ')
LawbotHQ = ('to', 'in', 'Trial Court HQ')
Tutorial = ('to the', 'in the', 'Toon-torial')
MyEstate = ('to', 'in', 'your house')
GolfZone = ('to', 'in', lGolfZone)
PartyHood = ('to the', 'in the', lPartyHood)
Factory = 'Factory'
Headquarters = 'Headquarters'
SellbotFrontEntrance = 'Front Entrance'
SellbotSideEntrance = 'Side Entrance'
Office = 'Office'
FactoryNames = {11500: 'Fashionbot Designers Room',
 11600: 'Fashionbot Cog Hard Mode',
 13300: 'Courtbot Cog Office'}
FactoryTypeLeg = 'Leg'
FactoryTypeArm = 'Arm'
FactoryTypeTorso = 'Torso'
MintFloorTitle = 'Floor %s'
lCancel = 'Cancel'
lClose = 'Close'
lOK = 'OK'
lNext = 'Next'
lQuit = 'Quit'
lYes = 'Yes'
lNo = 'No'
SleepAutoReply = '%s is sleeping right now.'
lHQOfficerF = 'HQ Officer'
lHQOfficerM = 'HQ Officer'
Cog = 'Robot'
Cogs = 'Robots'
ACog = 'a Robot'
TheCogs = 'The Robots'
ASkeleton = 'a Skeleton'
Skeleton = 'Skeleton'
SkeletonP = 'Skeletons'
Av2Cog = 'a Version 2.0 Cog'
v2Cog = 'Version 2.0 Cog'
v2CogP = 'Version 2.0 Cogs'
ASkeleton = 'a Skeleton'
Foreman = 'Factory Skeleton'
ForemanP = 'Factory Skeleton'
AForeman = 'a Factory Skeleton'
CogVP = Cog + ' Boss Fashionhood'
CogVPs = "Cog Boss Fashionhoods"
ACogVP = ACog + ' Boss Fashionhood.'
Supervisor = 'Mint Supervisor'
SupervisorP = 'Mint Supervisors'
ASupervisor = 'a Mint Supervisor'
CogCFO = Cog + ' Guardian'
CogCFOs = "Cog Guardian"
ACogCFO = ACog + ' Guardian'
CogCJs = "Cog C.J.'s"
ACogCJ = ACog + ' C.J.'
CogCEOs = "Cog C.E.O.'s"
ACogCEO = ACog + ' C.E.O.'
CogBosses = 'Cog Bosses'
ACogBoss = ACog + ' Boss'
TheFish = 'the Fish'
AFish = 'a fish'
Level = 'Level'
QuestsCompleteString = 'Complete'
QuestsNotChosenString = 'Not chosen'
Period = '.'
Laff = 'Laff'
QuestInLocationString = ' %(inPhrase)s %(location)s'
QuestsDefaultGreeting = ('Hello, _avName_!',
 'Hi, _avName_!',
 'Hey there, _avName_!',
 'Say there, _avName_!',
 'Welcome, _avName_!',
 'Howdy, _avName_!',
 'How are you, _avName_?',
 'Greetings _avName_!')
QuestsDefaultIncomplete = ("How's that task coming, _avName_?",
 'Looks like you still have more work to do on that task!',
 'Keep up the good work, _avName_!',
 'Keep trying to finish that task.  I know you can do it!',
 'Keep trying to complete that task, we are counting on you!',
 'Keep working on that ToonTask!')
QuestsDefaultIncompleteProgress = ('You came to the right place, but you need to finish your ToonTask first.', 'When you are finished with that ToonTask, come back here.', 'Come back when you are finished with your ToonTask.')
QuestsDefaultIncompleteWrongNPC = ('Nice work on that ToonTask. You should go visit _toNpcName_._where_', 'Looks like you are ready to finish your ToonTask. Go see _toNpcName_._where_.', 'Go see _toNpcName_ to finish your ToonTask._where_')
QuestsDefaultComplete = ('Nice work! Here is your reward...', 'Great job, _avName_! Take this reward...', 'Wonderful job, _avName_! Here is your reward...')
QuestsDefaultLeaving = ('Bye!',
 'Goodbye!',
 'So long, _avName_.',
 'See ya, _avName_!',
 'Good luck!',
 'Have fun in Toontown!',
 'See you later!')
QuestsDefaultReject = ('Heya, _avName_!',
 'Whatcha need?',
 'Hello! How are you doing?',
 'Hi there.',
 "Sorry _avName_, I'm a bit busy right now.",
 'Yes?',
 'Howdy, _avName_!',
 'Welcome, _avName_!',
 "Hey, _avName_! How's it hanging?",
 "Need any help?",
 "Hi _avName_, what brings you here?")
QuestsDefaultTierNotDone = ('Hello, _avName_! You must finish your current ToonTasks before getting a new one.', 'Hi there! You need to finish the ToonTasks you are working on in order to get a new one.', 'Hi, _avName_! Before I can give you a new ToonTask, you need to finish the ones you have.')
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ('I heard _toNpcName_ is looking for you._where_',
 'Stop by and see _toNpcName_ when you get a chance._where_',
 'Pay a visit to _toNpcName_ next time you are over that way._where_',
 'If you get a chance, stop in and say hi to _toNpcName_._where_',
 '_toNpcName_ will give you your next ToonTask._where_')
QuestsLocationArticle = ''

def getLocalNum(num):
    return str(num)


QuestsItemNameAndNum = '%(num)s %(name)s'
QuestsCogQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogQuestHeadline = 'WANTED'
QuestsCogQuestSCStringS = 'I need to defeat %(cogName)s%(cogLoc)s.'
QuestsCogQuestSCStringP = 'I need to defeat some %(cogName)s%(cogLoc)s.'
QuestsCogQuestDefeat = 'Defeat %s'
QuestsCogQuestDefeatDesc = '%(numCogs)s %(cogName)s'
QuestsCogTrackQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogTrackQuestHeadline = 'WANTED'
QuestsCogTrackQuestSCStringS = 'I need to defeat %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestSCStringP = 'I need to defeat some %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestDefeat = 'Defeat %s'
QuestsCogTrackDefeatDesc = '%(numCogs)s %(trackName)s'
QuestsCogLevelQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogLevelQuestHeadline = 'WANTED'
QuestsCogLevelQuestDefeat = 'Defeat %s'
QuestsCogLevelQuestDesc = 'a Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescC = '%(count)s Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescI = 'some Level %(level)s+ %(name)s'
QuestsCogLevelQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestFloorNumbers = ('',
 'two+',
 'three+',
 'four+',
 'five+')
QuestsBuildingQuestHeadline = 'DEFEAT'
QuestsBuildingQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsBuildingQuestString = 'Defeat %s'
QuestsBuildingQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestDesc = 'a %(type)s Building'
QuestsBuildingQuestDescF = 'a %(floors)s story %(type)s Building'
QuestsBuildingQuestDescC = '%(count)s %(type)s Buildings'
QuestsBuildingQuestDescCF = '%(count)s %(floors)s story %(type)s Buildings'
QuestsBuildingQuestDescI = 'some %(type)s Buildings'
QuestsBuildingQuestDescIF = 'some %(floors)s story %(type)s Buildings'
QuestsCogdoQuestDesc = 'a %(type)s Field Office'
QuestsCogdoQuestDescM = '%(count)s %(type)s Field Offices'
QuestsCogdoQuestDescMUI = 'some %(type)s Field Offices'
QuestsCogdoQuestDescU = 'a Field Office'
QuestsCogdoQuestDescUM = '%(count)s Field Offices'
QuestsCogdoQuestDescMI = 'some Field Offices'
QuestFactoryQuestFactory = 'Factory'
QuestsFactoryQuestFactories = 'Factories'
QuestsFactoryQuestHeadline = 'DEFEAT'
QuestsFactoryQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsFactoryQuestString = 'Defeat %s'
QuestsFactoryQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsFactoryQuestDesc = 'a %(type)s Factory'
QuestsFactoryQuestDescC = '%(count)s %(type)s Factories'
QuestsFactoryQuestDescI = 'some %(type)s Factories'
QuestMintQuestMint = 'Mint'
QuestsMintQuestMints = 'Mints'
QuestsMintQuestHeadline = 'DEFEAT'
QuestsMintQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsMintQuestString = 'Defeat %s'
QuestsMintQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsMintQuestDesc = 'a Cog Mint'
QuestsMintQuestDescC = '%(count)s Cog Mints'
QuestsMintQuestDescI = 'some Cog Mints'
QuestsRescueQuestProgress = '%(progress)s of %(numToons)s rescued'
QuestsRescueQuestHeadline = 'RESCUE'
QuestsRescueQuestSCStringS = 'I need to rescue a Toon %(toonLoc)s.'
QuestsRescueQuestSCStringP = 'I need to rescue some Toons %(toonLoc)s.'
QuestsRescueQuestRescue = 'Rescue %s'
QuestsRescueQuestRescueDesc = '%(numToons)s Toons'
QuestsRescueQuestToonS = 'a Toon'
QuestsRescueQuestToonP = 'Toons'
QuestsRescueQuestAux = 'Rescue:'
QuestCogPartQuestCogPart = 'Cog Suit Part'
QuestsCogPartQuestFactories = 'Factories'
QuestsCogPartQuestHeadline = 'RETRIEVE'
QuestsCogPartQuestProgressString = '%(progress)s of %(num)s retrieved'
QuestsCogPartQuestString = 'Retrieve %s'
QuestsCogPartQuestSCString = 'I need to retrieve %(objective)s%(location)s.'
QuestsCogPartQuestAux = 'Retrieve:'
QuestsCogPartQuestDesc = 'a Cog Suit Part'
QuestsCogPartQuestDescC = '%(count)s Cog Suit Parts'
QuestsCogPartQuestDescI = 'some Cog Suit Parts'
QuestsDeliverGagQuestProgress = '%(progress)s of %(numGags)s delivered'
QuestsDeliverGagQuestHeadline = 'DELIVER'
QuestsDeliverGagQuestToSCStringS = 'I need to deliver %(gagName)s.'
QuestsDeliverGagQuestToSCStringP = 'I need to deliver some %(gagName)s.'
QuestsDeliverGagQuestSCString = 'I need to make a delivery.'
QuestsDeliverGagQuestString = 'Deliver %s'
QuestsDeliverGagQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsDeliverGagQuestInstructions = 'You can buy this gag in the Gag Shop once you earn access to it.'
QuestsDeliverItemQuestProgress = ''
QuestsDeliverItemQuestHeadline = 'DELIVER'
QuestsDeliverItemQuestSCString = 'I need to deliver %(article)s%(itemName)s.'
QuestsDeliverItemQuestString = 'Deliver %s'
QuestsDeliverItemQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsVisitQuestProgress = ''
QuestsVisitQuestHeadline = 'VISIT'
QuestsVisitQuestStringShort = 'Visit'
QuestsVisitQuestStringLong = 'Visit _toNpcName_'
QuestsVisitQuestSeeSCString = 'I need to see %s.'
QuestsRecoverItemQuestProgress = '%(progress)s of %(numItems)s recovered'
QuestsRecoverItemQuestHeadline = 'RECOVER'
QuestsRecoverItemQuestSeeHQSCString = 'I need to see an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToHQSCString = 'I need to return %s to an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToSCString = 'I need to return %(item)s to %(npcName)s.'
QuestsRecoverItemQuestGoToHQSCString = 'I need to go to a Toon HQ.'
QuestsRecoverItemQuestGoToPlaygroundSCString = 'I need to go to %s Playground.'
QuestsRecoverItemQuestGoToStreetSCString = 'I need to go %(to)s %(street)s in %(hood)s.'
QuestsRecoverItemQuestVisitBuildingSCString = 'I need to visit %s%s.'
QuestsRecoverItemQuestWhereIsBuildingSCString = 'Where is %s%s?'
QuestsRecoverItemQuestRecoverFromSCString = 'I need to recover %(item)s from %(holder)s%(loc)s.'
QuestsRecoverItemQuestString = 'Recover %(item)s from %(holder)s'
QuestsRecoverItemQuestHolderString = '%(level)s %(holder)d+ %(cogs)s'
QuestsTrackChoiceQuestHeadline = 'CHOOSE'
QuestsTrackChoiceQuestSCString = 'I need to choose between %(trackA)s and %(trackB)s.'
QuestsTrackChoiceQuestMaybeSCString = 'Maybe I should choose %s.'
QuestsTrackChoiceQuestString = 'Choose between %(trackA)s and %(trackB)s'
QuestsFriendQuestHeadline = 'FRIEND'
QuestsFriendQuestSCString = 'I need to make a friend.'
QuestsFriendQuestString = 'Make a friend'
QuestsMailboxQuestHeadline = 'MAIL'
QuestsMailboxQuestSCString = 'I need to check my mail.'
QuestsMailboxQuestString = 'Check your mail'
QuestsPhoneQuestHeadline = 'CLARABELLE'
QuestsPhoneQuestSCString = 'I need to call Clarabelle.'
QuestsPhoneQuestString = 'Call Clarabelle'
QuestsTrolleyQuestHeadline = 'TROLLEY'
QuestsTrolleyQuestSCString = 'I need to ride the trolley.'
QuestsTrolleyQuestString = 'Ride on the trolley'
QuestsTrolleyQuestStringShort = 'Ride the trolley'
QuestsMaxHpReward = 'Your Laff limit has been increased by %s.'
QuestsMaxHpRewardPoster = 'Reward: %s point Laff boost'
QuestsMoneyRewardSingular = 'You get 1 Jellybean.'
QuestsMoneyRewardPlural = 'You get %s Jellybeans.'
QuestsMoneyRewardPosterSingular = 'Reward: 1 Jellybean'
QuestsMoneyRewardPosterPlural = 'Reward: %s Jellybeans'
QuestsMaxMoneyRewardSingular = 'You can now carry 1 Jellybean.'
QuestsMaxMoneyRewardPlural = 'You can now carry %s Jellybeans.'
QuestsMaxMoneyRewardPosterSingular = 'Reward: Carry 1 Jellybean'
QuestsMaxMoneyRewardPosterPlural = 'Reward: Carry %s Jellybeans'
QuestsMaxGagCarryReward = 'You get a %(name)s. You can now carry %(num)s gags.'
QuestsMaxGagCarryRewardPoster = 'Reward: %(name)s (%(num)s)'
QuestsMaxQuestCarryReward = 'You can now have %s ToonTasks.'
QuestsMaxQuestCarryRewardPoster = 'Reward: Carry %s ToonTasks'
QuestsTeleportReward = 'You now have teleport access to %s.'
QuestsTeleportRewardPoster = 'Reward: Teleport access to %s'
QuestsTrackTrainingReward = 'You can now train for "%s" gags.'
QuestsTrackTrainingRewardPoster = 'Reward: Gag training'
QuestsTrackProgressReward = 'You now have frame %(frameNum)s of the %(trackName)s track animation.'
QuestsTrackProgressRewardPoster = 'Reward: "%(trackName)s" track animation frame %(frameNum)s'
QuestsTrackCompleteReward = 'You may now carry and use "%s" gags.'
QuestsTrackCompleteRewardPoster = 'Reward: Final %s track training'
QuestsClothingTicketReward = 'You can change your clothes'
QuestsClothingTicketRewardPoster = 'Reward: Clothing Ticket'
TIPQuestsClothingTicketReward = 'You can change your shirt for a TIP shirt'
TIPQuestsClothingTicketRewardPoster = 'Reward: TIP Clothing Ticket'
QuestsCheesyEffectRewardPoster = 'Reward: %s'
QuestsCogSuitPartReward = 'You now have a %(cogTrack)s %(part)s Cog Suit Part.'
QuestsCogSuitPartRewardPoster = 'Reward: %(cogTrack)s %(part)s Part'
QuestsEPPReward = 'You now have %s Easy Promotion Papers.'
QuestsEPPRewardPoster = 'Reward: %s Easy Promotion Papers'
QuestsStreetLocationThisPlayground = 'in this playground'
QuestsStreetLocationThisStreet = 'on this street'
QuestsStreetLocationNamedPlayground = 'in the %s playground'
QuestsStreetLocationNamedStreet = 'on %(toStreetName)s in %(toHoodName)s'
QuestsLocationString = '%(string)s%(location)s'
QuestsLocationBuilding = "%s's building is called"
QuestsLocationBuildingVerb = 'which is'
QuestsLocationParagraph = '\x07%(building)s "%(buildingName)s"...\x07...%(buildingVerb)s %(street)s.'
QuestsGenericFinishSCString = 'I need to finish a ToonTask.'
QuestsMediumPouch = 'Medium Pouch'
QuestsLargePouch = 'Large Pouch'
QuestsSmallBag = 'Small Bag'
QuestsMediumBag = 'Medium Bag'
QuestsLargeBag = 'Large Bag'
QuestsSmallBackpack = 'Small Backpack'
QuestsMediumBackpack = 'Medium Backpack'
QuestsLargeBackpack = 'Large Backpack'
QuestsItemDict = {1: ['Pair of Glasses', 'Pairs of Glasses', 'a '],
 2: ['Key', 'Keys', 'a '],
 3: ['Blackboard', 'Blackboards', 'a '],
 4: ['Book', 'Books', 'a '],
 5: ['Candy Bar', 'Candy Bars', 'a '],
 6: ['Piece of Chalk', 'Pieces of Chalk', 'a '],
 7: ['Recipe', 'Recipes', 'a '],
 8: ['Note', 'Notes', 'a '],
 9: ['Adding machine', 'Adding machines', 'an '],
 10: ['Clown car tire', 'Clown car tires', 'a '],
 11: ['Air pump', 'Air pumps', 'an '],
 12: ['Octopus ink', 'Octopus inks', 'some '],
 13: ['Package', 'Package', 'a '],
 14: ['Goldfish receipt', 'Goldfish receipts', 'a '],
 15: ['Goldfish', 'Goldfish', 'a '],
 16: ['Oil', 'Oils', 'some '],
 17: ['Grease', 'Greases', 'some '],
 18: ['Water', 'Waters', 'some '],
 19: ['Gear report', 'Gear reports', 'a '],
 20: ['Blackboard Eraser', 'Blackboard Erasers', 'a '],
 110: ['TIP Clothing Ticket', 'Clothing Tickets', 'a '],
 1000: ['Clothing Ticket', 'Clothing Tickets', 'a '],
 2001: ['Inner Tube', 'Inner Tubes', 'an '],
 2002: ['Monocle Prescription', 'Monocle Prescriptions', 'a '],
 2003: ['Eyeglass Frames', 'Eyeglass Frames', 'some '],
 2004: ['Monocle', 'Monocles', 'a '],
 2005: ['Big White Wig', 'Big White Wigs', 'a '],
 2006: ['Bushel of Ballast', 'Bushels of Ballast', 'a '],
 2007: ['Cog Gear', 'Cog Gears', 'a '],
 2008: ['Sea Chart', 'Sea Charts', 'a '],
 2009: ['Cruddy Clovis', 'Cruddy Clovi', 'a '],
 2010: ['Clean Clovis', 'Clean Clovi', 'a '],
 2011: ['Clock Spring', 'Clock Springs', 'a '],
 2012: ['Counter Weight', 'Counter Weights', 'a '],
 4001: ["Tina's Inventory", "Tina's Inventories", ''],
 4002: ["Yuki's Inventory", "Yuki's Inventories", ''],
 4003: ['Inventory Form', 'Inventory Forms', 'an '],
 4004: ["Fifi's Inventory", "Fifi's Inventories", ''],
 4005: ["Lumber Jack's Ticket", "Lumber Jack's Tickets", ''],
 4006: ["Tabitha's Ticket", "Tabitha's Tickets", ''],
 4007: ["Barry's Ticket", "Barry's Tickets", ''],
 4008: ['Cloudy Castanet', 'Cloudy Castanets', ''],
 4009: ['Blue Squid Ink', 'Blue Squid Ink', 'some '],
 4010: ['Clear Castanet', 'Clear Castanets', 'a '],
 4011: ["Leo's Lyrics", "Leo's Lyrics", ''],
 5001: ['Silk necktie', 'Silk neckties', 'a '],
 5002: ['Pinstripe Suit', 'Pinstripe Suits', 'a '],
 5003: ['Pair of Scissors', 'Pairs of Scissors', 'a '],
 5004: ['Postcard', 'Postcards', 'a '],
 5005: ['Pen', 'Pens', 'a '],
 5006: ['Inkwell', 'Inkwells', 'an '],
 5007: ['Notepad', 'Notepads', 'a '],
 5008: ['Office Lockbox', 'Office Lockboxes', 'an '],
 5009: ['Bag of Bird Seed', 'Bags of Bird Seed', 'a '],
 5010: ['Sprocket', 'Sprockets', 'a '],
 5011: ['Salad', 'Salads', 'a '],
 5012: ['Key to ' + lDaisyGardens, 'Keys to ' + lDaisyGardens, 'a '],
 5013: [lSellbotHQ + ' Blueprints', lSellbotHQ + ' HQ Blueprints', 'some '],
 5014: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 5015: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 5016: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 5017: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 3001: ['Soccer ball', 'Soccer balls', 'a '],
 3002: ['Toboggan', 'Toboggans', 'a '],
 3003: ['Ice cube', 'Ice cubes', 'an '],
 3004: ['Love letter', 'Love letters', 'a '],
 3005: ['Wiener dog', 'Wiener dogs', 'a '],
 3006: ['Engagement ring', 'Engagement rings', 'an '],
 3007: ['Sardine whiskers', 'Sardine whiskers', 'some '],
 3008: ['Calming potion', 'Calming potion', 'a '],
 3009: ['Broken tooth', 'Broken teeth', 'a '],
 3010: ['Gold tooth', 'Gold teeth', 'a '],
 3011: ['Pine cone bread', 'Pine cone breads', 'a '],
 3012: ['Lumpy cheese', 'Lumpy cheeses', 'some '],
 3013: ['Simple spoon', 'Simple spoons', 'a '],
 3014: ['Talking toad', 'Talking toad', 'a '],
 3015: ['Ice cream cone', 'Ice cream cones', 'an '],
 3016: ['Wig powder', 'Wig powders', 'some '],
 3017: ['Rubber ducky', 'Rubber duckies', 'a '],
 3018: ['Fuzzy dice', 'Fuzzy dice', 'some '],
 3019: ['Microphone', 'Microphones', 'a '],
 3020: ['Electric keyboard', 'Electric keyboards', 'an '],
 3021: ['Platform shoes', 'Platform shoes', 'some '],
 3022: ['Caviar', 'Caviar', 'some '],
 3023: ['Make-up powder', 'Make-up powders', 'some '],
 3024: ['Yarn', 'Yarn', 'some '],
 3025: ['Knitting Needle', 'Knitting Needles', 'a '],
 3026: ['Alibi', 'Alibis', 'an '],
 3027: ['External Temperature Sensor', 'External Temperature Sensors', 'an '],
 6001: ['Cashbot HQ Plans', 'Cashbot HQ Plans', 'some '],
 6002: ['Rod', 'Rods', 'a '],
 6003: ['Drive Belt', 'Drive Belts', 'a '],
 6004: ['Pair of Pincers', 'Pairs of Pincers', 'a '],
 6005: ['Reading Lamp', 'Reading Lamps', 'a '],
 6006: ['Zither', 'Zithers', 'a '],
 6007: ['Zamboni', 'Zambonis', 'a '],
 6008: ['Zebra Zabuton', 'Zebra Zabutons', 'a '],
 6009: ['Zinnias', 'Zinnias', 'some '],
 6010: ['Zydeco Records', 'Zydeco Records', 'some '],
 6011: ['Zucchini', 'Zucchinis', 'a '],
 6012: ['Zoot Suit', 'Zoot Suits', 'a '],
 7001: ['Plain Bed', 'Plain Beds', 'a '],
 7002: ['Fancy Bed', 'Fancy Beds', 'a '],
 7003: ['Blue Bedspread', 'Blue Bedspreads', 'a '],
 7004: ['Paisley Bedspread', 'Paisley Bedspreads', 'a '],
 7005: ['Pillows', 'Pillows', 'some '],
 7006: ['Hard Pillows', 'Hard Pillows', 'some '],
 7007: ['Pajamas', 'Pajamas', 'a pair of '],
 7008: ['Footie Pajamas', 'Footie Pajamas', 'a pair of '],
 7009: ['Puce Footie Pajamas', 'Puce Footie Pajamas', 'a pair of '],
 7010: ['Fuchsia Footie Pajamas', 'Fuchsia Footie Pajamas', 'a pair of '],
 7011: ['Cauliflower Coral', 'Cauliflower Coral', 'some '],
 7012: ['Slimy Kelp', 'Slimy Kelp', 'some '],
 7013: ['Pestle', 'Pestles', 'a '],
 7014: ['Jar of Wrinkle Cream', 'Jars of Wrinkle Cream', 'a ']}
QuestsHQOfficerFillin = lHQOfficerM
QuestsHQWhereFillin = ''
QuestsHQBuildingNameFillin = lToonHQ
QuestsHQLocationNameFillin = 'in any neighborhood'
QuestsTailorFillin = 'Tailor'
QuestsTailorWhereFillin = ''
QuestsTailorBuildingNameFillin = 'Clothing Store'
QuestsTailorLocationNameFillin = 'in any neighborhood'
QuestsTailorQuestSCString = 'I need to see a Tailor.'
QuestMovieQuestChoiceCancel = 'Come back later if you need a ToonTask! Bye!'
QuestMovieTrackChoiceCancel = 'Come back when you are ready to decide! Bye!'
QuestMovieQuestChoice = 'Choose a ToonTask.'
QuestMovieTrackChoice = 'Ready to decide? Choose a track, or come back later.'
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
TheBrrrghTrackQuestDict = {GREETING: '',
 QUEST: 'Now you are ready.\x07Go out and walk the earth until you know which track you would like to choose.\x07Choose wisely, because this is your final track.\x07When you are certain, return to me.',
 INCOMPLETE_PROGRESS: 'Choose wisely.',
 INCOMPLETE_WRONG_NPC: 'Choose wisely.',
 COMPLETE: 'Very wise choice!',
 LEAVING: 'Good luck.  Return to me when you have mastered your new skill.'}
QuestDialog_3225 = {QUEST: "Oh, thanks for coming, _avName_!\x07The Cogs in the neighborhood frightened away my delivery person.\x07I don't have anyone to deliver this salad to _toNpcName_!\x07Can you do it for me? Thanks so much!_where_"}
QuestDialog_2910 = {QUEST: 'Back so soon?\x07Great job on the spring.\x07The final item is a counter weight.\x07Stop by and see _toNpcName_ and bring back whatever you can get._where_'}
QuestDialogDict = {
 120: {QUEST: "Nice job playing D&D!\x07Say, you know, there is this guy named Banker Bob?\x07You see, he hates D&D.\x07Why don't you go and teach him how to play D&D._where_"},
 121: {QUEST: "Hi.\x07No, no, D&D STINKS!\x07The Cogs stole my key, UGH! Fight a Cog and get my key.\x07WHAT ARE YOU STANDING THERE FOR!? GET MY KEY YOU NOOB!"},
 130: {QUEST: 'Nice job! I am glad you rode the trolley.\x07Hey, say, there is this guy named Moonlight Mimi.\x07She has a school that you can learn some stuff on.\x07Go to her to learn some stuff._where_'},
 131: {QUEST: "Hi, welcome to Moonlight Mimi's Highschool!\x07Wait, what?\x07Where is my blackboard??? I swear to Toon, I bet a Cog stole it.\x07No, don't talk to me, get my blackboard and get it right! >:("},
 140: {QUEST: "Good job finding the trolley!\x07By the way, I have a Librarian Friend, and well, let's just say, he hates Cookies.\x07I picked this book that was about cookies, and wanted to troll him lol.\x07Could you take it over to him? Thanks._where_"},
 141: {QUEST: "Hi there! This is a library!\x07Hey what's this? A book?\x07Ooo, let's see what it is!\x07(Notices that it's a book about cookies)...\x07A BOOK ABOUT COOKIES!? I SAID WE HAVE NO COOKIES! ONLY BOOKS! JUST BOOKS, NO COOKIES!\x07For your punishment, go fight a Cog."},
 142: {QUEST: "Thank you! I have a feeling you will be a great help to everyone around here.\x07By the way, I just received a message from Toon HQ.\x07They forgot to mention a few important concepts. You're needed there!"},
 160: {GREETING: '',
       QUEST: "Ok, now I think you are ready for something more rewarding.\x07If you can defeat 3 Bossbots I'll give you a little bonus.",
       INCOMPLETE_PROGRESS: TheCogs + ' are out in the streets, through the tunnels.',
       INCOMPLETE_WRONG_NPC: 'Good job defeating those Cogs. Now go to the Toon Headquarters for your next step!',
       COMPLETE: QuestsDefaultComplete,
       LEAVING: QuestsDefaultLeaving},
 161: {GREETING: '',
       QUEST: "Ok, now I think you are ready for something more rewarding.\x07Come back after you defeat 3 Lawbots and I'll have a little something for you.",
       INCOMPLETE_PROGRESS: TheCogs + ' are out in the streets, through the tunnels.',
       INCOMPLETE_WRONG_NPC: 'Good job defeating those Cogs. Now go to the Toon Headquarters for your next step!',
       COMPLETE: QuestsDefaultComplete,
       LEAVING: QuestsDefaultLeaving},
 162: {GREETING: '',
       QUEST: 'Ok, now I think you are ready for something more rewarding.\x07Defeat 3 Cashbots and come back here to claim the bounty.',
       INCOMPLETE_PROGRESS: TheCogs + ' are out in the streets, through the tunnels.',
       INCOMPLETE_WRONG_NPC: 'Good job defeating those Cogs. Now go to the Toon Headquarters for your next step!',
       COMPLETE: QuestsDefaultComplete,
       LEAVING: QuestsDefaultLeaving},
 163: {GREETING: '',
       QUEST: "Ok, now I think you are ready for something more rewarding.\x07Come see us after you defeat 3 Sellbots and we'll hook you up.",
       INCOMPLETE_PROGRESS: TheCogs + ' are out in the streets, through the tunnels.',
       INCOMPLETE_WRONG_NPC: 'Thank you for fighting the Cogs, now for the next step.',
       COMPLETE: QuestsDefaultComplete,
       LEAVING: QuestsDefaultLeaving},
 164: {QUEST: "Hi there, do you want to level up your new gags!?\x07It's easy, just visit %s, and maybe he can help you out._where_" % Flippy},
 165: {QUEST: 'Welcome!\x07Hm, it looks like you could use some gag training.\x07Ah yes, my Master used to tell me, the more gags you use, the more xp you get.\x07After a certain amount by the level, you get a new gag!\x07Now how do you do it? Just go and fight 2 simple cogs for now.'},
 166: {QUEST: 'Yay! You destroyed them!\x07Oh, that reminds me, Cogs come in 4 types, such as...\x07Fashionbots, Carebots, Defenderbots, and Jurybots.\x07You can tell if you read their labels. NOT THE CAN LABELS! It is a cog tag, not a label you noob!\x07Go fight 2 Jurybots.'},
 167: {QUEST: 'Yay! You destroyed them!\x07Oh, that reminds me, Cogs come in 4 types, such as...\x07Fashionbots, Carebots, Defenderbots, and Jurybots.\x07You can tell if you read their labels. NOT THE CAN LABELS! It is a cog tag, not a label you noob!\x07Go fight 2 Defenderbots'},
 168: {QUEST: 'Yay! You destroyed them!\x07Oh, that reminds me, Cogs come in 4 types, such as...\x07Fashionbots, Carebots, Defenderbots, and Jurybots.\x07You can tell if you read their labels. NOT THE CAN LABELS! It is a cog tag, not a label you noob!\x07Go fight 2 Fashionbots.'},
 169: {QUEST: 'Yay! You destroyed them!\x07Oh, that reminds me, Cogs come in 4 types, such as...\x07Fashionbots, Carebots, Defenderbots, and Jurybots.\x07You can tell if you read their labels. NOT THE CAN LABELS! It is a cog tag, not a label you noob!\x07Go fight 2 Carebots.'},
 170: {QUEST: 'Horray! They are gone! Yay!\x07I think you are ready to start training for your third gag track.\x07Go talk to _toNpcName_ to choose your next gag track - he can give you some expert advice._where_'},
 171: {QUEST: 'Horray! They are gone! Yay!\x07I think you are ready to start training for your third gag track.\x07Go talk to _toNpcName_ to choose your next gag track - he can give you some expert advice._where_'},
 172: {QUEST: 'Horray! They are gone! Yay!\x07I think you are ready to start training for your third gag track.\x07Go talk to _toNpcName_ to choose your next gag track - she can give you some expert advice._where_'},
 175: {GREETING: '',
       QUEST: "Did you know you have your very own Toon house?\x07Clarabelle Cow runs a phone catalog where you can order furniture to decorate your house.\x07You can also buy SpeedChat phrases, clothing, and other fun things!\x07I'll tell Clarabelle to send you your first catalog now.\x07You get a catalog with new items every week!\x07Go to your home and use your phone to call Clarabelle.",
       INCOMPLETE_PROGRESS: 'Go home and use your phone to call Clarabelle.',
       COMPLETE: 'Hope you have fun ordering things from Clarabelle!\x07I just finished redecorating my house. It looks Toontastic!\x07Keep doing ToonTasks to get more rewards!',
       LEAVING: QuestsDefaultLeaving},
 400: {GREETING: '',
       QUEST: "Throw and Squirt are great, but it won't be enough to last the game.\x07When you use gags with other Toons, you can create a massive amount of damage combos.\x07You may choose different gags of your choice, however you may have 6 out of 7, so choose wisely.\x07For your next track, choose between Sound and Toonup.\x07Sound is loud, weak alone, but can do a ton of damage if you make combos. And it hits all Cogs.\x07Toonup allows you to heal others, but yourself in battle.\x07I hope you're ready, so get ready to choose!",
       INCOMPLETE_PROGRESS: 'Back so soon?  Okay, are you ready to choose?',
       INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
       COMPLETE: 'Good decision.  Now you may start training for those tracks.\x07You need to complete 15 tasks in order to get the gag track.\x07Each task will give you a single frame of your gag attack animation.\x07After the 15 training points, you will have access to the final task.\x07Goodluck training! ^^',
       LEAVING: QuestsDefaultLeaving},
 1039: {QUEST: 'Visit _toNpcName_ if you want to get around town more easily._where_'},
 1040: {QUEST: 'Visit _toNpcName_ if you want to get around town more easily._where_'},
 1041: {QUEST: 'Hi!  What brings you here?\x07Everybody uses their portable hole to travel around Toontown.\x07Why, you can teleport to your friends using the Friends List, or to any neighborhood using the map in the Shticker Book.\x07Of course, you have to earn that!\x07Say, I can turn on your teleport access to ' + lToontownCentral + ' if you help out a friend of mine.\x07Seems the Cogs are causing trouble over on Loopy Lane.  Go visit _toNpcName_._where_'},
 1042: {QUEST: 'Hi!  What brings you here?\x07Everybody uses their portable hole to travel around Toontown.\x07Why, you can teleport to your friends using the Friends List, or to any neighborhood using the map in the Shticker Book.\x07Of course, you have to earn that!\x07Say, I can turn on your teleport access to ' + lToontownCentral + ' if you help out a friend of mine.\x07Seems the Cogs are causing trouble over on Loopy Lane.  Go visit _toNpcName_._where_'},
 1043: {QUEST: 'Hi!  What brings you here?\x07Everybody uses their portable hole to travel around Toontown.\x07Why, you can teleport to your friends using the Friends List, or to any neighborhood using the map in the Shticker Book.\x07Of course, you have to earn that!\x07Say, I can turn on your teleport access to ' + lToontownCentral + ' if you help out a friend of mine.\x07Seems the Cogs are causing trouble over on Loopy Lane.  Go visit _toNpcName_._where_'},
 1044: {QUEST: "Huh!? Who goes there???  Hi, I'm sorry, but I need your help.\x07Look at my place, I have no customers.\x07I had a secret recipe, but that COG DRAWN BARNACLE Plankton stole it!\x07I had it, but, it's gone...\x07There should be a samples of the recipe, please find them. Just fight Cogs.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'AHH! Oh, where is my recipe?'},
 1045: {QUEST: "Thank you so much!\x07Oh? What's this?\x07(checks my pockets)\x07Oh, it turns out the recipe was in my pocket the whole time! Arghghghghghgh!\x07Go to Toon HQ, cya!",
        LEAVING: '',
        COMPLETE: "Hi, so you're the guy who can fight huh?\x07It says you need teleport access.\x07Oh yeah, well, I can help.\x07Now you can just teleport to the playground! If you want to of course.\x07Just open your stinking map, and click TTC. ' + lToontownCentral + '."},
 1046: {QUEST: 'No, no, no! Not this!\x07THERE is still a problem! Please go to Tickles place._where_'},
 1047: {QUEST: 'UGH! I hate theives!\x07Please recover a couple of them from the Carebots.\x07But for more torture, well, idk just fight them.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Still looking for adding machines?'},
 1048: {QUEST: 'Wow!  Thanks for finding our adding machines.\x07Ugh, of course, piece of junk is damaged.\x07Say, could you take them over to _toNpcName_ over at her shop, "Tickle Machines" on this street?\x07See if she can fix them.',
        LEAVING: ''},
 1049: {QUEST: "What's that?  Broken adding machines?\x07Ugh, they look like a piece of junk.\x07Well, let's have a look see...\x07Yep, it looks like scrap, stall, slow, stickshift, waste gas, rattle, bounces, piece of junk.\x07When you think big, you gotta fight big.\x07-Does stupidity math-.  Ah ha, a couple large cogs should do it!\x07Bring them back all at once and I'll fix em up!",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Remember, I need 10 gears to fix the machines.'},
 1053: {QUEST: "Ah yes, that should do the trick indeedy.\x07All fixed now, free of charge.\x07Take these back to Funny Money, and tell 'im I said howdy.",
        LEAVING: '',
        COMPLETE: "Adding machines all fixed up?\x07Nice work.  I'm sure I've got something around here to reward you with..."},
 1054: {QUEST: '_toNpcName_ needs some help with his clown cars._where_'},
 1055: {QUEST: "Yowza!  I can't find the tires to this here clown car anywhere!\x07Do ya think you could help me out?\x07I think Loopy Bob may have tossed them in the pond in the " + lToontownCentral + ' playground.\x07If you stand on one of the docks there you can try and fish out the tires for me.',
        GREETING: 'Woohoo!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Are you having trouble fishing out all 4 tires?'},
 1056: {QUEST: 'Fan-flying-tastic!  Now I can get this old clown car on the road again!\x07Hey, I thought I had an air pump around here to inflate these tires...\x07Maybe _toNpcName_ borrowed it?\x07Could you go ask for it back for me?_where_',
        LEAVING: ''},
 1057: {QUEST: "Hi there.\x07A tire pump you say?\x07I'll tell you what - you help clean up the streets of some of those high level Cogs for me...\x07And I'll let you have the tire pump.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Is that the best you can do?'},
 1058: {QUEST: "Good job - I knew you could do it.\x07Here's the pump.  I'm sure _toNpcName_ will be glad to get it back.",
        LEAVING: '',
        GREETING: '',
        COMPLETE: "Yeehaw!  Now I'm good to go!\x07By the way, thanks for helping me out.\x07Here, take this."},
 1059: {QUEST: '_toNpcName_ is running low on supplies.  Maybe you can give him a hand?_where_'},
 1060: {QUEST: "Thanks for stopping by!\x07Those Cogs have been stealing my ink, so I'm running very low.\x07Could you fish some octopus ink out of the pond for me?\x07Just stand on a dock near the pond to fish.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Are you having trouble fishing?'},
 1061: {QUEST: "Great - thanks for the ink!\x07You know what, maybe if you cleared away some of those Pencil Pushers...\x07I wouldn't run out of ink again so quickly.\x07Defeat 6 Pencil Pushers in " + lToontownCentral + ' for your reward.',
        LEAVING: '',
        COMPLETE: 'Thanks!  Let me reward you for your help.',
        INCOMPLETE_PROGRESS: 'I just saw some more Pencil Pushers.'},
 1062: {QUEST: "Great - thanks for the ink!\x07You know what, maybe if you cleared away some of those Bloodsuckers...\x07I wouldn't run out of ink again so quickly.\x07Defeat 6 Bloodsuckers in " + lToontownCentral + ' for your reward.',
        LEAVING: '',
        COMPLETE: 'Thanks!  Let me reward you for your help.',
        INCOMPLETE_PROGRESS: 'I just saw some more Bloodsuckers.'},
 900: {QUEST: 'I hear _toNpcName_ needs help with a package._where_'},
 1063: {QUEST: 'Hi - thanks for coming in.\x07A Cog stole a very important package from right under my nose.\x07Please see if you can get it back.  I think he was a level 3...\x07So, defeat level 3 Cogs until you find my package.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding the package, huh?'},
 1067: {QUEST: "That's it, all right!\x07Hey, the address is smudged...\x07All I can read is that it's for a Dr. - the rest is all blurry.\x07Maybe it's for _toNpcName_?  Could you take it to him?_where_",
        LEAVING: ''},
 1068: {QUEST: "I wasn't expecting a package.  Maybe it's for Dr. I.M. Euphoric?\x07My assistant was going over there today anyway, so I'll have him check for you.\x07In the meantime, would you mind getting rid of some of the Cogs on my street?\x07Defeat 10 Cogs in " + lToontownCentral + '.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "My assistant isn't back yet."},
 1069: {QUEST: "Dr. Euphoric says he wasn't expecting a package either.\x07Unfortunately, a Cashbot stole it from my assistant on the way back.\x07Could you try and get it back?",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding the package, huh?'},
 1070: {QUEST: "Dr. Euphoric says he wasn't expecting a package either.\x07Unfortunately, a Sellbot stole the package from my assistant on the way back.\x07I'm sorry, but you'll have to find that Sellbot and get it back.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding the package, huh?'},
 1071: {QUEST: "Dr. Euphoric says he wasn't expecting a package either.\x07Unfortunately, a Bossbot stole it from my assistant on the way back.\x07Could you try and get it back?",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding the package, huh?'},
 1072: {QUEST: 'Great - you got it back!\x07Maybe you should try _toNpcName_, it could be for him._where_',
        LEAVING: ''},
 1073: {QUEST: 'Oh, thanks for bringing me my packages.\x07Wait a second, I was expecting two.  Could you check with _toNpcName_ and see if he has the other one?',
        INCOMPLETE: 'Were you able to find my other package?',
        LEAVING: ''},
 1074: {QUEST: 'He said there was another package?  Maybe the Cogs stole it too.\x07Defeat Cogs until you find the second package.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding the other package, huh?'},
 1075: {QUEST: 'I guess there was a second package after all!\x07Hurry and take it over to _toNpcName_ with my apologies.',
        COMPLETE: 'Hey, my package is here!\x07Since you seem to be such a helpful Toon, this should come in handy.',
        LEAVING: ''},
 1076: {QUEST: "There's been some trouble over at 14 Karat Goldfish.\x07_toNpcName_ could probably use a hand._where_"},
 1077: {QUEST: "Thanks for coming - the Cogs stole all my goldfish.\x07I think the Cogs want to sell them to make a quick buck.\x07Those 5 fish have been my only companions in this tiny store for so many years...\x07If you could get them back for me I'd really appreciate it.\x07I'm sure one of the Cogs has my fish.\x07Defeat Cogs until you find my goldfish.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Please return my goldfish to me.'},
 1078: {QUEST: "Oh, you have my fish!\x07Huh?  What's this - a receipt?\x07Sigh, I guess they are Cogs, after all.\x07I can't make heads or tails out of this receipt.  Could you take it to _toNpcName_ and see if he can read it?_where_",
        INCOMPLETE: 'What did _toNpcName_ have to say about the receipt?',
        LEAVING: ''},
 1079: {QUEST: "Mmm, let me see that receipt.\x07...Ah Yes, it says that 1 goldfish was sold to a Flunky.\x07It doesn't seem to mention what happened to the other 4 fish.\x07Maybe you should try and find that Flunky.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I don't think there's anything else I can help you with.\x07Why don't you try and find that goldfish?"},
 1092: {QUEST: "Mmm, let me see that receipt.\x07...Ah Yes, it says that 1 goldfish was sold to a Short Change.\x07It doesn't seem to mention what happened to the other 4 fish.\x07Maybe you should try and find that Short Change.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I don't think there's anything else I can help you with.\x07Why don't you try and find that goldfish?"},
 1080: {QUEST: "Oh thank heavens!  You found Oscar - he's my favorite.\x07What's that, Oscar?  Uh huh... they did? ... they are?\x07Oscar says the other 4 escaped into the pond in the playground.\x07Could you go round them up for me?\x07Just fish them out of the pond.",
        LEAVING: '',
        COMPLETE: 'Ahh, I am sooo happy!  To be reunited with my little buddies!\x07You deserve a handsome reward for this!',
        INCOMPLETE_PROGRESS: 'Are you having trouble finding those fish?'},
 1081: {QUEST: '_toNpcName_ appears to be in a sticky situation. He sure could use a hand._where_'},
 1082: {QUEST: "I spilled quick dry glue and I'm stuck - stuck cold!\x07If there were a way out, I sure would be sold.\x07That gives me an idea, if you are feeling loyal.\x07Defeat some Sellbots and bring back some oil.",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: 'Can you help me get un-stuck?'},
 1083: {QUEST: "Well, oil helped a little, but I still cannot budge,\x07What else would help?  It's hard to judge.\x07That gives me an idea; it's worth a try at least.\x07Defeat some Lawbots and bring back some grease.",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: 'Can you help me get un-stuck?'},
 1084: {QUEST: "Nope, that didn't help.  This is really not funny.\x07I put the grease right there on the money,\x07That gives me an idea, before I forget it.\x07Defeat some Cashbots; bring back water to wet it.",
        LEAVING: '',
        GREETING: '',
        COMPLETE: "Hooray, I'm free of this quick drying glue,\x07As a reward I give this gift to you,\x07You can laugh a little longer while battling and then...\x07Oh, no!  I'm already stuck here again!",
        INCOMPLETE_PROGRESS: 'Can you help me get un-stuck?'},
 1085: {QUEST: '_toNpcName_ is conducting some research on the Cogs.\x07Go talk to him if you want to help out._where_'},
 1086: {QUEST: "That's right, I'm conducting a study of the Cogs.\x07I want to know what makes them tick.\x07It sure would help me if you could gather some gears from Cogs.\x07Make sure they're from at least level 2 Cogs so they're big enough to examine.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Can't find enough gears?"},
 1089: {QUEST: "Okay, let's take a look.  These are excellent specimens!\x07Mmmm...\x07Okay, here's my report.  Take this back to Toon Headquarters right away.",
        INCOMPLETE: 'Have you delivered my report to Headquarters?',
        COMPLETE: "Good work _avName_, we'll take this one from here.",
        LEAVING: ''},
 1090: {QUEST: '_toNpcName_ has some useful information for you._where_'},
 1091: {QUEST: 'I hear that Toon Headquarters is working on a sort of Cog Radar.\x07It will let you see where the Cogs are so that it will be easier to find them.\x07That Cog Page in your Shticker Book is the key.\x07By defeating enough Cogs, you can tune in to their signals and actually track where they are.\x07Keep defeating Cogs, so you will be ready.',
        COMPLETE: 'Good work!  You could probably use this...',
        LEAVING: ''},
 401: {GREETING: '',
       QUEST: 'Now you get to choose the next gag track you want to learn.\x07Take your time deciding, and come back here when you are ready to choose.',
       INCOMPLETE_PROGRESS: 'Think about your decision before choosing.',
       INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
       COMPLETE: 'A wise decision...',
       LEAVING: QuestsDefaultLeaving},
 2201: {QUEST: 'Those sneaky Cogs are at it again.\x07_toNpcName_ has reported another missing item. Stop by and see if you can straighten it out._where_'},
 2202: {QUEST: "Hi, _avName_. Thank goodness you're here. A mean looking Penny Pincher was just in here and he made off with an inner tube.\x07I fear they may use it for their vile purposes.\x07Please see if you can find him and bring it back.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my inner tube?',
        COMPLETE: 'You found my inner tube! You ARE good. Here, take your reward...'},
 2203: {QUEST: TheCogs + ' are wreaking havoc over at the bank.\x07Go see Captain Carl and see what you can do._where_'},
 2204: {QUEST: "Welcome aboard, matey.\x07Argh! Those rapscallion Cogs smashed my monocle and I can't sort me change without it.\x07Be a good landlubber and take this prescription to _toNpcName_ and fetch me a new one._where_",
        GREETING: '',
        LEAVING: ''},
 2205: {QUEST: "What's this?\x07Oh, I'd love to fill this prescription but the Cogs have been pilfering my supplies.\x07If you can get me the eyeglass frames off a flunky I can probably help you out.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Sorry. No flunky frames, no monocle.'},
 2206: {QUEST: 'Excellent!\x07Just a second...\x07Your prescription is filled. Please take this monocle straight to Captain Carl._where_',
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Avast Ye!\x07You're gonna earn your sea legs after all.\x07Here ye be."},
 2207: {QUEST: "Barnacle Barbara has a Cog in her shop!\x07You'd better get over there pronto._where_"},
 2208: {QUEST: "Gosh! You just missed him, sweetie.\x07There was a Back Stabber in here. He took my big white wig.\x07He said it was for his boss and something about 'legal precedent.'\x07If you can get it back I'd be forever grateful.",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: "Still haven't found him?\x07He's tall and has a pointy head",
        COMPLETE: "You found it!?!?\x07Aren't you a darling!\x07You've more than earned this..."},
 2209: {QUEST: 'Melville is preparing for an important voyage.\x07Pop in and see what you can do to help sort him out._where_'},
 2210: {QUEST: "I can use your help.\x07I've been asked by Toon HQ to take a voyage and see if I can find where the Cogs are coming from.\x07I'll need a few things for my ship but I don't have many Jellybeans.\x07Stop by and pick up some ballast from Alice. You'll have to do a favor for her to get it._where_",
        GREETING: 'Howdy, _avName_!',
        LEAVING: ''},
 2211: {QUEST: "So Melville wants ballast, does he?\x07He still owes me for the last bushel.\x07I'll give it to you if you can clear five Micromanagers off my street.",
        INCOMPLETE_PROGRESS: 'No, silly! I said FIVE micromanagers...',
        GREETING: 'What can I do for you?',
        LEAVING: ''},
 2212: {QUEST: "A deal's a deal.\x07Here's your ballast for that cheapskate Melville._where_",
        GREETING: 'Well, look what the cat dragged in...',
        LEAVING: ''},
 2213: {QUEST: "Excellent work. I knew she'd be reasonable.\x07Next I'll need a sailing chart from Art.\x07I don't think my credit is good there either so you'll have to work something out with him._where_",
        GREETING: '',
        LEAVING: ''},
 2214: {QUEST: "Yes, I have the sea chart Melville wants.\x07And if you're willing to work for it I'll let you have it.\x07I'm trying to build an astrolabe to navigate by the stars.\x07I could use three Cog gears to build it.\x07Come back when you've found them.",
        INCOMPLETE_PROGRESS: "How's it coming with those Cog gears?",
        GREETING: 'Welcome!',
        LEAVING: 'Good luck!'},
 2215: {QUEST: "Ooh! These gears will do rather nicely.\x07Here's the chart. Give it to Melville with my compliments._where_",
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Well, that just about does it. I'm ready to sail!\x07I'd take you with me if you weren't so green. Take this instead."},
 901: {QUEST: "If you're up for it Ahab could use some assistance over at his place..._where_"},
 2902: {QUEST: "Are you the new recruit?\x07Good, good. Maybe you can help me.\x07I'm building a giant prefab crab to confuse the Cogs.\x07I could use a clovis though. Go see Claggart and bring one back, please._where_"},
 2903: {QUEST: "Hi there!\x07Yes, I heard about the giant crab Ahab's working on.\x07The best clovis I have is a little on the dirty side though.\x07Be a sport and run it by the cleaners for me before you drop it off._where_",
        LEAVING: 'Thanks!'},
 2904: {QUEST: 'You must be the one that Claggart sent over.\x07I think I can clean that up in short order.\x07Just a minute...\x07There you are. Good as new!\x07Tell Ahab I said hello._where_'},
 2905: {QUEST: "Ah, now this is exactly what I was looking for.\x07While you're here, I'm also going to need a very large clock spring.\x07Take a walk over to Hook's place and see if he has one._where_"},
 2906: {QUEST: "A large spring, eh?\x07I'm sorry but the largest spring I have is still quite small.\x07Perhaps I could assemble one out of squirt gun trigger springs.\x07Bring me three of these gags and I'll see what I can do."},
 2907: {QUEST: "Let's have a look then...\x07Smashing. Simply Smashing.\x07Sometimes I even surprise myself.\x07Here you go: one large spring for Ahab!_where_",
        LEAVING: 'Bon Voyage!'},
 2911: {QUEST: "I'd be happy to help the cause, _avName_.\x07But I'm afraid the streets are no longer safe.\x07Why don't you go take out some Cashbot Cogs and we'll talk.",
        INCOMPLETE_PROGRESS: 'I still think you need to make the streets safer.'},
 2916: {QUEST: 'Yes, I have a weight that Ahab can have.\x07I think it would be safer if you defeated a couple sellbots first though.',
        INCOMPLETE_PROGRESS: 'Not yet. Defeat some more sellbots.'},
 2921: {QUEST: "Hmmm, I suppose I could give up a weight.\x07I'd feel a lot better about it if there weren't so many Bossbot Cogs creeping around.\x07Defeat six and then come see me.",
        INCOMPLETE_PROGRESS: "I don't think its safe yet..."},
 2925: {QUEST: "All done?\x07Well, I guess it's safe enough now.\x07Here's the counter weight for Ahab._where_"},
 2926: {QUEST: "Well, that's everything.\x07Let's see if it works.\x07Hmmm, one small problem.\x07I'm not getting any power because that Cog building is blocking my solar panel.\x07Could you retake it for me?",
        INCOMPLETE_PROGRESS: 'Still no power. How about that building?',
        COMPLETE: 'Super! You are one heck of a Cog crusher! Here, take this as your reward...'},
 3200: {QUEST: "I just got a call in from _toNpcName_.\x07He's having a hard day. Maybe you can help him out!\x07Drop by and see what he needs._where_"},
 3201: {QUEST: 'Oh, thanks for coming!\x07I need someone to take this new silk tie to _toNpcName_.\x07Would you be able to do that for me?_where_'},
 3203: {QUEST: 'Oh, this must be the tie I ordered! Thanks!\x07It matches a pinstripe suit I just finished, right over here.\x07Hey, what happened to that suit?\x07Oh no! The Cogs must have stolen my new suit!\x07Defeat Cogs until you find my suit, and bring it back to me.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Have you found my suit yet? I'm sure the Cogs took it!",
        COMPLETE: 'Hooray! You found my new suit!\x07See, I told you the Cogs had it! Here is your reward...'},
 3204: {QUEST: "_toNpcName_ just called to report a theft.\x07Why don't you stop by and see if you can sort things out?_where_"},
 3205: {QUEST: "Hello, _avName_! Have you come to help me?\x07I just chased a Bloodsucker out of my shop. Whew! That was scary.\x07But now I can't find my scissors anywhere! I'm sure that Bloodsucker took them.\x07Find that Bloodsucker, and recover my scissors for me.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Are you still looking for my scissors?',
        COMPLETE: 'My scissors! Thank you so much! Here is your reward...'},
 3206: {QUEST: 'It sounds like _toNpcName_ is having problems with some Cogs.\x07Go see if you can help him out._where_'},
 3207: {QUEST: 'Hi, _avName_! Thanks for coming by!\x07A bunch of Double Talkers just broke in and stole a stack of postcards from my counter.\x07Please go out and defeat all those Double Talkers to get my postcards back!',
        INCOMPLETE_PROGRESS: "That's not enough postcards! Keep looking!",
        COMPLETE: 'Oh, thank you! Now I can deliver the mail on time! Here is your reward...'},
 3208: {QUEST: "We've been getting complaints from the residents lately about all of the Cold Callers.\x07See if you can defeat 10 Cold Callers to help out your fellow Toons in " + lDaisyGardens + '.'},
 3209: {QUEST: 'Thanks for taking care of those Cold Callers!\x07But now the Telemarketers have gotten out of hand.\x07Defeat 10 Telemarketers in ' + lDaisyGardens + ' and come back here for your reward.'},
 3247: {QUEST: "We've been getting complaints from the residents lately about all of the Bloodsuckers.\x07See if you can defeat 20 Bloodsuckers to help out your fellow Toons in " + lDaisyGardens + '.'},
 3210: {QUEST: 'Oh no, The Squirting Flower on Maple Street just ran out of flowers!\x07Take them ten of your own squirting flowers to help out.\x07Make sure you have 10 squirting flowers in your inventory first.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I need to have 10 squirting flowers. You don't have enough!"},
 3211: {QUEST: "Oh, thank you so much! Those squirting flowers will save the day.\x07But I'm scared of the Cogs outside.\x07Can you help me out and defeat some of those Cogs?\x07Come back to me after you have defeated 20 Cogs on this street.",
        INCOMPLETE_PROGRESS: 'There are still Cogs out there to defeat!  Keep it up!',
        COMPLETE: 'Oh, thank you! That helps a lot. Your reward is...'},
 3212: {QUEST: '_toNpcName_ needs some help looking for something she lost.\x07Go visit her and see what you can do._where_'},
 3213: {QUEST: 'Hi, _avName_. Can you help me?\x07I seem to have misplaced my pen. I think maybe some Cogs took it.\x07Defeat Cogs to find my stolen pen.',
        INCOMPLETE_PROGRESS: 'Have you found my pen yet?'},
 3214: {QUEST: "Yes, that's my pen! Thanks so much!\x07But while you were gone I realized my inkwell was missing too.\x07Defeat Cogs to find my inkwell.",
        INCOMPLETE_PROGRESS: "I'm still looking for my inkwell!"},
 3215: {QUEST: "Great! Now I have my pen and my inkwell back!\x07But wouldn't you know it?\x07My notepad is gone! They must have stolen it too!\x07Defeat Cogs to find my stolen notepad, and then bring it back for your reward.",
        INCOMPLETE_PROGRESS: 'Any word on that notepad yet?'},
 3216: {QUEST: "That's my notepad! Hooray! Your reward is...\x07Hey! Where did it go?\x07I had your reward right here in my office lockbox. But the whole lockbox is gone!\x07Can you believe it? Those Cogs stole your reward!\x07Defeat Cogs to recover my lockbox.\x07When you bring it back to me I'll give you your reward.",
        INCOMPLETE_PROGRESS: 'Keep looking for that lockbox!  It has your reward inside it!',
        COMPLETE: 'Finally! I had your new gag bag in that lockbox. Here it is...'},
 3217: {QUEST: "We've been performing some studies on Sellbot mechanics.\x07We still need to study some pieces more closely.\x07Bring us a sprocket from a Name Dropper.\x07You can catch one when the Cog is exploding."},
 3218: {QUEST: 'Good job! Now we need a sprocket from a Glad Hander for comparison.\x07These sprockets are harder to catch, so keep trying.'},
 3219: {QUEST: 'Great! Now we need just one more sprocket.\x07This time, we need a sprocket from a Mover & Shaker.\x07You might need to look inside some Sellbot buildings to find these Cogs.\x07When you catch one, bring it back for your reward.'},
 3244: {QUEST: "We've been performing some studies on Lawbot mechanics.\x07We still need to study some pieces more closely.\x07Bring us a sprocket from an Ambulance Chaser.\x07You can catch one when the Cog is exploding."},
 3245: {QUEST: 'Good job! Now we need a sprocket from a Back Stabber for comparison.\x07These sprockets are harder to catch, so keep trying.'},
 3246: {QUEST: 'Great! Now we need just one more sprocket.\x07This time, we need a sprocket from a Spin Doctor.\x07When you catch one, bring it back for your reward.'},
 3220: {QUEST: "I just heard that _toNpcName_ was asking around for you.\x07Why don't you drop by and see what she wants?_where_"},
 3221: {QUEST: 'Hi, _avName_! There you are!\x07I heard you were quite an expert in squirt attacks.\x07I need someone to set a good example for all the Toons in ' + lDaisyGardens + '.\x07Use your squirt attacks to defeat a bunch of Cogs.\x07Encourage your friends to use squirt too.\x07When you have defeated 20 Cogs, come back here for a reward!'},
 3222: {QUEST: "It's time to demonstrate your Toonmanship.\x07If you successfully reclaim a number of Cog buildings, you'll earn the right to carry three quests.\x07First, defeat any two Cog buildings.\x07Feel free to call on your friends to help you out."},
 3223: {QUEST: 'Great job on those buildings!\x07Now, defeat two more buildings.\x07These buildings must be at least two stories high, or higher.'},
 3224: {QUEST: 'Fantastic!\x07Now just defeat two more buildings.\x07These buildings must be at least three stories high.\x07When you finish, come back for your reward!',
        COMPLETE: 'You did it, _avName_!\x07You demonstrated your superior Toonmanship.',
        GREETING: ''},
 3225: {QUEST: "_toNpcName_ says she needs some help.\x07Why don't you go see what you can do to help out?_where_"},
 3235: {QUEST: "Oh, this is the salad I ordered!\x07Thank you for bringing it to me.\x07All those Cogs must have frightened away _toNpcName_'s regular delivery person again.\x07Why don't you do us a favor and defeat some of the Cogs out there?\x07Defeat 10 Cogs in " + lDaisyGardens + ' and then report back to _toNpcName_.',
        INCOMPLETE_PROGRESS: "You're working on defeating Cogs for me?\x07That's wonderful! Keep up the good work!",
        COMPLETE: 'Oh, thank you so much for defeating those Cogs!\x07Now maybe I can keep my regular delivery schedule.\x07Your reward is...',
        INCOMPLETE_WRONG_NPC: "Go tell _toNpcName_ about the Cogs you've defeated._where_"},
 3236: {QUEST: 'There are far too many Lawbots out there.\x07You can do your part to help!\x07Defeat 3 Lawbot buildings.'},
 3237: {QUEST: 'Great job on those Lawbot buildings!\x07But now there are too many Sellbots!\x07Defeat 3 Sellbot buildings, then come back for your reward.'},
 3238: {QUEST: 'Oh no! A "Mingler" Cog has stolen the Key to ' + lDaisyGardens + '!\x07See if you can recover it.\x07Remember, The Mingler can be found only inside Sellbot buildings.'},
 3239: {QUEST: "You found a key all right, but it isn't the right one!\x07We need the Key to " + lDaisyGardens + '.\x07Keep looking! A "Mingler" Cog still has it!'},
 3242: {QUEST: 'Oh no! A Legal Eagle Cog has stolen the Key to ' + lDaisyGardens + '!\x07See if you can recover it.\x07Remember, Legal Eagles can be found only inside Lawbot buildings.'},
 3243: {QUEST: "You found a key all right, but it isn't the right one!\x07We need the Key to " + lDaisyGardens + '.\x07Keep looking! A Legal Eagle Cog still has it!'},
 3240: {QUEST: "I've just heard from _toNpcName_ that a Legal Eagle stole a bag of his bird seed.\x07Defeat Legal Eagles until you recover Bud's bird seed, and take it to him.\x07Legal Eagles are only found inside Lawbot buildings._where_",
        COMPLETE: 'Oh, thank you so much for finding my bird seed!\x07Your reward is...',
        INCOMPLETE_WRONG_NPC: 'Good job getting that bird seed back!\x07Now take it to _toNpcName_._where_'},
 3241: {QUEST: 'Some of the Cog buildings out there are getting too tall for our comfort.\x07See if you can bring down some of the tallest buildings.\x07Rescue 5 3-story buildings or taller and come back for your reward.'},
 3250: {QUEST: 'Detective Lima over on Oak Street has heard some reports of a Sellbot Headquarters.\x07Head over there and help her investigate.'},
 3251: {QUEST: "There is something strange going on around here.\x07There are so many Sellbots!\x07I've heard they have organized their own headquarters at the end of this street.\x07Head down the street and see if you can get to the bottom of this.\x07Find Sellbot Cogs in their headquarters, defeat 5 of them, and report back."},
 3252: {QUEST: "Ok, spill the beans.\x07What's that you say?\x07Sellbot Headquarters?? Oh no!!! Something must be done.\x07We must notify Judge McIntosh - she'll know what to do.\x07Go at once and tell her what you have found out. She's just down the street."},
 3253: {QUEST: "Yes, can I help you? I'm very busy.\x07Eh? Cog Headquarters?\x07Eh? Nonsense. That could never happen.\x07You must be mistaken. Preposterous.\x07Eh? Don't argue with me.\x07Ok then, bring back some proof.\x07If Sellbots really are building this Cog HQ, any Cog there will be carrying blueprints.\x07Cogs love paperwork, you know?\x07Defeat Sellbots in there until you find blueprints.\x07Bring them back here and maybe I'll believe you."},
 3254: {QUEST: "You again, eh? Blueprints? You have them?\x07Let me see those! Hmmm... A factory?\x07That must be where they are building the Sellbots... And what's this?\x07Yes, just what I suspected. I knew it all along.\x07They are building a Sellbot Cog Headquarters.\x07This is not good. Must make some phone calls. Very busy. Goodbye!\x07Eh? Oh yes, take these blueprints back to Detective Lima.\x07She can make more sense of them.",
        COMPLETE: "What did Judge McIntosh say?\x07We were right? Oh no. Let's see those blueprints.\x07Hmmm... Looks like Sellbots constructed a factory with machinery for building Cogs.\x07Sounds very dangerous. Stay out until you have more Laff points.\x07When you have more Laff points, we have much more to learn about Sellbot HQ.\x07For now, nice work, here is your reward."},
 3255: {QUEST: '_toNpcName_ is investigating Sellbot Headquarters.\x07Go see if you can help._where_'},
 3256: {QUEST: '_toNpcName_ is investigating Sellbot Headquarters.\x07Go see if you can help._where_'},
 3257: {QUEST: '_toNpcName_ is investigating Sellbot Headquarters.\x07Go see if you can help._where_'},
 3258: {QUEST: 'There is much confusion about what the Cogs are up to in their new headquarters.\x07I need you to bring back some information directly from them.\x07If we can get four internal memos from Sellbots inside their HQ, that will clear things up.\x07Bring back your first memo to me so we can learn more.'},
 3259: {QUEST: 'Great! This let\'s see what the memo says....\x07"Attn Sellbots:"\x07"I\'ll be in my office at the top of Sellbot Towers promoting Cogs to higher levels."\x07"When you earn enough merits enter the elevator in the lobby to see me."\x07"Break time\'s over - back to work!"\x07"Signed, Sellbot V.P."\x07Aha.... Flippy will want to see this. I\'ll send it to him right now.\x07Please go get your second memo and bring it back.'},
 3260: {QUEST: 'Oh good, you\'re back. Let\'s see what you found....\x07"Attn Sellbots:"\x07"Sellbot Towers has installed a new security system to keep all Toons out."\x07"Toons caught in Sellbot Towers will be detained for questioning."\x07"Please meet in the lobby for appetizers to discuss."\x07"Signed, Mingler"\x07Very interesting... I\'ll pass on this information immediately.\x07Please bring a third memo back.'},
 3261: {QUEST: 'Excellent job _avName_! What does the memo say?\x07"Attn Sellbots:"\x07"Toons have somehow found a way to infiltrate Sellbot Towers."\x07"I\'ll call you tonight during dinner to give you the details."\x07"Signed, Telemarketer"\x07Hmmm... I wonder how Toons are breaking in....\x07Please bring back one more memo and I think we\'ll have enough info for now.',
        COMPLETE: 'I knew you could do it! Ok, the memo says....\x07"Attn Sellbots:"\x07"I was having lunch with Mr. Hollywood yesterday."\x07"He reports that the V.P. is very busy these days."\x07"He will only be taking appointments from Cogs that deserve a promotion."\x07"Forgot to mention, Gladhander is golfing with me on Sunday."\x07"Signed, Name Dropper"\x07Well... _avName_, this has been very helpful.\x07Here is your reward.'},
 3262: {QUEST: "_toNpcName_ has some new information about the Sellbot HQ Factory.\x07Go see what he's got._where_"},
 3263: {GREETING: 'Hi buddy!',
        QUEST: 'I\'m Coach Zucchini, but you can just call me Coach Z.\x07I put the "squash" in squash and stretch, if you know what I mean.\x07Listen, Sellbots have finished an enormous factory to pump out Sellbots 24 hours a day.\x07Get a group of Toon buddies together and squash the factory!\x07Inside Sellbot HQ, look for the tunnel to the Factory then board the Factory elevator.\x07Make sure you have full gags, full Laff points, and some strong Toons as guides.\x07Defeat the Foreman inside the factory to slow the Sellbot progress.\x07Sounds like a real workout, if you know what I mean.',
        LEAVING: 'See ya buddy!',
        COMPLETE: 'Hey buddy, nice work on that Factory!\x07Looks like you found part of a Cog suit.\x07It must be left over from their Cog manufacturing process.\x07That may come in handy. Keep collecting these when you have spare time.\x07Maybe when you collect an entire Cog suit it could be useful for something....'},
 4001: {GREETING: '',
        QUEST: 'Now you get to choose the next gag track you want to learn.\x07Take your time deciding, and come back here when you are ready to choose.',
        INCOMPLETE_PROGRESS: 'Think about your decision before choosing.',
        INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
        COMPLETE: 'A wise decision...',
        LEAVING: QuestsDefaultLeaving},
 4002: {GREETING: '',
        QUEST: 'Now you get to choose the next gag track you want to learn.\x07Take your time deciding, and come back here when you are ready to choose.',
        INCOMPLETE_PROGRESS: 'Think about your decision before choosing.',
        INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
        COMPLETE: 'A wise decision...',
        LEAVING: QuestsDefaultLeaving},
 4200: {QUEST: "I bet Tom could use some help with some research he's doing._where_"},
 4201: {GREETING: 'Howdy!',
        QUEST: "I'm very concerned about a rash of musical instrument theft.\x07I'm conducting a survey among my fellow merchants.\x07Perhaps I can find a pattern to help me crack this case.\x07Stop by and ask Tina for a concertina inventory._where_"},
 4202: {QUEST: 'Yes, I talked to Tom this morning.\x07I have the inventory right here.\x07Bring it right back to him, ok?_where_'},
 4203: {QUEST: "Great! One down...\x07Now swing by and get Yuki's._where_"},
 4204: {QUEST: 'Oh! The inventory!\x07I forgot all about it.\x07I bet I can have it done by the time you defeat 10 Cogs.\x07Stop in after that and I promise it will be ready.',
        INCOMPLETE_PROGRESS: '31, 32... DOH!\x07You made me lose count!',
        GREETING: ''},
 4205: {QUEST: 'Ah, there you are.\x07Thanks for giving me some time.\x07Take this to Tom and tell him I said Hello._where_'},
 4206: {QUEST: "Hmmm, very interesting.\x07Now we are getting somewhere.\x07Ok, the last inventory is Fifi's._where_"},
 4207: {QUEST: "Inventory?\x07How can I do an inventory if I don't have the form?\x07Go see Cleff and see if he has one for me._where_",
        INCOMPLETE_PROGRESS: 'Any sign of that form yet?'},
 4208: {QUEST: "Sure I got an inventory form, mon!\x07But dey ain't free, you know.\x07I'll tell you woht. I trade you for a whole cream pie.",
        GREETING: 'Hey, mon!',
        LEAVING: 'Cool runnings...',
        INCOMPLETE_PROGRESS: "A slice won't do.\x07I be hungry, mon. I need de WHOLE pie."},
 4209: {GREETING: '',
        QUEST: 'Mmmm...\x07Dem mighty nice!\x07Here be your form for Fifi._where_'},
 4210: {GREETING: '',
        QUEST: "Thank you. That's a big help.\x07Let's see...Fiddles: 2\x07All done! Off you go!_where_",
        COMPLETE: "Great work, _avName_.\x07I'm sure I'll get to the bottom of these thefts now.\x07Why don't you get to the bottom of this!"},
 4211: {QUEST: 'Say, Dr. Fret keeps calling every five minutes. Can you go see what his problem is?_where_'},
 4212: {QUEST: "Whew! I'm glad Toon HQ finally sent somebody.\x07I haven't had a customer in days.\x07It's these darned Number Crunchers every where.\x07I think they are teaching our residents bad oral hygiene.\x07Defeat ten of them and let's see if business picks up.",
        INCOMPLETE_PROGRESS: 'Still no customers. But keep it up!'},
 4213: {QUEST: "You know maybe it wasn't the Number Crunchers after all.\x07Maybe it's just the Cashbots in general.\x07Take out twenty of them and hopefully someone will come in for at least a checkup.",
        INCOMPLETE_PROGRESS: "I know twenty is a lot. But I'm sure it's going to pay off in spades."},
 4214: {GREETING: '',
        LEAVING: '',
        QUEST: "I just don't understand it!\x07Still not a SINGLE customer.\x07Maybe we need to go to the source.\x07Try reclaiming a Cashbot Cog building.\x07That Should do the trick...",
        INCOMPLETE_PROGRESS: 'Oh, please! Just one little building...',
        COMPLETE: "Still not a soul in here.\x07But you know, come to think of it.\x07I didn't have any customers before the Cogs invaded either!\x07I really appreciate all your help though.\x07This should help you get around."},
 4215: {QUEST: "Anna desperately needs someone to help her.\x07Why don't you drop in and see what you can do._where_"},
 4216: {QUEST: "Thanks for coming so quickly!\x07Seems like the Cogs have made off with several of my customers' cruise tickets.\x07Yuki said she saw a Glad Hander leaving here with his glad hands full of them.\x07See if you can get Lumber Jack's ticket to Alaska back.",
        INCOMPLETE_PROGRESS: 'Those Glad Handers could be anywhere now...'},
 4217: {QUEST: "Oh, great. You found it!\x07Now be a trooper and run in by Jack's for me, would you?_where_"},
 4218: {QUEST: "Great Googely Moogely!\x07Alaska here I come!\x07I can't take these infernal Cogs anymore.\x07Say, I think Anna needs you again._where_"},
 4219: {QUEST: "Yup, you guessed it.\x07I need you to shake down those pesky Glad Handers for Tabitha's ticket to Jazzfest.\x07You know the procedure...",
        INCOMPLETE_PROGRESS: "There's more out there somewhere..."},
 4220: {QUEST: 'Sweet!\x07Could you swing this one by his place for me too?_where_'},
 4221: {GREETING: '',
        LEAVING: 'Be cool...',
        QUEST: "Cool, daddio!\x07Now I'm in fat city, _avName_.\x07Before you split, you better go check out Anna Banana again..._where_"},
 4222: {QUEST: "This is the last one, I promise!\x07Now you are looking for Barry's ticket to the big singing contest.",
        INCOMPLETE_PROGRESS: "C'mon, _avName_.\x07Barry is counting on you."},
 4223: {QUEST: "This should put a smile on Barry's face._where_"},
 4224: {GREETING: '',
        LEAVING: '',
        QUEST: 'Hello, Hello, HELLO!\x07Terrific!\x07I just know me and the boys are going to clean up this year.\x07Anna says to swing back by and get your reward._where_\x07Goodbye, Goodbye, GOODBYE!',
        COMPLETE: 'Thanks for all your help, _avName_.\x07You really are an asset here in Toontown.\x07Speaking of assets...'},
 902: {QUEST: 'Go see Leo.\x07He needs someone to deliver a message for him._where_'},
 4903: {QUEST: 'Dude!\x07My castanets are all cloudy and I have a big show tonight.\x07Take them to Carlos and see if he can polish them up._where_'},
 4904: {QUEST: 'Jes, I tink I can polish dees.\x07But I need soma de blue ink from de squid.',
        GREETING: 'Hola!',
        LEAVING: 'Adios!',
        INCOMPLETE_PROGRESS: "Juo can find de squid wherever dere's a fishing pier"},
 4905: {QUEST: "Jes! Dat's it!\x07Now I need a leetle time to polish dees.\x07Why don juo go takeover a one story beelding while I work?",
        GREETING: 'Hola!',
        LEAVING: 'Adios!',
        INCOMPLETE_PROGRESS: 'Jest anodder minute...'},
 4906: {QUEST: 'Bery good!\x07Here are de castanets for Leo._where_'},
 4907: {GREETING: '',
        QUEST: "Cool, dude!\x07They look awesome!\x07Now I need you to get a copy of the lyrics to 'A Beat Christmas' from Hedy._where_"},
 4908: {QUEST: "Hello there!\x07Hmmm, I don't have a copy of that song handy.\x07If you give me a little while I could transcribe it from memory.\x07Why don't you run along and reclaim a two story building while I write?"},
 4909: {QUEST: "I'm sorry.\x07My memory is getting a little fuzzy.\x07If you go reclaim a three story building I'm sure I'll be done when you get back..."},
 4910: {QUEST: 'All done!\x07Sorry it took so long.\x07Take this back to Leo._where_',
        GREETING: '',
        COMPLETE: 'Awesome, dude!\x07My concert is gonna rock!\x07Speaking of rock, you can rock some Cogs with this...'},
 5247: {QUEST: 'This neighborhood is pretty tough...\x07You might want to learn some new tricks.\x07_toNpcName_ taught me everything I know, so maybe he can help you too._where_'},
 5248: {GREETING: 'Ahh, yes.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'You appear to be struggling with my assignment.',
        QUEST: 'Ahh, so welcome, new apprentice.\x07I know all there is to know about the pie game.\x07But before we can begin your training, a small demonstration is necessary.\x07Go out and defeat ten of the largest Cogs.'},
 5249: {GREETING: 'Mmmmm.',
        QUEST: 'Excellent!\x07Now demonstrate your skill as a fisherman.\x07I dropped three fuzzy dice in the pond yesterday.\x07Fish them out and bring them to me.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'It seems you may not be so clever with the rod and reel.'},
 5250: {GREETING: '',
        LEAVING: '',
        QUEST: 'Aha!  These dice will look great hanging from the rearview mirror of my ox cart!\x07Now, show me that you can tell your enemies from one another.\x07Return when you have restored two of the tallest Lawbot buildings.',
        INCOMPLETE_PROGRESS: 'Do the buildings give you trouble?'},
 5258: {GREETING: '',
        LEAVING: '',
        QUEST: 'Aha!  These dice will look great hanging from the rearview mirror of my ox cart!\x07Now, show me that you can tell your enemies from one another.\x07Return when you have restored two of the tallest Bossbot buildings.',
        INCOMPLETE_PROGRESS: 'Do the buildings give you trouble?'},
 5259: {GREETING: '',
        LEAVING: '',
        QUEST: 'Aha!  These dice will look great hanging from the rearview mirror of my ox cart!\x07Now, show me that you can tell your enemies from one another.\x07Return when you have restored two of the tallest Cashbot buildings.',
        INCOMPLETE_PROGRESS: 'Do the buildings give you trouble?'},
 5260: {GREETING: '',
        LEAVING: '',
        QUEST: 'Aha!  These dice will look great hanging from the rearview mirror of my ox cart!\x07Now, show me that you can tell your enemies from one another.\x07Return when you have restored two of the tallest Sellbot buildings.',
        INCOMPLETE_PROGRESS: 'Do the buildings give you trouble?'},
 5200: {QUEST: 'Those sneaky Cogs are at it again.\x07_toNpcName_ has reported another missing item. Stop by and see if you can straighten it out._where_'},
 5201: {GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x07A group of those Head Hunters came in and stole my soccer ball.\x07The leader told me that I had to make some cutbacks and just grabbed it away from me!\x07Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my soccer ball?',
        COMPLETE: 'Yeehaw! You found it!\x07 Here, take your reward...'},
 5261: {GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x07A group of those Two-Faces came in and stole my soccer ball.\x07The leader told me that I had to make some cutbacks and just grabbed it away from me!\x07Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my soccer ball?',
        COMPLETE: 'Yeehaw! You found it!\x07 Here, take your reward...'},
 5262: {GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x07A group of those Money Bags came in and stole my soccer ball.\x07The leader told me that I had to make some cutbacks and just grabbed it away from me!\x07Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my soccer ball?',
        COMPLETE: 'Yeehaw! You found it!\x07 Here, take your reward...'},
 5263: {GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x07A group of those Spin Doctors came in and stole my soccer ball.\x07The leader told me that I had to make some cutbacks and just grabbed it away from me!\x07Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my soccer ball?',
        COMPLETE: 'Yeehaw! You found it!\x07 Here, take your reward...'},
 5202: {QUEST: lTheBrrrgh + " has been overrun with some of the toughest Cogs we've seen yet.\x07You will probably want to carry more gags around here.\x07I hear _toNpcName_ may have a large bag you can use to carry more gags._where_"},
 5203: {GREETING: 'Huh?  Are you on my sledding team?',
        QUEST: "What's that?  You want a bag?\x07I had one somewhere around here... maybe it's in my toboggan?\x07Only... I haven't seen my toboggan since the big race!\x07Maybe one of those Cogs took it?",
        LEAVING: 'Have you seen my toboggan?',
        INCOMPLETE_PROGRESS: "Who are you again?  Sorry, I'm a little woozy from the crash."},
 5204: {GREETING: '',
        LEAVING: '',
        QUEST: "Is that my toboggan?  I don't see any bag here.\x07I think Bumpy Noggin was on the team... maybe he has it?_where_"},
 5205: {GREETING: 'Ohhh, my head!',
        LEAVING: '',
        QUEST: "Huh?  Ted who?  A bag?\x07Oh, maybe he was on our toboggan team?\x07My head hurts so much I can't think straight.\x07Could you fish me out some ice cubes from the frozen pond for my head?",
        INCOMPLETE_PROGRESS: "Oww, my head's killing me!  Got any ice?"},
 5206: {GREETING: '',
        LEAVING: '',
        QUEST: "Ahhh, that feels much better!\x07So you're looking for Ted's bag, huh?\x07I think it ended up on Sam Simian's head after the crash._where_"},
 5207: {GREETING: 'Eeeep!',
        LEAVING: '',
        QUEST: 'What is bag?  Who is Bompy?\x07Me scared of buildings!  You beat buildings, I give you bag!',
        INCOMPLETE_PROGRESS: 'More buildings!  Me still scared!',
        COMPLETE: 'Ooooh!  Me like you!'},
 5208: {GREETING: '',
        LEAVING: 'Eeeek!',
        QUEST: 'Ooooh!  Me like you!\x07Go to Ski Clinic. Bag there.'},
 5209: {GREETING: 'Dude!',
        LEAVING: 'Later!',
        QUEST: "Man, that Simian Sam is crazy!\x07If you're wild like Sam, I'll give you your bag, man.\x07Go bag some Cogs for your bag, man! Hey now!",
        INCOMPLETE_PROGRESS: "Are you sure you're extreme enough?  Go bag some more Cogs.",
        COMPLETE: "Hey, you are pretty wild!  That was a heap of Cogs you bagged!\x07Here's your bag!"},
 5210: {QUEST: '_toNpcName_ is secretly in love with someone in the neighborhood.\x07If you help her, she may reward you handsomely._where_'},
 5211: {GREETING: 'Boo hoo.',
        QUEST: 'I spent all last night writing a letter to the dog I love.\x07But before I could deliver it, one of those nasty Cogs with a beak came in and took it.\x07Can you get it back for me?',
        LEAVING: 'Boo hoo.',
        INCOMPLETE_PROGRESS: 'Please find my letter.'},
 5264: {GREETING: 'Boo hoo.',
        QUEST: 'I spent all last night writing a letter to the dog I love.\x07But before I could deliver it, one of those nasty Cogs with a fin came in and took it.\x07Can you get it back for me?',
        LEAVING: 'Boo hoo.',
        INCOMPLETE_PROGRESS: 'Please find my letter.'},
 5265: {GREETING: 'Boo hoo.',
        QUEST: 'I spent all last night writing a letter to the dog I love.\x07But before I could deliver it, one of those nasty Mingler Cogs came in and took it.\x07Can you get it back for me?',
        LEAVING: 'Boo hoo.',
        INCOMPLETE_PROGRESS: 'Please find my letter.'},
 5266: {GREETING: 'Boo hoo.',
        QUEST: 'I spent all last night writing a letter to the dog I love.\x07But before I could deliver it, one of those nasty Corporate Raiders came in and took it.\x07Can you get it back for me?',
        LEAVING: 'Boo hoo.',
        INCOMPLETE_PROGRESS: 'Please find my letter.'},
 5212: {QUEST: 'Oh, thank you for finding my letter!\x07Please, please, please could you deliver it to the most handsome dog in the neighborhood?',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "You didn't deliver my letter, did you?"},
 5213: {GREETING: "Charmed, I'm sure.",
        QUEST: "I can't be bothered with your letter, you see.\x07All my doggies have been taken from me!\x07If you bring them back, maybe we can talk then.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'My poor little doggies!'},
 5214: {GREETING: '',
        LEAVING: 'Toodleloo!',
        QUEST: "Thank you for bringing back my little beauties.\x07Let's take a look at your letter now...\nMmmm, it seems I have yet another secret admirer.\x07This calls for a trip to my dear friend Carl.\x07I'm sure you'll like him immensely._where_"},
 5215: {GREETING: 'Heh, heh...',
        LEAVING: 'Come back, yes, yes.',
        INCOMPLETE_PROGRESS: "There are still some big ones around.  Comes back to us when they're gone.",
        QUEST: "Who sent you to us?  We don't like Snootsies much, we don't...\x07But we likes Cogs even less...\x07Run the big ones off and we'll helps you we will."},
 5216: {QUEST: 'We told you we would helps you.\x07So take this ring to the girl.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'You still haves the ring???',
        COMPLETE: 'Oh darrrling!!! Thank you!!!\x07Oh, and I have something special for you as well.'},
 5217: {QUEST: 'It sounds like _toNpcName_ could use some help._where_'},
 5218: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm sure there are more Minglers around somewhere.",
        QUEST: "Help!!! Help!!! I can't take it anymore!\x07Those Minglers are driving me batty!!!"},
 5219: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "That can't be all of them.  I just saw one!!!",
        QUEST: "Oh, thanks, but now it's the Corporate Raiders!!!\x07You've got to help me!!!"},
 5220: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No, no, no there was one just here!',
        QUEST: "I realize now that it's those Loan Sharks!!!\x07I thought you were going to save me!!!"},
 5221: {GREETING: '',
        LEAVING: '',
        QUEST: "You know what, maybe it isn't the Cogs at all!\x07Could you ask Fanny to make me a soothing potion?  Maybe that would help...._where_"},
 5222: {LEAVING: '',
        QUEST: "Oh, that Harry, he sure is a card!\x07I'll whip up something that will fix him right up!\x07Oh, I appear to be out of sardine whiskers...\x07Be a dear and run down to the pond and catch some for me.",
        INCOMPLETE_PROGRESS: 'Got those whiskers for me yet?'},
 5223: {QUEST: 'Okay.  Thanks, hon.\x07Here, now take this to Harry.  It should calm him right down.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Go on now, take the potion to Harry.'},
 5224: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Go get those Legal Eagles for me, will you?',
        QUEST: "Oh thank goodness you're back!\x07Give me the potion, quick!!!\x07Glug, glug, glug...\x07That tasted awful!\x07You know, what, though?  I feel much calmer.  Now that I can think clearly, I realize that...\x07It was the Legal Eagles that were driving me crazy all this time!!!",
        COMPLETE: "Oh boy!  Now I can relax!\x07I'm sure there's something here I can give you.  Oh, take this!"},
 5225: {QUEST: 'Ever since the incident with the turnip bread, Grumpy Phil has been mad at _toNpcName_.\x07Maybe you could help Gus fix things between them?_where_'},
 5226: {QUEST: 'Yeah, you probably heard Grumpy Phil is mad at me...\x07I was just trying to be nice with that turnip bread.\x07Maybe you can help cheer him up.\x07Phil really hates those Cashbot Cogs, especially their buildings.\x07If you reclaim some Cashbot buildings, it might help.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Maybe a few more buildings?'},
 5227: {QUEST: "That's terrific!  Go tell Phil what you've done._where_"},
 5228: {QUEST: 'Oh he did, did he?\x07That Gus thinks he can get off so easy, does he?\x07Only broke my tooth, he did, with that turnip bread of his!\x07Maybe if you took my tooth to Dr. Mumbleface for me he could fix it.',
        GREETING: 'Mmmmrrphh.',
        LEAVING: 'Grumble, grumble.',
        INCOMPLETE_PROGRESS: 'You again?  I thought you were going to get my tooth fixed for me.'},
 5229: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm still working on the tooth.  It will be a bit longer.",
        QUEST: "Yes, that tooth looks pretty bad, alrighty.\x07Maybe I can do something, but it will be a little while.\x07Maybe you could clear some of those Cashbot Cogs off the streets while you're waiting?\x07They're scaring off my customers."},
 5267: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm still working on the tooth.  It will be a bit longer.",
        QUEST: "Yes, that tooth looks pretty bad, alrighty.\x07Maybe I can do something, but it will be a little while.\x07Maybe you could clear some of those Sellbot Cogs off the streets while you're waiting?\x07They're scaring off my customers."},
 5268: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm still working on the tooth.  It will be a bit longer.",
        QUEST: "Yes, that tooth looks pretty bad, alrighty.\x07Maybe I can do something, but it will be a little while.\x07Maybe you could clear some of those Lawbot Cogs off the streets while you're waiting?\x07They're scaring off my customers."},
 5269: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm still working on the tooth.  It will be a bit longer.",
        QUEST: "Yes, that tooth looks pretty bad, alrighty.\x07Maybe I can do something, but it will be a little while.\x07Maybe you could clear some of those Bossbot Cogs off the streets while you're waiting?\x07They're scaring off my customers."},
 5230: {GREETING: '',
        QUEST: "I'm glad you're back!\x07I gave up trying to fix that old tooth, and made a new gold tooth for Phil instead.\x07Unfortunately a Robber Baron came in and took it from me.\x07Maybe you can catch him if you hurry.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find that tooth yet?'},
 5270: {GREETING: '',
        QUEST: "I'm glad you're back!\x07I gave up trying to fix that old tooth, and made a new gold tooth for Phil instead.\x07Unfortunately a Big Cheese came in and took it from me.\x07Maybe you can catch him if you hurry.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find that tooth yet?'},
 5271: {GREETING: '',
        QUEST: "I'm glad you're back!\x07I gave up trying to fix that old tooth, and made a new gold tooth for Phil instead.\x07Unfortunately Mr. Hollywood came in and took it from me.\x07Maybe you can catch him if you hurry.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find that tooth yet?'},
 5272: {GREETING: '',
        QUEST: "I'm glad you're back!\x07I gave up trying to fix that old tooth, and made a new gold tooth for Phil instead.\x07Unfortunately a Big Wig came in and took it from me.\x07Maybe you can catch him if you hurry.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find that tooth yet?'},
 5231: {QUEST: "Great, that's the tooth alrighty!\x07Why don't you just run it over to Phil for me?",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I bet Phil would like to see his new tooth.'},
 5232: {QUEST: "Oh, thanks.\x07Mmmrrrphhhh\x07How's that look, huh?\x07Okay, you can tell Gus that I forgive him.",
        LEAVING: '',
        GREETING: ''},
 5233: {QUEST: "Oh, that's great to hear.\x07I figured old Phil couldn't stay mad at me.\x07As a gesture of goodwill, I baked him this Pine cone bread.\x07Could you run it over to him for me?",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Better hurry.  Pine cone bread is better when it's hot.",
        COMPLETE: "Oh, what's this?  For me?\x07Munch, munch...\x07Owwww!  My tooth!  That Gus Gooseburger!\x07Oh well, it wasn't your fault.  Here, you can have this for your trouble."},
 903: {QUEST: 'You may be ready to see _toNpcName_ the Blizzard Wizard for your final test._where_'},
 5234: {GREETING: '',
        QUEST: 'Aha, you are back.\x07Before we begin, we must eat.\x07Bring us some lumpy cheese for our broth.\x07Lumpy cheese can only be gathered from Big Cheese Cogs.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'We still need lumpy cheese'},
 5278: {GREETING: '',
        QUEST: 'Aha, you are back.\x07Before we begin, we must eat.\x07Bring us some caviar for our broth.\x07Caviar can only be gathered from Mr. Hollywood Cogs.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'We still need caviar'},
 5235: {GREETING: '',
        QUEST: 'A simple man eats with a simple spoon.\x07A Cog took my simple spoon, so I simply can not eat.\x07Return my spoon to me.  I think a Robber Baron took it.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I simply must have my spoon.'},
 5279: {GREETING: '',
        QUEST: 'A simple man eats with a simple spoon.\x07A Cog took my simple spoon, so I can not eat.\x07Return my spoon to me.  I think a Big Wig took it.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I simply must have my spoon.'},
 5236: {GREETING: '',
        QUEST: 'Many thanks.\x07Slurp, slurp...\x07Ahhh, now you must catch a talking toad.  Try fishing in the pond.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Where is that talking toad?'},
 5237: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'You have not yet obtained dessert.',
        QUEST: "Oh, that is certainly a talking toad.  Give him to me.\x07What's that you say, toad?\x07Uh huh.\x07Uh huh...\x07The toad has spoken.  We need dessert.\x07Bring us some ice cream cones from _toNpcName_.\x07The toad likes red bean flavored ice cream for some reason._where_"},
 5238: {GREETING: '',
        QUEST: "So the wizard sent you.  I'm sad to say we're fresh out of red bean ice cream cones.\x07You see, a bunch of Cogs came in and just took them.\x07They said they were for Mr. Hollywood, or some such nonsense.\x07I'd sure appreciate if you could round them back up for me.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Have you found all my ice cream cones yet?'},
 5280: {GREETING: '',
        QUEST: "So the wizard sent you.  I'm sad to say we're fresh out of red bean ice cream cones.\x07You see, a bunch of Cogs came in and just took them.\x07They said they were for The Big Cheese, or some such nonsense.\x07I'd sure appreciate if you could round them back up for me.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Have you found all my ice cream cones yet?'},
 5239: {QUEST: "Thanks for bringing back my ice cream cones!\x07Here's one for Lil Oldman.",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'You better bring that ice cream to Lil Oldman before it melts.'},
 5240: {GREETING: '',
        QUEST: 'Very good.  Here you go toad...\x07Slurp, slurp...\x07Okay, now we are almost ready.\x07If you can just bring me some powder to dry my hands.\x07I think those Big Wig Cogs sometimes have powder from their wigs.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find any powder?'},
 5281: {GREETING: '',
        QUEST: 'Very good.  Here you go toad...\x07Slurp, slurp...\x07Okay, now we are almost ready.\x07If you can just bring me some powder to dry my hands.\x07I think those Mr. Hollywood Cogs sometimes keep powder for their noses.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find any powder?'},
 5241: {QUEST: 'Okay.\x07As I once said, to truly throw a pie, you must throw not with the hand...\x07...but with the soul.\x07I know not what that means, so I will sit and contemplate while you restore buildings.\x07Return when you have completed your task.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Your task is not yet complete.'},
 5242: {GREETING: '',
        QUEST: 'Although I still know not what I am talking about, you truly are worthy.\x07I give you a final task...\x07The talking toad would like a girlfriend.\x07Find another talking toad.  The toad has spoken.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Where is that other talking toad?',
        COMPLETE: 'Whew!  I am tired from all this effort.  I must rest now.\x07Here, take your reward and be off.'},
 5243: {QUEST: 'Sweaty Pete is starting to stink up the street.\x07Can you talk him into taking a shower or something?_where_'},
 5244: {GREETING: '',
        QUEST: "Yeah, I guess I do work up quite a sweat in here.\x07Mmmm, maybe if I could fix that leaky pipe in my shower...\x07I figure a gear from one of those tiny Cogs would do the trick.\x07Go find a gear from a Micromanager and we'll try it.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Where's that gear you were going to get?"},
 5245: {GREETING: '',
        QUEST: 'Yup, that seemed to do the trick.\x07But I get lonely when I shower...\x07Could you go fish me up a rubber ducky to keep me company?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck with that duck?'},
 5246: {QUEST: "The ducky's great, but...\x07All those buildings around here make me nervous.\x07I'd feel a lot more relaxed if there were fewer buildings around.",
        LEAVING: '',
        COMPLETE: "Okay, I'll shower up now.  And here's something for you too.",
        INCOMPLETE_PROGRESS: "I'm still worried about buildings."},
 5251: {QUEST: 'Lounge Lassard is supposed to be playing a gig tonight.\x07I hear he might be having some trouble with his equipment._where_'},
 5252: {GREETING: '',
        QUEST: 'Oh yeah!  I could sure use some help.\x07Those Cogs came in and swiped all my gear while I was unloading the van.\x07Can you give me a hand and get back my microphone?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Hey man, I can't sing without my microphone."},
 5253: {GREETING: '',
        QUEST: "Yeah, that's my microphone all right.\x07Thanks for getting it for me, but...\x07I really need my keyboard so I can tickle the ivories.\x07I think one of those Corporate Raiders got my keyboard.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding my keboard?'},
 5273: {GREETING: '',
        QUEST: "Yeah, that's my microphone all right.\x07Thanks for getting it for me, but...\x07I really need my keyboard so I can tickle the ivories.\x07I think one of those Minglers got my keyboard.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding my keboard?'},
 5274: {GREETING: '',
        QUEST: "Yeah, that's my microphone all right.\x07Thanks for getting it for me, but...\x07I really need my keyboard so I can tickle the ivories.\x07I think one of those Loan Sharks got my keyboard.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding my keboard?'},
 5275: {GREETING: '',
        QUEST: "Yeah, that's my microphone all right.\x07Thanks for getting it for me, but...\x07I really need my keyboard so I can tickle the ivories.\x07I think one of those Legal Eagles got my keyboard.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding my keboard?'},
 5254: {GREETING: '',
        QUEST: "All right!  Now I'm in business.\x07If only they hadn't taken my platform shoes...\x07Those shoes probably ended up with a Mr. Hollywood, if I had to guess.",
        LEAVING: '',
        COMPLETE: "Allright!!  I'm ready now.\x07Hello Brrrgh!!!\x07Huh?  Where is everyone?\x07Okay, take this and round me up some fans, huh?",
        INCOMPLETE_PROGRESS: "I can't perform barefoot, can I?"},
 5282: {GREETING: '',
        QUEST: "All right!  Now I'm in business.\x07If only they hadn't taken my platform shoes...\x07Those shoes probably ended up with a Big Cheese, if I had to guess.",
        LEAVING: '',
        COMPLETE: "Allright!!  I'm ready now.\x07Hello Brrrgh!!!\x07Huh?  Where is everyone?\x07Okay, take this and round me up some fans, huh?",
        INCOMPLETE_PROGRESS: "I can't perform barefoot, can I?"},
 5283: {GREETING: '',
        QUEST: "All right!  Now I'm in business.\x07If only they hadn't taken my platform shoes...\x07Those shoes probably ended up with a Robber Baron, if I had to guess.",
        LEAVING: '',
        COMPLETE: "Allright!!  I'm ready now.\x07Hello Brrrgh!!!\x07Huh?  Where is everyone?\x07Okay, take this and round me up some fans, huh?",
        INCOMPLETE_PROGRESS: "I can't perform barefoot, can I?"},
 5284: {GREETING: '',
        QUEST: "All right!  Now I'm in business.\x07If only they hadn't taken my platform shoes...\x07Those shoes probably ended up with a Big Wig, if I had to guess.",
        LEAVING: '',
        COMPLETE: "Allright!!  I'm ready now.\x07Hello Brrrgh!!!\x07Huh?  Where is everyone?\x07Okay, take this and round me up some fans, huh?",
        INCOMPLETE_PROGRESS: "I can't perform barefoot, can I?"},
 5255: {QUEST: 'You look like you could use more Laff points.\x07Maybe _toNpcName_ could sort you out._where_'},
 5256: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "A deal's a deal.",
        QUEST: "So you're looking for Laff points, huh?\x07Have I got a deal for you!\x07Simply take care of a few Bossbot Cogs for me...\x07And I'll make it worth your while."},
 5276: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "A deal's a deal.",
        QUEST: "So you're looking for Laff points, huh?\x07Have I got a deal for you!\x07Simply take care of a few Lawbot Cogs for me...\x07And I'll make it worth your while."},
 5257: {GREETING: '',
        LEAVING: '',
        COMPLETE: "Okay, but I'm certain I told you to round up some Lawbot Cogs.\x07Well, if you say so, but you owe me one.",
        INCOMPLETE_PROGRESS: "I don't think you're done yet.",
        QUEST: "You say you're done?  Defeated all the Cogs?\x07You must have misunderstood, our deal was for Sellbot Cogs.\x07I'm sure I told you to defeat some Sellbot Cogs for me."},
 5277: {GREETING: '',
        LEAVING: '',
        COMPLETE: "Okay, but I'm certain I told you to round up some Lawbot Cogs.\x07Well, if you say so, but you owe me one.",
        INCOMPLETE_PROGRESS: "I don't think you're done yet.",
        QUEST: "You say you're done?  Defeated all the Cogs?\x07You must have misunderstood, our deal was for Cashbot Cogs.\x07I'm sure I told you to defeat some Cashbot Cogs for me."},
 5301: {QUEST: "I can't help you with Laff points, but maybe _toNpcName_ will cut you a deal.\x07He's a little on tempermental side though..._where_"},
 5302: {GREETING: '',
        LEAVING: '',
        COMPLETE: "I told you what?!?!\x07Thanks a bunch! Here's your Laff point!",
        INCOMPLETE_PROGRESS: 'Hi!\x07What are you doing in here again!',
        QUEST: 'A Laff point? I dont think so!\x07Sure, but only if you clear out some of these pesky Lawbots first.'},
 5303: {QUEST: lTheBrrrgh + " is teeming with very dangerous Cogs.\x07If I were you, I'd carry more gags around here.\x07I hear _toNpcName_ can make you a large bag if you are willing to do the legwork._where_"},
 5304: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'There should be plenty of Lawbots out there.\x07So get to it!',
        QUEST: "A bigger bag?\x07I could probably whip one up for ya.\x07I'll need some yarn though.\x07Some Lawbots made off with mine yesterday morning."},
 5305: {GREETING: 'Howdy!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Go get some more cogs.\x07This color hasn't taken yet.",
        QUEST: "That there's some fine yarn!\x07Not my first choice of color though.\x07Tell you what...\x07You go out there and beat up some of the tougher cogs...\x07And I'll get to work dyeing this yarn."},
 5306: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'They gotta be down there somewhere...',
        QUEST: "Well, the yarn is all dyed. But we've got a small problem.\x07I can't find my knitting needles anywhere.\x07Last place I saw them was down at the pond."},
 5307: {GREETING: '',
        LEAVING: 'Much obliged!',
        INCOMPLETE_PROGRESS: "Rome wasn't knit in a day!",
        QUEST: "Those are my needles alright.\x07While I'm knitting, why don't you go clear some of them big buildings?",
        COMPLETE: "Great work!\x07And speaking of great work...\x07Here's your new bag!"},
 5308: {GREETING: '',
        LEAVING: '',
        QUEST: 'I hear _toNpcName_ is having some legal troubles.\x07Can you stop by and check it out?_where_'},
 5309: {GREETING: "I'm glad you're here...",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Please hurry! The street is crawling with them!',
        QUEST: "The Lawbots have really taken over out there.\x07I'm afraid they are going to take me to court.\x07Do you think you could help get them off of this street?"},
 5310: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I think I hear them coming for me...',
        QUEST: "Thanks. I feel a little better now.\x07 But there is one more thing...\x07Could you drop by _toNpcName_'s and get me an alibi?_where_"},
 5311: {GREETING: 'WHAAAA!!!!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I can't help him if you can't find it!",
        QUEST: "Alibi?! Why that's a great idea!\x07You'd better make it two!\x07I bet a Legal Eagle would have some..."},
 5312: {GREETING: 'Finally!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '',
        COMPLETE: "Whew! Am I ever relieved to have this.\x07Here's your reward...",
        QUEST: "Super! You'd better run these back to _toNpcName_!"},
 6201: {QUEST: 'Powers Erge needs some help. Could you drop by and lend her a hand?_where_'},
 6202: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh, a customer! Great! What can I do for you?\x07What do you mean, what can you do for me? OH! You're not a customer.\x07I remember now. You're here to help with those dreadful Cogs.\x07Well I could certainly use the help even if you're not a customer.\x07If you clean up the streets a bit, I'll have a little something for you.",
        INCOMPLETE_PROGRESS: "If you don't want electricity, I can't help you until you defeat those Cogs.",
        COMPLETE: "Good job on those Cogs, _avName_.\x07Now, are you sure I can't interest you in some electricity? Might come in handy....\x07No? OK, suit yourself.\x07Hunh? Oh yeah, I remember. Here ya go. This is sure to help with those nasty Cogs.\x07Keep up the good work!"},
 6206: {QUEST: "Well, _avName_, I don't have anything for you right now.\x07Wait! I think Susan Siesta was looking for help. Why don't you go see her?_where_"},
 6207: {GREETING: '',
        LEAVING: '',
        QUEST: "I'll never get rich with those darn Cogs driving away all my business!\x07You've got to help me, _avName_.\x07Clear out a few Cog buildings for the sake of the neighborhood and I'll add to your riches.",
        INCOMPLETE_PROGRESS: "Poor me! Can't you get rid of those buildings?",
        COMPLETE: "Now I'll be in the money! I can see it now!\x07I'll spend all my time fishing. Now, let me enrich your life a little.\x07There you go!"},
 6211: {QUEST: 'Hey _avName_! I heard Lawful Linda was looking for you.\x07You should stop by and pay her a visit._where_'},
 6212: {GREETING: '',
        LEAVING: '',
        QUEST: "Hi there! Wow, am I glad to see you!\x07I've been working on this answering machine in my spare time but I'm short a couple of parts.\x07I need three more rods and the ones from Bean Counters seem to work pretty well.\x07Could you see if you could find some rods for me?",
        INCOMPLETE_PROGRESS: 'Still trying to find those rods?'},
 6213: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh, those will do nicely.\x07That's funny. I was sure I had a spare drive belt around here but I can't find it.\x07Could you please get one from a Money Bags for me? Thanks!",
        INCOMPLETE: "Well, I can't help you until I get that drive belt."},
 6214: {GREETING: '',
        LEAVING: '',
        QUEST: "Ah, that's it. Now it should run like a charm.\x07Where'd my pliers go? I can't tighten this up without the pliers.\x07Maybe pincers from a Penny Pincher would do the job?\x07If you'd go find one, I could give you a little something to help you with those Cogs.",
        INCOMPLETE_PROGRESS: 'No pincers yet, hunh? Keep looking.',
        COMPLETE: "Great! Now I'll just tighten this up.\x07It seems to be working now. Back in business!\x07Well, except that we don't have a phone. But I'm glad for the help, anyway.\x07I think this'll help you out with those Cogs. Good luck!"},
 6221: {QUEST: 'I heard Rocco was looking for help. See what you can do for him._where_'},
 6222: {GREETING: '',
        LEAVING: '',
        QUEST: "Yo! Youse came to da right place. I ain't too happy.\x07Yeah, I was lookin for some help wid dose Cogs. Dey always come and boss me around.\x07If you can retire some of dem Bossbots, I'll make it worth your while.",
        INCOMPLETE_PROGRESS: "Hey, _avName_, what's up wid youse?\x07You gotta keep after dem Bossbots. We got a deal, remember?\x07Rocco always keeps his word.",
        COMPLETE: "Yo, _avName_! Youse ok in my book.\x07Dem Bossbots ain't so bossy now, is they?\x07Here ya go! A nice big boost. Now, you stay outta trouble, ya hear!"},
 6231: {QUEST: 'Nat over on Pajama Place heard rumors about a Cashbot Headquarters.\x07Head over there and see if you can help him out._where_'},
 6232: {GREETING: '',
        LEAVING: '',
        QUEST: "I got a nibble about some strange goings on.\x07Well, maybe it's the fleas but something is going on anyway.\x07All these Cashbots!\x07I think they've opened another headquarters right off Pajama Place.\x07P.J. knows his way around.\x07Go see _toNpcName_ _where_ Ask him if he's heard anything.",
        INCOMPLETE_PROGRESS: "You haven't seen P.J. yet? What's keeping you?\x07Oh, these darn fleas!"},
 6233: {GREETING: '',
        LEAVING: '',
        QUEST: "Hey there _avName_, where are you headed?\x07Cashbot Headquarters?? I haven't seen anything.\x07Could you go to the end of Pajama Place and see if it's true?\x07Find some Cashbot Cogs in their headquarters, defeat a few of them, and come tell me about it.",
        INCOMPLETE_PROGRESS: "Found the HQ yet? You'll need to defeat some Cashbots there to scope it out."},
 6234: {GREETING: '',
        LEAVING: '',
        QUEST: "What?! There really IS a Cashbot HQ?\x07You better go tell Nat right away!\x07Who would have guessed there'd be a Cog HQ right down the street from him?",
        INCOMPLETE_PROGRESS: "What did Nat have to say? You haven't seen him yet?"},
 6235: {GREETING: '',
        LEAVING: '',
        QUEST: "So, I'm itching to hear what P.J. had to say.\x07Hmm...we need more information about this Cog business but I've got to get rid of these fleas!\x07I know! YOU can go find out more!\x07Go defeat Cashbots at the HQ until you find some plans then come right back!",
        INCOMPLETE_PROGRESS: "No plans yet? Keep searching those Cogs!\x07They're bound to have some plans!",
        COMPLETE: "You got the plans?\x07Great! Let's see what they say.\x07I see... the Cashbots built a Mint to make Cogbucks.\x07It must be FULL of Cashbots. We should find out more about this.\x07Maybe if you had a disguise. Hmmm...wait! I think I've got part of a Cog suit here somewhere....\x07Here it is! Why don't you take this for your trouble? Thanks again for your help!"},
 6241: {QUEST: "The Countess has been looking everywhere for you! Please pay her a visit so she'll stop calling._where_"},
 6242: {GREETING: '',
        LEAVING: '',
        QUEST: "_avName_, I'm counting on you to help me!\x07You see, these Cogs are making so much noise that I simply can't concentrate.\x07I keep losing count of my sheep!\x07If you'll cut down on the noise, I'll help you out too! You can count on it!\x07Now, where was I? Right, one hundred thirty-six, one hundred thirty-seven....",
        INCOMPLETE_PROGRESS: "Four hundred forty-two...four hundred forty-three...\x07What? You're back already? But it's still so noisy!\x07Oh no, I've lost count again.\x07 One...two...three....",
        COMPLETE: "Five hundred ninety-three...five hundred ninety-four...\x07Hello? Oh, I knew I could count on you! It's much quieter now.\x07Here you go, for all those Number Crunchers.\x07Number? Now I need to start counting all over again! One...two...."},
 6251: {QUEST: "Poor Zari broke her zipper and now she can't make deliveries to her customers. She could sure use your help._where_"},
 6252: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh, hi _avName_. You're here to help with my deliveries?\x07That's terrific! This broken zipper makes it tough to zip around.\x07Let me see...ok, this should be easy. Cowboy George ordered a zither last week.\x07Could you please bring it over to him? _where_",
        INCOMPLETE_PROGRESS: 'Oh, hi! Did you forget something? Cowboy George is waiting for that zither.'},
 6253: {GREETING: '',
        LEAVING: '',
        QUEST: "My zither! At last! Gosh, I can't wait to play it.\x07Go tell Zari that I said thanks, would you?",
        INCOMPLETE_PROGRESS: "Thanks again for the zither. Doesn't Zari have more deliveries for you to do?"},
 6254: {GREETING: '',
        LEAVING: '',
        QUEST: "That was fast. What's next on my list?\x07Right. Master Mike ordered a Zamboni. That zany guy.\x07Could you bring this to him, please?_where_",
        INCOMPLETE_PROGRESS: 'That Zamboni needs to go to Master Mike._where_'},
 6255: {GREETING: '',
        LEAVING: '',
        QUEST: "All-right! The Zamboni I ordered!\x07Now, if only there weren't so many Cogs around, I might have some time to use it.\x07Be a sport and take care of a few of those Cashbots for me, would you?",
        INCOMPLETE_PROGRESS: 'Those Cashbots are tough, hunh? They make it hard to test my Zamboni.'},
 6256: {GREETING: '',
        LEAVING: '',
        QUEST: "Excellent! Now I can go try out my Zamboni.\x07Tell Zari that I'll be in next week to place my next order, please.",
        INCOMPLETE_PROGRESS: "That's all I need for now. Isn't Zari waiting for you?"},
 6257: {GREETING: '',
        LEAVING: '',
        QUEST: "So, Master Mike was happy with his Zamboni? Great.\x07Who's next? Oh, Zen Glen ordered a zebra-striped zabuton.\x07Here it is! Could you zoom over to his place, please?_where_",
        INCOMPLETE_PROGRESS: 'I think Zen Glen needs that zabuton to meditate.'},
 6258: {GREETING: '',
        LEAVING: '',
        QUEST: "Ah, my zabuton at last. Now I can meditate.\x07Who could focus with that racket going on? All those Cogs!\x07Since you're already here, maybe you could take care of some of these Cogs?\x07Then I could use my zabuton in peace.",
        INCOMPLETE_PROGRESS: 'Still so noisy with those Cogs! Who could focus?'},
 6259: {GREETING: '',
        LEAVING: '',
        QUEST: 'Peace and quiet at last. Thanks, _avName_.\x07Please tell Zari how happy I am. OM....',
        INCOMPLETE_PROGRESS: 'Zari called looking for you. You should go see what she needs.'},
 6260: {GREETING: '',
        LEAVING: '',
        QUEST: "I'm glad to hear that Zen Glen is happy with his zebra zabuton.\x07Oh, these zinnias just came in for Rose Petals.\x07Since you seem to have some zeal for deliveries, perhaps you could take them over to her?_where_",
        INCOMPLETE_PROGRESS: "Those zinnias will wilt if you don't deliver them soon."},
 6261: {GREETING: '',
        LEAVING: '',
        QUEST: 'What lovely zinnias! Zari sure does deliver.\x07Oh, well, I guess YOU deliver, _avName_. Please thank Zari for me!',
        INCOMPLETE_PROGRESS: "Don't forget to thank Zari for the zinnias!"},
 6262: {GREETING: '',
        LEAVING: '',
        QUEST: "Welcome back, _avName_. You're pretty zippy.\x07Let's see...what's next on my list to deliver? Zydeco records for Wyda Wake._where_",
        INCOMPLETE_PROGRESS: "I'm sure Wyda Wake is waiting for those Zydeco records."},
 6263: {GREETING: '',
        LEAVING: '',
        QUEST: "Zydeco records? I don't remember asking for Zydeco records.\x07Oh, I bet Lullaby Lou ordered them._where_",
        INCOMPLETE_PROGRESS: 'No, those Zydeco records are for Lullaby Lou._where_'},
 6264: {GREETING: '',
        LEAVING: '',
        QUEST: "At last, my Zydeco records! I thought Zari had forgotten.\x07Could you please bring this zucchini to her? She'll find someone who wants one. Thanks!",
        INCOMPLETE_PROGRESS: "Oh, I've got plenty of zucchini already. Take that one to Zari."},
 6265: {GREETING: '',
        LEAVING: '',
        QUEST: "Zucchini? Hmm. Well, someone will want it, I'm sure.\x07Ok, we're nearly done with my list. One more delivery to make.\x07Babyface MacDougal ordered a zoot suit._where_",
        INCOMPLETE_PROGRESS: "If you don't deliver that zoot suit to Babyface MacDougal,\x07 it'll get all wrinkled."},
 6266: {GREETING: '',
        LEAVING: '',
        QUEST: "Once upon a time...oh! You're not here for a story, are you?\x07You're delivering my zoot suit? Great! Wow, that's something.\x07Hey, could you give Zari a message for me? I'll be needing zircon cufflinks to go with the suit. Thanks!",
        INCOMPLETE_PROGRESS: 'Did you give Zari my message?',
        COMPLETE: "Zircon cufflinks, hunh? Well, I'll see what I can do for him.\x07Anyway, you've been the very zenith of helpfulness and I can't let you leave with zilch.\x07Here's a BIG boost to help you zap those Cogs!"},
 6271: {QUEST: "Drowsy Dave is having some trouble that you might be able to help with. Why don't you stop by his shop?_where_"},
 6272: {GREETING: '',
        LEAVING: '',
        QUEST: "What? Huh? Oh, I must've fallen asleep.\x07You know, those Cogs buildings are full of machinery that makes me really sleepy.\x07I listen to them humming all day and...\x07Huh? Oh, yeah, right. If you could get rid of some of those Cog buildings, I could stay awake.",
        INCOMPLETE_PROGRESS: "Zzzzz...huh? Oh, it's you, _avName_.\x07Back already? I was just taking a little nap.\x07Come back when you're done with those buildings.",
        COMPLETE: "What? I dropped off to sleep for a minute there.\x07Now that those Cog buildings are gone I can finally relax.\x07Thanks for your help, _avName_.\x07See you later! I think maybe I'll take a little nap."},
 6281: {QUEST: "Head over and call on Teddy Blair. He's got a job for you._where_"},
 6282: {GREETING: '',
        LEAVING: '',
        QUEST: "What did you say? No, I don't have a fob for you.\x07Oh, a job! Why didn't you say so? You'll need to speak up.\x07Those Cogs make it hard to hibernate. If you'll help make Dreamland quieter,\x07I'll give you a little something.",
        INCOMPLETE_PROGRESS: "You beat the bogs? What bogs?\x07Oh, the Cogs! Why didn't you say so?\x07Hmm, it's still pretty loud. How 'bout you defeat a few more?",
        COMPLETE: "You had fun? Huh? Oh!\x07You're done! Great. Really nice of you to help out this way.\x07I found this in the back room but I don't have any use for it.\x07Maybe you'll find something to do with it. So long, _avName_!"},
 6291: {QUEST: 'Cogs broke into the First Security Blanket Bank! Go see William Teller and see if you can help.'},
 6292: {QUEST: 'Oh those darn Cashbot Cogs! They stole my reading lamps!\x07I need them back right away. Can you go look for them?\x07If you can get my reading lamps, I might be able to help you get into see the C.F.O.\x07Hurry!',
        INCOMPLETE_PROGRESS: 'I need those lamps back. Keep looking for them!',
        COMPLETE: "You're back! And you got my lamps!\x07I can't thank you enough but I can give you this."},
 7201: {QUEST: 'Nina Nightlight was looking for you, _avName_. She needs some help._where_'},
 7202: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh! I'm so glad to see you, _avName_. I could use some help!\x07Those darn Cogs have kept the delivery folks away and I have no beds in stock.\x07Could you go see Hardy O'Toole and bring me back a bed?_where_ ",
        INCOMPLETE_PROGRESS: "Did Hardy have any beds? I was sure he'd have one.",
        COMPLETE: ''},
 7203: {GREETING: '',
        LEAVING: '',
        QUEST: 'A bed? Sure, here\'s one all ready to go.\x07Just bring it over to her for me, would you? Get it?\x07"WOOD" you? Hee-hee!\x07Pretty funny. No? Well, take it over there anyway, please?',
        INCOMPLETE_PROGRESS: 'Did Nina like the bed?',
        COMPLETE: ''},
 7204: {GREETING: '',
        LEAVING: '',
        QUEST: "This bed isn't right. It's much too plain.\x07Go see if he has anything fancier, would you?\x07I'm sure it won't take but a minute.",
        INCOMPLETE_PROGRESS: "I'm certain that Hardy has a fancier bed.",
        COMPLETE: ''},
 7205: {GREETING: '',
        LEAVING: '',
        QUEST: "Didn't hit the nail on the head with that bed, huh? I've got one here that will do the job.\x07One small problem though - it needs to be assembled first.\x07While I hammer out this problem, could you get rid of some of those Cogs that are outside?\x07Those awful Cogs throw a wrench in the works.\x07Come back when you're done and the bed will be ready.",
        INCOMPLETE_PROGRESS: "Not quite done with assembling the bed.\x07When you're done with the Cogs, it'll be ready.",
        COMPLETE: ''},
 7206: {GREETING: '',
        LEAVING: '',
        QUEST: 'Hey there _avName_!\x07You did a bang-up job on those Cogs.\x07The bed is all ready. Could you please deliver it for me?\x07Now that those Cogs are gone, business will be brisk!',
        INCOMPLETE_PROGRESS: "I think Nina's waiting for that bed delivery.",
        COMPLETE: 'What a lovely bed!\x07Now my customers will be happy. Thanks, _avName_.\x07Say, you might be able to use this. Someone left it here.'},
 7209: {QUEST: 'Go see Honey Moon. She needs some help._where_'},
 7210: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh! I'm so glad to see you, _avName_. I really need some help!\x07I haven't been able to get my beauty sleep for ages. You see, those Cogs stole my bedspread.\x07Say, could you please run over and see if Ed's got anything in blue?_where_",
        INCOMPLETE_PROGRESS: 'What did Ed have to say about a blue bedspread?',
        COMPLETE: ''},
 7211: {GREETING: '',
        LEAVING: '',
        QUEST: "So, Honey wants a bedspread, huh?\x07What color? BLUE?!\x07Well, I'd have to make that for her special. Everything I've got is red.\x07Tell ya what...if you'll go deal with some of those Cogs out there, I'll make a special blue bedspread just for her.\x07Blue bedspreads...what'll it be next?",
        INCOMPLETE_PROGRESS: 'Still working on this blue bedspread, _avName_. Keep at those Cogs!',
        COMPLETE: ''},
 7212: {GREETING: '',
        LEAVING: '',
        QUEST: "Nice to see you again. I've got something for you!\x07Here's the bedspread and it's blue. She'll love it.",
        INCOMPLETE_PROGRESS: 'Did Honey like the bedspread?',
        COMPLETE: ''},
 7213: {GREETING: '',
        LEAVING: '',
        QUEST: "My bedspread? No, that's not right.\x07It's PLAID! How can anyone sleep with such a LOUD pattern?\x07You'll just have to take it back and get a different one.\x07I'm sure he'll have others.",
        INCOMPLETE_PROGRESS: 'I simply will not accept a plaid bedspread. See what Ed can do about it.',
        COMPLETE: ''},
 7214: {GREETING: '',
        LEAVING: '',
        QUEST: "What? She doesn't like PLAID?\x07Hmm...let me see what we've got here.\x07This will take a while. Why don't you go take care of a few Cogs while I try to find something else?\x07I'll have something by the time you get back here.",
        INCOMPLETE_PROGRESS: "I'm still looking for another bedspread. How's it going with the Cogs?",
        COMPLETE: ''},
 7215: {GREETING: '',
        LEAVING: '',
        QUEST: "Hey, good job on those Cogs!\x07Here you go, it's blue and it's not plaid.\x07Sure hope she likes paisley.\x07Bring the bedspread back to Honey.",
        INCOMPLETE_PROGRESS: "That's all I've got for you right now.\x07Please bring that bedspread to Honey.",
        COMPLETE: "Oh! That's lovely! Paisley suits me quite well.\x07Time for my beauty sleep, then! So long, _avName_.\x07What? You're still here? Can't you see I'm trying to sleep?\x07Here, take this and let me rest. I must look a fright!"},
 7218: {QUEST: 'Dreamy Daphne could use a hand._where_'},
 7219: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh, _avName_, I'm glad to see you! Those Cogs took my pillows.\x07Could you go see if Tex has some pillows?_where_\x07I'm sure he can help.",
        INCOMPLETE_PROGRESS: 'Does Tex have any pillows for me? ',
        COMPLETE: ''},
 7220: {GREETING: '',
        LEAVING: '',
        QUEST: "Howdy! Daphne needs some pillows, huh? Well, you came to the right place, pardner!\x07More pillows in here than there's spines on a cactus.\x07Here you go, _avName_. Take these back over to Daphne with my compliments.\x07Always glad to help a gal out.",
        INCOMPLETE_PROGRESS: 'Were those pillows soft enough for the little lady?',
        COMPLETE: ''},
 7221: {GREETING: '',
        LEAVING: '',
        QUEST: "You got the pillows! Great!\x07Hey, wait a second! These pillows are awfully soft.\x07Much too soft for me. I need harder pillows.\x07Take these back to Tex and see what else he's got. Thanks.",
        INCOMPLETE_PROGRESS: 'Nope! Too soft. Ask Tex for different pillows.',
        COMPLETE: ''},
 7222: {GREETING: '',
        LEAVING: '',
        QUEST: "Too soft, huh? Well, let me see what I've got....\x07Hmm...seems I had me a whole passel of hard pillows. Where'd they get to?\x07Oh! I remember. I was fixing to send them back so they're in storage.\x07How 'bout you clean up some of those Cog buildings out there while I get 'em out of storage, pardner?",
        INCOMPLETE_PROGRESS: "Cog buildings are hard. But these pillows aren't.\x07I'll keep looking.",
        COMPLETE: ''},
 7223: {GREETING: '',
        LEAVING: '',
        QUEST: "Back already? Well, that's jess fine. See, I found those pillows Daphne wanted.\x07Now, you jess take these over to her. They're hard enough to break a tooth on!",
        INCOMPLETE_PROGRESS: "Yeah, those pillows are mighty hard. I hope Daphne fancies 'em.",
        COMPLETE: 'I knew Tex would have some harder pillows.\x07Oh yes, those are perfect. Nice and hard.\x07Would you have a use for this piece of a Cog suit? Might as well take it with you.'},
 7226: {QUEST: "Drop by to see Sandy Sandman. She's lost her pajamas._where_"},
 7227: {GREETING: '',
        LEAVING: '',
        QUEST: "I have no pajamas! They're missing!\x07What will I do? Oh! I know!\x07Go see Big Mama. She'll have pajamas for me._where_",
        INCOMPLETE_PROGRESS: 'Does Big Mama have pajamas for me?',
        COMPLETE: ''},
 7228: {GREETING: '',
        LEAVING: '',
        QUEST: "Hey there, little toon! Big Mama's got the best pajamas from the Bahamas.\x07Oh, something for Sandy Sandman, huh? Well, let me see what I've got.\x07Here's a little something. Now she can sleep in style!\x07Would you run these back over to her for me? I can't leave the shop just now.\x07Thanks, _avName_. See you around!",
        INCOMPLETE_PROGRESS: 'You need to take those pajamas to Sandy._where_',
        COMPLETE: ''},
 7229: {GREETING: '',
        LEAVING: '',
        QUEST: "Big Mama sent these for me? Oh...\x07Doesn't she have any pajamas with feet on them?\x07I always wear pajamas with feet. Doesn't everybody?\x07Take these back and ask her to find some with feet.",
        INCOMPLETE_PROGRESS: 'My pajamas must have feet. See what Big Mama can do.',
        COMPLETE: ''},
 7230: {GREETING: '',
        LEAVING: '',
        QUEST: "Feet? Let me think....\x07Wait! I've got just the thing!\x07Ta-dah! Pajamas with feet. Nice blue pajamas with feet. Best ones on any island.\x07Please take them back to her, would you? Thanks!",
        INCOMPLETE_PROGRESS: 'Did Sandy like the blue footie pajamas?',
        COMPLETE: ''},
 7231: {GREETING: '',
        LEAVING: '',
        QUEST: "Well, these DO have feet, but I can't wear blue pajamas!\x07Ask Big Mama if she has a different color.",
        INCOMPLETE_PROGRESS: "I'm sure Big Mama has footie pajamas in a different color.",
        COMPLETE: ''},
 7232: {GREETING: '',
        LEAVING: '',
        QUEST: "That's too bad. These are the only pajamas with feet I have.\x07Oh, I've got an idea. Go ask Cat. She may have some pajamas with feet._where_",
        INCOMPLETE_PROGRESS: "Nope, those are all the pajamas I've got. Go see what Cat has._where_",
        COMPLETE: ''},
 7233: {GREETING: '',
        LEAVING: '',
        QUEST: "Pajamas with feet? Sure thing.\x07What do you mean, these are blue? She doesn't want blue?\x07Oh, that's a little trickier. Here, try these.\x07They're not blue and they DO have feet.",
        INCOMPLETE_PROGRESS: "I just love puce, don't you?\x07I hope Sandy likes them....",
        COMPLETE: ''},
 7234: {GREETING: '',
        LEAVING: '',
        QUEST: "No, these aren't blue but no one with my complexion could possibly wear puce.\x07Absolutely not. Back they go and you with them! See what else Cat has.",
        INCOMPLETE_PROGRESS: 'Cat must have more pajamas. No puce for me!',
        COMPLETE: ''},
 7235: {GREETING: '',
        LEAVING: '',
        QUEST: "Not puce either. Hmm....\x07By my whiskers, I know I have some other ones.\x07They'll take a little while to find. Let's make a deal.\x07I'll find the other pajamas if you'll get rid of some of these Cog buildings. They're very unsettling.\x07I'll have the pajamas ready when you get back, _avName_.",
        INCOMPLETE_PROGRESS: 'You need to clear out a few more Cog buildings while I look for other pajamas.',
        COMPLETE: ''},
 7236: {GREETING: '',
        LEAVING: '',
        QUEST: 'You did a great job on those Cogs! Thanks!\x07I found those pajamas for Sandy; hope she likes them.\x07Bring them over to her. Thank you.',
        INCOMPLETE_PROGRESS: "Sandy's waiting for those pajamas, _avName_.",
        COMPLETE: "Fuchsia pajamas with feet! Purr-fect!\x07Ah, now I'm all set. Let's see....\x07Oh, I suppose I should give you something for helping me out.\x07Maybe you can use this. Someone left it here."},
 7239: {QUEST: "Go see Smudgy Mascara. She's been looking for some help._where_"},
 7240: {GREETING: '',
        LEAVING: '',
        QUEST: 'Those darn Cogs took my wrinkle cream!\x07My customers simply MUST have wrinkle cream while I work on them.\x07Go see Rip and see if he has my special formula in stock._where_',
        INCOMPLETE_PROGRESS: 'I refuse to work on anyone without wrinkle cream.\x07See what Rip has for me.'},
 7241: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh, that Smudgy's a picky character. She won't settle for my usual formula.\x07That means I'll need some cauliflower coral, my super-secret special ingredient. But I haven't any in stock.\x07Could you go fish some out of the pond for me? As soon as you get the coral, I'll whip up a batch for Smudgy.",
        INCOMPLETE_PROGRESS: "I'll need that cauliflower coral to make a batch of wrinkle cream."},
 7242: {GREETING: '',
        LEAVING: '',
        QUEST: "Wow, that's a nice cauliflower coral!\x07Ok, let's see...a little of this and a splash of that...now, just a dollop of kelp.\x07Huh, where's the kelp? Looks like I'm out of kelp, too.\x07Could you pop down to the pond and fish me out some nice, slimy kelp?",
        INCOMPLETE_PROGRESS: "Not a strip of slimy kelp in the shop.\x07Can't make the cream without it."},
 7243: {GREETING: '',
        LEAVING: '',
        QUEST: "Oooh! Very slimy kelp you've got there, _avName_.\x07Now, I just crush some pearls with the mortar and pestle.\x07Um, where's my pestle? What good is a mortar without a pestle?\x07I bet that darn Loan Shark took it when he came in here!\x07You need to help me find it! He was headed for Cashbot HQ!",
        INCOMPLETE_PROGRESS: 'I simply cannot crush the pearls without a pestle.\x07Darn those Loan Sharks!'},
 7244: {GREETING: '',
        LEAVING: '',
        QUEST: "Alright! You got my pestle!\x07Now we're in business. Crush that...stir this up and...\x07There ya go! Tell Smudgy's it's good and fresh.",
        INCOMPLETE_PROGRESS: "You should bring this over to Smudgy while it's fresh.\x07She's very picky.",
        COMPLETE: "Didn't Rip have a bigger jar of wrinkle cream than this? No?\x07Well, I guess I'll just order more when I run out.\x07So long, _avName_.\x07What? You're still here? Can't you see I'm trying to work?\x07Here, take this."},
 11000: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you are interested in Lawbot disguise parts you should visit _toNpcName_.\x07I hear he could use some help with his weather research._where_'},
 11001: {GREETING: '',
         LEAVING: '',
         QUEST: 'Yes, yes. I have Lawbot disguise parts.\x07But they are of no interest to me.\x07The focus of my research is fluctuations in the ambient temperature of Toontown.\x07I will gladly trade you disguise parts for cog temperature sensors.\x07You can start on %s.' % GlobalStreetNames[2100][-1],
         INCOMPLETE_PROGRESS: 'Have you tried looking on %s?' % GlobalStreetNames[2100][-1],
         COMPLETE: 'Ah, excellent!\x07Just as I feared...\x07Oh, yes! Here is your disguise part.'},
 11002: {GREETING: '',
         LEAVING: '',
         QUEST: 'For more Lawbot disguise parts you should visit _toNpcName_ again.\x07I hear he needs more research assistants._where_'},
 11003: {GREETING: '',
         LEAVING: '',
         QUEST: 'More Lawbot disguise parts?\x07Well, if you insist...\x07but I will require another cog temperature sensor.\x07This time look on %s.' % GlobalStreetNames[2200][-1],
         INCOMPLETE_PROGRESS: 'You are looking on %s, right?' % GlobalStreetNames[2200][-1],
         COMPLETE: 'Thank you!\x07And here is your disguise part.'},
 11004: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you need more Lawbot disguise parts you should return to _toNpcName_.\x07I hear he still needs help with his weather reasearch._where_'},
 11005: {GREETING: '',
         LEAVING: '',
         QUEST: "You're proving yourself quite useful!\x07Can you take a look on %s?" % GlobalStreetNames[2300][-1],
         INCOMPLETE_PROGRESS: "Are you sure you're looking on %s?" % GlobalStreetNames[2300][-1],
         COMPLETE: "Hmmm, I don't like the looks of this...\x07but here is your disguise part..."},
 11006: {GREETING: '',
         LEAVING: '',
         QUEST: 'You-know-who needs more temperature readings.\x07Stop by if you would like another disguise part._where_'},
 11007: {GREETING: '',
         LEAVING: '',
         QUEST: 'Back again?\x07You are very dedicated...\x07The next stop is %s.' % GlobalStreetNames[1100][-1],
         INCOMPLETE_PROGRESS: 'Have you tried looking on %s?' % GlobalStreetNames[1100][-1],
         COMPLETE: 'Good! You seem to be getting the hang of this!\x07Your disguise part...'},
 11008: {GREETING: '',
         LEAVING: '',
         QUEST: "If you're up for another Lawbot disguise part..._where_"},
 11009: {GREETING: '',
         LEAVING: '',
         QUEST: 'Fancy seeing you here!\x07Now I need readings on %s.' % GlobalStreetNames[1200][-1],
         INCOMPLETE_PROGRESS: 'You are looking on %s, right?' % GlobalStreetNames[1200][-1],
         COMPLETE: 'Thank you very much.\x07Your disguise must be getting close...'},
 11010: {GREETING: '',
         LEAVING: '',
         QUEST: 'I believe _toNpcName_ has more work for you._where_'},
 11011: {GREETING: '',
         LEAVING: '',
         QUEST: 'Good to see you again, _avName_!\x07Can you get a reading on %s, please?' % GlobalStreetNames[1300][-1],
         INCOMPLETE_PROGRESS: 'Have you tried looking on %s?' % GlobalStreetNames[1300][-1],
         COMPLETE: "Great work!\x07Here's your well earned reward!"},
 11012: {GREETING: '',
         LEAVING: '',
         QUEST: 'You know the drill._where_'},
 11013: {GREETING: '',
         LEAVING: '',
         QUEST: '_avName_, my dear friend!\x07Can you go to %s and find another temperature sensor?' % GlobalStreetNames[5100][-1],
         INCOMPLETE_PROGRESS: "Are you sure you're looking on %s?" % GlobalStreetNames[5100][-1],
         COMPLETE: "Excellent!\x07With your help my research is coming quickly!\x07Here's your reward."},
 11014: {GREETING: '',
         LEAVING: '',
         QUEST: "_toNpcName_ was asking for you by name.\x07It appears you've made quite an impression!_where_"},
 11015: {GREETING: '',
         LEAVING: '',
         QUEST: "Welcome back!\x07I've been waiting for you.\x07The next reading I need is on %s." % GlobalStreetNames[5200][-1],
         INCOMPLETE_PROGRESS: 'You are looking on %s, right?' % GlobalStreetNames[5200][-1],
         COMPLETE: "Thanks!\x07Here's your reward."},
 11016: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you need to finish your Lawbot disguise...\x07_toNpcName_ can help you out._where_'},
 11017: {GREETING: '',
         LEAVING: '',
         QUEST: 'Hello, Junior Research Scientist!\x07We still need readings from %s.' % GlobalStreetNames[5300][-1],
         INCOMPLETE_PROGRESS: 'Have you tried looking on %s?' % GlobalStreetNames[5300][-1],
         COMPLETE: 'Excellent job!\x07Here is your Lawbot thingy...'},
 11018: {GREETING: '',
         LEAVING: '',
         QUEST: "_toNpcName_ has another job for you.\x07If you're not sick of him yet..._where_"},
 11019: {GREETING: '',
         LEAVING: '',
         QUEST: 'Well, then.\x07Are you ready for another recovery?\x07This time try %s.' % GlobalStreetNames[4100][-1],
         INCOMPLETE_PROGRESS: "Are you sure you're looking on %s?" % GlobalStreetNames[4100][-1],
         COMPLETE: 'Another one!\x07My you are the picture of efficiency!'},
 11020: {GREETING: '',
         LEAVING: '',
         QUEST: 'Are you still after Lawbot disguise parts?_where_'},
 11021: {GREETING: '',
         LEAVING: '',
         QUEST: 'You could probably guess by now...\x07but I need readings from %s.' % GlobalStreetNames[4200][-1],
         INCOMPLETE_PROGRESS: 'You are looking on %s, right?' % GlobalStreetNames[4200][-1],
         COMPLETE: 'Almost there!\x07Here you go...'},
 11022: {GREETING: '',
         LEAVING: '',
         QUEST: 'I hate to say it, but..._where_'},
 11023: {GREETING: '',
         LEAVING: '',
         QUEST: 'What do you think about %s? Could you get a sensor from there too?' % GlobalStreetNames[4300][-1],
         INCOMPLETE_PROGRESS: 'Have you tried looking on %s?' % GlobalStreetNames[4300][-1],
         COMPLETE: 'Another excellent job, _avName_'},
 11024: {GREETING: '',
         LEAVING: '',
         QUEST: 'Go visit the Professor if you still need disguise parts._where_'},
 11025: {GREETING: '',
         LEAVING: '',
         QUEST: 'I believe we still need a reading from %s.' % GlobalStreetNames[9100][-1],
         INCOMPLETE_PROGRESS: "Are you sure you're looking on %s?" % GlobalStreetNames[9100][-1],
         COMPLETE: 'Good work!\x07I think we are getting very close...'},
 11026: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ has one final mission for you._where_'},
 11027: {GREETING: '',
         LEAVING: '',
         QUEST: 'Back so soon?\x07The final reading is on %s.' % GlobalStreetNames[9200][-1],
         INCOMPLETE_PROGRESS: 'You are looking on %s, right?' % GlobalStreetNames[9200][-1],
         COMPLETE: "You're all done!\x07Now you are ready to infiltrate the District Attorney's Office and collect Jury Notices.\x07Good luck and thanks for all your help!"},
 12000: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you are interested in Bossbot disguise parts you should visit _toNpcName_._where_'},
 12001: {GREETING: '',
         LEAVING: '',
         QUEST: "Yes, I can get you Bossbot parts.\x07But I'll need you to help me complete my Bossbot collection.\x07Go out there and defeat a Flunky.",
         INCOMPLETE_PROGRESS: "You can't find a Flunky? For shame...",
         COMPLETE: "You didn't flunk that, now did you?\x07Here's your first disguise part."},
 12002: {GREETING: '',
         LEAVING: '',
         QUEST: "_toNpcName_ needs more help, if you're up for it._where_"},
 12003: {GREETING: '',
         LEAVING: '',
         QUEST: 'Another disguise part?\x07Certainly...\x07but only if you defeat a Pencil Pusher.',
         INCOMPLETE_PROGRESS: 'Pencil Pushers can be found in the streets.',
         COMPLETE: "He was a real pushover!\x07Here's your second disguise part."},
 12004: {GREETING: '',
         LEAVING: '',
         QUEST: "There's really only one place to go for Bossbot parts._where_"},
 12005: {GREETING: '',
         LEAVING: '',
         QUEST: 'Now I need a Yesman...',
         INCOMPLETE_PROGRESS: 'Yesmen can be found in the streets.',
         COMPLETE: "Yes! Man, you are good.\x07Here's your third disguise part."},
 12006: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ has more parts for you...'},
 12007: {GREETING: '',
         LEAVING: '',
         QUEST: "If you defeat a Micromanager I'll give you another part.",
         INCOMPLETE_PROGRESS: 'Try looking on %s' % GlobalStreetNames[1100][-1],
         COMPLETE: "You managed that quite well!\x07Here's your fourth disguise part."},
 12008: {GREETING: '',
         LEAVING: '',
         QUEST: 'Head on over to..._where_'},
 12009: {GREETING: '',
         LEAVING: '',
         QUEST: "I'm after a Downsizer now...",
         INCOMPLETE_PROGRESS: 'Having trouble? Try looking on %s' % GlobalStreetNames[3100][-1],
         COMPLETE: "He went down hard!\x07Here's your fifth disguise part."},
 12010: {GREETING: '',
         LEAVING: '',
         QUEST: 'I think you know where to go by now..._where_'},
 12011: {GREETING: '',
         LEAVING: '',
         QUEST: 'A Head Hunter is next on my list.',
         INCOMPLETE_PROGRESS: 'You might have better luck looking buildings.',
         COMPLETE: "I see you had no problem hunting one down.\x07Here's your sixth disguise part."},
 12012: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ needs more Bossbots.'},
 12013: {GREETING: '',
         LEAVING: '',
         QUEST: "Next I'll need you to track down a Corporate Raider.",
         INCOMPLETE_PROGRESS: 'You might have better luck looking buildings.',
         COMPLETE: "You're quite the little raider yourself!\x07Here's your seventh disguise part."},
 12014: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you want more disguise parts, go to..._where_'},
 12015: {GREETING: '',
         LEAVING: '',
         QUEST: 'Now the coup de grace: The Big Cheese!',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "I knew I could count on you to cut...\x07Ah, never mind.\x07Here's your next disguise part."},
 12016: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ was looking for you...'},
 12017: {GREETING: '',
         LEAVING: '',
         QUEST: 'Now I need you to defeat one of the new, more treacherous Bossbot Cogs.',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: 'They are tougher than they look, huh?\x07I guess I owe you a disguise part.'},
 12018: {GREETING: '',
         LEAVING: '',
         QUEST: 'Could you swing by..._where_'},
 12019: {GREETING: '',
         LEAVING: '',
         QUEST: 'These Version 2.0 Cogs are very interesting.\x07Please go defeat another one.',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: 'Thanks!\x07Another disguise part coming right up.'},
 12020: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you get a chance, stop by and see _toNpcName_.'},
 12021: {GREETING: '',
         LEAVING: '',
         QUEST: 'I wonder if they can keep regenerating...',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "I guess not.\x07Here's your part..."},
 12022: {GREETING: '',
         LEAVING: '',
         QUEST: 'You know..._where_'},
 12023: {GREETING: '',
         LEAVING: '',
         QUEST: "Maybe they aren't Bossbots at all...",
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: 'Hmmm, I guess they are Bossbots after all.\x07Help yourself to another part.'},
 12024: {GREETING: '',
         LEAVING: '',
         QUEST: "You probably know what I'm going to say already..."},
 12025: {GREETING: '',
         LEAVING: '',
         QUEST: 'Perhaps they are related to the Skelecogs somehow...',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "That was inconclusive...\x07Here's your disguise part."},
 12026: {GREETING: '',
         LEAVING: '',
         QUEST: 'Please go see _toNpcName_ again.'},
 12027: {GREETING: '',
         LEAVING: '',
         QUEST: "I'm still not convinced they aren't some type of Skelecog...",
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "Well, maybe not.\x07Here's your next part."},
 12028: {GREETING: '',
         LEAVING: '',
         QUEST: "It's probably the last place you want to go. but..."},
 12029: {GREETING: '',
         LEAVING: '',
         QUEST: 'I am still quite baffled by these new cogs.\x07Could you go defeat another, please?',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: 'Fascinating. Simply fascinating.\x07A disguise part for your troubles.'},
 12030: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ is starting to sound like a broken record...'},
 12031: {GREETING: '',
         LEAVING: '',
         QUEST: "I've almost determined what these new Cogs are.\x07Just one more...",
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "Yes, I think I'm onto something.\x07Oh, yes.\x07This is for you..."},
 12032: {GREETING: '',
         LEAVING: '',
         QUEST: 'You need to go tell Flippy about this...',
         INCOMPLETE_PROGRESS: 'Flippy can be found in Toon Hall',
         COMPLETE: 'A new type of Cog!\x07Good work!\x07Here is your final disguise part.'}}
ChatGarblerDog = ['woof', 'arf', 'rruff']
ChatGarblerCat = ['meow', 'mew']
ChatGarblerMouse = ['squeak', 'squeaky', 'squeakity']
ChatGarblerHorse = ['neigh', 'brrr']
ChatGarblerRabbit = ['eek', 'eepr', 'eepy', 'eeky']
ChatGarblerDuck = ['quack', 'quackity', 'quacky']
ChatGarblerMonkey = ['ooh', 'ooo', 'ahh']
ChatGarblerBear = ['growl', 'grrr']
ChatGarblerPig = ['oink', 'oik', 'snort']
ChatGarblerDefault = ['blah']
Bossbot = 'Royalbot'
Lawbot = 'Courtbot'
Cashbot = 'Carebot'
Sellbot = 'Fashionbot'
BossbotS = 'a Royalbot'
LawbotS = 'a Courtbot'
CashbotS = 'a Fashionbot'
SellbotS = 'a Carebot'
BossbotP = 'Royalbots'
LawbotP = 'Courtbots'
CashbotP = 'Carebots'
SellbotP = 'Fashionbots'
BossbotSkelS = 'a Royalbot Droid'
LawbotSkelS = 'a Courtbot Droid'
CashbotSkelS = 'a Carebot Droid'
SellbotSkelS = 'a Fashionbot Droid'
BossbotSkelP = 'Royalbot Droids'
LawbotSkelP = 'Courtbot Droids'
CashbotSkelP = 'Carebot Droids'
SellbotSkelP = 'Fashionbot Droids'
SkeleRevivePostFix = ' v%s.0'
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = lClose
AvatarDetailPanelLookup = 'Looking up details for %s.'
AvatarDetailPanelFailedLookup = 'Unable to get details for %s.'
AvatarDetailPanelOnline = 'District: %(district)s\nLocation: %(location)s\nIdentifier: %(identifier)s'
AvatarDetailPanelOffline = 'District: offline\nLocation: offline\nIdentifier: %(identifier)s'
OfflineLocation = 'Offline'
AvatarPanelFriends = 'Friends'
AvatarPanelWhisper = 'Whisper'
AvatarPanelTrueFriends = 'True Friends'
AvatarPanelGoTo = 'Go To'
AvatarPanelPet = 'Show Doodle'
AvatarPanelIgnore = 'Ignore'
AvatarPanelIgnoreCant = 'Okay'
AvatarPanelStopIgnoring = 'Stop Ignoring'
AvatarPanelReport = 'Report'
AvatarPanelCogLevel = 'Level: %s'
AvatarPanelCogDetailClose = lClose
AvatarPanelDetail = 'Toon Details'
AvatarPanelGroupInvite = 'Invite'
AvatarPanelGroupMerge = 'Resulting in'
AvatarPanelGroupRetract = 'Retract Invitation'
AvatarPanelGroupMember = 'Already In Group'
AvatarPanelGroupMemberKick = 'Remove'
AvatarPanelCast = 'Cast Member'
AvatarPanelCastInfo = '%s is a Toontown Stride Cast Member.'
ReportPanelTitle = 'Report A Toon'
ReportPanelBody = 'This feature will send a complete report to a Moderator. Instead of sending a report, you might choose to do one of the following:\n\n  - Teleport to another district\n  - Use "Ignore" on the toon\'s panel\n\nDo you really want to report %s to a Moderator?'
ReportPanelBodyFriends = 'This feature will send a complete report to a Moderator. Instead of sending a report, you might choose to do one of the following:\n\n  - Teleport to another district\n  - Break your friendship\n\nDo you really want to report %s to a Moderator?\n\n(This will also break your friendship)'
ReportPanelCategoryBody = 'You are about to report %s. A Moderator will be alerted to your complaint and will take appropriate action for anyone breaking our rules. Please choose the reason you are reporting %s:'
ReportPanelCategoryLanguage = 'Inappropriate Language'
ReportPanelCategoryRude = 'Rude or Mean Behavior'
ReportPanelCategoryName = 'Bad Name'
ReportPanelCategoryHacking = 'Hacking'
ReportPanelCategoryGreening = 'Greening'
ReportPanelConfirmations = ('You are about to report that %s has used obscene, bigoted or sexually explicit language.',
 'You are about to report that %s has disrupted your experience by intentionally causing your toon to go sad.',
 'You are about to report that %s is bullying, harassing, or using extreme behavior to disrupt the game.',
 "You are about to report that %s has created a name that does not follow the rules.",
 'You are about to report that %s has hacked/tampered with the game or used third party software.')
ReportPanelWarning = "We take reporting very seriously. Your report will be viewed by a Moderator who will take appropriate action for anyone breaking our rules. If your account is found to have participated in breaking the rules, or if you make false reports or abuse the 'Report a Toon' system, a Moderator may take action against your account. Are you absolutely sure you want to report this toon?"
ReportPanelThanks = 'Thank you! Your report has been sent to a Moderator for review. There is no need to contact us again about the issue. The moderation team will take appropriate action for a toon found breaking our rules.'
ReportPanelRemovedFriend = 'We have automatically removed %s from your Toon Friends List.'
ReportPanelAlreadyReported = 'You have already reported %s during this session. A Moderator will review your previous report.'
IgnorePanelTitle = 'Ignore A Toon'
IgnorePanelAddIgnore = 'Would you like to ignore %s?'
IgnorePanelIgnore = 'You are now ignoring %s.'
IgnorePanelRemoveIgnore = 'Would you like to stop ignoring %s?'
IgnorePanelEndIgnore = 'You are no longer ignoring %s.'
IgnorePanelAddFriendAvatar = '%s is your friend, you cannot ignore them while you are friends.'
PetPanelFeed = 'Feed'
PetPanelCall = 'Call'
PetPanelGoTo = 'Go To'
PetPanelOwner = 'Show Owner'
PetPanelDetail = 'Pet Details'
PetPanelScratch = 'Scratch'
PetDetailPanelTitle = 'Trick Training'
PetTrickStrings = {0: 'Jump',
 1: 'Beg',
 2: 'Play dead',
 3: 'Rollover',
 4: 'Backflip',
 5: 'Dance',
 6: 'Speak'}
PetMoodAdjectives = {'neutral': 'neutral',
 'hunger': 'hungry',
 'boredom': 'bored',
 'excitement': 'excited',
 'sadness': 'sad',
 'restlessness': 'restless',
 'playfulness': 'playful',
 'loneliness': 'lonely',
 'fatigue': 'tired',
 'confusion': 'confused',
 'anger': 'angry',
 'surprise': 'surprised',
 'affection': 'affectionate'}
SpokenMoods = {'neutral': 'neutral',
 'hunger': ["I'm tired of Jellybeans! How'bout giving me a slice of pie?", "How'bout a Red Jellybean? I'm tired of the Green ones!", "Oh, those Jellybeans were for planting?!! But I'm hungry!"],
 'boredom': ["I'm dying of boredom over here!", "You didn't think I understood you, huh?", 'Could we, like, DO something already?'],
 'excitement': ["Wow, it's you, it's you, it's you!",
                'mmm, Jellybeans, mmm!',
                'Does it GET any better than this?',
                "Happy April Toons' Week!"],
 'sadness': ["Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go...", "I'll be good, I promise!", "I don't know WHY I'm sad, I just am!!!"],
 'restlessness': ["I'm sooo restless!!!"],
 'playfulness': ["Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play...", 'Play with me or I dig up some flowers!', 'Lets run around and  around and around and around and around and around...'],
 'loneliness': ['Where have you been?', 'Wanna cuddle?', 'I want to go with you when you fight Cogs!'],
 'fatigue': ['That swim in the pond really tired me out!', 'Being a Doodle is exhausting!', 'I gotta get to Dreamland!'],
 'confusion': ['Where am I? Who are you again?', "What's a Toon-up again?", "Whoa, I'm standing between you and the Cogs! Run away!"],
 'anger': ['... and you wonder why I never give you a Toon-up?!!!', 'You always leave me behind!', 'You love your gags more than you love me!'],
 'surprise': ['Of course Doodles can talk!', 'Toons can talk?!!', 'Whoa, where did you come from?'],
 'affection': ["You're the best Toon EVER!!!!!!!!!!", 'Do you even KNOW how great you are?!?', 'I am SO lucky to be with you!!!']}
DialogQuestion = '?'
FriendsListLabel = 'Friends'
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = 'Trying to go to %s.'
TeleportPanelNotAvailable = '%s is busy right now; try again later.'
TeleportPanelIgnored = '%s is ignoring you.'
TeleportPanelNotOnline = "%s isn't online right now."
TeleportPanelWentAway = '%s went away.'
TeleportPanelUnknownHood = "You don't know how to get to %s!"
TeleportPanelDenySelf = "You can't go to yourself!"
TeleportPanelOtherShard = "%(avName)s is in district %(shardName)s, and you're in district %(myShardName)s.  Do you want to switch to %(shardName)s?"
TeleportPanelBusyShard = '%(avName)s is in a full District.'
BattleBldgBossTaunt = "I see that you made it to the top floor. Now be ready for sadness."
CogdoBattleBldgBossTaunt = "Welcome to the Field Office, be doomed!"
FactoryBossTaunt = "I'm the Designer!"
FactoryBossBattleTaunt = 'Talk to the Designer.'
MintBossTaunt = "I'm the Money Maker!"
MintBossBattleTaunt = 'You need to talk to the Money Maker.'
StageBossTaunt = "I'm the Manager in this office."
StageBossBattleTaunt = 'Talk to the Manager. He will help you.'
CountryClubBossTaunt = "I'm the Lair Master."
CountryClubBossBattleTaunt = 'You need to talk to the Lair Master.'
ForcedLeaveCountryClubAckMsg = 'The Club President was defeated before you could reach him. You did not recover any Stock Options.'
ToonHealJokes = [['What should you love on?', 'Head Hunters!'],
 ['Yo Chris guess what?', "You rule!"],
 ['What should I do?', 'I should sue somebody cuz me bored.'],
 ["I'm gonna do it, I'm gonna do it.", 'I am so not dating a Head Hunter!'],
 ['Who is a furry?', 'Master Cool Cat!'],
 ["Why did Dark Angel ride on a broom?", "So she could fall off of it cause she don't know how to power one!"],
 ['Why did the Toon run away from the Cog?', 'Because the Cog was not a Head Hunter.'],
 ['Why did the Boos boo?', 'Because they are Noobs.'],
 ['Why did the chicken cross the road?', 'Cause he went sad. What a Noob.'],
 ['What flower is blue?', 'ROZIE!'],
 ["Who is the best character?", "Family Guy!"],
 ["What's the best ship?", 'DORA X DORA!'],
 ["Why did the CFO quit his job?", 'Cause he saw his ride to money. OH WHAT A MR KRABS WANNABE!'],
 ['What did big bear say to little bear?', "YOU SCRAM! I'M BIGGER THAN YOU!"],
 ['Hey what is this?', 'OH NO A PILE OF GUM! GO AWAY NO!'],
 ['What is this?', 'No! Get out! No! Mine!'],
 ['What is a blueberry made of?', 'Jellyious.']]
MovieHealLaughterMisses = ('What.',
 'Why.',
 ':(',
 ':(')
MovieHealLaughterHits1 = ('Ha Ha Ha',
 'Hee Hee',
 'Tee Hee',
 'Ha Ha')
MovieHealLaughterHits2 = ('BWAH HAH HAH!', 'HO HO HO!', 'HA HA HA!')
MovieSOSCallHelp = '%s HELP!'
MovieSOSWhisperHelp = '%s needs help in battle!'
MovieSOSObserverHelp = 'HELP!'
MovieNPCSOSGreeting = 'Hi %s! Glad to help!'
MovieNPCSOSGoodbye = 'See you later!'
MovieNPCSOSToonsHit = 'Toons Always Hit!'
MovieNPCSOSCogsMiss = 'Cogs Always Miss!'
MovieNPCSOSRestockGags = 'Restocking %s gags!'
MovieNPCSOSHeal = 'Heal'
MovieNPCSOSTrap = 'Trap'
MovieNPCSOSLure = 'Stun'
MovieNPCSOSSound = 'Instruments'
MovieNPCSOSThrow = 'Dessert'
MovieNPCSOSSquirt = 'Water'
MovieNPCSOSDrop = 'Drop'
MovieNPCSOSAll = 'All'
MoviePetSOSTrickFail = 'Sigh...'
MoviePetSOSTrickSucceedBoy = 'Good boy!'
MoviePetSOSTrickSucceedGirl = 'Good girl!'
MovieSuitCancelled = 'CANCELLED\nCANCELLED\nCANCELLED'
RewardPanelToonTasks = 'ToonTasks'
RewardPanelItems = 'Items Recovered'
RewardPanelMissedItems = 'Items Not Recovered'
RewardPanelQuestLabel = 'Quest %s'
RewardPanelCongratsStrings = ['YAY! YOU DID IT!',
 'GROUNDED GROUNDED GROUNDED!',
 'SUING!!!!!',
 'DORA!!!!',
 'HAMBURGERS!!!!!!!!!',
 'WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!']
RewardPanelNewGag = 'New %(gagName)s gag for %(avName)s!'
RewardPanelUberGag = '%(avName)s earned the %(gagName)s gag with %(exp)s experience points!'
RewardPanelEndTrack = 'Yay! %(avName)s has reached the end of the %(gagName)s Gag Track!'
RewardPanelMeritsMaxed = 'Maxed'
RewardPanelMeritBarLabels = ['Pizza',
 'Chicken',
 'Medicine',
 'Fashion Tickets']
RewardPanelMeritAlert = 'Ready for promotion!'
RewardPanelCogPart = 'You gained a Cog disguise part!'
RewardPanelPromotion = 'Ready for promotion in %s  track!'
RewardPanelSkip = 'Skip'
CheesyEffectDescriptions = [('Normal Toon', 'you will be normal'),
 ('Big head', 'you will have a big head'),
 ('Small head', 'you will have a small head'),
 ('Big legs', 'you will have big legs'),
 ('Small legs', 'you will have small legs'),
 ('Big toon', 'you will be a little bigger'),
 ('Small toon', 'you will be a little smaller'),
 ('Flat portrait', 'you will be two-dimensional'),
 ('Flat profile', 'you will be two-dimensional'),
 ('Transparent', 'you will be transparent'),
 ('No color', 'you will be colorless'),
 ('Invisible toon', 'you will be invisible')]
CheesyEffectIndefinite = 'Until you choose another effect, %(effectName)s%(whileIn)s.'
CheesyEffectMinutes = 'For the next %(time)s minutes, %(effectName)s%(whileIn)s.'
CheesyEffectHours = 'For the next %(time)s hours, %(effectName)s%(whileIn)s.'
CheesyEffectDays = 'For the next %(time)s days, %(effectName)s%(whileIn)s.'
CheesyEffectWhileYouAreIn = ' while you are in %s'
CheesyEffectExceptIn = ', except in %s'
SuitFlunky = 'Red Hander'
SuitPencilPusher = 'Pencil Head'
SuitYesman = 'Shiny Stabber'
SuitMicromanager = 'Fancy Kitten'
SuitDownsizer = 'Hudson'
SuitHeadHunter = 'Dr. Simon'
SuitCorporateRaider = 'Scaringler'
SuitTheBigCheese = 'Mozzerella Cheeze'
SuitColdCaller = 'Blue Caller'
SuitTelemarketer = 'Telecaller'
SuitNameDropper = 'Blackler'
SuitGladHander = 'Shaker Wizard'
SuitMoverShaker = 'Scary Dropper'
SuitTwoFace = 'Two-Man'
SuitTheMingler = 'Spongebob'
SuitMrHollywood = 'Amanda Rose'
SuitShortChange = 'Conichange'
SuitPennyPincher = 'Dandy Shark'
SuitTightwad = 'Janet'
SuitBeanCounter = 'Candace Flynn'
SuitNumberCruncher = 'Number Man'
SuitMoneyBags = 'Shiny Mingler'
SuitLoanShark = 'Dark Angel'
SuitRobberBaron = 'Moonlight Mimi'
SuitBottomFeeder = 'Cute Flunky'
SuitBloodsucker = 'Vam\x03pire'
SuitDoubleTalker = 'Sally'
SuitAmbulanceChaser = 'Microripoff'
SuitBackStabber = 'Textured Counter'
SuitSpinDoctor = 'Cog Monkey'
SuitLegalEagle = 'Black Eagle'
SuitBigWig = 'Full Wig'
SuitFlunkyS = 'a Red Hander'
SuitPencilPusherS = 'a Pencil Head'
SuitYesmanS = 'a Shiny Stabber'
SuitMicromanagerS = 'a Fancy Kitten'
SuitDownsizerS = 'a Hudson'
SuitHeadHunterS = 'a Dr. Simon'
SuitCorporateRaiderS = 'a Scaringler'
SuitTheBigCheeseS = 'a Mozzerella Cheese'
SuitColdCallerS = 'a Blue Caller'
SuitTelemarketerS = 'a Telecaller'
SuitNameDropperS = 'a Blackler'
SuitGladHanderS = 'a Shaker Wizard'
SuitMoverShakerS = 'a Scary Dropper'
SuitTwoFaceS = 'a Two-Man'
SuitTheMinglerS = 'a Spongebob'
SuitMrHollywoodS = 'a Amanda Rose'
SuitShortChangeS = 'a Conichange'
SuitPennyPincherS = 'a Dandy Shark'
SuitTightwadS = 'a Janet'
SuitBeanCounterS = 'a Candace Flynn'
SuitNumberCruncherS = 'a Number Man'
SuitMoneyBagsS = 'a Shiny Mingler'
SuitLoanSharkS = 'a Dark Angel'
SuitRobberBaronS = 'a Moonlight Mimi'
SuitBottomFeederS = 'a Cute Flunky'
SuitBloodsuckerS = 'a Vampire'
SuitDoubleTalkerS = 'a Sally'
SuitAmbulanceChaserS = 'an Microripoff'
SuitBackStabberS = 'a Textured Counter'
SuitSpinDoctorS = 'a Cog Monkey'
SuitLegalEagleS = 'a Black Eagle'
SuitBigWigS = 'a Full Wig'
SuitFlunkyP = 'Red Handers'
SuitPencilPusherP = 'Pencil heads'
SuitYesmanP = 'Shiny Stabbers'
SuitMicromanagerP = 'Fancy Kittens'
SuitDownsizerP = 'Hudsons'
SuitHeadHunterP = 'Dr. Simons'
SuitCorporateRaiderP = 'Scaringlers'
SuitTheBigCheeseP = 'Mozzerella Cheeses'
SuitColdCallerP = 'Black Callers'
SuitTelemarketerP = 'Telecallers'
SuitNameDropperP = 'Blacklers'
SuitGladHanderP = 'Scary Wizards'
SuitMoverShakerP = 'Scary Droppers'
SuitTwoFaceP = 'Two-Men'
SuitTheMinglerP = 'Mini Spongbobs'
SuitMrHollywoodP = 'Amanda Roses'
SuitShortChangeP = 'Conichanges'
SuitPennyPincherP = 'Dandy Sharks'
SuitTightwadP = 'Janets'
SuitBeanCounterP = 'Candace Flynns'
SuitNumberCruncherP = 'Number Men'
SuitMoneyBagsP = 'Shiny Minglers'
SuitLoanSharkP = 'Dark Angels'
SuitRobberBaronP = 'Moonlight Mimis'
SuitBottomFeederP = 'Cute Flunkies'
SuitBloodsuckerP = 'Vampires'
SuitDoubleTalkerP = 'Sallies'
SuitAmbulanceChaserP = 'Microripoffs'
SuitBackStabberP = 'Textured Counters'
SuitSpinDoctorP = 'Cog Monkies'
SuitLegalEagleP = 'Black Eagles'
SuitBigWigP = 'Full Wigs'
SuitFaceoffDefaultTaunts = ['Boo!']
SuitAttackDefaultTaunts = ['Take that!', 'Take a memo on this!']
SuitAttackNames = {'Audit': 'Audit!',
 'Bite': 'Bite!',
 'BounceCheck': 'Bounce Check!',
 'BrainStorm': 'Brain Storm!',
 'BuzzWord': 'Buzz Word!',
 'Calculate': 'Calculate!',
 'Canned': 'Canned!',
 'Chomp': 'Chomp!',
 'CigarSmoke': 'Cigar Smoke!',
 'ClipOnTie': 'Clip On Tie!',
 'Crunch': 'Crunch!',
 'Demotion': 'Demotion!',
 'Downsize': 'Downsize!',
 'DoubleTalk': 'Double Talk!',
 'EvictionNotice': 'Eviction Notice!',
 'BlackOrb': 'Black Orb!',
 'Filibuster': 'Filibuster!',
 'FillWithLead': 'Fill With Lead!',
 'FiveOClockShadow': "Five O'Clock Shadow!",
 'FingerWag': 'Finger Wag!',
 'Fired': 'Fired!',
 'FloodTheMarket': 'Flood The Market!',
 'FountainPen': 'Fountain Pen!',
 'FreezeAssets': 'Freeze Assets!',
 'Gavel': 'Gavel!',
 'GlowerPower': 'Glower Power!',
 'GuiltTrip': 'Guilt Trip!',
 'HalfWindsor': 'Half Windsor!',
 'HangUp': 'Hang Up!',
 'HeadShrink': 'Head Shrink!',
 'HotAir': 'Hot Air!',
 'Jargon': 'Jargon!',
 'Legalese': 'Legalese!',
 'Liquidate': 'Liquidate!',
 'MarketCrash': 'Market Crash!',
 'MumboJumbo': 'Mumbo Jumbo!',
 'ParadigmShift': 'Paradigm Shift!',
 'PeckingOrder': 'Pecking Order!',
 'PickPocket': 'Pick Pocket!',
 'PinkSlip': 'Pink Slip!',
 'PlayHardball': 'Play Hardball!',
 'PoundKey': 'Pound Key!',
 'PowerTie': 'Power Tie!',
 'PowerTrip': 'Power Trip!',
 'Quake': 'Quake!',
 'RazzleDazzle': 'Razzle Dazzle!',
 'RedTape': 'Red Tape!',
 'ReOrg': 'Re-Org!',
 'RestrainingOrder': 'Restraining Order!',
 'Rolodex': 'Rolodex!',
 'RubberStamp': 'Rubber Stamp!',
 'RubOut': 'Rub Out!',
 'Sacked': 'Sacked!',
 'SandTrap': 'Sand Trap!',
 'Schmooze': 'Schmooze!',
 'Shake': 'Shake!',
 'Shred': 'Shred!',
 'SongAndDance': 'Song And Dance!',
 'Spin': 'Spin!',
 'Synergy': 'Synergy!',
 'Tabulate': 'Tabulate!',
 'Golf': 'Golf!',
 'ThrowBook': 'Throw Book!',
 'Tremor': 'Tremor!',
 'Watercooler': 'Watercooler!',
 'Withdrawal': 'Withdrawal!',
 'WriteOff': 'Write Off!'}
SuitAttackTaunts = {'Audit': ["Can we check this?",
           "This is ready to Audit, Toon.",
           "Watch out Toon! You're payments are getting too high!",
           'This will be fun to Audit.',
           "Hmm, let's see. 1 plus 1 equals Aduit check."],
 'Bite': ["What's for supper?",
          "Want a bite of Potatoes?",
          "I'm going to bite you!",
          "Bite! Off more than you can chew!"],
 'BounceCheck': ["Pay off your check.",
                 'This check is now in fund.',
                 'Check, check, check!',
                 'This is going to cost ya!',
                 "Your checks are getting too much."],
 'BrainStorm': ['Ever heard of a Forecast?',
                'You might want to run Toon! Storm incoming!',
                'This is going to be a Brain Storm.',
                "It's sunny! Not!",
                'Not so sunny now, are you Toon?',
                'Nature storms cause chaos.'],
 'BuzzWord': ['Busy bees.',
              'This sting is going to only hurt a lot!',
              'Sting!',
              'Bees buzzing? Pathetic.',
              'Buzzing in your trees.'],
 'Calculate': ['Add it up, you will end up with nothing!',
               "Don't forget to calculate on this.",
               "This is what you need for Homework.",
               "Do you need to calculate this?"],
 'Canned': ['Can you throw this into the trash?',
            'Throw the can, can, can, today!',
            "You're going to get hit by this can!",
            'Want to throw a can for you?',
            "Can up time!",
            "I'm going to throw this can on you."],
 'Chomp': ['Us Cogs have 32 teeth.',
           'Chomp, chomp, chomp!',
           "Are you ready for chomps?",
           'Buy the chompers!',
           'Yummy Chompers!'],
 'CigarSmoke': ['Gentlemen.',
                "This smoke is our hope for survival.",
                'This is a good cigar.',
                "I'll quit tomorrow! I swear!",
                'Breathing smoke is our tradition.',
                'When your cigar is out, get another!',
                'This is a good smoke, right?',
                'And then after that, the moon blew up the end.'],
 'ClipOnTie': ['Go to our meeting.',
               "Hold on! You can't run without your tie yet!",
               'This tie is perfect size.',
               'Tie this up!',
               "This tie is good, right?"],
 'Crunch': ["Are we having milk with this crunch?",
            "You better crunch this!",
            "This is a crunch time!"],
 'Demotion': ["Where are you moving next, Toon?",
              "This is going to get sent to the Post Office.",
              "You're gonna pop this!",
              "You're not going anywhere, Toon!",
              'This is way too much, you gotta go.'],
 'DoubleTalk': ["I'm Double Talking this!",
              "Talk not only once, but twice!",
              'Take a memo on this!',
              "Do you wanna talk twice?",
              "I'm wording your reports.",
              "Can you talk to me?"],
 'Downsize': ['Shrink down!',
              'This will downsize some of your health.',
              'Get this size down.',
              'Want to be thrown down?',
              'This size will now fit you!'],
 'EvictionNotice': ["Want your notification checks thrown?",
                    'Pack up the bags!',
                    'PACK UP TOON!',
                    "This notification will be thrown to you."],
 'BlackOrb': ["This Orb is being traveled to you.",
             "Aware of my Magic!",
			 "Don't be scared, it's just Magic.",
			 "What are you looking at, Toon?",
			 "Want to see a Magic trick? It's the Orb.",
             "Never underestimate Cog's magic."],
 'Filibuster': ["Fill it up, Toon!",
                'This will be the more ready.',
                'What kind of Filibuster is this?',
                'This speaking will be in attack mode.'],
 'FillWithLead': ["I need to sharpen this.",
                'Give me a minute, let me sharpen your pencil.',
                'Sharpen this!',
                "Do you want your pencil sharpened?",
                "Don't worry, your pencil will be sharp in no time!",
                'Sharpen, sharpen, sharpen.'],
 'FingerWag': ['I have told you a thousand times.',
               'You better watch me Toon.',
			   "I use this finger to solve crimes.",
			   "Toon! I will wag you if you don't stop!",
			   "Do you really want me to blah blah you?",
               "This finger means, Don't mess with me!"],
 'Fired': ['Toasty!',
           "No, this is your fire! Not mine!",
           'This fire is going on you Toon!',
           "Can we cook with this?",
           'Want a chrispy toast?',
           "You're Fired!"],
 'FountainPen': ['This pen will be used to you.',
                 "I replaced the water with the pen.",
				 "You thirsty for some water pen?",
                 "Um, uh, um, uh, um, uh, um, uh, um, uh."],
 'FreezeAssets': ['Is this cold or hot?',
                  'These assets will be used for you.',
				  "Be aware, you're in a breeze!",
                  "It's cold!"],
 'GlowerPower': ["Don't you look at me!",
                 "Wait, this isn't family friendly, WHY AM I BLASTING THIS!?",
                 'This is such a Glower tonight!',
                 'I have the power!'],
 'GuiltTrip': ["It's your fault!",
               "You are the worst liar I ever met.",
			   "If you trip, you're guilty!",
               'Is this the Power Trip? Or the guilt?',
               'Are you innocent, or guilty?'],
 'HalfWindsor': ["This Tie will get you!",
                 'Do you accept Ties?',
				 "I wanna cut this tie in half.",
				 "Buy 1, get the other tie free.",
                 "Ever had a Tie?"],
 'HangUp': ["I can't hear you from here!",
            'Good bye!',
            "I would rather listen to 'Where are U now by Justin Bieber!'",
            "Can you please repeat that?",
            'Leave a message after the beep.'],
 'HeadShrink': ["This is a Toon Shrink.",
                'Can we Shrink this?',
                'This is Shrink Mode!'],
 'HotAir': ["This is too Hot!",
            "HOT, HOT, HOT!",
			"It's over 100 degrees in here, might wanna grab some shade.",
			"Wanna buy this hot air conditioning?",
            'Burn!!'],
 'Jargon': ['Stop with the nonsense!',
            'This is too much nonsense.',
            'This talk interesting?',
            "Hey, no arguing over this important Jargon!"],
 'Legalese': ["Isn't this Illigal?",
              "You're committing a huge crime, Toon. Stop it!",
			  "Shall I arrest you for breaking the Law?",
			  "Toon, don't think about it!",
              'This attack is not incorporated by the attacks of Toontown Mystery!'],
 'Liquidate': ['Ever had shower problems?',
               'Classic Noah Stinks!',
               "This is going to be a light shower."],
 'MarketCrash': ["This will crash on you, Toon!",
                 "Want extra help with your bags?"],
 'MumboJumbo': ['Let me make this perfectly clear.',
                "Aren't these the words for the Jumbo?",
				"This Jumbo shall be traveled.",
				"Ever Mumboed this Jumbo?",
                'This is nonsense!'],
 'ParadigmShift': ["I'm giving you the big shift now!",
                   "Be careful of this Shift!",
				   "This shift, is going to you.",
				   "Be aware, I will shift.",
                   "Isn't this a shift day?"],
 'PeckingOrder': ["Ever been attacked by a Bird?",
                  'This is the last bird I will give you today!',
                  "I will throw these birds in your bath!",
                  'This is a good Bath!'],
 'PickPocket': ['Can I have your Money?',
                "I'll take your Money!",
				"Huh? What's that, oops, I got your money.",
                'This Pocket is mine.'],
 'PinkSlip': ['Pink Up!',
              "Why are you normal? Why not Pink?",
              'This is the Real Slip!'],
 'PlayHardball': ['PLAY BALL!',
                  "Strike 1!",
                  'Strike 2!',
                  'Strike 3!',
                  "You're out!",
                  "Ball 1.",
                  "Ball 2.",
                  "Ball 3.",
                  'Ball 4.',
                  "Home run!",
                  "Ball 1, no no wait, strike 1, no no ball, strike, ball, what?"],
 'PoundKey': ['Call 1800-999-1110 for Toontown Mysterys latest updates.',
              "Call me please!",
              "Do you want my phone number?",
              "This is crazy! Here's my number, so call me maybe!",
              'Sorry, gotta go!'],
 'PowerTie': ["I have the power tie now!",
              'Go tie die in this!',
              "It's a red tie.",
              'It is a blue tie.',
              "Ties are cool and so are you.",
              "Wanna buy this tie from me? It's only 999,999,999,999,999 dollars."],
 'PowerTrip': ["Most Sellbots have this Power Trip!",
               'Power, Power, Power.',
               "Can I trip this?",
               'Oops! It slipped.',
			   'Please trip on this, please?',
               'I hope you fall in a Trip!!'],
 'Quake': ["Quake this, Toon!",
           "I shake, I quake, you fall, now we're both happy.",
           "Why you shaking? We need to Quake it.",
		   "What's the matter? Can't handle a Quake?",
           "You're in a Quake!"],
 'RazzleDazzle': ['I clean my Teeth everyday.',
                  "Isn't this dazzling?",
                  "My dentist gave me great Teeth.",
				  "Smile! You're on camera!",
                  'Say Cheese!'],
 'RedTape': ['This should a great Tape.',
             "This tape is no2 tape, don't ask.",
			 "Wanna roll in some tape?",
             "I'm going to roll this on you."],
 'ReOrg': ["This needs to be Organized.",
           "?????????????",
		   "Hey Toon, your station needs to be organized.",
           "Clean your room!"],
 'RestrainingOrder': ['I will throw this order on you.',
                      "Order in the Court!",
					  "Stay 6 feet away from me!",
                      "Why is this order being sent?",
                      "This is an Order!"],
 'Rolodex': ["This is a real card for you.",
             "This is a real Rolodex!",
			 "Ever gotten papercuts?",
			 "'Take this and some lemonade, get papercuts.'",
			 "Scan all of these files for me!",
             'I got you covered.'],
 'RubberStamp': ['Uh, how do I stamp a letter?',
                 "I have shall sent you this.",
				 "Behold, the letter!",
				 "I need these stamps for your letters!",
                 "Can you respond to this?"],
 'RubOut': ['You will disappear now.',
            "You'll disappear today!"],			
 'Sacked': ["Even though Toontown Stinks, Us Cogs are in it.",
            "Hey Toon, enjoy this sack.",
			"Honey, I sacked the Toon!",
            'This sack will give you all of Toontown.'],
 'Schmooze': ["Uh oh.",
              'But, but, but, but, but, but.',
			  "I will persuade you, Toon!",
			  "Are you feeling manipulated? Hehe.",
              "This is a Schmooze today.",
              "You're Grounded!"],
 'Shake': ["How ya feeling Toon?",
           "This is shaking today.",
		   "I am aware of how much you're shaking.",
		   "Stop feeling scared, feel the power!",
           "Shake it off!"],
 'Shred': ['Mind if I shred your papers?',
           "Ah yes, my shredder, here you go.",
           "I need to shred this."],
 'SongAndDance': ["We dancing tonight?",
                  "Praise the Dance!",
				  "Dance with me, Baby!",
				  "Dance to the beat!!",
                  'Care to dance?',
		          'Dance to this!',
		          'Dance with me!!',
		          "Can't you dance right?",
		          'Show me the dance to the beat!',
		          'Is this too much for you to handle?',
                  'Whoa, whoa, whoa.'],
 'Spin': ['Want to spin?',
          "Ever been on a marry-go-round?",
		  "I'm taking you for a spin. Enjoy.",
          'Spin around!'],
 'Synergy': ["I'm taking this to committee.",
             "Your project's been cancelled.",
			 "Where is your money? Did you lose it?",
             'This attack will cause harm.'],
 'Tabulate': ["Add it up!",
              'Do you know how much this is gonna cost?',
              'Can you add this?'],
 'Golf': ["I will golf on you.",
           'Wanna play golf with me?',
		   'Fore!',
		   'This ball, in your face, right now.',
		   "Who wants to golf?",
		   'And I putt putt into the hole!',
		   'GOLF!!!',
           'Get your golfing in today!'],
 'ThrowBook': ['Are you ready to pass?',
               'This Book is from the Laws.',
               "This Book is magical.",
               'Time to go sad, Toon.',
               'You can find all the Laws in here.',
               'Do you want a Ticket?',
               'No breaking the Law!',
               "Order in the Court!",
               "This is your court law."],
 'Tremor': ['Oof! Oof! Oof!',
            "Be aware Toon, the Tremor is coming!",
            "I'm going to Tremor on you!",
			"Are you feeling shaken up, Toon?",
            'Pump it up.'],
 'Watercooler': ['Cool off.',
                 "This is a big delivery, isn't it?",
                 'Delivery!'],
 'Withdrawal': ["White powder on you becomes a black Toon.",
                'Enjoying this?',
                "Fun has it's price you know.",
                'Is it just me? Or did you change?',
                "Take this!"],
 'WriteOff': ['I will balance you in my checkbook.',
              "Forget the bonus, you get an Z-.",
              'Let me grade your papers real quick.',
              "Mark this, mark that, oop- you failed!",
              "I hate my job, just take this check.",
              'You want this check in cash? Or credit?',
              'Take this check to the bank for a deposit!',
              "Do you want your accounts deleted?",
              "I'm sorry, but we do not accept bonuses.",
              'Discounts stink!!!!!!!!']}
WaitingForOtherToons = 'Waiting for other toons...'
WaitingForOtherToonsDots = 'Waiting for other toons%s'
ElevatorHopOff = 'Hop off'
ElevatorLeaderOff = 'Only your leader can decide when to hop off.'
ElevatorHopOK = 'Okay'
ElevatorGroupMember = 'Only your group leader can\n decide when to board.'
CogsIncExt = ', Inc.'
CogsIncModifier = '%s' + CogsIncExt
CogsInc = Cogs.upper() + CogsIncExt
CogdominiumsExt = ' Field Office'
Cogdominiums = Cog.upper() + CogdominiumsExt
DoorKnockKnock = 'Knock, knock.'
DoorWhosThere = "Who's there?"
DoorWhoAppendix = ' who?'
DoorNametag = 'Door'
FADoorCodes_UNLOCKED = None
FADoorCodes_TALK_TO_TOM = 'You need gags! Go talk to Tutorial Tom!'
FADoorCodes_DEFEAT_FLUNKY_HQ = 'Come back here when you have defeated the Flunky!'
FADoorCodes_TALK_TO_HQ = 'Go get your reward from HQ Harry!'
FADoorCodes_WRONG_DOOR_HQ = 'Wrong door! Take the other door to the playground!'
FADoorCodes_GO_TO_PLAYGROUND = 'Wrong way! You need to go to the playground!'
FADoorCodes_DEFEAT_FLUNKY_TOM = 'Walk up to that Flunky to battle him!'
FADoorCodes_TALK_TO_HQ_TOM = 'Go get your reward from Toon Headquarters!'
FADoorCodes_SUIT_APPROACHING = None
FADoorCodes_BUILDING_TAKEOVER = "Watch out! There's a Cog in there!"
FADoorCodes_SB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Sellbot Disguise first!\n\nBuild your Sellbot Disguise out of parts from the Factory."
FADoorCodes_CB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Cashbot Disguise first!\n\nBuild your Cashbot Disguise by doing ToonTasks in Donald's Dreamland."
FADoorCodes_LB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Lawbot Disguise first!\n\nBuild your Lawbot Disguise by doing the ToonTasks after Donald's Dreamland."
FADoorCodes_BB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Bossbot Disguise first!\n\nBuild your Bossbot Disguise by doing the ToonTasks after Donald's Dreamland."
KnockKnockJokes = [['Who', "Bad echo in here, isn't there?"],
 ['Dozen', 'Dozen anybody want to let me in?'],
 ['Freddie', 'Freddie or not, here I come.'],
 ['Dishes', 'Dishes your friend, let me in.'],
 ['Wooden shoe', 'Wooden shoe like to know.'],
 ['Betty', "Betty doesn't know who I am."],
 ['Kent', 'Kent you tell?'],
 ['Noah', "Noah don't know who either."],
 ["I don't know", 'Neither do I, I keep telling you that.'],
 ['Howard', 'Howard I know?'],
 ['Emma', 'Emma so glad you asked me that.'],
 ['Auto', "Auto know, but I've forgotten."],
 ['Jess', 'Jess me and my shadow.'],
 ['One', 'One-der why you keep asking that?'],
 ['Alma', 'Alma not going to tell you!'],
 ['Zoom', 'Zoom do you expect?'],
 ['Amy', "Amy fraid I've forgotten."],
 ['Arfur', 'Arfur got.'],
 ['Ewan', 'No, just me'],
 ['Cozy', "Cozy who's knocking will you?"],
 ['Sam', 'Sam person who knocked on the door last time.'],
 ['Fozzie', 'Fozzie hundredth time, my name is ' + Flippy + '.'],
 ['Deduct', 'Donald Deduct.'],
 ['Max', 'Max no difference, just open the door.'],
 ['N.E.', 'N.E. body you like, let me in.'],
 ['Amos', 'Amos-quito bit me.'],
 ['Alma', "Alma candy's gone."],
 ['Bruce', "I Bruce very easily, don't hit me."],
 ['Colleen', "Colleen up your room, it's filthy."],
 ['Elsie', 'Elsie you later.'],
 ['Hugh', 'Hugh is going to let me in?'],
 ['Hugo', "Hugo first - I'm scared."],
 ['Ida', 'Ida know.  Sorry!'],
 ['Isabel', 'Isabel on a bike really necessary?'],
 ['Joan', "Joan call us, we'll call you."],
 ['Kay', 'Kay, L, M, N, O, P.'],
 ['Justin', 'Justin time for dinner.'],
 ['Liza', 'Liza wrong to tell.'],
 ['Luke', 'Luke and see who it is.'],
 ['Mandy', "Mandy the lifeboats, we're sinking."],
 ['Max', 'Max no difference - just open the door!'],
 ['Nettie', 'Nettie as a fruitcake.'],
 ['Olivia', 'Olivia me alone!'],
 ['Oscar', 'Oscar stupid question, you get a stupid answer.'],
 ['Patsy', 'Patsy dog on the head, he likes it.'],
 ['Paul', "Paul hard, the door's stuck again."],
 ['Thea', 'Thea later, alligator.'],
 ['Tyrone', "Tyrone shoelaces, you're old enough."],
 ['Stella', 'Stella no answer at the door.'],
 ['Uriah', 'Keep Uriah on the ball.'],
 ['Dwayne', "Dwayne the bathtub.  I'm drowning."],
 ['Dismay', "Dismay be a joke, but it didn't make me laugh."],
 ['Ocelot', "Ocelot of questions, don't you?"],
 ['Thermos', 'Thermos be a better knock knock joke than this.'],
 ['Sultan', 'Sultan Pepper.'],
 ['Vaughan', 'Vaughan day my prince will come.'],
 ['Donald', 'Donald come baby, cradle and all.'],
 ['Lettuce', "Lettuce in, won't you?"],
 ['Ivor', 'Ivor sore hand from knocking on your door!'],
 ['Isabel', 'Isabel broken, because I had to knock.'],
 ['Heywood, Hugh, Harry', 'Heywood Hugh Harry up and open this door.'],
 ['Juan', "Juan of this days you'll find out."],
 ['Earl', 'Earl be glad to tell you if you open this door.'],
 ['Abbot', 'Abbot time you opened this door!'],
 ['Ferdie', 'Ferdie last time, open the door!'],
 ['Don', 'Don mess around, just open the door.'],
 ['Sis', 'Sis any way to treat a friend?'],
 ['Isadore', 'Isadore open or locked?'],
 ['Harry', 'Harry up and let me in!'],
 ['Theodore', "Theodore wasn't open so I knocked-knocked."],
 ['Ken', 'Ken I come in?'],
 ['Boo', "There's no need to cry about it."],
 ['You', 'You who!  Is there anybody there?'],
 ['Ice cream', "Ice cream if you don't let me in."],
 ['Sarah', "Sarah 'nother way into this building?"],
 ['Mikey', 'Mikey dropped down the drain.'],
 ['Doris', 'Doris jammed again.'],
 ['Yelp', 'Yelp me, the door is stuck.'],
 ['Scold', 'Scold outside.'],
 ['Diana', 'Diana third, can I have a drink please?'],
 ['Doris', 'Doris slammed on my finger, open it quick!'],
 ['Lettuce', 'Lettuce tell you some knock knock jokes.'],
 ['Izzy', 'Izzy come, izzy go.'],
 ['Omar', 'Omar goodness gracious - wrong door!'],
 ['Says', "Says me, that's who!"],
 ['Duck', "Just duck, they're throwing things at us."],
 ['Tank', "You're welcome."],
 ['Eyes', 'Eyes got loads more knock knock jokes for you.'],
 ['Pizza', 'Pizza cake would be great right now.'],
 ['Closure', 'Closure mouth when you eat.'],
 ['Harriet', "Harriet all my lunch, I'm starving."],
 ['Wooden', 'Wooden you like to know?'],
 ['Punch', 'Not me, please.'],
 ['Gorilla', 'Gorilla me a hamburger.'],
 ['Jupiter', "Jupiter hurry, or you'll miss the trolley."],
 ['Bertha', 'Happy Bertha to you!'],
 ['Cows', 'Cows go "moo" not "who."'],
 ['Tuna fish', "You can tune a piano, but you can't tuna fish."],
 ['Consumption', 'Consumption be done about all these knock knock jokes?'],
 ['Banana', 'Banana spilt so ice creamed.'],
 ['X', 'X-tremely pleased to meet you.'],
 ['Haydn', 'Haydn seek is fun to play.'],
 ['Rhoda', 'Rhoda boat as fast as you can.'],
 ['Quacker', "Quacker 'nother bad joke and I'm off!"],
 ['Nana', 'Nana your business.'],
 ['Ether', 'Ether bunny.'],
 ['Little old lady', "My, you're good at yodelling!"],
 ['Beets', 'Beets me, I forgot the joke.'],
 ['Hal', 'Halloo to you too!'],
 ['Sarah', 'Sarah doctor in the house?'],
 ['Aileen', 'Aileen Dover and fell down.'],
 ['Atomic', 'Atomic ache'],
 ['Agatha', 'Agatha headache.  Got an aspirin?'],
 ['Stan', "Stan back, I'm going to sneeze."],
 ['Hatch', 'Bless you.'],
 ['Ida', "It's not Ida who, it's Idaho."],
 ['Zippy', 'Mrs. Zippy.'],
 ['Yukon', 'Yukon go away and come back another time.']]
ScientistPhase1Dialogue = ['Fellow Toons, this is the Silly Meter!',
                           "It is tracking Toontown's rising silly levels...",
                           'Which are causing objects on the street to animate!',
                           'And YOU can help push these levels higher!',
                           'Battle Cogs to cause Silly Surges...',
                           'Make Toontown sillier than ever...',
                           "And let's watch the world come alive!",
                           "Now I'll repeat what I said, but only once more."]
ScientistPhase2Dialogue = ['Good Gag work, Toons!',
                           "You're keeping those silly levels rising...",
                           'And Toontown is getting sillier every day!',
                           'Fire hydrants, trash cans, and mailboxes are springing to life...',
                           'Making the world more animated than ever!',
                           "You know the Cogs aren't happy about this...",
                           'But Toons sure are!']
ScientistPhase3Dialogue = ['Gadzooks! The Silly Meter is even crazier than expected!',
                           'Your Silly Surges are working wonders...',
                           'And Toontown is getting more animated every day!',
                           'Keep up the good Gag work...',
                           'And lets see how silly we can make Toontown!',
                           "You know the Cogs aren't happy about what's going on...",
                           'But Toons sure are!']
ScientistPhase4Dialogue = ['YOU DID IT TOONS!',
                           'You brought the streets of Toontown to life!',
                           'You deserve a reward!',
                           'Enter the code SILLYMETER in your Shticker Book...',
                           '...to get a Silly Meter T-Shirt!']
ScientistPhase5Dialogue = ['Attention all Toons!',
                           'The Cog invasions have been an unhappy event.',
                           'As a result, silly levels have rapidly fallen...',
                           'And no new objects are coming to life.',
                           'But those that have are very thankful...',
                           'And are showing their appreciation by helping in battle!',
                           'We may hold off the Cogs yet, so keep up the fight!']
ScientistPhase6Dialogue = ['Congratulations Toons!',
                          'You all succesfully held off the Cog Invasions...',
                          'With a little help from our newly animated friends...',
                          'And brought Toontown back to its usual silly self!',
                          'We hope to get the Silly Meter rising again soon...',
                          'So in the meantime, keep up the Cog fight...',
                          'And enjoy the silliest place ever, Toontown!']
FriendsListPanelNewFriend = 'New Friend'
FriendsListPanelOnlineFriends = 'ONLINE TOON\nFRIENDS'
FriendsListPanelAllFriends = 'ALL TOON\nFRIENDS'
FriendsListPanelPets = 'NEARBY\nPETS'
FriendsListPanelTrueFriends = 'True Friends'
FriendInviterClickToon = 'Click on the toon you would like to make friends with.\n\n(You have %s friends)'
FriendInviterThatToon = 'That toon'
FriendInviterToonTooMany = 'You have too many toon friends to add another one now. You will have to remove some toon friends if you want to make friends with %s.'
FriendInviterToonAlready = '%s is already your toon friend.'
FriendInviterStopBeingToonFriends = 'Stop being toon friends'
FriendInviterEndFriendshipToon = 'Are you sure you want to stop being toon friends with %s?'
FriendInviterRemainToon = '\n(You will still be toon friends with %s)'
AvatarChoiceMakeAToon = 'Make A\nToon'
AvatarChoicePlayThisToon = 'Play\nThis Toon'
AvatarChoiceDelete = 'Delete'
AvatarChoiceDeleteConfirm = 'This will delete %s forever.'
AvatarChoiceNameRejected = 'Name\nRejected'
AvatarChoiceNameApproved = 'Name\nApproved!'
AvatarChoiceNameReview = 'Under\nReview'
AvatarChoiceNameYourToon = 'Name\nYour Toon!'
AvatarChoiceDeleteConfirmText = "Careful! This will delete %(name)s forever.  If you are sure you want to do this, type your toon's name and click OK."
AvatarChoiceDeletePasswordTitle = 'Delete Toon?'
AvatarChoiceDeletePasswordOK = lOK
AvatarChoiceDeletePasswordCancel = lCancel
AvatarChoiceDeleteWrongConfirm = "You didn\'t type the right thing.  To delete %(name)s, type your toon's name and click OK.  Do not type the quotation marks.  Click Cancel if you have changed your mind."
AvatarChooserPickAToon = 'Pick  A  Toon  To  Play'
AvatarChooserQuit = lQuit
DateOfBirthEntryMonths = ['Jan',
 'Feb',
 'Mar',
 'Apr',
 'May',
 'Jun',
 'Jul',
 'Aug',
 'Sep',
 'Oct',
 'Nov',
 'Dec']
PhotoPageTitle = 'Snapshots'
PhotoPageNoName = 'Unnamed'
PhotoPageUnknownName = 'Unknown'
PhotoPageAddName = 'Add Caption'
PhotoPageAddNamePanel = 'Add a Caption to this Snapshot:'
PhotoPageDelete = 'Are you sure you want to delete'
PhotoPageConfirm = 'Yep!'
PhotoPageCancel = lCancel
PhotoPageClose = lClose
PhotoPageDirectory = 'Open Folder'
PhotoPageTutorial = 'You haven\'t taken any snapshots yet! Press TAB to change your camera angle, and press F9 to take a snapshot.\n\n Once you\'ve made a snapshot, come here to manage and name them.'
BuildingPageTitle = 'Buildings\n(Coming Soon)'
InventoryPageTitle = 'Gags'
InventoryPageTrackFull = 'You have all the gags in the %s track.'
InventoryPagePluralPoints = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s points.'
InventoryPageSinglePoint = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s point.'
InventoryPageNoAccess = 'You do not have access to the %s track yet.'
NPCFriendPageTitle = 'SOS Toons'
PartyDateFormat = '%(mm)s %(dd)d, %(yyyy).4d'
PartyTimeFormat = '%d:%.2d %s'
PartyTimeFormatMeridiemAM = 'am'
PartyTimeFormatMeridiemPM = 'pm'
PartyCanStart = "It's Party Time, click Start Party in your Shticker Book Hosting page!"
PartyHasStartedAcceptedInvite = '%s party has started! Teleport to the host!'
PartyHasStartedNotAcceptedInvite = '%s party has started! You can still go to it by teleporting to the host.'
EventsPageName = 'Events'
EventsPageCalendarTabName = 'Calendar'
EventsPageCalendarTabParty = 'Party'
EventsPageToontownTimeIs = 'TOONTOWN TIME IS'
EventsPageConfirmCancel = 'If you cancel, you will get a %d%% refund. Are you sure you want to cancel your party?'
EventsPageCancelPartyResultOk = 'Your party was cancelled and you got %d Jellybeans back!'
EventsPageCancelPartyResultError = 'Sorry, your party was not cancelled.'
EventsPageCancelPartyAlreadyRefunded = 'Your party was never started. Check your mailbox for your refund!'
EventsPageTooLateToStart = 'Sorry, it is too late to start your party. You can cancel it and plan another one.'
EventsPagePublicPrivateChange = "Changing your party's privacy setting..."
EventsPagePublicPrivateNoGo = "Sorry, you can't change your party's privacy setting right now."
EventsPagePublicPrivateAlreadyStarted = "Sorry, your party has already started, so you can't change your party's privacy setting."
EventsPageHostTabName = 'Hosting'
EventsPageHostTabTitle = 'My Next Party'
EventsPageHostTabTitleNoParties = 'No Parties'
EventsPageHostTabDateTimeLabel = 'You are having a party on %s at %s Toontown Time.'
EventsPageHostingTabNoParty = 'Go to a playground\nParty Gate to plan\nyour own party!'
EventsPageHostTabPublicPrivateLabel = 'This party is:'
EventsPageHostTabToggleToPrivate = 'Private'
EventsPageHostTabToggleToPublic = 'Public'
EventsPageHostingTabGuestListTitle = 'Guests'
EventsPageHostingTabActivityListTitle = 'Activities'
EventsPageHostingTabDecorationsListTitle = 'Decorations'
EventsPageHostingTabPartiesListTitle = 'Hosts'
EventsPageHostTabCancelButton = 'Cancel Party'
EventsPageGoButton = 'Start\nParty!'
EventsPageGoBackButton = 'Party\nNow!'
EventsPageInviteGoButton = 'Go to\nParty!'
EventsPageUnknownToon = 'Unknown Toon'
EventsPageInvitedTabName = 'Invitations'
EventsPageInvitedTabTitle = 'Party Invitations'
EventsPageInvitedTabInvitationListTitle = 'Invitations'
EventsPageInvitedTabActivityListTitle = 'Activities'
EventsPageInvitedTabTime = '%s %s Toontown Time'
SelectedInvitationInformation = '%s is having a party on %s at %s Toontown Time.'
PartyPlannerNextButton = 'Continue'
PartyPlannerPreviousButton = 'Back'
PartyPlannerWelcomeTitle = 'Toontown Party Planner'
PartyPlannerInstructions = 'Hosting your own party is a lot of fun!\nStart planning with the arrows at the bottom!'
PartyPlannerDateTitle = 'Pick A Day For Your Party'
PartyPlannerTimeTitle = 'Pick A Time For Your Party'
PartyPlannerGuestTitle = 'Choose Your Guests'
PartyPlannerEditorTitle = 'Design Your Party\nPlace Activities and Decorations'
PartyPlannerConfirmTitle = 'Choose Invitations To Send'
PartyPlannerConfirmTitleNoFriends = 'Double Check Your Party'
PartyPlannerTimeToontown = 'Toontown'
PartyPlannerTimeTime = 'Time'
PartyPlannerTimeRecap = 'Party Date and Time'
PartyPlannerPartyNow = 'As Soon As Possible'
PartyPlannerTimeToontownTime = 'Toontown Time:'
PartyPlannerTimeLocalTime = 'Party Local Time : '
PartyPlannerPublicPrivateLabel = 'This party will be:'
PartyPlannerPublicDescription = 'Any Toon\ncan come!'
PartyPlannerPrivateDescription = 'Only\nInvited Toons\ncan come!'
PartyPlannerPublic = 'Public'
PartyPlannerPrivate = 'Private'
PartyPlannerCheckAll = 'Check\nAll'
PartyPlannerUncheckAll = 'Uncheck\nAll'
PartyPlannerDateText = 'Date'
PartyPlannerTimeText = 'Time'
PartyPlannerTTTimeText = 'Toontown Time'
PartyPlannerEditorInstructionsIdle = 'Click on the Party Activity or Decoration you would like to purchase.'
PartyPlannerEditorInstructionsClickedElementActivity = 'Click Buy or Drag the Activity Icon onto the Party Grounds Map'
PartyPlannerEditorInstructionsClickedElementDecoration = 'Click Buy or Drag the Decoration onto the Party Grounds Map'
PartyPlannerEditorInstructionsDraggingActivity = 'Drag the Activity onto the Party Grounds Map.'
PartyPlannerEditorInstructionsDraggingDecoration = 'Drag the Activity onto the Party Grounds Map.'
PartyPlannerEditorInstructionsPartyGrounds = 'Click and Drag items to move them around the Party Grounds Map'
PartyPlannerEditorInstructionsTrash = 'Drag an Activity or Decoration here to remove it.'
PartyPlannerEditorInstructionsNoRoom = 'There is no room to place that activity.'
PartyPlannerEditorInstructionsRemoved = '%(removed)s removed since %(added)s was added.'
PartyPlannerBeans = 'beans'
PartyPlannerTotalCost = 'Total Cost:\n%d beans'
PartyPlannerSoldOut = 'SOLD OUT'
PartyPlannerBuy = 'BUY'
PartyPlannerPartyGrounds = 'PARTY GROUNDS MAP'
PartyPlannerOkWithGroundsLayout = 'Are you done moving your Party Activities and Decorations around the Party Grounds Map?'
PartyPlannerChooseFutureTime = 'Please choose a time in the future.'
PartyPlannerInviteButton = 'Send Invites'
PartyPlannerInviteButtonNoFriends = 'Plan Party'
PartyPlannerBirthdayTheme = 'Birthday'
PartyPlannerGenericMaleTheme = 'Star'
PartyPlannerGenericFemaleTheme = 'Flower'
PartyPlannerRacingTheme = 'Racing'
PartyPlannerValentoonsTheme = 'ValenToons'
PartyPlannerVictoryPartyTheme = 'Victory'
PartyPlannerWinterPartyTheme = 'Winter'
PartyPlannerGuestName = 'Guest Name'
PartyPlannerClosePlanner = 'Close Planner'
PartyPlannerConfirmationAllOkTitle = 'Congratulations!'
PartyPlannerConfirmationAllOkText = 'Your party has been created and your invitations sent out.\nThanks!'
PartyPlannerConfirmationAllOkTextNoFriends = 'Your party has been created!\nThanks!'
PartyPlannerConfirmationErrorTitle = 'Oops.'
PartyPlannerConfirmationValidationErrorText = 'Sorry, there seems to be a problem\nwith that party.\nPlease go back and try again.'
PartyPlannerConfirmationDatabaseErrorText = "Sorry, I couldn't record all your information.\nPlease try again later.\nDon't worry, no beans were lost."
PartyPlannerConfirmationTooManyText = 'Sorry, you are already hosting a party.\nIf you want to plan another party, please\ncancel your current party.'
PartyPlannerInvitationThemeWhatSentence = 'You are invited to my %s party! %s!'
PartyPlannerInvitationThemeWhatSentenceNoFriends = 'I am hosting a %s party! %s!'
PartyPlannerInvitationThemeWhatActivitiesBeginning = 'It will have '
PartyPlannerInvitationWhoseSentence = '%s Party'
PartyPlannerInvitationTheme = 'Theme'
PartyPlannerInvitationWhenSentence = 'It will be on %s,\nat %s Toontown Time.\nHope you can make it!'
PartyPlannerInvitationWhenSentenceNoFriends = 'It will be on %s,\nat %s Toontown Time.\nToontastic!'
PartyPlannerGenericName = 'Party Planner'
PartyJukeboxOccupied = 'Someone else is using the jukebox. Try again later.'
PartyJukeboxNowPlaying = 'The song you chose is now playing on the jukebox!'
MusicEncntrGeneralBg = 'Encounter With Cogs'
MusicTcSzActivity = 'Toontorial Medley'
MusicTcSz = 'Strolling Along'
MusicCreateAToon = 'The New Toon in Town'
MusicTtsTheme = 'The Toontown Stride Theme'
MusicTtTheme = 'The Toontown Theme'
MusicMinigameRace = 'Slow and Steady'
MusicTcNbrhood = 'Toontown Central'
MusicMgDiving = 'Treasure Lullaby'
MusicMgCannonGame = 'Fire the Cannons!'
MusicMgTwodgame = 'Running Toon'
MusicMgCogthief = 'Catch That Cog!'
MusicMgTugOWar = 'Tug-of-War'
MusicMgVine = 'The Jungle Swing'
MusicMgIcegame = 'Slippery Situation'
MusicMgToontag = 'Minigame Medley'
MusicMMatchBg2 = 'Jazzy Minnie'
MusicMgTarget = "Soarin' Over Toontown"
MusicFfSafezone = 'The Funny Farm'
MusicDdSz = 'Waddling Way'
MusicMmNbrhood = "Minnie's Melodyland"
MusicGzPlaygolf = "Let's Play Golf!"
MusicGsSz = 'Goofy Speedway'
MusicOzSz = "Chip n' Dale's Acres"
MusicGsRaceCc = 'Downtown Driving'
MusicGsRaceSs = 'Ready, Set, Go!'
MusicGsRaceRr = 'Route 66'
MusicGzSz = 'The Putt-Putt Polka'
MusicMmSz = 'Dancing in the Streets'
MusicMmSzActivity = 'Here Comes Treble'
MusicDdNbrhood = "Donald's Dock"
MusicGsKartshop = 'Mr. Goofywrench'
MusicDdSzActivity = 'Sea Shanty'
MusicEncntrGeneralBgIndoor = 'Building Excitement'
MusicTtElevator = 'Going Up?'
MusicEncntrToonWinningIndoor = 'Toons Unite!'
MusicEncntrGeneralSuitWinningIndoor = 'Cog-tastrophe!'
MusicTbNbrhood = 'The Brrrgh'
MusicDlNbrhood = "Donald's Dreamland"
MusicDlSzActivity = 'Counting Sheep'
MusicDgSz = 'Waltz of the Flowers'
MusicDlSz = 'Sleepwalking'
MusicTbSzActivity = 'Snow Problem'
MusicTbSz = 'Shiver and Shimmy'
MusicDgNbrhood = "Daisy's Garden"
MusicEncntrHallOfFame = 'The Hall of Fame'
MusicEncntrSuitHqNbrhood = 'Dollars and Cents'
MusicChqFactBg = 'Cog Factory'
MusicCoghqFinale = 'Triumph of the Toons'
MusicEncntrToonWinning = 'Cashing In!'
MusicEncntrSuitWinning = 'Selling You Short'
MusicEncntrHeadSuitTheme = 'The Big Boss'
MusicLbJurybg = 'Court is in Session'
MusicLbCourtyard = 'Balancing Act'
MusicBossbotCeoV2 = 'Head Honcho'
MusicBossbotFactoryV1 = 'Cog Waltz'
MusicBossbotCeoV1 = 'Bossing You Around'
MusicPartyOriginalTheme = 'Party Time'
MusicPartyPolkaDance = 'Party Polka'
MusicPartySwingDance = 'Party Swing'
MusicPartyWaltzDance = 'Party Waltz'
MusicPartyGenericThemeJazzy = 'Party Jazz'
MusicPartyGenericTheme = 'Party Jingle'
JukeboxAddSong = 'Add\nSong'
JukeboxReplaceSong = 'Replace\nSong'
JukeboxQueueLabel = 'Playing Next:'
JukeboxSongsLabel = 'Pick a Song:'
JukeboxClose = 'Done'
JukeboxCurrentlyPlaying = 'Currently Playing'
JukeboxCurrentlyPlayingNothing = 'Jukebox is paused.'
JukeboxCurrentSongNothing = 'Add a song to the playlist!'
PartyOverWarningNoName = 'The party has ended! Thanks for coming!'
PartyOverWarningWithName = '%s party has ended! Thanks for coming!'
PartyCountdownClockText = 'Time\n\nLeft'
PartyTitleText = '%s Party'
PartyActivityConjunction = ', and'
PartyActivityNameDict = {0: {'generic': 'Jukebox',
     'invite': 'a Jukebox',
     'editor': 'Jukebox',
     'description': 'Listen to music with your own jukebox!'},
 1: {'generic': 'Party Cannons',
     'invite': 'Party Cannons',
     'editor': 'Cannons',
     'description': 'Fire yourself out of the cannons and into fun!'},
 2: {'generic': 'Trampoline',
     'invite': 'Trampoline',
     'editor': 'Trampoline',
     'description': 'Collect Jellybeans and bounce the highest!'},
 3: {'generic': 'Party Catch',
     'invite': 'Party Catch',
     'editor': 'Party Catch',
     'description': 'Catch fruit to win beans! Dodge those anvils!'},
 4: {'generic': 'Dance Floor\n10 moves',
     'invite': 'a 10 move Dance Floor',
     'editor': 'Dance Floor - 10',
     'description': 'Show off all 10 of your moves, toon style!'},
 5: {'generic': 'Party Tug-of-War',
     'invite': 'Party Tug-of-War',
     'editor': 'Tug-of-War',
     'description': 'Up to 4 on 4 toon tugging craziness!'},
 6: {'generic': 'Party Fireworks',
     'invite': 'Party Fireworks',
     'editor': 'Fireworks',
     'description': 'Launch your very own fireworks show!'},
 7: {'generic': 'Party Clock',
     'invite': 'a Party Clock',
     'editor': 'Party Clock',
     'description': 'Counts down the time left in your party.'},
 8: {'generic': 'Deluxe Jukebox',
     'invite': 'a deluxe jukebox',
     'editor': 'Deluxe Jukebox',
     'description': 'Your own deluxe jukebox with double the tunes for double the deal!'},
 9: {'generic': 'Dance Floor\n20 moves',
     'invite': 'a 20 move Dance Floor',
     'editor': 'Dance Floor - 20',
     'description': 'Show off all 20 of your moves, toon style!'},
 10: {'generic': 'Cog-O-War',
      'invite': 'Cog-O-War',
      'editor': 'Cog-O-War',
      'description': 'The team vs. team game of Cog splatting!'},
 11: {'generic': 'Cog Trampoline',
      'invite': 'Cog Trampoline',
      'editor': 'Cog Trampoline',
      'description': "Jump on a Cog's face!"},
 12: {'generic': 'Present Catch',
      'invite': 'Present Catch',
      'editor': 'Present Catch',
      'description': 'Catch presents to win beans! Dodge those anvils!'},
 13: {'generic': 'Holiday Trampoline',
      'invite': 'Holiday Trampoline',
      'editor': 'Holiday Trampoline',
      'description': 'Jump if you love Winter Holidays!'},
 14: {'generic': 'Holiday Cog-O-War',
      'invite': 'Holiday Cog-O-War',
      'editor': 'Holiday Cog-O-War',
      'description': 'The team vs. team game of Cog splattering!'},
 15: {'generic': 'Dance Floor\n10 moves',
      'invite': 'a 10 move ValenToons Dance Floor',
      'editor': 'Dance Floor - 10',
      'description': 'Get your ValenToon Groove On!'},
 16: {'generic': 'Dance Floor\n20 moves',
      'invite': 'a 20 move ValenToons Dance Floor',
      'editor': 'Dance Floor - 20',
      'description': 'Get your ValenToon Groove On!'},
 17: {'generic': 'Jukebox\n20 songs',
      'invite': 'a 20 song Valentoons Jukebox',
      'editor': 'Jukebox - 20',
      'description': 'Nothing sets the mood like music!'},
 18: {'generic': 'Jukebox\n40 songs',
      'invite': 'a 40 song Valentoons jukebox',
      'editor': 'Jukebox - 40',
      'description': 'Nothing sets the mood like music!'},
 19: {'generic': 'Trampoline',
      'invite': 'ValenToons Trampoline',
      'editor': 'Trampoline',
      'description': "Jump to your heart's content!"}}
PartyDecorationNameDict = {0: {'editor': 'Balloon Anvil',
     'description': 'Try to keep the fun from floating away!'},
 1: {'editor': 'Party Stage',
     'description': 'Balloons, stars, what else could you want?'},
 2: {'editor': 'Party Bow',
     'description': 'Wrap up the fun!'},
 3: {'editor': 'Cake',
     'description': 'Delicious.'},
 4: {'editor': 'Party Castle',
     'description': "A Toon's home is his castle."},
 5: {'editor': 'Gift Pile',
     'description': 'Gifts for every Toon!'},
 6: {'editor': 'Streamer Horn',
     'description': 'This horn is a hoot! Streamers!'},
 7: {'editor': 'Party Gate',
     'description': 'Multi-colored and crazy!'},
 8: {'editor': 'Noise Makers',
     'description': 'Tweeeeet!'},
 9: {'editor': 'Pinwheel',
     'description': 'Colorful twirling for everyone!'},
 10: {'editor': 'Gag Globe',
      'description': 'Gag and star globe designed by Olivea'},
 11: {'editor': 'Bean Banner',
      'description': 'A Jellybean banner designed by Cassidy'},
 12: {'editor': 'Gag Cake',
      'description': 'A Topsy Turvy gag cake designed by Felicia'},
 13: {'editor': "Cupid's Heart",
      'description': 'Ready...Aim...\nValenToons!'},
 14: {'editor': 'Candy Hearts\n Banner',
      'description': "Who doesn't love candy hearts?"},
 15: {'editor': 'Flying Heart',
      'description': 'This heart is getting carried away!'},
 16: {'editor': 'Victory Bandstand',
      'description': 'All our new friends are ready to dance!'},
 17: {'editor': 'Victory Banner',
      'description': 'Not just a normal banner!'},
 18: {'editor': 'Confetti Cannons',
      'description': 'BOOM! Confetti! Fun!'},
 19: {'editor': 'Cog & Doodle',
      'description': "Ouch! That's gotta hurt."},
 20: {'editor': 'Cog Flappy Man',
      'description': 'A Cog full of hot air, what a shock!'},
 21: {'editor': 'Cog Ice Cream',
      'description': 'A Cog looking his best.'},
 22: {'editor': 'CogCicle',
      'description': 'A Cog looking his holiday best.'},
 23: {'editor': 'Holiday Bandstand',
      'description': 'Everyone loves a Holiday Party!'},
 24: {'editor': 'Chilly Cog',
      'description': "Ouch! That's gotta hurt."},
 25: {'editor': 'Snowman',
      'description': "So cool, he's hot!"},
 26: {'editor': 'SnowDoodle',
      'description': 'His only trick is being cold!'},
 27: {'editor': 'ValenToons Anvil',
      'description': "We've got your heart on a string!"}}
ActivityLabel = 'Cost - Activity Name'
PartyDoYouWantToPlan = 'Would you like to plan a new party right now?'
PartyPlannerOnYourWay = 'Have fun planning your party!'
PartyPlannerMaybeNextTime = 'Maybe next time.  Have a good day!'
PartyPlannerHostingTooMany = 'You can only host one party at a time, sorry.'
PartyPlannerNpcMinCost = 'It costs a minimum of %d Jellybeans to plan a party.'
PartyHatPublicPartyChoose = 'Do you want to go to the 1st available public party?'
PartyGateTitle = 'Public Parties'
PartyGateGoToParty = 'Go to\nParty!'
PartyGatePartiesListTitle = 'Hosts'
PartyGatesPartiesListToons = 'Toons'
PartyGatesPartiesListActivities = 'Activities'
PartyGatesPartiesListMinLeft = 'Minutes Left'
PartyGateLeftSign = 'Come On In!'
PartyGateRightSign = 'Public Parties Here!'
PartyGatePartyUnavailable = 'Sorry. That party is no longer available.'
PartyGatePartyFull = 'Sorry. That party is full.'
PartyGateInstructions = 'Click on a host, then click on "Go to Party"'
PartyActivityWaitingForOtherPlayers = 'Waiting for other toons to join the party game...'
PartyActivityPleaseWait = 'Please wait...'
DefaultPartyActivityTitle = 'Party Game Title'
DefaultPartyActivityInstructions = 'PartyGame Instructions'
PartyOnlyHostLeverPull = 'Only the host can start this activity. Sorry.'
PartyActivityDefaultJoinDeny = 'You cannot join this activity right now. Sorry.'
PartyActivityDefaultExitDeny = 'You cannot leave this activity right now. Sorry.'
PartyJellybeanRewardOK = 'OK'
PartyCatchActivityTitle = 'Party Catch Activity'
PartyCatchActivityInstructions = "Catch as many pieces of fruit as you can. Try not to 'catch' any %(badThing)s!"
PartyCatchActivityFinishPerfect = 'PERFECT GAME!'
PartyCatchActivityFinish = 'Good Game!'
PartyCatchActivityExit = 'EXIT'
PartyCatchActivityApples = 'apples'
PartyCatchActivityOranges = 'oranges'
PartyCatchActivityPears = 'pears'
PartyCatchActivityCoconuts = 'coconuts'
PartyCatchActivityWatermelons = 'watermelons'
PartyCatchActivityPineapples = 'pineapples'
PartyCatchActivityAnvils = 'anvils'
PartyCatchStarted = 'The game has started. Go play it.'
PartyCatchCannotStart = 'The game could not start right now.'
PartyCatchRewardMessage = 'Pieces of fruit caught: %s\n\nJellybeans earned: %d'
WinterPartyCatchActivityInstructions = "Catch as many presents as you can. Try not to 'catch' any %(badThing)s!"
WinterPartyCatchRewardMessage = 'Presents caught: %s\n\nJellybeans earned: %s'
PartyDanceActivityTitle = 'Party Dance Floor'
PartyDanceActivityInstructions = 'Combine 3 or more ARROW KEY patterns to do dance moves! There are 10 dance moves available. Can you find them all?'
PartyDanceActivity20Title = 'Party Dance Floor'
PartyDanceActivity20Instructions = 'Combine 3 or more ARROW KEY patterns to do dance moves! There are 20 dance moves available. Can you find them all?'
DanceAnimRight = 'Right'
DanceAnimReelNeutral = 'The Fishertoon'
DanceAnimConked = 'The Headbob'
DanceAnimHappyDance = 'The Happy Dance'
DanceAnimConfused = 'Very Dizzy'
DanceAnimWalk = 'Walking on the Moon'
DanceAnimJump = 'The Jump!'
DanceAnimFirehose = 'The Firetoon'
DanceAnimShrug = 'Who Knows?'
DanceAnimSlipForward = 'The Fall'
DanceAnimSadWalk = 'Tired'
DanceAnimWave = 'Hello Goodbye'
DanceAnimStruggle = 'The Shuffle Hop'
DanceAnimRunningJump = 'The Running Toon'
DanceAnimSlipBackward = 'The Backfall'
DanceAnimDown = 'Down'
DanceAnimUp = 'Up'
DanceAnimGoodPutt = 'The Putt'
DanceAnimVictory = 'The Victory Dance'
DanceAnimPush = 'The Mimetoon'
DanceAnimAngry = "Rock n' Roll"
DanceAnimLeft = 'Left'
PartyCannonActivityTitle = 'Party Cannons'
PartyCannonActivityInstructions = 'Hit the clouds to change their color and bounce in the air! While IN THE AIR, you can USE THE ARROW KEYS to GLIDE.'
PartyCannonResults = 'You collected %d jelly beans!\n\nNumber of Clouds Hit: %d'
FireworksActivityInstructions = 'Look up using the "Page Up" key to see better.'
FireworksActivityBeginning = 'Party fireworks are about to start! Enjoy the show!'
FireworksActivityEnding = 'Hope you enjoyed the show!'
PartyFireworksAlreadyActive = 'The fireworks show has already started.'
PartyFireworksAlreadyDone = 'The fireworks show is over.'
PartyTrampolineJellyBeanTitle = 'Jelly Beans Trampoline'
PartyTrampolineTricksTitle = 'Tricks Trampoline'
PartyTrampolineActivityInstructions = 'Use the Control key to jump.\n\nJump when your Toon is at its lowest point on the trampoline to jump higher.'
PartyTrampolineActivityOccupied = 'Trampoline in use.'
PartyTrampolineQuitEarlyButton = 'Hop Off'
PartyTrampolineBeanResults = 'You collected %d jelly beans.'
PartyTrampolineBonusBeanResults = 'You collected %d jelly beans, plus %d more for getting the Big Bean. '
PartyTrampolineTopHeightResults = 'Your top height was %d ft.'
PartyTrampolineTimesUp = "Time's Up"
PartyTrampolineReady = 'Ready...'
PartyTrampolineGo = 'Go!'
PartyTrampolineBestHeight = 'Best Height So Far:\n%s\n%d ft'
PartyTrampolineNoHeightYet = 'How high\ncan you jump?'
PartyTrampolineGetHeight = '%d ft'
PartyTeamActivityForMorePlural = 's'
PartyTeamActivityForMore = 'Waiting  for  %d  toon%s\non  each  side...'
PartyTeamActivityForMoreWithBalance = 'Waiting  for  %d  more  toon%s...'
PartyTeamActivityWaitingForOtherPlayers = 'Waiting  for  other  toons...'
PartyTeamActivityWaitingToStart = 'Starting  in...'
PartyTeamActivityExitButton = 'Hop Off'
PartyTeamActivitySwitchTeamsButton = 'Switch\nTeams'
PartyTeamActivityWins = '%s team wins!'
PartyTeamActivityLocalAvatarTeamWins = 'Your team won!'
PartyTeamActivityGameTie = "It's a tie!"
PartyTeamActivityJoinDenied = "Sorry, you can't join %s at this time."
PartyTeamActivityExitDenied = 'Sorry, you are unable to leave %s at this time.'
PartyTeamActivitySwitchDenied = "Sorry, you cant's switch teams at this time."
PartyTeamActivityTeamFull = 'Sorry, that team is already full!'
PartyTeamActivityRewardMessage = 'You got %d Jellybeans. Good job!'
PartyCogTeams = ('Blue', 'Orange')
PartyCogRewardMessage = 'Your Score: %d\n'
PartyCogRewardBonus = '\nYou got %d additional Jellybean%s because your team won!'
PartyCogJellybeanPlural = 's'
PartyCogSignNote = 'HI-SCORE\n%s\n%d'
PartyCogTitle = 'Cog-O-War'
PartyCogInstructions = 'Throw pies at cogs to push them away from your team. ' + "When time's up, the team with most cogs on the other side wins!" + '\n\nThrow with the CONTROL KEY. Move with the ARROW KEYS.'
PartyCogDistance = '%d ft'
PartyCogTimeUp = "Time's up!"
PartyCogGuiScoreLabel = 'SCORE'
PartyCogGuiPowerLabel = 'POWER'
PartyCogGuiSpamWarning = 'Hold CONTROL for more power!'
PartyCogBalanceBar = 'BALANCE'
PartyTugOfWarReady = 'Ready...'
PartyTugOfWarGo = 'GO!'
PartyTugOfWarGameEnd = 'Good  game!'
PartyTugOfWarTitle = 'Party Tug-of-War'
CalendarShowAll = 'Show All'
CalendarShowOnlyHolidays = 'Show Only Holidays'
CalendarShowOnlyParties = 'Show Only Parties'
CalendarEndsAt = 'Ends on'
CalendarStartedOn = 'Started on'
CalendarEndOf = 'End of'
CalendarPartyGetReady = 'Get ready!'
CalendarPartyGo = 'Go party!'
CalendarPartyFinished = "It's over..."
CalendarPartyCancelled = 'Cancelled.'
CalendarPartyNeverStarted = 'Never Started.'
NPCFriendPanelRemaining = '%d Remaining'
MapPageTitle = 'Map'
MapPageBackToPlayground = 'Back to Playground'
MapPageBackToCogHQ = 'Back to Cog Headquarters'
MapPageGoHome = 'Go Home'
MapPageYouAreHere = 'You are in: %s\n%s'
MapPageYouAreAtHome = 'You are at\nyour estate'
MapPageYouAreAtSomeonesHome = 'You are at %s estate'
MapPageGoTo = 'Go To\n%s'
OptionsPageTitle = 'Options'
ExtraOptionsPageTitle = 'Extra'
OptionsTabTitle = 'Options\n& Codes'
OptionsPageExitToontown = 'Exit Toontown'
OptionsPageMusic = 'Music Volume:'
OptionsPageSFX = 'SFX Volume:'
OptionsPageSFXOnLabel = 'Sound Effects are on.'
OptionsPageSFXOffLabel = 'Sound Effects are off.'
OptionsPageToonChatSoundsOnLabel = '   Type Chat Sounds are on.'
OptionsPageToonChatSoundsOffLabel = '   Type Chat Sounds are off.'
OptionsPageFriendsEnabledLabel = 'Accepting new friend requests.'
OptionsPageFriendsDisabledLabel = 'Not accepting friend requests.'
OptionsPageWhisperEnabledLabel = 'Allowing whispers from anyone.'
OptionsPageWhisperDisabledLabel = 'Allowing whispers from friends only.'
OptionsPageSpeedChatStyleLabel = 'SpeedChat Color'
OptionsPageDisplayWindowed = 'windowed'
OptionsPageSelect = 'Select'
OptionsPageToggleOn = 'Turn On'
OptionsPageToggleOff = 'Turn Off'
OptionsPageChange = 'Change'
OptionsPageDisplaySettings = 'Display: %(screensize)s, %(api)s'
OptionsPageDisplaySettingsNoApi = 'Display: %(screensize)s'
OptionsPageExitConfirm = 'Exit Toontown?'
DisplaySettingsTitle = 'Display Settings'
DisplaySettingsIntro = 'The following settings are used to configure the way Toontown is displayed on your computer.  It is usually unnecessary to adjust these unless you are experiencing a problem.'
DisplaySettingsIntroSimple = 'You may adjust the screen resolution to a higher value to improve the clarity of text and graphics in Toontown, but depending on your graphics card, some higher values may make the game run less smoothly or may not work at all.'
DisplaySettingsApi = 'Graphics API:'
DisplaySettingsResolution = 'Resolution:'
DisplaySettingsWindowed = 'In a window'
DisplaySettingsFullscreen = 'Full screen'
DisplaySettingsApply = 'Apply'
DisplaySettingsCancel = lCancel
DisplaySettingsApplyWarning = 'When you press OK, the display settings will change.  If the new configuration does not display properly on your computer, the display will automatically return to its original configuration after %s seconds.'
DisplaySettingsAccept = 'Press OK to keep the new settings, or Cancel to revert.  If you do not press anything, the settings will automatically revert back in %s seconds.'
DisplaySettingsRevertUser = 'Your previous display settings have been restored.'
DisplaySettingsRevertFailed = 'The selected display settings do not work on your computer.  Your previous display settings have been restored.'
OptionsPageCodesTab = 'Enter Code'
CdrPageTitle = 'Enter a Code'
CdrInstructions = 'Enter your code to receive a special item in your mailbox.'
CdrResultSuccess = 'Congratulations! Check your mailbox to claim your item!'
CdrResultInvalidCode = "You've entered an invalid code. Please check the code and try again."
CdrResultExpiredCode = "We're sorry. This code has expired."
CdrResultMailboxFull = 'Your mailbox is full. Please remove an item, then enter your code again.'
CdrResultAlreadyRedeemed = "You've already redeemed this item!"
CdrResultNotReady = "This code can't be used yet!"
CdrResultNotEligible = 'You are not eligible to use this code!'
TrackPageTitle = 'Gag Track Training'
TrackPageShortTitle = 'Gag Training'
TrackPageSubtitle = 'Complete ToonTasks to learn how to use new gags!'
TrackPageTraining = 'You are training to use %s gags.\nWhen you complete all 16 tasks you\nwill be able to use %s gags in battle.'
TrackPageClear = 'You are not training any Gag Tracks now.'
TrackPageFilmTitle = '%s\nTraining\nFilm'
TrackPageDone = 'FIN'
QuestPageToonTasks = 'ToonTasks'
QuestPageChoose = 'Choose'
QuestPageLocked = 'Locked'
QuestPageDestination = '%s\n%s\n%s'
QuestPageNameAndDestination = '%s\n%s\n%s\n%s'
QuestPosterHQOfficer = lHQOfficerM
QuestPosterHQBuildingName = lToonHQ
QuestPosterHQStreetName = 'Any Street'
QuestPosterHQLocationName = 'Any Neighborhood'
QuestPosterTailor = 'Tailor'
QuestPosterTailorBuildingName = 'Clothing Store'
QuestPosterTailorStreetName = 'Any Playground'
QuestPosterTailorLocationName = 'Any Neighborhood'
QuestPosterPlayground = 'In the playground'
QuestPosterAtHome = 'At your home'
QuestPosterInHome = 'In your home'
QuestPosterOnPhone = 'On your phone'
QuestPosterEstate = 'At your estate'
QuestPosterAnywhere = 'Anywhere'
QuestPosterAuxTo = 'to:'
QuestPosterAuxFrom = 'from:'
QuestPosterAuxFor = 'for:'
QuestPosterAuxOr = 'or:'
QuestPosterAuxReturnTo = 'Return to:'
QuestPosterLocationIn = ' in '
QuestPosterLocationOn = ' in '
QuestPosterFun = 'Just for fun!'
QuestPosterFishing = 'GO FISHING'
QuestPosterComplete = 'COMPLETE'
QuestPosterConfirmDelete = 'Are you sure you want to delete this ToonTask?'
QuestPosterDeleteBtn = 'Delete'
QuestPosterDialogYes = 'Delete'
QuestPosterDialogNo = 'Cancel'
ShardPageTitle = 'Districts'
ShardPageHelpIntro = 'Each District is a copy of the Toontown world.'
ShardPageHelpWhere = '  You are currently in the "%s" District.'
ShardPageHelpMove = '  To move to a new District, click on its name.'
ShardPagePopulationTotal = 'Total Toontown Population:\n%d'
ShardPageScrollTitle = 'Name            Population'
ShardPageLow = 'Quiet'
ShardPageMed = 'Ideal'
ShardPageHigh = 'Full'
ShardPageChoiceReject = 'Sorry, that district is full. Please try another one.'
SuitPageTitle = 'Cog Gallery'
SuitPageMystery = DialogQuestion + DialogQuestion + DialogQuestion
SuitPageQuota = '%s of %s'
SuitPageCogRadar = '%s present'
SuitPageBuildingRadarS = '%s building'
SuitPageBuildingRadarP = '%s buildings'
DisguisePageTitle = Cog + ' Disguise'
DisguisePageMeritAlert = 'Ready for\npromotion!'
DisguisePageCogLevel = 'Level %s'
DisguisePageMeritFull = 'Full'
FishPageTitle = 'Fishing'
FishPageTitleTank = 'Fish Bucket'
FishPageTitleCollection = 'Fish Album'
FishPageTitleTrophy = 'Fishing Trophies'
FishPageWeightStr = 'Weight: '
FishPageWeightLargeS = '%d lb. '
FishPageWeightLargeP = '%d lbs. '
FishPageWeightSmallS = '%d oz.'
FishPageWeightSmallP = '%d oz.'
FishPageWeightConversion = 16
FishPageValueS = 'Value: %d Jellybean'
FishPageValueP = 'Value: %d Jellybeans'
FishPageCollectedTotal = 'Fish Species Collected: %d of %d'
FishPageRodInfo = '%s Rod\n%d - %d Pounds'
FishPageTankTab = 'Bucket'
FishPageCollectionTab = 'Album'
FishPageTrophyTab = 'Trophies'
FishPickerTotalValue = 'Bucket: %s / %s\nValue: %d Jellybeans'
UnknownFish = '???'
FishingRod = '%s Rod'
FishTank = '%s Fishing Bucket'
FishingRodNameDict = {0: 'Twig',
 1: 'Bamboo',
 2: 'Hardwood',
 3: 'Steel',
 4: 'Gold'}
FishTankNameDict = {40: 'Medium',
 60: 'Big',
 80: 'Large',
 100: 'Ultra'}
FishTrophyNameDict = {0: 'Guppy',
 1: 'Minnow',
 2: 'Fish',
 3: 'Flying Fish',
 4: 'Shark',
 5: 'Swordfish',
 6: 'Killer Whale'}
GardenPageTitle = 'Gardening'
GardenPageTitleBasket = 'Flower Basket'
GardenPageTitleCollection = 'Flower Album'
GardenPageTitleTrophy = 'Gardening Trophies'
GardenPageTitleSpecials = 'Gardening Specials'
GardenPageBasketTab = 'Basket'
GardenPageCollectionTab = 'Album'
GardenPageTrophyTab = 'Trophies'
GardenPageSpecialsTab = 'Specials'
GardenPageCollectedTotal = 'Flower Varieties Collected: %d of %d'
GardenPageValueS = 'Value: %d Jellybean'
GardenPageValueP = 'Value: %d Jellybeans'
FlowerPickerTotalValue = 'Basket: %s / %s\nValue: %d Jellybeans'
GardenPageShovelInfo = '%s Shovel: %d / %d\n'
GardenPageWateringCanInfo = '%s Watering Can: %d / %d'
FlowerPageWeightConversion = 1
FlowerPageWeightLargeP = 'Large P'
FlowerPageWeightLargeS = 'LargeS '
FlowerPageWeightSmallP = 'SmallP '
FlowerPageWeightSmallS = 'SmallS '
FlowerPageWeightStr = 'Weight: %s'
KartPageTitle = 'Karts'
KartPageTitleCustomize = 'Kart Customizer'
KartPageTitleRecords = 'Personal Best Records'
KartPageTitleTrophy = 'Racing Trophies'
KartPageCustomizeTab = 'Customize'
KartPageRecordsTab = 'Records'
KartPageTrophyTab = 'Trophy'
KartPageTrophyDetail = 'Trophy %s : %s'
KartPageTickets = 'Tickets : '
KartPageConfirmDelete = 'Delete Accessory?'
KartShtikerDelete = 'Delete'
KartShtikerSelect = 'Select a Category'
KartShtikerNoAccessories = 'No Accessories Owned'
KartShtikerBodyColors = 'Kart Colors'
KartShtikerAccColors = 'Accessory Colors'
KartShtikerEngineBlocks = 'Hood Accessories'
KartShtikerSpoilers = 'Trunk Accessories'
KartShtikerFrontWheelWells = 'Front Wheel Accessories'
KartShtikerBackWheelWells = 'Back Wheel Accessories'
KartShtikerRims = 'Rim Accessories'
KartShtikerDecals = 'Decal Accessories'
KartShtikerBodyColor = 'Kart Color'
KartShtikerAccColor = 'Accessory Color'
KartShtikerEngineBlock = 'Hood'
KartShtikerSpoiler = 'Trunk'
KartShtikerFrontWheelWell = 'Front Wheel'
KartShtikerBackWheelWell = 'Back Wheel'
KartShtikerRim = 'Rim'
KartShtikerDecal = 'Decal'
KartShtikerDefault = 'Default %s'
KartShtikerNo = 'No %s Accessory'
QuestChoiceGuiCancel = lCancel
TrackChoiceGuiChoose = 'Choose'
TrackChoiceGuiCancel = lCancel
TrackChoiceGuiHEAL = 'Toonup lets you heal other Toons in battle.'
TrackChoiceGuiTRAP = 'Traps are powerful gags that must be used with Lure.'
TrackChoiceGuiLURE = 'Use Lure to stun Cogs or draw them into traps.'
TrackChoiceGuiSOUND = 'Sound gags affect all Cogs, but are not very powerful.'
TrackChoiceGuiDROP = 'Drop gags do lots of damage, but are not very accurate.'
EmotePageTitle = 'Expressions / Emotions'
EmotePageDance = 'You have built the following dance sequence:'
EmoteJump = 'Jump'
EmoteDance = 'Dance'
EmoteHappy = 'Happy'
EmoteSad = 'Sad'
EmoteAnnoyed = 'Annoyed'
EmoteSleep = 'Sleepy'
SuitBaseNameWithLevel = '%(name)s\n%(dept)s\nLevel %(level)s'
HealthForceAcknowledgeMessage = 'You cannot leave the playground until your Laff meter is smiling!'
InventoryTotalGags = 'Total gags\n%d / %d'
InventoryPinkSlips = '%s Pink Slips'
InventoryPinkSlip = '1 Pink Slip'
InventoryCrateKeys = '%s Crate Keys'
InventoryCrateKey = '1 Crate Key'
InventoryDelete = 'DELETE'
InventoryDone = 'DONE'
InventoryDeleteHelp = 'Click on a gag to DELETE it.'
InventorySkillCredit = 'Skill credit: %s'
InventorySkillCreditNone = 'Skill credit: None'
InventoryDetailAmount = '%(numItems)s / %(maxItems)s'
InventoryDetailData = 'Accuracy: %(accuracy)s\n%(damageString)s: %(damage)d%(bonus)s\n%(singleOrGroup)s'
InventoryTrackExp = '%(curExp)s / %(nextExp)s'
InventoryUberTrackExp = '%(nextExp)s to Go!'
InventoryAffectsOneCog = 'Affects: One ' + Cog
InventoryAffectsOneToon = 'Affects: One Toon'
InventoryAffectsAllToons = 'Affects: All Toons'
InventoryAffectsAllCogs = 'Affects: All ' + Cogs
InventoryHealString = 'Toon-up'
InventoryDamageString = 'Damage'
InventoryLureString = 'Rounds effective'
InventoryBattleMenu = 'BATTLE MENU'
InventoryRun = 'RUN'
InventorySOS = 'SOS'
InventoryPass = 'PASS'
InventoryFire = 'FIRE'
InventoryClickToAttack = 'Click a\ngag to\nattack'
InventoryDamageBonus = '(+%d)'
NPCForceAcknowledgeMessage = "You must ride the trolley before leaving.\n\n\n\n\n\n\n\n\nYou can find the trolley next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage2 = 'You must return to Toon Headquarters before leaving.\n\n\n\n\n\n\n\n\n\nToon Headquarters is located near the center of the playground.'
NPCForceAcknowledgeMessage3 = "Remember to ride the trolley.\n\n\n\n\n\n\n\nYou can find the trolley next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage4 = 'Congratulations!  You found and rode the trolley!\n\n\n\n\n\n\n\n\n\nNow report back to Toon Headquarters.'
NPCForceAcknowledgeMessage5 = "Don't forget your ToonTask!\n\n\n\n\n\n\n\n\n\n\nYou can find Cogs to defeat on the other side of tunnels like this."
NPCForceAcknowledgeMessage6 = 'Great job defeating those Cogs!\n\n\n\n\n\n\n\n\nHead back to Toon Headquarters as soon as possible.'
NPCForceAcknowledgeMessage7 = "Don't forget to make a friend!\n\n\n\n\n\n\nClick on another toon and use the New Friend button."
NPCForceAcknowledgeMessage8 = 'Great! You made a new friend!\n\n\n\n\n\n\n\n\nYou should go back at Toon Headquarters now.'
NPCForceAcknowledgeMessage9 = 'Good job using the phone!\n\n\n\n\n\n\n\n\nReturn to Toon Headquarters to claim your reward.'
ToonSleepString = '. . . ZZZ . . .'
MovieTutorialReward1 = 'You received %s %s point! When you get 10, you will get a new gag!'
MovieTutorialReward3 = 'Good job! You completed your first ToonTask!'
MovieTutorialReward4 = 'Go to Toon Headquarters for your reward!'
MovieTutorialReward5 = 'Have fun!'
BattleGlobalTracks = ['toon-up',
 'trap',
 'lure',
 'sound',
 'throw',
 'squirt',
 'drop']
BattleGlobalNPCTracks = ['restock', 'toons hit', 'cogs miss']
BattleGlobalAvPropStrings = (('Feather',
  'Megaphone',
  'Lipstick',
  'Bamboo Cane',
  'Pixie Dust',
  'Juggling Balls',
  'High Dive'),
 ('Banana Peel',
  'Rake',
  'Marbles',
  'Quicksand',
  'Trapdoor',
  'TNT',
  'Railroad'),
 ('$1 bill',
  'Small Magnet',
  '$5 bill',
  'Big Magnet',
  '$10 bill',
  'Hypno-goggles',
  'Presentation'),
 ('Bike Horn',
  'Whistle',
  'Bugle',
  'Aoogah',
  'Elephant Trunk',
  'Foghorn',
  'Opera Singer'),
 ('Cupcake',
  'Fruit Pie Slice',
  'Cream Pie Slice',
  'Whole Fruit Pie',
  'Whole Cream Pie',
  'Bomb Cake',
  'Wedding Cake'),
 ('Squirting Flower',
  'Glass of Water',
  'Squirt Gun',
  'Seltzer Bottle',
  'Fire Hose',
  'Storm Cloud',
  'Geyser'),
 ('Flower Pot',
  'Sandbag',
  'Anvil',
  'Big Weight',
  'Safe',
  'Grand Piano',
  'Toontanic'))
BattleGlobalAvPropStringsSingular = (('a Feather',
  'a Megaphone',
  'a Lipstick',
  'a Bamboo Cane',
  'a Pixie Dust',
  'a set of Juggling Balls',
  'a High Dive'),
 ('a Banana Peel',
  'a Rake',
  'a set of Marbles',
  'a patch of Quicksand',
  'a Trapdoor',
  'a TNT',
  'a Railroad'),
 ('a $1 bill',
  'a Small Magnet',
  'a $5 bill',
  'a Big Magnet',
  'a $10 bill',
  'a pair of Hypno-goggles',
  'a Presentation'),
 ('a Bike Horn',
  'a Whistle',
  'a Bugle',
  'an Aoogah',
  'an Elephant Trunk',
  'a Foghorn',
  'an Opera Singer'),
 ('a Cupcake',
  'a Fruit Pie Slice',
  'a Cream Pie Slice',
  'a Whole Fruit Pie',
  'a Whole Cream Pie',
  'a Bomb Cake',
  'a Wedding Cake'),
 ('a Squirting Flower',
  'a Glass of Water',
  'a Squirt Gun',
  'a Seltzer Bottle',
  'a Fire Hose',
  'a Storm Cloud',
  'a Geyser'),
 ('a Flower Pot',
  'a Sandbag',
  'an Anvil',
  'a Big Weight',
  'a Safe',
  'a Grand Piano',
  'the Toontanic'))
BattleGlobalAvPropStringsPlural = (('Feathers',
  'Megaphones',
  'Lipsticks',
  'Bamboo Canes',
  'Pixie Dusts',
  'sets of Juggling Balls',
  'High Dives'),
 ('Banana Peels',
  'Rakes',
  'sets of Marbles',
  'patches of Quicksand',
  'Trapdoors',
  'TNTs',
  'Railroads'),
 ('$1 bills',
  'Small Magnets',
  '$5 bills',
  'Big Magnets',
  '$10 bills',
  'pairs of Hypno-goggles',
  'Presentations'),
 ('Bike Horns',
  'Whistles',
  'Bugles',
  'Aoogahs',
  'Elephant Trunks',
  'Foghorns',
  'Opera Singers'),
 ('Cupcakes',
  'Fruit Pie Slices',
  'Cream Pie Slices',
  'Whole Fruit Pies',
  'Whole Cream Pies',
  'Bomb Cakes',
  'Wedding cakes'),
 ('Squirting Flowers',
  'Glasses of Water',
  'Squirt Guns',
  'Seltzer Bottles',
  'Fire Hoses',
  'Storm Clouds',
  'Geysers'),
 ('Flower Pots',
  'Sandbags',
  'Anvils',
  'Big Weights',
  'Safes',
  'Grand Pianos',
  'Oceanliners'))
BattleGlobalAvTrackAccStrings = ('Medium',
 'Perfect',
 'Low',
 'High',
 'Medium',
 'High',
 'Low')
BattleGlobalLureAccLow = 'Low'
BattleGlobalLureAccMedium = 'Medium'
AttackMissed = 'MISSED'
NPCCallButtonLabel = 'CALL'
LoaderLabel = 'Loading...'
StarringIn = 'Starring In...'
HeadingToHood = 'Heading %(to)s %(hood)s...'
HeadingToYourEstate = 'Heading to your estate...'
HeadingToEstate = "Heading to %s's estate..."
HeadingToFriend = "Heading to %s's friend's estate..."
HeadingToPlayground = 'Heading to the Playground...'
HeadingToStreet = 'Heading %(to)s %(street)s...'
TownBattleRun = 'Run all the way back to the playground?'
TownBattleChooseAvatarToonTitle = 'WHICH TOON?'
TownBattleChooseAvatarCogTitle = 'WHICH ' + Cog.upper() + '?'
TownBattleChooseAvatarBack = 'BACK'
FireCogTitle = 'PINK SLIPS LEFT:%s\nFIRE WHICH COG?'
FireCogLowTitle = 'PINK SLIPS LEFT:%s\nNOT ENOUGH SLIPS!'
TownBattleSOSNoFriends = 'No friends to call!'
TownBattleSOSWhichFriend = 'Call which friend?'
TownBattleSOSNPCFriends = 'Rescued Toons'
TownBattleSOSBack = 'BACK'
TownBattleToonSOS = 'SOS'
TownBattleToonFire = 'Fire'
TownBattleUndecided = '?'
TownBattleHealthText = '%(hitPoints)s/%(maxHit)s'
TownBattleWaitTitle = 'Waiting for\nother toons...'
TownSoloBattleWaitTitle = 'Please wait...'
TownBattleWaitBack = 'BACK'
TownBattleSOSPetSearchTitle = 'Searching for doodle\n%s...'
TownBattleSOSPetInfoTitle = '%s is %s'
TownBattleSOSPetInfoOK = lOK
TrolleyHFAMessage = 'You may not board the trolley until your Laff meter is smiling.'
TrolleyTFAMessage = 'You may not board the trolley until Joey says so.'
TrolleyHopOff = 'Hop off'
FishingExit = 'Exit'
FishingCast = 'Cast'
FishingAutoReel = 'Auto Reel'
FishingItemFound = 'You caught:'
FishingCrankTooSlow = 'Too\nslow'
FishingCrankTooFast = 'Too\nfast'
FishingFailure = "You didn't catch anything!"
FishingFailureTooSoon = "Don't start to reel in the line until you see a nibble.  Wait for your float to bob up and down rapidly!"
FishingFailureTooLate = 'Be sure to reel in the line while the fish is still nibbling!'
FishingFailureAutoReel = "The auto-reel didn't work this time.  Turn the crank by hand, at just the right speed, for your best chance to catch something!"
FishingFailureTooSlow = 'You turned the crank too slowly.  Some fish are faster than others.  Try to keep the speed bar centered!'
FishingFailureTooFast = 'You turned the crank too quickly.  Some fish are slower than others.  Try to keep the speed bar centered!'
FishingOverTankLimit = 'Your fish bucket is full. Go sell your fish to the Pet Shop Clerk and come back.'
FishingBroke = 'You do not have any more Jellybeans for bait! Ride the trolley or sell fish to the Pet Shop Clerks to earn more Jellybeans.'
FishingHowToFirstTime = 'Click and drag down from the Cast button. The farther down you drag, the stronger your cast will be. Adjust your angle to hit the fish targets.\n\nTry it now!'
FishingHowToFailed = 'Click and drag down from the Cast button. The farther down you drag, the stronger your cast will be. Adjust your angle to hit the fish targets.\n\nTry it again now!'
FishingBootItem = 'An old boot'
FishingJellybeanItem = '%s Jellybeans'
FishingNewEntry = 'New Species!'
FishingNewRecord = 'New Record!'
FishPokerCashIn = 'Cash In\n%s\n%s'
FishPokerLock = 'Lock'
FishPokerUnlock = 'Unlock'
FishPoker5OfKind = '5 of a Kind'
FishPoker4OfKind = '4 of a Kind'
FishPokerFullHouse = 'Full House'
FishPoker3OfKind = '3 of a Kind'
FishPoker2Pair = '2 Pair'
FishPokerPair = 'Pair'
TutorialGreeting1 = 'Hi %s!'
TutorialGreeting2 = 'Hi %s!\nCome over here!'
TutorialGreeting3 = 'Hi %s!\nCome over here!\nUse the arrow keys!'
PetTutorialTitle1 = 'The Doodle Panel'
PetTutorialTitle2 = 'Doodle SpeedChat'
PetTutorialTitle3 = 'Doodle Cattlelog'
PetTutorialNext = 'Next Page'
PetTutorialPrev = 'Previous Page'
PetTutorialDone = 'Done'
PetTutorialPage1 = 'Click on a Doodle to display the Doodle panel.  From here you can feed, scratch, and call the Doodle.'
PetTutorialPage2 = "Use the new 'Pets' area in the SpeedChat menu to get a Doodle to do a trick.  If he does it, reward him and he'll get better!"
PetTutorialPage3 = "Purchase new Doodle tricks from Clarabelle's Cattlelog.  Better tricks give better Toon-Ups!"

def getPetGuiAlign():
    from pandac.PandaModules import TextNode
    return TextNode.ACenter


GardenTutorialTitle1 = 'Gardening'
GardenTutorialTitle2 = 'Flowers'
GardenTutorialTitle3 = 'Trees'
GardenTutorialTitle4 = 'How-to'
GardenTutorialTitle5 = 'Statues'
GardenTutorialNext = 'Next Page'
GardenTutorialPrev = 'Previous Page'
GardenTutorialDone = 'Done'
GardenTutorialPage1 = 'Toon up your Estate with a garden!  You can plant flowers, grow trees, harvest super-powerful gags, and decorate with statues!'
GardenTutorialPage2 = 'Flowers are finicky and require unique Jellybean recipes. Once grown, put them in the wheelbarrow to sell them and work toward Laff boosts!'
GardenTutorialPage3 = 'Use a gag from your inventory to plant a tree.  After a few days, that gag will do more damage!  Remember to keep it healthy or the damage boost will go away.'
GardenTutorialPage4 = 'Walk up to these spots to plant, water, dig up or harvest your garden.'
GardenTutorialPage5 = "Statues can be purchased in Clarabelle's Cattlelog. Increase your skill to unlock the more extravagant statues!"
EstatePlaneReturn = "Cog invasion!!!"
EstatePlaneHoliday = "Happy halloween!!!"
PlaygroundDeathAckMessage = TheCogs + ' took all your gags!\n\nYou are sad. You may not leave the playground until you are happy.'
ForcedLeaveFactoryAckMsg = 'The ' + Foreman + ' was defeated before you could reach him. You did not recover any Cog parts.'
ForcedLeaveMintAckMsg = 'The Mint Floor Supervisor was defeated before you could reach him. You did not recover any Cogbucks.'
HeadingToFactoryTitle = '%s'
ForemanConfrontedMsg = '%s is battling the ' + Foreman + '!'
MintBossConfrontedMsg = '%s is battling the Supervisor!'
StageBossConfrontedMsg = '%s is battling the District Attorney!'
StageToonEnterElevator = '%s\nhas entered the elevator!'
ForcedLeaveStageAckMsg = 'The Law Clerk was defeated before you could reach him. You did not recover any Jury Notices.'
MinigameWaitingForOtherToons = 'Waiting for other toons to join...'
MinigamePleaseWait = 'Please wait...'
DefaultMinigameTitle = 'Minigame Title'
DefaultMinigameInstructions = 'Minigame Instructions'
HeadingToMinigameTitle = '%s'
MinigamePowerMeterLabel = 'Power Meter'
MinigamePowerMeterTooSlow = 'Too\nslow'
MinigamePowerMeterTooFast = 'Too\nfast'
MinigameTemplateTitle = 'Minigame Template'
MinigameTemplateInstructions = 'This is a template minigame. Use it to create new minigames.'
CannonGameTitle = 'Cannon Game'
CannonGameInstructions = 'Shoot your toon into the water tower as quickly as you can. Use the mouse or the arrow keys to aim the cannon. Be quick and win a big reward for everyone!'
CannonGameReward = 'REWARD'
TwoDGameTitle = 'Toon Escape'
TwoDGameInstructions = 'Escape from the ' + Cog + ' den as soon as you can. Use arrow keys to run/jump and Ctrl to squirt a ' + Cog + '. Collect ' + Cog + ' treasures to gain even more points.'
TwoDGameElevatorExit = 'EXIT'
TugOfWarGameTitle = 'Tug-of-War'
TugOfWarInstructions = "Alternately tap the left and right arrow keys just fast enough to line up the green bar with the red line. Don't tap them too slow or too fast, or you'll end up in the water!"
TugOfWarGameGo = 'GO!'
TugOfWarGameReady = 'Ready...'
TugOfWarGameEnd = 'Good game!'
TugOfWarGameTie = 'You tied!'
TugOfWarPowerMeter = 'Power meter'
PatternGameTitle = 'Match Jaymo'
PatternGameInstructions = 'Jaymo will show you a dance sequence. ' + "Try to repeat Jaymo's dance just the way you see it using the arrow keys!"
PatternGameWatch = 'Watch these dance steps...'
PatternGameGo = 'GO!'
PatternGameRight = 'Good, %s!'
PatternGameWrong = 'Oops!'
PatternGamePerfect = 'That was perfect, %s!'
PatternGameBye = 'Thanks for playing!'
PatternGamePleaseWait = 'Please wait...'
PatternGameFaster = 'You were\nfaster!'
PatternGameFastest = 'You were\nthe fastest!'
PatternGameYouCanDoIt = 'Come on!\nYou can do it!'
PatternGameOtherFaster = '\nwas faster!'
PatternGameOtherFastest = '\nwas the fastest!'
PatternGameGreatJob = 'Great Job!'
PatternGameRound = 'Round %s!'
PatternGameImprov = 'You did great!  Now Improv!'
RaceGameTitle = 'Race Game'
RaceGameInstructions = 'Click a number. Choose wisely! You only advance if no one else picked the same number.'
RaceGameWaitingChoices = 'Waiting for other toons to choose...'
RaceGameCardText = '%(name)s draws: %(reward)s'
RaceGameCardTextBeans = '%(name)s receives: %(reward)s'
RaceGameCardTextHi1 = '%(name)s is one Fabulous Toon!'
RaceGameForwardOneSpace = ' forward 1 space'
RaceGameForwardTwoSpaces = ' forward 2 spaces'
RaceGameForwardThreeSpaces = ' forward 3 spaces'
RaceGameBackOneSpace = ' back 1 space'
RaceGameBackTwoSpaces = ' back 2 spaces'
RaceGameBackThreeSpaces = ' back 3 spaces'
RaceGameOthersForwardThree = ' all others forward \n3 spaces'
RaceGameOthersBackThree = 'all others back \n3 spaces'
RaceGameInstantWinner = 'Instant Winner!'
RaceGameJellybeans2 = '2 Jellybeans'
RaceGameJellybeans4 = '4 Jellybeans'
RaceGameJellybeans10 = '10 Jellybeans!'
RingGameTitle = 'Ring Game'
RingGameInstructionsSinglePlayer = 'Try to swim through as many of the %s rings as you can.  Use the arrow keys to swim.'
RingGameInstructionsMultiPlayer = 'Try to swim through the %s rings.  Other toons will try for the other colored rings.  Use the arrow keys to swim.'
RingGameMissed = 'THAT WAS JUST PLASTIC!!'
RingGameGroupPerfect = 'GROUP\nPERFECT!!'
RingGamePerfect = 'PERFECT!'
RingGameGroupBonus = 'GROUP BONUS'
ColorRed = 'red'
ColorGreen = 'green'
ColorOrange = 'orange'
ColorPurple = 'purple'
ColorWhite = 'white'
ColorBlack = 'black'
ColorYellow = 'yellow'
DivingGameTitle = 'Treasure Dive'
DivingInstructionsSinglePlayer = 'Treasures will appear at the bottom of the lake.  Use the arrow keys to swim.  Avoid the fish and get the treasures up to the boat!'
DivingInstructionsMultiPlayer = 'Treasures will appear at the bottom of the lake.  Use the arrow keys to swim.  Work together to get the treasures up to the boat!'
DivingGameTreasuresRetrieved = 'Treasures Retrieved'
TargetGameTitle = 'Toon Slingshot'
TargetGameInstructionsSinglePlayer = 'Use your umbrella to land on the targets. The smaller the target, the more Jellybeans you get!'
TargetGameInstructionsMultiPlayer = 'Use your umbrella to land on the targets. The smaller the target, the more Jellybeans you get!'
TargetGameBoard = 'Round %s - Keeping Best Score'
TargetGameCountdown = 'Forced launch in %s seconds'
TargetGameCountHelp = 'Pound left and right arrows for power, stop to launch'
TargetGameFlyHelp = 'Press down to open umbrella'
TargetGameFallHelp = 'Use the arrow keys to land on target'
TargetGameBounceHelp = ' Bouncing can knock you off target'
TagGameTitle = 'Tag Game'
TagGameInstructions = 'Collect the treasures. You cannot collect treasure when you are IT!'
TagGameYouAreIt = 'You Are IT!'
TagGameSomeoneElseIsIt = '%s is IT!'
MazeGameTitle = 'Maze Game'
MazeGameInstructions = 'Collect the treasures. Try to get them all, but look out for the ' + Cogs + '!'
CatchGameTitle = 'Catching Game'
CatchGameInstructions = 'Catch as many %(fruit)s as you can. Watch out for the ' + Cogs + ", and try not to 'catch' any %(badThing)s!"
CatchGamePerfect = 'PERFECT!'
CatchGameApples = 'apples'
CatchGameOranges = 'oranges'
CatchGamePears = 'pears'
CatchGameCoconuts = 'coconuts'
CatchGameWatermelons = 'watermelons'
CatchGamePineapples = 'pineapples'
CatchGameAnvils = 'anvils'
PieTossGameTitle = 'Pie Toss Game'
PieTossGameInstructions = 'Toss pies at the targets.'
CogThiefGameTitle = 'Cog Thief'
CogThiefGameInstructions = 'Stop these Cogs from stealing our Gags! Press the Control key to throw pies. But be careful... they have a tendancy to explode!'
CogThiefBarrelsSaved = '%(num)d Barrels\nSaved!'
CogThiefBarrelSaved = '%(num)d Barrel\nSaved!'
CogThiefNoBarrelsSaved = 'No Barrels\nSaved'
CogThiefPerfect = 'PERFECT!'
MinigameRulesPanelPlay = 'PLAY'
MinigameRulesPanelSkip = 'SKIP\n%s/%s'
GagShopName = "Goofy's Gag Shop"
GagShopPlayAgain = 'PLAY\nAGAIN'
GagShopBackToPlayground = 'EXIT BACK TO\nPLAYGROUND'
GagShopYouHave = 'You have %s Jellybeans to spend'
GagShopYouHaveOne = 'You have 1 Jellybean to spend'
GagShopTooManyProps = 'Sorry, you have too many props'
GagShopDoneShopping = 'DONE\nSHOPPING'
GagShopTooManyOfThatGag = 'Sorry, you have enough %s already'
GagShopInsufficientSkill = 'You do not have enough skill for that yet'
GagShopNotEnoughJellybeans = 'You do not have enough Jellybeans for that gag'
GagShopYouPurchased = 'You purchased %s'
GagShopOutOfJellybeans = 'Sorry, you are all out of Jellybeans!'
GagShopPlayerDisconnected = '%s has disconnected'
GagShopPlayerExited = '%s has exited'
GagShopPlayerPlayAgain = 'Play Again'
GagShopPlayerBuying = 'Buying'
GenderShopFollow = 'Follow me!'
GenderShopSeeYou = 'See you later!'
GenderShopBoyButtonText = 'Boy'
GenderShopGirlButtonText = 'Girl'
BodyShopHead = 'Head'
BodyShopBody = 'Body'
BodyShopLegs = 'Legs'
ColorShopToon = 'Toon Color'
ColorShopHead = 'Head'
ColorShopBody = 'Body'
ColorShopLegs = 'Legs'
ColorShopParts = 'Multi Color'
ColorShopAll = 'Single Color'
ClothesShopShorts = 'Shorts'
ClothesShopShirt = 'Shirts'
ClothesShopBottoms = 'Bottoms'
PromptTutorial = "Congratulations!!\nYou are Toontown's newest citizen!\n\nWould you like to continue to the Toontorial or teleport directly to Toontown Central?"
MakeAToonSkipTutorial = 'Skip Toontorial'
MakeAToonEnterTutorial = 'Enter Toontorial'
MakeAToonDone = 'Done'
MakeAToonCancel = lCancel
MakeAToonNext = lNext
MakeAToonLast = 'Back'
CreateYourToon = 'Click the arrows to create your toon.'
CreateYourToonTitle = 'Choose  Boy  or  Girl'
ShapeYourToonTitle = 'Choose  Your  Type'
PaintYourToonTitle = 'Choose  Your  Color'
PickClothesTitle = 'Choose  Your  Clothes'
NameToonTitle = 'Choose  Your  Name'
CreateYourToonHead = "Click the 'head' arrows to pick different animals."
MakeAToonClickForNextScreen = 'Click the arrow below to go to the next screen.'
PickClothes = 'Click the arrows to pick clothes!'
PaintYourToon = 'Click the arrows to paint your toon!'
MakeAToonYouCanGoBack = 'You can go back to change your body too!'
MakeAFunnyName = 'Choose a funny name for your toon with my Pick-A-Name game!'
MustHaveAFirstOrLast1 = "Your toon should have a first or last name, don't you think?"
MustHaveAFirstOrLast2 = "Don't you want your toon to have a first or last name?"
ApprovalForName1 = "That's it, your toon deserves a great name!"
ApprovalForName2 = 'Toon names are the best kind of names!'
MakeAToonLastStep = 'Last step before going to Toontown!'
PickANameYouLike = 'Pick a name you like!'
TitleCheckBox = 'Title'
FirstCheckBox = 'First'
LastCheckBox = 'Last'
RandomButton = 'Random'
ShuffleButton = 'Shuffle'
NameShopSubmitButton = 'Submit'
TypeANameButton = 'Type-A-Name'
TypeAName = "Don't like these names?\nClick here -->"
PickAName = 'Try the PickAName game!\nClick here -->'
PickANameButton = 'Pick-A-Name'
RejectNameText = 'That name is not allowed. Please try again.'
WaitingForNameSubmission = 'Submitting your name...'
PetshopUnknownName = 'Name: ???'
PetshopDescGender = 'Gender:\t%s'
PetshopDescCost = 'Cost:\t%s Jellybeans'
PetshopDescTrait = 'Traits:\t%s'
PetshopDescStandard = 'Standard'
PetshopCancel = lCancel
PetshopSell = 'Sell Fish'
PetshopAdoptAPet = 'Adopt a Doodle'
PetshopReturnPet = 'Return your Doodle'
PetshopAdoptConfirm = 'Adopt %s for %d Jellybeans?'
PetshopGoBack = 'Go Back'
PetshopAdopt = 'Adopt'
PetshopReturnConfirm = 'Return %s?'
PetshopReturn = 'Return'
PetshopChooserTitle = "TODAY'S DOODLES"
PetshopGoHomeText = 'Would you like to go to your estate to play with your new Doodle?'
NameShopNameMaster = 'NameMasterEnglish.txt'
NameShopContinueSubmission = 'Continue Submission'
NameShopChooseAnother = 'Choose Another Name'
NameShopToonCouncil = 'The Toon Council\nwill review your\nname.  ' + 'Review may\ntake a few days.\nWhile you wait\nyour name will be\n '
PleaseTypeName = 'Please type your name:'
AllNewNames = 'All new names must be\napproved by the Toon Council.'
NameMessages = 'Be creative, and remember:\nno NPC names, please.'
NameShopNameRejected = 'The name you\nsubmitted has\nbeen rejected.'
NoPunctuation = "You can't use punctuation marks in your name!"
PeriodOnlyAfterLetter = 'You can use a period in your name, but only after a letter.'
ApostropheOnlyAfterLetter = 'You can use an apostrophe in your name, but only after a letter.'
NoNumbersInTheMiddle = 'Numeric digits may not appear in the middle of a word.'
ThreeWordsOrLess = 'Your name must be three words or fewer.'
NumToColor = ['White',
 'Peach',
 'Bright Red',
 'Red',
 'Maroon',
 'Sienna',
 'Brown',
 'Tan',
 'Coral',
 'Orange',
 'Yellow',
 'Cream',
 'Citrine',
 'Lime',
 'Sea Green',
 'Green',
 'Light Blue',
 'Aqua',
 'Blue',
 'Periwinkle',
 'Royal Blue',
 'Slate Blue',
 'Purple',
 'Lavender',
 'Pink',
 'Plum',
 'Black',
 'Mountain Green',
 'Icy Blue',
 'Desert Sand',
 'Mint',
 'Charcoal',
 'Hot Pink',
 'Honey Mustard',
 'Gray',
 'Neon Orange',
 'Sapphire',
 'Crimson',
 'Emerald',
 'Bronze']
AnimalToSpecies = {'dog': 'Dog',
 'cat': 'Cat',
 'mouse': 'Mouse',
 'horse': 'Horse',
 'rabbit': 'Rabbit',
 'duck': 'Duck',
 'monkey': 'Monkey',
 'bear': 'Bear',
 'pig': 'Pig'}
NameTooLong = 'That name is too long. Please try again.'
ToonAlreadyExists = 'You already have a toon named %s!'
NameAlreadyInUse = 'That name is already used!'
EmptyNameError = 'You must enter a name first.'
NameError = 'Sorry.  That name will not work.'
NCTooShort = 'That name is too short.'
NCNoDigits = 'Your name cannot contain numbers.'
NCNeedLetters = 'Each word in your name must contain some letters.'
NCNeedVowels = 'Each word in your name must contain some vowels.'
NCAllCaps = 'Your name cannot be all capital letters.'
NCMixedCase = 'That name has too many capital letters.'
NCBadCharacter = "Your name cannot contain the character '%s'"
NCGeneric = 'Sorry, that name will not work.'
NCTooManyWords = 'Your name cannot be more than four words long.'
NCDashUsage = "Dashes may only be used to connect two words together (like in 'Boo-Boo')."
NCCommaEdge = 'Your name may not begin or end with a comma.'
NCCommaAfterWord = 'You may not begin a word with a comma.'
NCCommaUsage = 'That name does not use commas properly. Commas must join two words together, like in the name "Dr. Quack, MD". Commas must also be followed by a space.'
NCPeriodUsage = 'That name does not use periods properly. Periods are only allowed in words like "Mr.", "Mrs.", "J.T.", etc.'
NCApostrophes = 'That name has too many apostrophes.'
RemoveTrophy = lToonHQ + ': ' + TheCogs + ' took over one of the buildings you rescued!'
STOREOWNER_TOOKTOOLONG = 'Need more time to think?'
STOREOWNER_GOODBYE = 'See you later!'
STOREOWNER_NEEDJELLYBEANS = 'You need to ride the Trolley to get some Jellybeans.'
STOREOWNER_GREETING = 'Choose what you want to buy.'
STOREOWNER_BROWSING = 'You can browse, but you need a clothing ticket to buy.'
STOREOWNER_BROWSING_JBS = 'You can browse, but you need at least 200 Jellybeans to buy.'
STOREOWNER_NOCLOTHINGTICKET = 'You need a clothing ticket to shop for clothes.'
STOREOWNER_NOFISH = 'Come back here to sell fish to the Pet Shop for Jellybeans.'
STOREOWNER_THANKSFISH = 'Thanks! The Pet Shop will love these. Bye!'
STOREOWNER_THANKSFISH_PETSHOP = 'These are some fine specimens! Thanks.'
STOREOWNER_PETRETURNED = "Don't worry.  We'll find a good home for your Doodle."
STOREOWNER_PETADOPTED = 'Congratulations on purchasing a Doodle! You can play with your new friend at your estate.'
STOREOWNER_PETCANCELED = 'Remember, if you see a Doodle you like, make sure to adopt him before someone else does!'
STOREOWNER_NOROOM = 'Hmm...you might want to make room in your closet before you buy new clothes.\n'
STOREOWNER_CONFIRM_LOSS = 'Your closet is full.  You will lose the clothes you were wearing.'
STOREOWNER_OK = lOK
STOREOWNER_CANCEL = lCancel
STOREOWNER_TROPHY = 'Wow! You collected %s of %s fish. That deserves a trophy and a Laff boost!'
SuitInvasionPrefix = '%s: ' % lToonHQ
SuitInvasionBegin = [
 'A Cog invasion has begun!!!',
 '%(plural)s have taken over Toontown!!!'
]
SuitInvasionEnd = [
 'The %(singular)s invasion has ended!!!',
 'The Toons have saved the day once again!!!'
]
SuitInvasionUpdate = [
 'Keep it up, Toons!!!',
 "The Cogs are beginning to explode in laughter!!!"
]
SuitInvasionBulletin = [
 'There is a Cog invasion in progress!!!',
 '%(plural)s have taken over Toontown!!!'
]
SkelecogInvasionBegin = [
 "This just in, Sellbot HQ's factory is going bonkers!",
 "Sellbot HQ's factory is pushing out incomplete cogs!",
 '%(singular)s Skelecogs have taken over Toontown!!!'
]
SkelecogInvasionEnd = [
 'The %(singular)s Skelecog invasion has ended!!!',
 'The Toons have saved the day once again!!!'
]
SkelecogInvasionBulletin = [
 'There is a Cog invasion in progress!!!',
 "Sellbot HQ's factory has pushed out incomplete Cogs!",
 '%(singular)s Skelecogs have taken over Toontown!!!'
]
WaiterInvasionBegin = [
 'Uh oh, it appears that the Cogs banquet has been rescheduled!',
 'The Waiter %(singular)s are invading Toontown!!!'
]
WaiterInvasionEnd = [
 'The Waiter %(singular)s waiters have been defeated!!!',
 'The Toons have saved the day once again!!!'
]
WaiterInvasionBulletin = [
 'There is a Cog invasion in progress!!!',
 'The Cogs banquet has been rescheduled!!!',
 'The Waiter %(singular)s are invading Toontown!!!'
]
V2InvasionBegin = [
 "Oh my, stock up on gags toons!",
 'The Toon HQ has spotted a Version 2.0 Cog Invasion!',
 'The V2 %(plural)s have taken over Toontown!!!'
]
V2InvasionEnd = [
 'The V2 %(singular)s invasion has ended!!!',
 'The Toons have saved the day once again!!!'
]
V2InvasionBulletin = [
 "There is a Cog invasion in progress!!!",
 'The Toon HQ has spotted a storm of Version 2.0 Cogs!',
 'The V2 %(plural)s have taken over Toontown!!!'
]
LeaderboardTitle = 'Toon Platoon'
QuestScript101_0 = 'Come here! Use the arrow keys to move.'
QuestScript101_1 = 'These are Cogs. They are robots that are trying to take over Toontown.'
QuestScript101_2 = 'There are many different kinds of Cogs and...'
QuestScript101_3 = '...they turn happy Toon buildings...'
QuestScript101_4 = '...into ugly Cog buildings!'
QuestScript101_5 = "But Cogs can't take a joke!"
QuestScript101_6 = 'A good gag will stop them.'
QuestScript101_8 = 'You also need a Laff meter.'
QuestScript101_9 = "If your Laff meter gets too low, you'll be sad!"
QuestScript101_10 = 'A happy Toon is a healthy Toon!'
QuestScript101_11 = "OH NO! There's a Cog outside my shop!"
QuestScript101_12 = 'HELP ME, PLEASE! Defeat that Cog!'
QuestScript101_13 = 'Here is your first ToonTask!'
QuestScript101_14 = 'Hurry up! Go defeat that Flunky!'
QuestScript110_1 = 'Good work defeating that Flunky. Let me give you a Shticker Book...'
QuestScript110_2 = 'The book is full of good stuff.'
QuestScript110_3 = "Open it, and I'll show you."
QuestScript110_4 = "The map shows where you've been."
QuestScript110_5 = 'Turn the page to see your gags...'
QuestScript110_6 = 'You can see your gags here.'
QuestScript110_7 = 'Turn the page to see your tasks.'
QuestScript110_8 = 'Take a ride on the trolley, and earn jelly beans to buy gags!'
QuestScript110_9 = 'To get to the trolley, go out the door behind me and head for the playground.'
QuestScript110_10 = 'Now, close the book and find the trolley!'
QuestScript110_11 = 'Return to Toon HQ when you are done. Bye!'
QuestScriptTutorialBlocker_1 = 'Why, hello there!'
QuestScriptTutorialBlocker_2 = 'Hello?'
QuestScriptTutorialBlocker_3 = "Oh! You don't know how to use SpeedChat!"
QuestScriptTutorialBlocker_4 = 'Click on the button to say something.'
QuestScriptTutorialBlocker_5 = 'Very good!\x07Where you are going there are many Toons to talk to.'
QuestScriptTutorialBlocker_6 = "If you want to chat with other Toons using the keyboard, there's another button you can use."
QuestScriptTutorialBlocker_7 = "It's called the SpeedChat Plus button."
QuestScriptTutorialBlocker_8 = 'Good luck! See you later!'
QuestScriptGagShop_1 = 'Welcome to the Gag Shop!'
QuestScriptGagShop_1a = 'This is where Toons come to buy gags to use against the Cogs.'
QuestScriptGagShop_3 = 'To buy gags, click on the gag buttons. Try getting some now!'
QuestScriptGagShop_4 = 'Good! You can use these gags in battle against the Cogs.'
QuestScriptGagShop_5 = "Here's a peek at the advanced gags..."
QuestScriptGagShop_6 = "When you're done buying gags, click this button to return to the Playground."
QuestScriptGagShop_7 = 'Normally you can use this button to play another Trolley Game...'
QuestScriptGagShop_8 = "...but there's no time for another game right now. You're needed in Toon HQ!"
QuestScript145_1 = 'I see you had no problem with the trolley!\x07Listen, the Cogs have stolen our blackboard eraser.\x07Go into the streets and fight Cogs until you recover the eraser.\x07To reach the streets go through one of the tunnels like this:'
QuestScript145_2 = "When you find our eraser, bring it back here.\x07Don't forget, if you need gags, ride the trolley.\x07Also, if you need to recover Laff points, collect ice cream cones in the Playground."
QuestScript150_1 = 'Great work!\x07Toontown is more fun when you have friends!'
QuestScript150_2 = 'To make friends, find another toon, and use the New Friend button.'
QuestScript150_3 = 'Once you have made a friend, come back here.'
QuestScript150_4 = 'Some tasks are too difficult to do alone!'
MissingKeySanityCheck = 'Ignore me'
SellbotBossName = 'FashionBoss'
CashbotBossName = 'Doctor Elvis'
LawbotBossName = 'Chief Office Master'
BossbotBossName = 'Chief Justice'
BossCogNameWithDept = '%(name)s\n%(dept)s'
BossCogPromoteDoobers = 'Welcome all new %s.   You are now going to be promoted to be the Fashion Designers. Congratulations!'
BossCogDoobersAway = {'s': "Give anyone who doesn't have design some."}
BossCogWelcomeToons = 'Welcome new Fashion Designers!'
BossCogPromoteToons = "I see that you new %s. need some design, let's go and..."
CagedToonInterruptBoss = "Hey! Over Here!"
CagedToonRescueQuery = "Hi. If you're such a great design. Come rescue me Toons."
BossCogDiscoverToons = 'What? Toons? In disguise?!'
BossCogAttackToons = "Attack them!!"
CagedToonDrop = ["HURRY UP YOU LAME TOONS!!",
 "HURRY UP!!",
 "YOU CAN'T DO IT! YOUR GONNA FAIL!",
 "YOU CAN'T DO IT! YOUR GONNA FAIL!"]
CagedToonPrepareBattleTwo = "Help Me! The Boss is getting stronger!\x07Go on and defeat his next set of Cogs.\x07But before you do, I must say this.\x07Just remember, you're going to fail!"
CagedToonPrepareBattleThree = "What you must do is throw a bunch of pies at the Boss.\x07But don't worry, I got pies that you can use.\x07Just jump up to my cage, and you can get cakes.\x07But there is a limit of 30 cakes. So you will need to jump back after you run out to restock.\x07Good Luck Toons!"
BossBattleNeedMorePies = 'Get pies you lame Toon!'
BossBattleHowToGetPies = 'ARE YOU NEW OR SOMETHING!??!?!??!?!'
BossBattleHowToThrowPies = 'THERES A DELETE KEY YOU KNOW!!'
CagedToonYippee = 'Yay!'
CagedToonThankYou = "Thank You for rescuing me!!\x07You sure taught that noob a lesson!!\x07You can come to my house anytime for a hangout.\x07Here's my phone number. If you ever want a hangout, call my phone.\x07Just click on the number I gave you."
CagedToonPromotion = "\x07Hmm, the boss left a Magic Wand.\x07Take it, then you can cast some spells if you need it."
CagedToonLastPromotion = "\x07Sweet, your a level %s on your Sarah Rose disguise.!\x07Clones normally don't get higher than 50.\x07You can't level up anymore, but you can get better spells if you keep rescuing more of us Evil Clones."
CagedToonHPBoost = "\x07You've rescued me my wonderful Padawans!\x07The Jeci Council decided to give you another Level. Congratulations!"
CagedToonMaxed = '\x07I see you progressed to a %s In your new Bad Guy Suit. I like it!\x07Flippy called me from the Jedi Council and said you should go rescue more Padawans!!'
CagedToonGoodbye = 'Good Luck! And may the force be with you!'
CagedToonBattleThree = {10: 'Nice jump, %(toon)s.  Here are some pies!',
 11: 'Hi, %(toon)s!  Thank You for shopping at my cage.',
 12: "Hey there, %(toon)s!  Thank You for shopping at my cage.",
 20: 'Hey, %(toon)s!  Throw the pies to deal damage.',
 21: 'Hi, %(toon)s!  Throw some pies to deal damage.',
 100: 'Make sure you restock when your pies run out.',
 101: 'Make sure you restock when your pies run out.',
 102: 'Be aware to "Jump" when he jumps.',
 103: 'Be aware to "Jump" when he jumps.',
 104: 'Be aware to "Jump" when he jumps.',
 105: "Make sure you restock when your pies run out.",
 106: 'Make sure you restock when your pies run out.'}
CagedToonBattleThreeMaxGivePies = 12
CagedToonBattleThreeMaxTouchCage = 21
CagedToonBattleThreeMaxAdvice = 106
CashbotBossHadEnough = "I had enough!"
CashbotBossOuttaHere = "I'm going to get a Train."
ResistanceToonCongratulations = "Horray! You did it!  Good Job!!\x07You done us a huge favor!\x07I hope that V.P wansn't too hard to destroy. Here is a reward.\x07%s\x07When you say the code. %s.\x07But you may only. I mean ONLY! Use it once, so be wise. If you don't, then you dumb.!"
ResistanceToonToonupInstructions = 'all the Toons near you will gain %s Laff points'
ResistanceToonToonupAllInstructions = 'all the Toons near you will gain full Laff points'
ResistanceToonMoneyInstructions = 'all the Toons near you will gain %s jellybeans'
ResistanceToonMoneyAllInstructions = 'all the Toons near you will fill their jellybean jars'
ResistanceToonTicketsInstructions = 'all the Toons near you will gain %s tickets'
ResistanceToonRestockInstructions = 'all the Toons near you will restock their "%s" gags'
ResistanceToonRestockAllInstructions = 'all the Toons near you will restock all their gags'
ResistanceToonMeritsInstructions = 'all the Toons near you will fill part of their %s'
ResistanceToonMeritsAllInstructions = 'all the Toons near you will fill part of all their promotion papers'
ResistanceToonLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog suit anymore, but you can certainly keep working for the Resistance!"
ResistanceToonHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
ResistanceToonMaxed = '\x07I see you progressed in this new %s Fighter suit.. Good Job!\x07On this day forth, you will now be helping us protect Jedi from the Jedi council.!'
CashbotBossCogAttack = 'Finish Them!!'
ResistanceToonWelcome = "Yay! You Made it Toons, now let's go to the School House before the Doctor sees us."
ResistanceToonTooLate = "Blast it! The Doctor is here, we're too late!"
CashbotBossDiscoverToons1 = "What is this?"
CashbotBossDiscoverToons2 = "I knew something was fishy about you Cogs. You're all Toons!"
ResistanceToonKeepHimBusy = "Fight the Cogs while I set up a trap!"
ResistanceToonWatchThis = 'Watch this!'
CashbotBossGetAwayFromThat = 'Hey!  You get away from that crane!'
ResistanceToonCraneInstructions1 = 'Get ready for my Trap C.F.O!'
ResistanceToonCraneInstructions2 = 'You see, we have a powerful weapon.'
ResistanceToonCraneInstructions3 = "We got Cranes!"
ResistanceToonCraneInstructions4 = 'Now what you must do is...'
ResistanceToonGetaway = "WHAT! I WASN'T FINISHED YET!"
ResistanceToonRunaway = "Get out there and fight the Boss, I know you can do it!"
CashbotCraneLeave = 'Leave Crane'
CashbotCraneAdvice = 'HURRY UP!'
CashbotMagnetAdvice = 'DO YOU NOT KNOW HOW TO CRANE YOU TOON???????'
CashbotCraneLeaving = 'Leaving crane'
MintElevatorRejectMessage = 'You cannot enter the Mints until you have completed your %s Cog Suit.'
BossElevatorRejectMessage = 'You cannot board this elevator until you have earned a promotion.'
SellbotRentalSuitMessage = "Wear this Rental Suit so you can get close enough to the VP to attack.\n\nYou won't earn Merits or promotions, but you can rescue a Toon for an SOS reward!"
SellbotCogSuitNoMeritsMessage = "Your Sellbot Disguise will get you in, but since you don't have enough Merits, you won't earn a promotion.\n\nIf you rescue the trapped Toon, you will earn an SOS Toon reward!"
SellbotCogSuitHasMeritsMessage = "It's Operation: Storm Sellbot!\n\nBring 5 or more Rental Suit Toons with you to defeat the VP and earn credit towards a reward!"
LawbotRentalSuitMessage = "Wear this Rental Suit so you can get close enough to the CJ to attack.\n\nYou won't earn Jury Notices or promotions, but you can pass the bar exam for a Cog Summon!"
LawbotCogSuitNoNoticesMessage = "Your Lawbot Disguise will get you in, but since you don't have enough Jury Notices, you won't earn a promotion.\n\nIf you pass the bar exam, you will earn a Cog Summon!"
LawbotCogSuitHasNoticesMessage = "It's Operation: Lawbots Lose!\n\nBring 7 or more Rental Suit Toons with you to defeat the CJ and earn credit towards a summon!"
CashbotRentalSuitMessage = "Wear this Rental Suit so you can get close enough to the CFO to attack.\n\nYou wont earn Cogbucks or promotions, but you can delay the CFO for a Toon Unite!"
CashbotCogSuitNoCogbucksMessage = "Your Cashbot Disguise will get you in, but since you don't have enough Cogbucks, you won't earn a promotion.\n\n If you delay the CFO, you will earn a Toon Unite!"
CashbotCogSuitHasCogbucksMessage = "It's Operation: Cashbot Chaos!\n\n Bring 6 or more Rental Suit Toons with you to defeat the CFO and earn credit towards a unite!"
BossbotRentalSuitMessage = "Wear this Rental Suit so you can get close enough to the CEO to attack.\n\bYou wont earn Stock Options or promotions, but you can soak the CEO for a Fire!"
BossbotCogSuitNoOptionsMessage = "Your Bossbot Disguise will get you in, but since you don't have enough Stock Options you won't warn a promotion.\n\n If you soak the CEO, you will earn a Fire!"
BossbotCogSuitHasOptionsMessage = "It's Operation: Besiege Bossbot!\n\n Bring in 8 Rental Suit Toons with you to defeat the CEO and earn credit towards a Fire!"
FurnitureTypeName = 'Furniture'
PaintingTypeName = 'Painting'
ClothingTypeName = 'Clothing'
ChatTypeName = 'SpeedChat Phrase'
EmoteTypeName = 'Acting Lessons'
BeanTypeName = 'Jellybeans'
PoleTypeName = 'Fishing Pole'
TankTypeName = 'Fishing Bucket'
WindowViewTypeName = 'Window View'
PetTrickTypeName = 'Doodle Training'
GardenTypeName = 'Garden Supplies'
RentalTypeName = 'Rental Item'
GardenStarterTypeName = 'Gardening Kit'
NametagTypeName = 'Name tag'
AccessoryTypeName = 'Accessory'
HatStylesDescriptions = {'hbb1': 'Green Baseball Cap',
 'kmh1': 'Mouskateer',
 'hbb2': 'Blue Baseball Cap',
 'hbb3': 'Orange Baseball Cap',
 'hsf1': 'Beige Safari Hat',
 'hsf2': 'Brown Safari Hat',
 'hsf3': 'Green Safari Hat',
 'hrb1': 'Pink Bow',
 'hrb2': 'Red Bow',
 'hrb3': 'Purple Bow',
 'hht1': 'Pink Heart',
 'hht2': 'Yellow Heart',
 'htp1': 'Black Top Hat',
 'htp2': 'Blue Top Hat',
 'hav1': 'Anvil Hat',
 'hfp1': 'Flower Hat',
 'hsg1': 'Sandbag Hat',
 'hwt1': 'Weight Hat',
 'hfz1': 'Fez Hat',
 'hgf1': 'Golf Hat',
 'hpt1': 'Party Hat',
 'hpt2': 'Toon Party Hat',
 'hpb1': 'Fancy Hat',
 'hcr1': 'Crown',
 'hcw1': 'Cowboy Hat',
 'hpr1': 'Pirate Hat',
 'hpp1': 'Propeller Hat',
 'hfs1': 'Fishing Hat',
 'hsb1': 'Sombrero Hat',
 'hst1': 'Straw Hat',
 'hsu1': 'Sun Hat',
 'hrb4': 'Yellow Bow',
 'hrb5': 'Checker Bow',
 'hrb6': 'Light Red Bow',
 'hrb7': 'Rainbow Bow',
 'hat1': 'Antenna Thingy',
 'hhd1': 'Beehive Hairdo',
 'hbw1': 'Bowler Hat',
 'hch1': 'Chef Hat',
 'hdt1': 'Detective Hat',
 'hft1': 'Fancy Feathers Hat',
 'hfd1': 'Fedora',
 'hmk1': "Mickey's Band Hat",
 'hft2': 'Feather Headband',
 'hhd2': 'Pompadour Hairdo',
 'hpc1': 'Princess Hat',
 'hrh1': 'Archer Hat',
 'hhm1': 'Roman Helmet',
 'hat2': 'Spider Antenna Thingy',
 'htr1': 'Tiara',
 'hhm2': 'Viking Helmet',
 'hwz1': 'Witch Hat',
 'hwz2': 'Wizard Hat',
 'hhm3': 'Conquistador Helmet',
 'hhm4': 'Firefighter Helmet',
 'hfp2': 'Anti-Cog Control Hat',
 'hhm5': 'Miner Hat',
 'hnp1': 'Napoleon Hat',
 'hpc2': 'Pilot Cap',
 'hph1': 'Cop Hat',
 'hwg1': 'Rainbow Wacky Wig',
 'hbb4': 'Yellow Baseball Cap',
 'hbb5': 'Red Baseball Cap',
 'hbb6': 'Aqua Baseball Cap',
 'hsl1': 'Sailor Hat',
 'hfr1': 'Samba Hat',
 'hby1': 'Bobby Hat',
 'hrb8': 'Pink Dots Bow',
 'hjh1': 'Jester Hat',
 'hbb7': 'Purple Baseball Cap',
 'hrb9': 'Green Checker Bow',
 'hwt2': 'Winter Hat',
 'hhw1': 'Bandana',
 'hhw2': 'Toonosaur Hat',
 'hob1': 'Jamboree Hat',
 'hbn1': 'Bird Hat'}
GlassesStylesDescriptions = {'grd1': 'Round Glasses',
 'gmb1': 'White Mini Blinds',
 'gnr1': 'Purple Narrow Glasses',
 'gst1': 'Yellow Star Glasses',
 'g3d1': 'Movie Glasses',
 'gav1': 'Aviator',
 'gce1': 'Cateye Glasses',
 'gdk1': 'Nerd Glasses',
 'gjo1': 'Celebrity Shades',
 'gsb1': 'Scuba Mask',
 'ggl1': 'Goggles',
 'ggm1': 'Groucho Glasses',
 'ghg1': 'Heart Glasses',
 'gie1': 'Bug Eye Glasses',
 'gmt1': 'Black Secret ID Mask',
 'gmt2': 'Blue Secret ID Mask',
 'gmt3': 'Blue Carnivale Mask',
 'gmt4': 'Purple Carnivale Mask',
 'gmt5': 'Aqua Carnivale Mask',
 'gmn1': 'Monocle',
 'gmo1': 'Smooch Glasses',
 'gsr1': 'Square Frame Glasses',
 'ghw1': 'Skull Eyepatch',
 'ghw2': 'Gem Eyepatch',
 'gag1': 'Alien Eyes',
 'ghy1': 'Hypno Lure Look'}
BackpackStylesDescriptions = {'bpb1': 'Blue Backpack',
 'bpb2': 'Orange Backpack',
 'bpb3': 'Purple BackPack',
 'bpd1': 'Red Dot Backpack',
 'bpd2': 'Yellow Dot Backpack',
 'bwg1': 'Bat Wings',
 'bwg2': 'Bee Wings',
 'bwg3': 'DragonFly Wings',
 'bst1': 'Scuba Tank',
 'bfn1': 'Shark Fin',
 'baw1': 'White Angel Wings',
 'baw2': 'Rainbow Angel Wings',
 'bwt1': 'Toys Backpack',
 'bwg4': 'Butterfly Wings',
 'bwg5': 'Pixie Wings',
 'bwg6': 'Dragon Wings',
 'bjp1': 'Jet Pack',
 'blg1': 'Bug Backpack',
 'bsa1': 'Plush Bear Pack',
 'bwg7': 'Bird wings',
 'bsa2': 'Plush Cat Pack',
 'bsa3': 'Plush Dog Pack',
 'bap1': 'Airplane Wings',
 'bhw1': 'Pirate Sword',
 'bhw2': 'Super Toon Cape',
 'bhw3': 'Vampire Cape',
 'bhw4': 'Toonosaur Backpack',
 'bob1': 'Jamboree Pack',
 'bfg1': 'Gag Attack Pack',
 'bfl1': 'Cog Pack'}
ShoesStylesDescriptions = {'sat1': 'Green Athletic Shoes',
 'sat2': 'Red Athletic Shoes',
 'smb1': 'Green Toon Boots',
 'scs1': 'Green Sneakers',
 'swt1': 'Wingtips',
 'smj1': 'Black Fancy Shoes',
 'sdk1': 'Boat Shoes',
 'sat3': 'Yellow Athletic Shoes',
 'scs2': 'Black Sneakers',
 'scs3': 'White Sneakers',
 'scs4': 'Pink Sneakers',
 'scb1': 'Cowboy Boots',
 'sfb1': 'Purple Boots',
 'sht1': 'Green Hi Top Sneakers',
 'smj2': 'Brown Fancy Shoes',
 'smj3': 'Red Fancy Shoes',
 'ssb1': 'Red Super Toon Boots',
 'sts1': 'Green Tennis Shoes',
 'sts2': 'Pink Tennis Shoes',
 'scs5': 'Red Sneakers',
 'smb2': 'Aqua Toon Boots',
 'smb3': 'Brown Toon Boots',
 'smb4': 'Yellow Toon Boots',
 'sfb2': 'Blue Square Boots',
 'sfb3': 'Green Hearts Boots',
 'sfb4': 'Grey Dots Boots',
 'sfb5': 'Orange Stars Boots',
 'sfb6': 'Pink Stars Boots',
 'slf1': 'Loafers',
 'smj4': 'Purple Fancy Shoes',
 'smt1': 'Motorcycle Boots',
 'sox1': 'Oxfords',
 'srb1': 'Pink Rain Boots',
 'sst1': 'Jolly Boots',
 'swb1': 'Beige Winter Boots',
 'swb2': 'Pink Winter Boots',
 'swk1': 'Work Boots',
 'scs6': 'Yellow Sneakers',
 'smb5': 'Pink Toon Boots',
 'sht2': 'Pink Hi Top Sneakers',
 'srb2': 'Red Dots Rain Boots',
 'sts3': 'Purple Tennis Shoes',
 'sts4': 'Violet Tennis Shoes',
 'sts5': 'Yellow Tennis Shoes',
 'srb3': 'Blue Rain Boots',
 'srb4': 'Yellow Rain Boots',
 'sat4': 'Black Athletic Shoes',
 'shw1': 'Pirate Shoes',
 'shw2': 'Toonosaur Feet'}
AccessoryNamePrefix = {0: 'hat unisex ',
 1: 'glasses unisex ',
 2: 'backpack unisex ',
 3: 'shoes unisex ',
 4: 'hat boy ',
 5: 'glasses boy ',
 6: 'backpack boy ',
 7: 'shoes boy ',
 8: 'hat girl ',
 9: 'glasses girl ',
 10: 'backpack girl ',
 11: 'shoes girl '}
AccessoryTypeNames = {}
for accessoryId in CatalogAccessoryItemGlobals.AccessoryTypes.keys():
    accessoryInfo = CatalogAccessoryItemGlobals.AccessoryTypes[accessoryId]
    if accessoryInfo[0] % 4 == 0:
        accessoryStyleDescription = HatStylesDescriptions
    elif accessoryInfo[0] % 4 == 1:
        accessoryStyleDescription = GlassesStylesDescriptions
    elif accessoryInfo[0] % 4 == 2:
        accessoryStyleDescription = BackpackStylesDescriptions
    else:
        accessoryStyleDescription = ShoesStylesDescriptions
    AccessoryTypeNames[accessoryId] = accessoryStyleDescription[accessoryInfo[1]]

SpecialEventMailboxStrings = {1: 'A special item from the Toon Council just for you!',
 2: "Here is your Melville's Fishing Tournament prize! Congratulations!",
 3: "Here is your Billy Budd's Fishing Tournament prize! Congratulations!",
 4: 'Here is your Acorn Acres April Invitational prize! Congratulations!',
 5: 'Here is your Acorn Acres C.U.P. Championship prize! Congratulations!',
 6: 'Here is your Gift-Giving Extravaganza prize! Congratulations!',
 7: "Here is your Top Toons New Year's Day Marathon prize! Congratulations!",
 8: 'Here is your Perfect Trolley Games Weekend prize! Congratulations!',
 9: 'Here is your Trolley Games Madness prize! Congratulations!',
 10: 'Here is your Grand Prix Weekend prize! Congratulations!',
 11: 'Here is your ToonTask Derby prize! Congratulations!',
 12: 'Here is your Save a Building Marathon prize! Congratulations!',
 13: 'Here is your Most Cogs Defeated Tournament prize! Congratulations!',
 14: 'Here is your Most V.P.s Defeated Tournament prize! Congratulations!',
 15: 'Here is your Operation: Storm Sellbot prize! Congratulations!',
 16: 'Here is your Most C.J.s Defeated Tournament prize! Congratulations!',
 17: 'Here is your Operation: Lawbots Lose prize! Congratulations!',
 18: 'Here is your Most C.F.O.s Defeated Tournament prize! Congratulations!',
 19: 'Here is your Operation: Cashbot Chaos prize! Congratulations!',
 20: 'Here is your Most C.E.O.s Defeated Tournament prize! Congratulations!',
 21: 'Here is your Operation: Besiege Bossbot prize! Congratulations!'}
RentalHours = 'Hours'
RentalOf = 'Of'
RentalCannon = 'Cannons!'
RentalGameTable = 'Game Table!'
EstateCannonGameEnd = 'The Cannon Game rental is over.'
GameTableRentalEnd = 'The Game Table rental is over.'
MessageConfirmRent = 'Begin rental? Cancel to save the rental for later'
MessageConfirmGarden = 'Are you sure you want to start a garden?'
FurnitureYourOldCloset = 'your old wardrobe'
FurnitureYourOldBank = 'your old bank'
TrunkHatGUI = 'Hats'
TrunkGlassesGUI = 'Glasses'
TrunkBackpackGUI = 'Backpacks'
TrunkShoesGUI = 'Shoes'
ChatItemQuotes = '"%s"'
FurnitureNames = {100: 'Armchair',
 105: 'Armchair',
 110: 'Chair',
 120: 'Desk Chair',
 130: 'Log Chair',
 140: 'Lobster Chair',
 145: 'Lifejacket Chair',
 150: 'Saddle Stool',
 160: 'Native Chair',
 170: 'Cupcake Chair',
 200: 'Bed',
 205: 'Bed',
 210: 'Bed',
 220: 'Bathtub Bed',
 230: 'Leaf Bed',
 240: 'Boat Bed',
 250: 'Cactus Hammock',
 260: 'Ice Cream Bed',
 270: "Olivia Erin & Cat's Bed",
 300: 'Player Piano',
 310: 'Pipe Organ',
 400: 'Fireplace',
 410: 'Fireplace',
 420: 'Round Fireplace',
 430: 'Fireplace',
 440: 'Apple Fireplace',
 450: "Erin's Fireplace",
 460: "Erin's Lit Fireplace",
 470: 'Lit Fireplace',
 480: 'Round Lit Fireplace',
 490: 'Lit Fireplace',
 491: 'Lit Fireplace',
 492: 'Apple Lit Fireplace',
 500: 'Wardrobe',
 502: '15 item Wardrobe',
 504: '20 item Wardrobe',
 506: '25 item Wardrobe',
 508: '50 item Wardrobe',
 510: 'Wardrobe',
 512: '15 item Wardrobe',
 514: '20 item Wardrobe',
 516: '25 item Wardrobe',
 518: '50 item Wardrobe',
 600: 'Short Lamp',
 610: 'Tall Lamp',
 620: 'Table Lamp',
 625: 'Table Lamp',
 630: 'Daisy Lamp',
 640: 'Daisy Lamp',
 650: 'Jellyfish Lamp',
 660: 'Jellyfish Lamp',
 670: 'Cowboy Lamp',
 680: 'Candle',
 681: 'Lit Candle',
 700: 'Cushioned Chair',
 705: 'Cushioned Chair',
 710: 'Couch',
 715: 'Couch',
 720: 'Hay Couch',
 730: 'Shortcake Couch',
 800: 'Desk',
 810: 'Log Desk',
 900: 'Umbrella Stand',
 910: 'Coat Rack',
 920: 'Trash Can',
 930: 'Red Mushroom',
 940: 'Yellow Mushroom',
 950: 'Coat Rack',
 960: 'Barrel Stand',
 970: 'Cactus Plant',
 980: 'Teepee',
 990: "Juliette's Fan",
 1000: 'Large Rug',
 1010: 'Round Rug',
 1015: 'Round Rug',
 1020: 'Small Rug',
 1030: 'Leaf Mat',
 1040: 'Presents',
 1050: 'Sled',
 1100: 'Display Cabinet',
 1110: 'Display Cabinet',
 1120: 'Tall Bookcase',
 1130: 'Low Bookcase',
 1140: 'Sundae Chest',
 1200: 'End Table',
 1210: 'Small Table',
 1215: 'Small Table',
 1220: 'Coffee Table',
 1230: 'Coffee Table',
 1240: "Snorkeler's Table",
 1250: 'Cookie Table',
 1260: 'Bedroom Table',
 1300: 'Bean Bank',
 1310: '15000 Bean Bank',
 1320: '20000 Bean Bank',
 1330: '25000 Bean Bank',
 1340: '30000 Bean Bank',
 1399: 'Telephone',
 1400: 'Cezanne Toon',
 1410: 'Flowers',
 1420: 'Modern Mickey',
 1430: 'Rembrandt Toon',
 1440: 'Toonscape',
 1441: "Whistler's Horse",
 1442: 'Toon Star',
 1443: 'Not a Pie',
 1450: 'Mickey and Minnie',
 1500: 'Radio',
 1510: 'Radio',
 1520: 'Radio',
 1530: 'Television',
 1531: '50" HD Television',
 1532: '100" HD Television', 
 1600: 'Short Vase',
 1610: 'Tall Vase',
 1620: 'Short Vase',
 1630: 'Tall Vase',
 1640: 'Short Vase',
 1650: 'Short Vase',
 1660: 'Coral Vase',
 1661: 'Shell Vase',
 1670: 'Rose Vase',
 1680: 'Rose Watercan',
 1700: 'Popcorn Cart',
 1710: 'Ladybug',
 1720: 'Fountain',
 1725: 'Washing Machine',
 1800: 'Fish Bowl',
 1810: 'Fish Bowl',
 1900: 'Swordfish',
 1910: 'Hammerhead',
 1920: 'Hanging Horns',
 1930: 'Simple Sombrero',
 1940: 'Fancy Sombrero',
 1950: 'Dream Catcher',
 1960: 'Horseshoe',
 1970: 'Bison Portrait',
 2000: 'Candy Swing Set',
 2010: 'Cake Slide',
 3000: 'Banana Split Tub',
 4000: 'Boy Trunk',
 4010: 'Girl Trunk',
 10000: 'Short Pumpkin',
 10010: 'Tall Pumpkin',
 10020: 'Winter Tree',
 10030: 'Winter Wreath',
 10040: 'Cog Nation Crate'}
ClothingArticleNames = ('Shirt',
 'Shirt',
 'Shirt',
 'Shorts',
 'Shorts',
 'Skirt',
 'Shorts')
ClothingTypeNames = {1001: 'Ghost Shirt',
 1002: 'Pumpkin Shirt',
 1112: 'Bee Shirt',
 1113: 'Pirate Shirt',
 1114: 'Super Toon Shirt',
 1115: 'Vampire Shirt',
 1116: 'Toonosaur Shirt',
 1117: 'Bee Shorts',
 1118: 'Pirate Shorts',
 1119: 'Super Toon Shorts',
 1120: 'Vampire Shorts',
 1121: 'Toonosaur Shorts',
 1122: 'Bee Shorts',
 1123: 'Pirate Shorts',
 1124: 'Super Toon Shorts',
 1125: 'Vampire Shorts',
 1126: 'Toonosaur Shorts',
 1127: 'Pirate Skirt',
 1304: "O'Shirt",
 1305: "O'Shorts",
 1306: "O'Skirt",
 1400: "Matthew's Shirt",
 1401: "Jessica's Shirt",
 1402: "Marissa's Shirt",
 1600: 'Trap Outfit',
 1601: 'Sound Outfit',
 1602: 'Lure Outfit',
 1603: 'Trap Outfit',
 1604: 'Sound Outfit',
 1605: 'Lure Outfit',
 1606: 'Trap Outfit',
 1607: 'Sound Outfit',
 1608: 'Lure Outfit',
 1723: 'Bee Shirt',
 1724: 'SuperToon Shirt',
 1734: 'Bee Shorts',
 1735: 'SuperToon Shorts',
 1739: 'Bee Skirt',
 1740: 'SuperToon Skirt',
 1743: 'Skeleton Shirt',
 1744: 'Spider Shirt',
 1745: 'Spider Shorts',
 1746: 'Skeleton Shorts',
 1747: 'Skeleton Skirt',
 1748: 'Spider Skirt',
 1749: 'Silly Mailbox Shirt',
 1750: 'Silly Trash Can Shirt',
 1751: 'Loony Labs Shirt',
 1752: 'Silly Hydrant Shirt',
 1753: 'Silly Meter Shirt',
 1754: 'Cog-Crusher Shirt',
 1755: 'Cog-Crusher Shorts',
 1756: 'Cog-Crusher Shorts',
 1757: 'Victory Party Shirt',
 1758: 'Relaxed Victory Shirt',
 1763: 'Smashed Sellbot Shirt',
 1764: 'Most V.P.s Defeated Shirt',
 1765: 'Sellbot Smasher Shirt',
 1766: 'Sellbot Smasher Shorts',
 1767: 'Sellbot Smasher Shorts',
 1768: 'Jellybean Bank Shirt',
 1769: 'Doodle Shirt',
 1770: 'Vampire Shirt',
 1771: 'Turtle Shirt',
 1772: 'Vampire Shorts',
 1773: 'Vampire Shorts',
 1774: 'Turtle Shorts',
 1775: 'Turtle Shorts',
 1776: 'Get Connected Mover & Shaker Shirt',
 1777: 'Smashed Lawbot Shirt',
 1778: 'Most C.J.s Defeated Shirt',
 1779: 'Lawbot Smasher Shirt',
 1780: 'Lawbot Smasher Shorts',
 1781: 'Lawbot Smasher Shorts',
 1782: 'Racing Shirt 3',
 1783: 'Racing Shorts 1',
 1784: 'Racing Skirt 1',
 1801: 'Batty Moon Shirt',
 1802: 'Mittens Shirt',
 1821: 'Plaid Punk Shirt'}
AccessoryArticleNames = ('Hat',
 'Glasses',
 'Backpack',
 'Shoes',
 'Hat',
 'Glasses',
 'Backpack',
 'Shoes',
 'Hat',
 'Glasses',
 'Backpack',
 'Shoes')
SurfaceNames = ('Wallpaper',
 'Moulding',
 'Flooring',
 'Wainscoting',
 'Border')
WallpaperNames = {1000: 'Parchment',
 1100: 'Milan',
 1200: 'Dover',
 1300: 'Victoria',
 1400: 'Newport',
 1500: 'Pastoral',
 1600: 'Harlequin',
 1700: 'Moon',
 1800: 'Stars',
 1900: 'Flowers',
 2000: 'Spring Garden',
 2100: 'Formal Garden',
 2200: 'Race Day',
 2300: 'Touchdown!',
 2400: 'Cloud 9',
 2500: 'Climbing Vine',
 2600: 'Springtime',
 2700: 'Kokeshi',
 2800: 'Posies',
 2900: 'Angel Fish',
 3000: 'Bubbles',
 3100: 'Bubbles',
 3200: 'Go Fish',
 3300: 'Stop Fish',
 3400: 'Sea Horse',
 3500: 'Sea Shells',
 3600: 'Underwater',
 3700: 'Boots',
 3800: 'Cactus',
 3900: 'Cowboy Hat',
 10100: 'Cats',
 10200: 'Bats',
 11000: 'Snowflakes',
 11100: 'Hollyleaf',
 11200: 'Snowman',
 12000: 'ValenToons',
 12100: 'ValenToons',
 12200: 'ValenToons',
 12300: 'ValenToons',
 13000: 'Shamrock',
 13100: 'Shamrock',
 13200: 'Rainbow',
 13300: 'Shamrock'}
FlooringNames = {1000: 'Hardwood Floor',
 1010: 'Carpet',
 1020: 'Diamond Tile',
 1030: 'Diamond Tile',
 1040: 'Grass',
 1050: 'Beige Bricks',
 1060: 'Red Bricks',
 1070: 'Square Tile',
 1080: 'Stone',
 1090: 'Boardwalk',
 1100: 'Dirt',
 1110: 'Wood Tile',
 1120: 'Tile',
 1130: 'Honeycomb',
 1140: 'Water',
 1150: 'Beach Tile',
 1160: 'Beach Tile',
 1170: 'Beach Tile',
 1180: 'Beach Tile',
 1190: 'Sand',
 10000: 'Ice Cube',
 10010: 'Igloo',
 11000: 'Shamrock',
 11010: 'Shamrock'}
MouldingNames = {1000: 'Knotty',
 1010: 'Painted',
 1020: 'Dental',
 1030: 'Flowers',
 1040: 'Flowers',
 1050: 'Ladybug',
 1060: 'ValenToons',
 1070: 'Beach',
 1080: 'Winter Lights 1',
 1085: 'Winter Lights 2',
 1090: 'Winter Lights 3',
 1100: "ValenToon's Cupid",
 1110: "ValenToon's Heart 1",
 1120: "ValenToon's Heart 2"}
WainscotingNames = {1000: 'Painted',
 1010: 'Wood Panel',
 1020: 'Wood',
 1030: 'ValenToons',
 1040: 'Underwater'}
WindowViewNames = {10: 'Large Garden',
 20: 'Wild Garden',
 30: 'Greek Garden',
 40: 'Cityscape',
 50: 'Wild West',
 60: 'Under the Sea',
 70: 'Tropical Island',
 80: 'Starry Night',
 90: 'Tiki Pool',
 100: 'Frozen Frontier',
 110: 'Farm Country',
 120: 'Native Camp',
 130: 'Main Street'}
SpecialEventNames = {1: 'Generic Award',
 2: "Melville's Fishing Tournament",
 3: "Billy Budd's Fishing Tournament",
 4: 'Acorn Acres April Invitational',
 5: 'Acorn Acres C.U.P. Championship',
 6: 'Gift-Giving Extravaganza',
 7: "Top Toons New Year's Day Marathon",
 8: 'Perfect Trolley Games Weekend',
 9: 'Trolley Games Madness',
 10: 'Grand Prix Weekend',
 11: 'ToonTask Derby',
 12: 'Save a Building Marathon',
 13: 'Most Cogs Defeated',
 14: 'Most V.P.s Defeated',
 15: 'Operation Storm Sellbot Event',
 16: 'Most C.J.s Defeated',
 17: 'Operation Lawbots Lose Event',
 18: 'Most C.F.O.s Defeated',
 19: 'Operation Cashbot Chaos Event',
 20: 'Most C.E.O.s Defeated',
 21: 'Operation Besiege Bossbot Event'}
NewCatalogNotify = 'There are new items available to order at your phone!'
NewDeliveryNotify = 'A new delivery has just arrived at your mailbox!'
CatalogNotifyFirstCatalog = 'Your first cattlelog has arrived!  You may use this to order new items for yourself or for your house.'
CatalogNotifyNewCatalog = 'Your cattlelog #%s has arrived!  You can go to your phone to order items from this cattlelog.'
CatalogNotifyNewCatalogNewDelivery = 'A new delivery has arrived at your mailbox!  Also, your cattlelog #%s has arrived!'
CatalogNotifyNewDelivery = 'A new delivery has arrived at your mailbox!'
CatalogNotifyNewCatalogOldDelivery = 'Your cattlelog #%s has arrived, and there are still items waiting in your mailbox!'
CatalogNotifyOldDelivery = 'There are still items waiting in your mailbox for you to pick up!'
CatalogNotifyInstructions = 'Click the "Go home" button on the map page in your Shticker Book, then walk up to the phone inside your house.'
CatalogNewDeliveryButton = 'New\nDelivery!'
CatalogNewCatalogButton = 'New\nCattlelog'
CatalogSaleItem = 'Sale!  '
DistributedMailboxEmpty = 'Your mailbox is empty right now.  Come back here to look for deliveries after you place an order from your phone!'
DistributedMailboxWaiting = 'Your mailbox is empty right now, but the package you ordered is on its way.  Check back later!'
DistributedMailboxReady = 'Your order has arrived!'
DistributedMailboxNotOwner = 'Sorry, this is not your mailbox.'
Clarabelle = 'Clarabelle'
MailboxExitButton = 'Close Mailbox'
MailboxAcceptButton = 'Take this item'
MailBoxDiscard = 'Discard this item'
MailboxAcceptInvite = 'Accept this invite'
MailBoxRejectInvite = 'Reject this invite'
MailBoxDiscardVerify = 'Are you sure you want to Discard %s?'
MailBoxRejectVerify = 'Are you sure you want to Reject %s?'
MailboxOneItem = 'Your mailbox contains 1 item.'
MailboxNumberOfItems = 'Your mailbox contains %s items.'
MailboxGettingItem = 'Taking %s from mailbox.'
MailboxGiftTag = 'Gift From: %s'
MailboxGiftTagAnonymous = 'Anonymous'
MailboxItemNext = 'Next\nItem'
MailboxItemPrev = 'Previous\nItem'
MailboxDiscard = 'Discard'
MailboxReject = 'Reject'
MailboxLeave = 'Keep'
CatalogCurrency = 'beans'
CatalogHangUp = 'Hang Up'
CatalogNew = 'NEW'
CatalogBackorder = 'BACKORDER'
CatalogSpecial = 'SPECIAL'
CatalogEmblem = 'EMBLEM'
CatalogPagePrefix = 'Page'
CatalogGreeting = "Hello! Thanks for calling Clarabelle's Cattlelog. Can I help you?"
CatalogGoodbyeList = ['Bye now!',
 'Call back soon!',
 'Thanks for calling!',
 'Ok, bye now!',
 'Bye!']
CatalogHelpText1 = 'Turn the page to see items for sale.'
CatalogSeriesLabel = 'Series %s'
CatalogGiftError = 'Error'
CatalogGiftFor = 'Buy Gift for:'
CatalogGiftTo = 'To: %s'
CatalogGiftToggleOn = 'Stop Gifting'
CatalogGiftToggleOff = 'Buy Gifts'
CatalogGiftUpdating = 'Updating...'
CatalogGiftChoose = 'Choose a friend!'
CatalogPurchaseItemAvailable = 'Congratulations on your new purchase!  You can start using it right away.'
CatalogPurchaseGiftItemAvailable = 'Excellent!  %s can start using your gift right away.'
CatalogPurchaseItemOnOrder = 'Congratulations! Your purchase will be delivered to your mailbox soon.'
CatalogPurchaseGiftItemOnOrder = 'Excellent! Your gift to %s will be delivered to their mailbox.'
CatalogAnythingElse = 'Anything else I can get you today?'
CatalogPurchaseClosetFull = 'Your closet is full.  You may purchase this item anyway, but if you do you will need to delete something from your closet to make room for it when it arrives.\n\nDo you still want to purchase this item?'
CatalogPurchaseTrunkFull = 'Your trunk is full. If you purchase this item, you\xe2\x80\x99ll need to delete another item from your trunk to make more room.\n\nDo you still want to purchase this item?'
CatalogAcceptClosetFull = 'Your closet is full.  You must go inside and delete something from your closet to make room for this item before you can take it out of your mailbox.'
CatalogAcceptTrunkFull = 'Your trunk is full.  You must delete something from your trunk before you can take this item out of your mailbox.'
CatalogAcceptShirt = 'You are now wearing your new hat.  The hat you were wearing before has been moved to your trunk.'
CatalogAcceptShorts = 'You are now wearing your new shorts.  What you were wearing before has been moved to your closet.'
CatalogAcceptSkirt = 'You are now wearing your new skirt.  What you were wearing before has been moved to your closet.'
CatalogAcceptHat = 'You are now wearing your new hat.  The hat you were wearing before has been moved to your trunk.'
CatalogAcceptGlasses = 'You are now wearing your new glasses.  The glasses you were wearing before have been moved to your trunk.'
CatalogAcceptBackpack = 'You are now wearing your new backpack.  The backpack you were wearing before has been moved to your trunk.'
CatalogAcceptShoes = 'You are now wearing your new shoes.  The shoes you were wearing before have been moved to your trunk.'
CatalogAcceptPole = "You're now ready to go catch some bigger fish with your new pole!"
CatalogAcceptPoleUnneeded = 'You already have a better pole than this one!'
CatalogAcceptTank = "You're now ready to catch more fish!"
CatalogAcceptTankUnneeded = 'You already have a bigger tank than this one!'
CatalogAcceptChat = 'You now have a new SpeedChat!'
CatalogAcceptEmote = 'You now have a new Emotion!'
CatalogAcceptBeans = 'You received some jelly beans!'
CatalogAcceptRATBeans = 'Your Toon recruit reward has arrived!'
CatalogAcceptPartyRefund = "Your party was never started. Here's your refund!"
CatalogAcceptNametag = 'Your new name tag has arrived!'
CatalogAcceptGarden = 'Your garden supplies have arrived!'
CatalogAcceptPet = 'You now have a new Pet Trick!'
CatalogPurchaseHouseFull = 'Your house is full.  You may purchase this item anyway, but if you do you will need to delete something from your house to make room for it when it arrives.\n\nDo you still want to purchase this item?'
CatalogAcceptHouseFull = 'Your house is full. You can not accept this item until you free up some room. Would you like to discard this item now?'
CatalogAcceptInAttic = 'Your new item is now in your attic.  You can put it in your house by going inside and clicking on the "Move Furniture" button.'
CatalogAcceptInAtticP = 'Your new items are now in your attic.  You can put them in your house by going inside and clicking on the "Move Furniture" button.'
CatalogPurchaseMailboxFull = "Your mailbox is full!  You can't purchase this item until you take some items out of your mailbox to make room."
CatalogPurchaseGiftMailboxFull = "%s's mailbox is full!  You can't purchase this item."
CatalogPurchaseOnOrderListFull = "You have too many items currently on order.  You can't order any more items until some of the ones you have already ordered arrive."
CatalogPurchaseGiftOnOrderListFull = '%s has too many items currently on order.'
CatalogPurchaseGeneralError = 'The item could not be purchased because of some internal game error: error code %s.'
CatalogPurchaseGiftGeneralError = 'The item could not be gifted to %(friend)s because of some internal game error: error code %(error)s.'
CatalogPurchaseGiftNotAGift = 'This item could not be sent to %s because it would be an unfair advantage.'
CatalogPurchaseGiftWillNotFit = "This item could not be sent to %s because it doesn't fit them."
CatalogPurchaseGiftLimitReached = "This item could not be sent to %s because they already have it."
CatalogPurchaseGiftNotEnoughMoney = "This item could not be sent to %s because you can't afford it."
CatalogPurchaseGiftTooFast = "This item could not be sent to %s because you are sending gifts too fast."
CatalogAcceptGeneralError = 'The item could not be removed from your mailbox because of some internal game error: error code %s.'
CatalogAcceptRoomError = "You don't have any place to put this. You'll have to get rid of something."
CatalogAcceptLimitError = "You already have as many of these as you can handle. You'll have to get rid of something."
CatalogAcceptFitError = "This won't fit you!"
CatalogAcceptInvalidError = 'This item has gone out of style!'
CatalogAcceptClosetError = 'You already have a bigger closet!'
MailboxOverflowButtonDicard = 'Discard'
MailboxOverflowButtonLeave = 'Leave'
HDMoveFurnitureButton = 'Move\nFurniture'
HDStopMoveFurnitureButton = 'Done\nMoving'
HDAtticPickerLabel = 'In the attic'
HDInRoomPickerLabel = 'In the room'
HDInTrashPickerLabel = 'In the trash'
HDDeletePickerLabel = 'Delete?'
HDInAtticLabel = 'Attic'
HDInRoomLabel = 'Room'
HDInTrashLabel = 'Trash'
HDToAtticLabel = 'Send\nto attic'
HDMoveLabel = 'Move'
HDRotateCWLabel = 'Rotate Right'
HDRotateCCWLabel = 'Rotate Left'
HDReturnVerify = 'Return this item to the attic?'
HDReturnFromTrashVerify = 'Return this item to the attic from the trash?'
HDDeleteItem = 'Click OK to send this item to the trash, or Cancel to keep it.'
HDNonDeletableItem = "You can't delete items of this type!"
HDNonDeletableBank = "You can't delete your bank!"
HDNonDeletableCloset = "You can't delete your wardrobe!"
HDNonDeletablePhone = "You can't delete your phone!"
HDNonDeletableTrunk = "You can't delete your trunk!"
HDNonDeletableNotOwner = "You can't delete %s's things!"
HDHouseFull = 'Your house is full.  You have to delete something else from your house or attic before you can return this item from the trash.'
HDHelpDict = {'DoneMoving': 'Finish room decorating.',
 'Attic': 'Show list of items in attic. The attic stores items that are not in your room.',
 'Room': 'Show list of items in room. Useful for finding lost items.',
 'Trash': 'Show items in trash. Oldest items are deleted after a while or when trash overflows.',
 'ZoomIn': 'Get a closer view of room.',
 'ZoomOut': 'Get a farther view of room.',
 'SendToAttic': 'Send the current furniture item to attic for storage.',
 'RotateLeft': 'Turn left.',
 'RotateRight': 'Turn right.',
 'DeleteEnter': 'Change to delete mode.',
 'DeleteExit': 'Exit delete mode.',
 'FurnitureItemPanelDelete': 'Send %s to trash.',
 'FurnitureItemPanelAttic': 'Place %s in room.',
 'FurnitureItemPanelRoom': 'Return %s to attic.',
 'FurnitureItemPanelTrash': 'Return %s to attic.'}
MessagePickerTitle = 'You have too many phrases. In order to purchase\n"%s"\n you must choose one to remove:'
MessagePickerCancel = lCancel
MessageConfirmDelete = 'Are you sure you want to remove "%s" from your SpeedChat menu?'
CatalogBuyText = 'Buy'
CatalogRentText = 'Rent'
CatalogGiftText = 'Gift'
CatalogOnOrderText = 'On Order'
CatalogPurchasedText = 'Already\nPurchased'
CatalogGiftedText = 'Gifted\nTo You'
CatalogPurchasedGiftText = 'Already\nOwned'
CatalogMailboxFull = 'No Room'
CatalogNotAGift = 'Not a Gift'
CatalogNoFit = "Doesn't\nFit"
CatalogSndOnText = 'Snd On'
CatalogSndOffText = 'Snd Off'
CatalogPurchasedMaxText = 'Already\nPurchased Max'
CatalogVerifyPurchase = 'Purchase %(item)s for %(price)s Jellybeans?'
CatalogVerifyPurchaseBeanSilverGold = 'Purchase %(item)s for %(price)s Jellybeans, %(silver)s silver emblems and %(gold)s gold emblems?'
CatalogVerifyPurchaseBeanGold = 'Purchase %(item)s for %(price)s Jellybeans and %(gold)s gold emblems?'
CatalogVerifyPurchaseBeanSilver = 'Purchase %(item)s for %(price)s Jellybeans and %(silver)s silver emblems?'
CatalogVerifyPurchaseSilverGold = 'Purchase %(item)s for %(silver)s silver emblems and %(gold)s gold emblems?'
CatalogVerifyPurchaseSilver = 'Purchase %(item)s for %(silver)s silver emblems?'
CatalogVerifyPurchaseGold = 'Purchase %(item)s for %(gold)s gold emblems?'
CatalogVerifyRent = 'Rent %(item)s for %(price)s Jellybeans?'
CatalogVerifyGift = 'Purchase %(item)s for %(price)s Jellybeans as a gift for %(friend)s?'
CatalogOnlyOnePurchase = 'You may only have one of these items at a time.  If you purchase this one, it will replace %(old)s.\n\nAre you sure you want to purchase %(item)s for %(price)s Jellybeans?'
CatalogExitButtonText = 'Hang Up'
CatalogPastButtonText = 'To Past Items'
TutorialHQOfficerName = 'HQ Harry'
NPCToonNames = {20000: 'Tutorial Tom',
 999: 'Toon Tailor',
 1000: lToonHQ,
 20001: Flippy,
 2001: Flippy,
 2002: 'Master Cool Cat',
 2003: 'Professor Pete',
 2004: 'Tammy the Tailor',
 2005: 'Roflando',
 2006: 'Clerk Clark',
 2011: 'Hudson',
 2007: lHQOfficerM,
 2008: lHQOfficerM,
 2009: lHQOfficerF,
 2010: lHQOfficerF,
 2012: 'Fisherman Freddy',
 2013: 'Clerk Poppy',
 2014: 'Clerk Peppy',
 2015: 'Clerk Pappy',
 2016: 'Party Planner Pumpkin',
 2017: 'Party Planner Polly',
 2018: 'Doctor Surlee',
 2019: 'Doctor Dimm',
 2020: 'Professor Prepostera',
 2021: 'Painter Eddy',
 2101: 'Dentist Daniel',
 2102: 'Sheriff Sherry',
 2103: 'Sneezy Kitty',
 2104: lHQOfficerM,
 2105: lHQOfficerM,
 2106: lHQOfficerF,
 2107: lHQOfficerF,
 2108: 'Canary Coalmine',
 2109: 'Sir Babbles A Lot',
 2110: 'Bill Board',
 2111: 'Dancing Diego',
 2112: 'Dr. Tom',
 2113: 'Rollo The Amazing',
 2114: 'Roz Berry',
 2115: 'Patty Papercut',
 2116: 'Bruiser McDougal',
 2117: 'Ma Putrid',
 2118: 'Jesse Jester',
 2119: 'Honey Haha',
 2120: 'Professor Binky',
 2121: 'Sweet',
 2122: 'Harry Ape',
 2123: 'Spamonia Biggles',
 2124: 'T.P. Rolle',
 2125: 'Lazy Hal',
 2126: 'Professor Guffaw',
 2127: 'Woody Nickel',
 2128: 'Loony Louis',
 2129: 'Frank Furter',
 2130: 'Joy Buzzer',
 2131: 'Feather Duster',
 2132: 'Ezmerelda',
 2133: 'Dr. Euphoric',
 2134: 'Silent Simone',
 2135: 'Mary',
 2136: 'Sal Snicker',
 2137: 'Happy Heikyung',
 2138: 'Muldoon',
 2139: 'Dan Dribbles',
 2140: 'Fisherman Billy',
 2201: 'Postmaster Pete',
 2202: 'Shirley U. Jest',
 2203: lHQOfficerM,
 2204: lHQOfficerM,
 2205: lHQOfficerF,
 2206: lHQOfficerF,
 2207: 'Will Wiseacre',
 2208: 'Sticky Lou',
 2209: 'Charlie Chortle',
 2210: 'Tee Hee',
 2211: 'Sally Spittake',
 2212: 'Weird Warren',
 2213: 'Lucy Tires',
 2214: 'Sam Stain',
 2215: 'Sid Seltzer',
 2216: 'Nona Seeya',
 2217: 'Sharky Jones',
 2218: 'Fanny Pages',
 2219: 'Chef Knucklehead',
 2220: 'Rick Rockhead',
 2221: 'Clovinia Cling',
 2222: 'Shorty Fuse',
 2223: 'Sasha Sidesplitter',
 2224: 'Smokey Joe',
 2225: 'Fisherman Droopy',
 2301: 'Dr. Pulyurleg',
 2302: 'Professor Wiggle',
 2303: 'Nurse Nancy',
 2304: lHQOfficerM,
 2305: lHQOfficerM,
 2306: lHQOfficerF,
 2307: lHQOfficerF,
 2308: 'Rozie',
 2309: 'Big Bruce',
 2311: 'Doctor McMouse',
 2312: 'Dr. Sensitive',
 2313: 'Lucy Shirtspot',
 2314: 'Ned Slinger',
 2315: 'Chewy Morsel',
 2316: 'Cindy Sprinkles',
 2318: 'Tony Maroni',
 2319: 'Zippy',
 2320: 'Crunchy Alfredo',
 2321: 'Fisherman Punchy',
 1001: 'Sophia',
 1002: 'Clerk Bill',
 1003: lHQOfficerM,
 1004: lHQOfficerF,
 1005: lHQOfficerM,
 1006: lHQOfficerF,
 1007: 'Longjohn Leroy',
 1008: 'Fisherman Furball',
 1009: 'Clerk Barky',
 1010: 'Clerk Purr',
 1011: 'Clerk Bloop',
 1012: 'Party Planner Pickles',
 1013: 'Party Planner Patty',
 1101: 'Billy Budd',
 1102: 'Captain Carl',
 1103: 'Fishy Frank',
 1104: 'Doctor Squall',
 1105: 'Admiral Hook',
 1106: 'Mrs. Starch',
 1107: 'Cal Estenicks',
 1108: lHQOfficerM,
 1109: lHQOfficerF,
 1110: lHQOfficerM,
 1111: lHQOfficerF,
 1112: 'Gary Glubglub',
 1113: 'Lisa Luff',
 1114: 'Charlie Chum',
 1115: 'Sheila Squid, Atty',
 1116: 'Cuddles',
 1117: 'Captain Yucks',
 1118: 'Choppy McDougal',
 1121: 'Linda Landlubber',
 1122: 'Salty Stan',
 1123: 'Electra Eel',
 1124: 'Flappy Docksplinter',
 1125: 'Eileen Overboard',
 1126: 'Fisherman Barney',
 1201: 'Barnacle Barbara',
 1202: 'Art',
 1203: 'Ahab',
 1204: 'Rocky Shores',
 1205: lHQOfficerM,
 1206: lHQOfficerF,
 1207: lHQOfficerM,
 1208: lHQOfficerF,
 1209: 'Professor Plank',
 1210: 'Gang Wei',
 1211: 'Wynn Bag',
 1212: 'Toby Tonguestinger',
 1213: 'Dante Dolphin',
 1214: 'Gusty Kate',
 1215: 'Dinah Down',
 1216: 'Rod Reel',
 1217: 'CC Weed',
 1218: 'Pacific Tim',
 1219: 'Brian Beachead',
 1220: 'Carla Canal',
 1221: 'Blisters McKee',
 1222: 'Shep Ahoy',
 1223: 'Sid Squid',
 1224: 'Emily Eel',
 1225: 'Bonzo Bilgepump',
 1226: 'Heave Ho',
 1227: 'Coral Reef',
 1228: 'Fisherman Reed',
 1301: 'Alice',
 1302: 'Melville',
 1303: 'Claggart',
 1304: 'Svetlana',
 1305: lHQOfficerM,
 1306: lHQOfficerF,
 1307: lHQOfficerM,
 1308: lHQOfficerF,
 1309: 'Seafoam',
 1310: 'Ted Tackle',
 1311: 'Topsy Turvey',
 1312: 'Ethan Keel',
 1313: 'William Wake',
 1314: 'Rusty Ralph',
 1315: 'Doctor Drift',
 1316: 'Wilma Wobble',
 1317: 'Paula Pylon',
 1318: 'Dinghy Dan',
 1319: 'Davey Drydock',
 1320: 'Ted Calm',
 1321: 'Dinah Docker',
 1322: 'Whoopie Cushion',
 1323: 'LILY THE FAT NOOB',
 1324: 'Pearl Diver',
 1325: 'Ned Setter',
 1326: 'Felicia Chips',
 1327: 'Cindy Splat',
 1328: 'Fred Flounder',
 1329: 'Shelly Seaweed',
 1330: 'Porter Hole',
 1331: 'Rudy Rudder',
 1332: 'Fisherman Shane',
 3001: 'Betty Freezes',
 3002: lHQOfficerM,
 3003: lHQOfficerF,
 3004: lHQOfficerM,
 3005: lHQOfficerM,
 3006: 'Clerk Lenny',
 3007: 'Chloe',
 3008: 'Warren Bundles',
 3009: 'Fisherman Frizzy',
 3010: 'Clerk Skip',
 3011: 'Clerk Dip',
 3012: 'Clerk Kipp',
 3013: 'Party Planner Pete',
 3014: 'Party Planner Penny',
 3101: 'Mr. Cow',
 3102: 'Auntie Freeze',
 3103: 'Fred',
 3104: 'Bonnie',
 3105: 'Frosty Freddy',
 3106: 'Gus Gooseburger',
 3107: 'Patty Passport',
 3108: 'Toboggan Ted',
 3109: 'Kate',
 3110: 'Chicken Boy',
 3111: 'Snooty Sinjin',
 3112: 'Classic Noah',
 3113: 'Hysterical Harry',
 3114: 'Henry the Hazard',
 3115: lHQOfficerM,
 3116: lHQOfficerF,
 3117: lHQOfficerM,
 3118: lHQOfficerM,
 3119: 'Creepy Carl',
 3120: 'Mike Mittens',
 3121: 'Joe Shockit',
 3122: 'Lucy Luge',
 3123: 'Frank Lloyd Ice',
 3124: 'Lance Iceberg',
 3125: 'Colonel Crunchmouth',
 3126: 'Colestra Awl',
 3127: 'Ifalla Yufalla',
 3128: 'Sticky George',
 3129: 'Baker Bridget',
 3130: 'Sandy',
 3131: 'Lazy Lorenzo',
 3132: 'Ashy',
 3133: 'Dr. Friezeframe',
 3134: 'Lounge Lassard',
 3135: 'Soggy Nell',
 3136: 'Happy Sue',
 3137: 'Mr. Freeze',
 3138: 'Chef Bumblesoup',
 3139: 'Granny Icestockings',
 3140: 'Fisherman Lucille',
 3201: 'Aunt Arctic',
 3202: 'Shakey',
 3203: 'Walt',
 3204: 'Dr. Ivanna Cee',
 3205: 'Bumpy Noggin',
 3206: 'Vidalia VaVoom',
 3207: 'Dr. Mumbleface',
 3208: 'Grumpy Phil',
 3209: 'Giggles McGhee',
 3210: 'Simian Sam',
 3211: 'Fanny Freezes',
 3212: 'Frosty Fred',
 3213: lHQOfficerM,
 3214: lHQOfficerF,
 3215: lHQOfficerM,
 3216: lHQOfficerM,
 3217: 'Sweaty Pete',
 3218: 'Blue Lou',
 3219: 'Tom Tandemfrost',
 3220: 'Mr. Sneeze',
 3221: 'Nelly Snow',
 3222: 'Mindy Windburn',
 3223: 'Chappy',
 3224: 'Freida Frostbite',
 3225: 'Blake Ice',
 3226: 'Santa Paws',
 3227: 'Solar Ray',
 3228: 'Wynne Chill',
 3229: 'Hernia Belt',
 3230: 'Balding Benjy',
 3231: 'Choppy',
 3232: 'Fisherman Albert',
 3301: 'Paisley Patches',
 3302: 'Bjorn Bord',
 3303: 'Dr. Peepers',
 3304: 'Eddie the Yeti',
 3305: 'Mack Ramay',
 3306: 'Paula Behr',
 3307: 'Fisherman Fredrica',
 3308: 'Donald Frump',
 3309: 'Bootsy',
 3310: 'Professor Flake',
 3311: 'Connie Ferris',
 3312: 'March Harry',
 3313: lHQOfficerM,
 3314: lHQOfficerF,
 3315: lHQOfficerM,
 3316: lHQOfficerF,
 3317: 'Kissy Krissy',
 3318: 'Johnny Cashmere',
 3319: 'Sam Stetson',
 3320: 'Fizzy Lizzy',
 3321: 'Pickaxe Paul',
 3322: 'Flue Lou',
 3323: 'Dallas Borealis',
 3324: 'Snaggletooth Stu',
 3325: 'Groovy Garland',
 3326: 'Blanche',
 3327: 'Chuck Roast',
 3328: 'Shady Sadie',
 3329: 'Treading Ed',
 4001: 'Molly Molloy',
 4002: lHQOfficerM,
 4003: lHQOfficerF,
 4004: lHQOfficerF,
 4005: lHQOfficerF,
 4006: 'Clerk Doe',
 4007: 'Clerk Ray',
 4008: 'Tailor Harmony',
 4009: 'Fisherman Fanny',
 4010: 'Clerk Chris',
 4011: 'Clerk Neil',
 4012: 'Clerk Westin Girl',
 4013: 'Party Planner Preston',
 4014: 'Party Planner Penelope',
 4101: 'Tom',
 4102: 'Fifi',
 4103: 'Dr. Fret',
 4104: lHQOfficerM,
 4105: lHQOfficerF,
 4106: lHQOfficerF,
 4107: lHQOfficerF,
 4108: 'Cleff',
 4109: 'Carlos',
 4110: 'Metra Gnome',
 4111: 'Tom Hum',
 4112: 'Fa',
 4113: 'Madam Manners',
 4114: 'Offkey Eric',
 4115: 'Baby Cool Cat',
 4116: 'Piccolo',
 4117: 'Mandy Lynn',
 4118: 'Attendant Abe',
 4119: 'Lizzy',
 4120: 'Viola Padding',
 4121: 'Gee Minor',
 4122: 'Minty Bass',
 4123: 'Lightning Ted',
 4124: 'Riff Raff',
 4125: 'Melody Wavers',
 4126: 'Mel Canto',
 4127: 'Happy Feet',
 4128: 'Luciano Scoop',
 4129: 'Tootie Twostep',
 4130: 'Metal Mike',
 4131: 'Abraham Armoire',
 4132: 'Lowdown Sally',
 4133: 'Scott Poplin',
 4134: 'Disco Dave',
 4135: 'Sluggo Songbird',
 4136: 'Patty Pause',
 4137: 'Tony Deff',
 4138: 'Cliff Cleff',
 4139: 'Harmony Swell',
 4140: 'Chris',
 4141: 'Fisherman Jed',
 4201: 'Tina',
 4202: 'Barry',
 4203: 'Lumber Jack',
 4204: lHQOfficerM,
 4205: lHQOfficerF,
 4206: lHQOfficerF,
 4207: lHQOfficerF,
 4208: 'Hedy',
 4209: 'Corny Canter',
 4211: 'Carl Concerto',
 4212: 'Detective Dirge',
 4213: 'Fran Foley',
 4214: 'Tina Toehooks',
 4215: 'Tim Tailgater',
 4216: 'Gummy Whistle',
 4217: 'Handsome Anton',
 4218: 'Wilma Wind',
 4219: 'FOG DOG',
 4220: 'Curtis Finger',
 4221: 'Moe Madrigal',
 4222: 'John Doe',
 4223: 'Penny Prompter',
 4224: 'Jungle Jim',
 4225: 'Holly Hiss',
 4226: 'Thelma Throatreacher',
 4227: 'Quiet Francesca',
 4228: 'August Winds',
 4229: 'June Loon',
 4230: 'Julius Wheezer',
 4231: 'Steffi Squeezebox',
 4232: 'Hedly Hymn',
 4233: 'Charlie Carp',
 4234: 'Leed Guitar',
 4235: 'Fisherman Larry',
 4301: 'Yuki',
 4302: 'Anna',
 4303: 'Leo',
 4304: lHQOfficerM,
 4305: lHQOfficerF,
 4306: lHQOfficerF,
 4307: lHQOfficerF,
 4308: 'Tabitha',
 4309: 'Marshall',
 4310: 'Martha Mopp',
 4311: 'Sea Shanty',
 4312: 'Moe Saj',
 4313: 'Dumb Dolph',
 4314: 'Dana Dander',
 4315: 'Karen Clockwork',
 4316: 'Tim Tango',
 4317: 'Stubby Toe',
 4318: 'Bob Marlin',
 4319: 'Rinky Dink',
 4320: 'Cammy Coda',
 4321: 'Luke Lute',
 4322: 'Randy Rythm',
 4323: 'Hanna Hogg',
 4324: 'Ellie',
 4325: 'Banker Bran',
 4326: 'Fran Fret',
 4327: 'Flim Flam',
 4328: 'Wagner',
 4329: 'Telly Prompter',
 4330: 'Quentin',
 4331: 'Mellow Costello',
 4332: 'Ziggy',
 4333: 'Harry',
 4334: 'Fast Freddie',
 4335: 'Fisherman Walden',
 5001: lHQOfficerM,
 5002: lHQOfficerM,
 5003: lHQOfficerF,
 5004: lHQOfficerF,
 5005: 'Clerk Peaches',
 5006: 'Clerk Herb',
 5007: 'Bonnie Blossom',
 5008: 'Fisherman Flora',
 5009: 'Clerk Bo Tanny',
 5010: 'Clerk Tom A. Dough',
 5011: 'Clerk Doug Wood',
 5012: 'Party Planner Pierce',
 5013: 'Party Planner Peggy',
 5101: 'Artie',
 5102: 'Susan',
 5103: 'Bud',
 5104: 'Flutterby',
 5105: 'Jack',
 5106: 'Barber Bjorn',
 5107: 'Postman Felipe',
 5108: 'Innkeeper Janet',
 5109: lHQOfficerM,
 5110: lHQOfficerM,
 5111: lHQOfficerF,
 5112: lHQOfficerF,
 5113: 'Dr. Spud',
 5114: 'Wilt',
 5115: 'Honey Dew',
 5116: 'Vegetable Vern',
 5117: 'Petal',
 5118: 'Pop Corn',
 5119: 'Barry Medly',
 5120: 'Gopher',
 5121: 'Paula Peapod',
 5122: 'Leif Pyle',
 5123: 'Diane Vine',
 5124: 'Soggy Bottom',
 5125: 'Sanjay Splash',
 5126: 'Madam Mum',
 5127: 'Polly Pollen',
 5128: 'Shoshanna Sap',
 5129: 'Fisherman Sally',
 5201: 'Jake',
 5202: 'Cynthia',
 5203: 'Lisa',
 5204: 'Bert',
 5205: 'Dan D. Lion',
 5206: 'Vine Green',
 5207: 'Sofie Squirt',
 5208: 'Samantha Spade',
 5209: lHQOfficerM,
 5210: lHQOfficerM,
 5211: lHQOfficerF,
 5212: lHQOfficerF,
 5213: 'Big Galoot',
 5214: 'Itchie Bumps',
 5215: 'Tammy Tuber',
 5216: 'Stinky Jim',
 5217: 'Greg Greenethumb',
 5218: 'Rocky Raspberry',
 5219: 'Lars Bicep',
 5220: 'Lacy Underalls',
 5221: 'Pink Flamingo',
 5222: 'Whiny Wilma',
 5223: 'Wet Will',
 5224: 'Uncle Bumpkin',
 5225: 'Pamela Puddle',
 5226: 'Pete Moss',
 5227: 'Begonia Biddlesmore',
 5228: 'Digger Mudhands',
 5229: 'Fisherman Lily',
 5301: lHQOfficerM,
 5302: lHQOfficerM,
 5303: lHQOfficerM,
 5304: lHQOfficerM,
 5305: 'Crystal',
 5306: 'S. Cargo',
 5307: 'Fun Gus',
 5308: 'Naggy Nell',
 5309: 'Ro Maine',
 5310: 'Timothy',
 5311: 'Judge McIntosh',
 5312: 'Eugene',
 5313: 'Coach Zucchini',
 5314: 'Aunt Hill',
 5315: 'Uncle Mud',
 5316: 'Uncle Spud',
 5317: 'Detective Lima',
 5318: 'Caesar',
 5319: 'Rose',
 5320: 'April',
 5321: 'Professor Ivy',
 5322: 'Fisherman Rose',
 6000: 'Fisherman Melville',
 8001: 'Graham Pree',
 8002: 'Ivona Race',
 8003: 'Anita Winn',
 8004: 'Phil Errup',
 9001: "Snoozin' Susan",
 9002: 'Sleeping Tom',
 9003: 'Drowsy Dennis',
 9004: lHQOfficerF,
 9005: lHQOfficerF,
 9006: lHQOfficerM,
 9007: lHQOfficerM,
 9008: 'Clerk Jill',
 9009: 'Clerk Phil',
 9010: 'Worn Out Waylon',
 9011: 'Fisherman Freud',
 9012: 'Clerk Sarah Snuze',
 9013: 'Clerk Kat Knap',
 9014: 'Clerk R. V. Winkle',
 9015: 'Party Planner Pebbles',
 9016: 'Party Planner Pearl',
 9101: 'Ed',
 9102: 'Big Mama',
 9103: 'P.J.',
 9104: 'Sweet Slumber',
 9105: 'Professor Yawn',
 9106: 'Max',
 9107: 'Snuggles',
 9108: 'Winky Wilbur',
 9109: 'Dreamy Daphne',
 9110: 'Kathy Nip',
 9111: 'Powers Erge',
 9112: 'Lullaby Lou',
 9113: 'Jacques Clock',
 9114: 'Smudgy Mascara',
 9115: 'Babyface MacDougal',
 9116: 'Dances with Sheep',
 9117: 'Afta Hours',
 9118: 'Starry Knight',
 9119: 'Rocco',
 9120: 'Sarah Slumber',
 9121: 'Serena Shortsheeter',
 9122: 'Puffy Ayes',
 9123: 'Teddy Blair',
 9124: 'Nina Nitelight',
 9125: 'Dr. Bleary',
 9126: 'Wyda Wake',
 9127: 'Tabby Tucker',
 9128: "Hardy O'Toole",
 9129: 'Bertha Bedhog',
 9130: 'Charlie Chamberpot',
 9131: 'Susan Siesta',
 9132: lHQOfficerF,
 9133: lHQOfficerF,
 9134: lHQOfficerF,
 9135: lHQOfficerF,
 9136: 'Fisherman Taylor',
 9201: 'Bernie',
 9202: 'Orville',
 9203: 'Nat',
 9204: 'Claire de Loon',
 9205: 'Zen Glen',
 9206: 'Skinny Ginny',
 9207: 'Jane Drain',
 9208: 'Drowsy Dave',
 9209: 'Dr. Floss',
 9210: 'Master Mike',
 9211: 'Dawn',
 9212: 'Moonbeam',
 9213: 'Rooster Rick',
 9214: 'Dr. Blinky',
 9215: 'Rip',
 9216: 'Cat',
 9217: 'Lawful Linda',
 9218: 'Waltzing Matilda',
 9219: 'The Countess',
 9220: 'Grumpy Gordon',
 9221: 'Zari',
 9222: 'Cowboy George',
 9223: 'Mark the Lark',
 9224: 'Sandy Sandman',
 9225: 'Fidgety Bridget',
 9226: 'William Teller',
 9227: 'Bed Head Ted',
 9228: 'Whispering Willow',
 9229: 'Rose Petals',
 9230: 'Tex',
 9231: 'Harry Hammock',
 9232: 'Honey Moon',
 9233: lHQOfficerM,
 9234: lHQOfficerM,
 9235: lHQOfficerM,
 9236: lHQOfficerM,
 9237: 'Fisherman Jung',
 9301: 'Fisherman John',
 9302: 'Blithesome Barbra',
 9303: 'Hasty John',
 9304: 'Angry Dan',
 9305: lHQOfficerM,
 9306: lHQOfficerM,
 9307: lHQOfficerF,
 9308: lHQOfficerF,
 9309: 'Ori-O',
 9310: 'Mr. Batty',
 9311: 'Doctor Flippenbrains',
 9312: 'Barden Betty',
 9313: 'Frekly Fred',
 9314: 'Robby',
 9315: 'Baker Penelope',
 9316: 'Angie Lerr',
 9317: 'Nocturnal Nattie',
 9318: 'Los Carlos',
 9319: 'Psyche',
 9320: 'Toony Bob',
 9321: 'Sir Biscuit',
 9322: 'Glower',
 9323: 'Zedd',
 9324: 'Nacib',
 7001: 'N. Prisoned',
 7002: 'R.E. Leaseme',
 7003: 'Lemmy Owte',
 7004: 'T. Rapped',
 7005: 'Little Helphere',
 7006: 'Gimmy Ahand',
 7007: 'Dewin Tymme',
 7008: 'Ima Cagedtoon',
 7009: 'Jimmy Thelock',
 7010: 'Jaymo',
 7011: 'Donald',
 7012: 'A',
 7013: 'B',
 7014: 'C',
 7015: 'D',
 7016: 'F',
 7017: 'G',
 7018: 'H',
 7019: 'I',
 7020: 'J',
 7021: 'K',
 7022: 'L',
 7023: 'M',
 10001: 'Healer Sara',
 10002: "Journei Bensonadams",
 11001: 'Healer Gabriel',
 12001: 'Healer Bill',
 12002: 'QueenShine',
 13001: 'Healer Clover',
 13002: 'Bumpy Bumblebehr'}
zone2TitleDict = {2513: ('Toon Hall', ''),
 2514: ('Toontown Bank', ''),
 2516: ('Toontown School House', ''),
 2518: ('Toontown Library', ''),
 2519: ('Gag Shop', ''),
 2520: (lToonHQ, ''),
 2521: ('Clothing Shop', ''),
 2522: ('Pet Shop', ''),
 2601: ('All Smiles Tooth Repair', ''),
 2602: ('', ''),
 2603: ('One-Liner Miners', ''),
 2604: ('Hogwash & Dry', ''),
 2605: ('Toontown Sign Factory', ''),
 2606: ('', ''),
 2607: ('Jumping Beans', ''),
 2610: ('Dr. Tom Foolery', ''),
 2611: ('', ''),
 2616: ("Weird Beard's Disguise Shop", ''),
 2617: ('Silly Stunts', ''),
 2618: ('All That Razz', ''),
 2621: ('Paper Airplanes', ''),
 2624: ('Happy Hooligans', ''),
 2625: ('House of Bad Pies', ''),
 2626: ("Jesse's Joke Repair", ''),
 2629: ("The Laughin' Place", ''),
 2632: ('Clown Class', ''),
 2633: ('Tee-Hee Tea Shop', ''),
 2638: ('Toontown Playhouse', ''),
 2639: ('Monkey Tricks', ''),
 2643: ('Canned Bottles', ''),
 2644: ('Impractical Jokes', ''),
 2649: ('All Fun and Games Shop', ''),
 2652: ('', ''),
 2653: ('', ''),
 2654: ('Laughing Lessons', ''),
 2655: ('Funny Money Savings & Loan', ''),
 2656: ('Used Clown Cars', ''),
 2657: ("Frank's Pranks", ''),
 2659: ('Joy Buzzers to the World', ''),
 2660: ('Tickle Machines', ''),
 2661: ('Daffy Taffy', ''),
 2662: ('Dr. I.M. Euphoric', ''),
 2663: ('Toontown Cinerama', ''),
 2664: ('The Merry Mimes', ''),
 2665: ("Mary's Go Around Travel Company", ''),
 2666: ('Laughing Gas Station', ''),
 2667: ('Happy Times', ''),
 2669: ("Muldoon's Maroon Balloons", ''),
 2670: ('Soup Forks', ''),
 2671: ('', ''),
 2701: ('', ''),
 2704: ('Movie Multiplex', ''),
 2705: ("Wiseacre's Noisemakers", ''),
 2708: ('Blue Glue', ''),
 2711: ('Toontown Post Office', ''),
 2712: ('Chortle Cafe', ''),
 2713: ('Laughter Hours Cafe', ''),
 2714: ('Kooky CinePlex', ''),
 2716: ('Soup and Crack Ups', ''),
 2717: ('Bottled Cans', ''),
 2720: ('Crack Up Auto Repair', ''),
 2725: ('', ''),
 2727: ('Seltzer Bottles and Cans', ''),
 2728: ('Vanishing Cream', ''),
 2729: ('14 Karat Goldfish', ''),
 2730: ('News for the Amused', ''),
 2731: ('', ''),
 2732: ('Spaghetti and Goofballs', ''),
 2733: ('Cast Iron Kites', ''),
 2734: ('Suction Cups and Saucers', ''),
 2735: ('The Kaboomery', ''),
 2739: ("Sidesplitter's Mending", ''),
 2740: ('Used Firecrackers', ''),
 2741: ('', ''),
 2742: ('', ''),
 2743: ('Ragtime Dry Cleaners', ''),
 2744: ('', ''),
 2747: ('Visible Ink', ''),
 2748: ('Jest for Laughs', ''),
 2801: ('Sofa Whoopee Cushions', ''),
 2802: ('Inflatable Wrecking Balls', ''),
 2803: ('The Karnival Kid', ''),
 2804: ('Dr. Pulyurleg, Chiropractor', ''),
 2805: ('', ''),
 2809: ('The Punch Line Gym', ''),
 2814: ('Toontown Theatre', ''),
 2818: ('The Flying Pie', ''),
 2821: ('', ''),
 2822: ('Rubber Chicken Sandwiches', ''),
 2823: ('Sundae Funnies Ice Cream', ''),
 2824: ('Punchline Movie Palace', ''),
 2829: ('Phony Baloney', ''),
 2830: ("Zippy's Zingers", ''),
 2831: ("Professor Wiggle's House of Giggles", ''),
 2832: ('', ''),
 2833: ('', ''),
 2834: ('Funny Bone Emergency Room', ''),
 2836: ('', ''),
 2837: ('Hardy Harr Seminars', ''),
 2839: ('Barely Palatable Pasta', ''),
 2841: ('', ''),
 1506: ('Gag Shop', ''),
 1507: ('Toon Headquarters', ''),
 1508: ('Clothing Shop', ''),
 1510: ('', ''),
 1602: ('Used Life Preservers', ''),
 1604: ('Wet Suit Dry Cleaners', ''),
 1606: ("Hook's Clock Repair", ''),
 1608: ("Luff 'N Stuff", ''),
 1609: ('Every Little Bait', ''),
 1612: ('Dime & Quarterdeck Bank', ''),
 1613: ('Squid Pro Quo, Attorneys at Law', ''),
 1614: ('Trim the Nail Boutique', ''),
 1615: ("Yacht's All, Folks!", ''),
 1616: ("Blackbeard's Beauty Parlor", ''),
 1617: ('Out to See Optics', ''),
 1619: ('Disembark! Tree Surgeons', ''),
 1620: ('From Fore to Aft', ''),
 1621: ('Poop Deck Gym', ''),
 1622: ('Bait and Switches Electrical Shop', ''),
 1624: ('Soles Repaired While U Wait', ''),
 1626: ('Salmon Chanted Evening Formal Wear', ''),
 1627: ("Billy Budd's Big Bargain Binnacle Barn", ''),
 1628: ('Piano Tuna', ''),
 1629: ('', ''),
 1701: ('Buoys and Gulls Nursery School', ''),
 1703: ('Wok the Plank Chinese Food', ''),
 1705: ('Sails for Sale', ''),
 1706: ('Peanut Butter and Jellyfish', ''),
 1707: ('Gifts With a Porpoise', ''),
 1709: ('Windjammers and Jellies', ''),
 1710: ('Barnacle Bargains', ''),
 1711: ('Deep Sea Diner', ''),
 1712: ('Able-Bodied Gym', ''),
 1713: ("Art's Smart Chart Mart", ''),
 1714: ("Reel 'Em Inn", ''),
 1716: ('Mermaid Swimwear', ''),
 1717: ('Be More Pacific Ocean Notions', ''),
 1718: ('Run Aground Taxi Service', ''),
 1719: ("Duck's Back Water Company", ''),
 1720: ('The Reel Deal', ''),
 1721: ('All For Nautical', ''),
 1723: ("Squid's Seaweed", ''),
 1724: ("That's  a Moray!", ''),
 1725: ("Ahab's Prefab Sea Crab Center", ''),
 1726: ('Root Beer Afloats', ''),
 1727: ('This Oar That', ''),
 1728: ('Good Luck Horseshoe Crabs', ''),
 1729: ('', ''),
 1802: ('Nautical But Nice', ''),
 1804: ('Mussel Beach Gymnasium', ''),
 1805: ('Tackle Box Lunches', ''),
 1806: ('Cap Size Hat Store', ''),
 1807: ('Keel Deals', ''),
 1808: ('Knots So Fast', ''),
 1809: ('Rusty Buckets', ''),
 1810: ('Anchor Management', ''),
 1811: ("What's Canoe With You?", ''),
 1813: ('Pier Pressure Plumbing', ''),
 1814: ('The Yo Ho Stop and Go', ''),
 1815: ("What's Up, Dock?", ''),
 1818: ('Seven Seas Cafe', ''),
 1819: ("Docker's Diner", ''),
 1820: ('Hook, Line, and Sinker Prank Shop', ''),
 1821: ("King Neptoon's Cannery", ''),
 1823: ('The Clam Bake Diner', ''),
 1824: ('Dog Paddles', ''),
 1825: ('Wholly Mackerel! Fish Market', ''),
 1826: ("Claggart's Clever Clovis Closet", ''),
 1828: ("Alice's Ballast Palace", ''),
 1829: ('Seagull Statue Store', ''),
 1830: ('Lost and Flounder', ''),
 1831: ('Kelp Around the House', ''),
 1832: ("Melville's Massive Mizzenmast Mart", ''),
 1833: ('This Transom Man Custom Tailored Suits', ''),
 1834: ('Rudderly Ridiculous!', ''),
 1835: ('', ''),
 4503: ('Gag Shop', ''),
 4504: ('Toon Headquarters', ''),
 4506: ('Clothing Shop', ''),
 4508: ('', ''),
 4603: ("Tom-Tom's Drums", ''),
 4604: ('In Four-Four Time', ''),
 4605: ("Fifi's Fiddles", ''),
 4606: ('Casa De Castanets', ''),
 4607: ('Catchy Toon Apparel', ''),
 4609: ('Do, Rae, Me Piano Keys', ''),
 4610: ('Please Refrain', ''),
 4611: ('Tuning Forks and Spoons', ''),
 4612: ("Dr. Fret's Dentistry", ''),
 4614: ('Shave and a Haircut for a Song', ''),
 4615: ("Piccolo's Pizza", ''),
 4617: ('Happy Mandolins', ''),
 4618: ('Rests Rooms', ''),
 4619: ('More Scores', ''),
 4622: ('Chin Rest Pillows', ''),
 4623: ('Flats Sharpened', ''),
 4625: ('Tuba Toothpaste', ''),
 4626: ('Notations', ''),
 4628: ('Accidental Insurance', ''),
 4629: ("Riff's Paper Plates", ''),
 4630: ('Music Is Our Forte', ''),
 4631: ('Canto Help You', ''),
 4632: ('Dance Around the Clock Shop', ''),
 4635: ('Tenor Times', ''),
 4637: ('For Good Measure', ''),
 4638: ('Hard Rock Shop', ''),
 4639: ('Four Score Antiques', ''),
 4641: ('Blues News', ''),
 4642: ('Ragtime Dry Cleaners', ''),
 4645: ('Club 88', ''),
 4646: ('', ''),
 4648: ('Carry a Toon Movers', ''),
 4649: ('', ''),
 4652: ('Full Stop Shop', ''),
 4653: ('', ''),
 4654: ('Pitch Perfect Roofing', ''),
 4655: ("The Treble Chef's Cooking School", ''),
 4656: ('', ''),
 4657: ('Barbershop Quartet', ''),
 4658: ('Plummeting Pianos', ''),
 4659: ('', ''),
 4701: ('The Schmaltzy Waltz School of Dance', ''),
 4702: ('Timbre! Equipment for the Singing Lumberjack', ''),
 4703: ('I Can Handel It!', ''),
 4704: ("Tina's Concertina Concerts", ''),
 4705: ('Zither Here Nor There', ''),
 4707: ("Doppler's Sound Effects Studio", ''),
 4709: ('On Ballet! Climbing Supplies', ''),
 4710: ('Hurry Up, Slow Polka! School of Driving', ''),
 4712: ('C-Flat Tire Repair', ''),
 4713: ('B-Sharp Fine Menswear', ''),
 4716: ('Four-Part Harmonicas', ''),
 4717: ('Sonata Your Fault! Discount Auto Insurance', ''),
 4718: ('Chopin Blocks and Other Kitchen Supplies', ''),
 4719: ('Madrigal Motor Homes', ''),
 4720: ('Name That Toon', ''),
 4722: ('Overture Understudies', ''),
 4723: ('Haydn Go Seek Playground Supplies', ''),
 4724: ('White Noise for Girls and Boys', ''),
 4725: ('The Baritone Barber', ''),
 4727: ('Vocal Chords Braided', ''),
 4728: ("Sing Solo We Can't Hear You", ''),
 4729: ('Double Reed Bookstore', ''),
 4730: ('Lousy Lyrics', ''),
 4731: ('Toon Tunes', ''),
 4732: ('Etude Brute? Theatre Company', ''),
 4733: ('', ''),
 4734: ('', ''),
 4735: ('Accordions, If You Want In, Just Bellow!', ''),
 4736: ('Her and Hymn Wedding Planners', ''),
 4737: ('Harp Tarps', ''),
 4738: ('Canticle Your Fancy Gift Shop', ''),
 4739: ('', ''),
 4801: ("Marshall's Stacks", ''),
 4803: ('What a Mezzo! Maid Service', ''),
 4804: ('Mixolydian Scales', ''),
 4807: ('Relax the Bach', ''),
 4809: ("I Can't Understanza!", ''),
 4812: ('', ''),
 4817: ('The Ternary Pet Shop', ''),
 4819: ("Yuki's Ukeleles", ''),
 4820: ('', ''),
 4821: ("Anna's Cruises", ''),
 4827: ('Common Time Watches', ''),
 4828: ("Schumann's Shoes for Men", ''),
 4829: ("Pachelbel's Canonballs", ''),
 4835: ('Ursatz for Kool Katz', ''),
 4836: ('Reggae Regalia', ''),
 4838: ('Kazoology School of Music', ''),
 4840: ('Coda Pop Musical Beverages', ''),
 4841: ('Lyre, Lyre, Pants on Fire!', ''),
 4842: ('The Syncopation Corporation', ''),
 4843: ('', ''),
 4844: ('Con Moto Cycles', ''),
 4845: ("Ellie's Elegant Elegies", ''),
 4848: ('Lotsa Lute Savings & Loan', ''),
 4849: ('', ''),
 4850: ('The Borrowed Chord Pawn Shop', ''),
 4852: ('Flowery Flute Fleeces', ''),
 4853: ("Leo's Fenders", ''),
 4854: ("Wagner's Vocational Violin Videos", ''),
 4855: ('The Teli-Caster Network', ''),
 4856: ('', ''),
 4862: ("Quentin's Quintessen\x03tial Quadrilles", ''),
 4867: ("Mr. Costello's Yellow Cellos", ''),
 4868: ('', ''),
 4870: ("Ziggy's Zoo of Zigeuner\x03musik", ''),
 4871: ("Harry's House of Harmonious Humbuckers", ''),
 4872: ("Fast Freddie's Fretless Fingerboards", ''),
 4873: ('', ''),
 5501: ('Gag Shop', ''),
 5502: (lToonHQ, ''),
 5503: ('Clothing Shop', ''),
 5505: ('', ''),
 5601: ('Eye of the Potato Optometry', ''),
 5602: ("Artie Choke's Neckties", ''),
 5603: ('Lettuce Alone', ''),
 5604: ('Cantaloupe Bridal Shop', ''),
 5605: ('Vege-tables and Chairs', ''),
 5606: ('Petals', ''),
 5607: ('Compost Office', ''),
 5608: ('Mom and Pop Corn', ''),
 5609: ('Berried Treasure', ''),
 5610: ("Black-eyed Susan's Boxing Lessons", ''),
 5611: ("Gopher's Gags", ''),
 5613: ('Crop Top Barbers', ''),
 5615: ("Bud's Bird Seed", ''),
 5616: ('Dew Drop Inn', ''),
 5617: ("Flutterby's Butterflies", ''),
 5618: ("Peas and Q's", ''),
 5619: ("Jack's Beanstalks", ''),
 5620: ('Rake It Inn', ''),
 5621: ('Grape Expectations', ''),
 5622: ('Petal Pusher Bicycles', ''),
 5623: ('Bubble Bird Baths', ''),
 5624: ("Mum's the Word", ''),
 5625: ('Leaf It Bees', ''),
 5626: ('Pine Needle Crafts', ''),
 5627: ('', ''),
 5701: ('From Start to Spinach', ''),
 5702: ("Jake's Rakes", ''),
 5703: ("Photo Cynthia's Camera Shop", ''),
 5704: ('Lisa Lemon Used Cars', ''),
 5705: ('Poison Oak Furniture', ''),
 5706: ('14 Carrot Jewelers', ''),
 5707: ('Musical Fruit', ''),
 5708: ("We'd Be Gone Travel Agency", ''),
 5709: ('Astroturf Mowers', ''),
 5710: ('Tuft Guy Gym', ''),
 5711: ('Garden Hosiery', ''),
 5712: ('Silly Statues', ''),
 5713: ('Trowels and Tribulations', ''),
 5714: ('Spring Rain Seltzer Bottles', ''),
 5715: ('Hayseed News', ''),
 5716: ('Take It or Leaf It Pawn Shop', ''),
 5717: ('The Squirting Flower', ''),
 5718: ('The Dandy Lion Exotic Pets', ''),
 5719: ('Trellis the Truth! Private Investi\x03gators', ''),
 5720: ('Vine and Dandy Menswear', ''),
 5721: ('Root 66 Diner', ''),
 5725: ('Barley, Hops, and Malt Shop', ''),
 5726: ("Bert's Dirt", ''),
 5727: ('Gopher Broke Savings & Loan', ''),
 5728: ('', ''),
 5802: (lToonHQ, ''),
 5804: ('Just Vase It', ''),
 5805: ('Snail Mail', ''),
 5809: ('Fungi Clown School', ''),
 5810: ('Honeydew This', ''),
 5811: ('Lettuce Inn', ''),
 5815: ('Grass Roots', ''),
 5817: ('Apples and Oranges', ''),
 5819: ('Green Bean Jeans', ''),
 5821: ('Squash and Stretch Gym', ''),
 5826: ('Ant Farming Supplies', ''),
 5827: ('Dirt. Cheap.', ''),
 5828: ('Couch Potato Furniture', ''),
 5830: ('Spill the Beans', ''),
 5833: ('The Salad Bar', ''),
 5835: ('Flower Bed and Breakfast', ''),
 5836: ("April's Showers and Tubs", ''),
 5837: ('School of Vine Arts', ''),
 9501: ('Lullaby Library', ''),
 9503: ('The Snooze Bar', ''),
 9504: ('Gag Shop', ''),
 9505: (lToonHQ, ''),
 9506: ('Clothing Shop', ''),
 9508: ('', ''),
 9601: ('Snuggle Inn', ''),
 9602: ('Forty Winks for the Price of Twenty', ''),
 9604: ("Ed's Red Bed Spreads", ''),
 9605: ('Cloud Nine Design', ''),
 9607: ("Big Mama's Bahama Pajamas", ''),
 9608: ('Cat Nip for Cat Naps', ''),
 9609: ('Deep Sleep for Cheap', ''),
 9613: ('Clock Cleaners', ''),
 9616: ('Lights Out Electric Co.', ''),
 9617: ('Crib Notes - Music to Sleep By', ''),
 9619: ('Relax to the Max', ''),
 9620: ("PJ's Taxi Service", ''),
 9622: ('Sleepy Time Pieces', ''),
 9625: ('Curl Up Beauty Parlor', ''),
 9626: ('Bed Time Stories', ''),
 9627: ('The Sleepy Teepee', ''),
 9628: ('Call It a Day Calendars', ''),
 9629: ('Silver Lining Jewelers', ''),
 9630: ('Rock to Sleep Quarry', ''),
 9631: ('Down Time Watch Repair', ''),
 9633: ('The Dreamland Screening Room', ''),
 9634: ('Mind Over Mattress', ''),
 9636: ('Insomniac Insurance', ''),
 9639: ('House of Hibernation', ''),
 9640: ('Nightstand Furniture Company', ''),
 9642: ('Sawing Wood Slumber Lumber', ''),
 9643: ('Shut-Eye Optometry', ''),
 9644: ('Pillow Fights Nightly', ''),
 9645: ('The All Tucked Inn', ''),
 9647: ('Make Your Bed! Hardware Store', ''),
 9649: ('Snore or Less', ''),
 9650: ('Crack of Dawn Repairs', ''),
 9651: ('For Richer or Snorer', ''),
 9652: ('', ''),
 9703: ('Fly By Night Travel Agency', ''),
 9704: ('Night Owl Pet Shop', ''),
 9705: ('Asleep At The Wheel Car Repair', ''),
 9706: ('Tooth Fairy Dentistry', ''),
 9707: ("Dawn's Yawn & Garden Center", ''),
 9708: ('Bed Of Roses Florist', ''),
 9709: ('Pipe Dream Plumbers', ''),
 9710: ('REM Optometry', ''),
 9711: ('Wake-Up Call Phone Company', ''),
 9712: ("Counting Sheep - So You Don't Have To!", ''),
 9713: ('Wynken, Blynken & Nod, Attorneys at Law', ''),
 9714: ('Dreamboat Marine Supply', ''),
 9715: ('First Security Blanket Bank', ''),
 9716: ('Wet Blanket Party Planners', ''),
 9717: ("Baker's Dozin' Doughnuts", ''),
 9718: ("Sandman's Sandwiches", ''),
 9719: ('Armadillo Pillow Company', ''),
 9720: ('Talking In Your Sleep Voice Training', ''),
 9721: ('Snug As A Bug Rug Dealer', ''),
 9722: ('Dream On Talent Agency', ''),
 9725: ("Cat's Pajamas", ''),
 9727: ('You Snooze, You Lose', ''),
 9736: ('Dream Jobs Employment Agency', ''),
 9737: ("Waltzing Matilda's Dance School", ''),
 9738: ('House of Zzzzzs', ''),
 9740: ('Hit The Sack Fencing School', ''),
 9741: ("Don't Let The Bed Bugs Bite Exterminators", ''),
 9744: ("Rip Van Winkle's Wrinkle Cream", ''),
 9752: ('Midnight Oil & Gas Company', ''),
 9753: ("Moonbeam's Ice Creams", ''),
 9754: ('Sleepless in the Saddle All Night Pony Rides', ''),
 9755: ('Bedknobs & Broomsticks Movie House', ''),
 9756: ('', ''),
 9759: ('Sleeping Beauty Parlor', ''),
 3507: ('Gag Shop', ''),
 3508: (lToonHQ, ''),
 3509: ('Clothing Shop', ''),
 3511: ('', ''),
 3601: ('Northern Lights Electric Company', ''),
 3602: ("Nor'easter Bonnets", ''),
 3605: ('', ''),
 3607: ('The Blizzard Wizard', ''),
 3608: ('Nothing to Luge', ''),
 3610: ("Mike's Massive Mukluk Mart", ''),
 3611: ("Mr. Cow's Snow Plows", ''),
 3612: ('Igloo Design', ''),
 3613: ('Ice Cycle Bikes', ''),
 3614: ('Snowflakes Cereal Company', ''),
 3615: ('Fried Baked Alaskas', ''),
 3617: ('Cold Air Balloon Rides', ''),
 3618: ('Snow Big Deal! Crisis Management', ''),
 3620: ('Skiing Clinic', ''),
 3621: ('The Melting Ice Cream Bar', ''),
 3622: ('', ''),
 3623: ('The Mostly Toasty Bread Company', ''),
 3624: ('Subzero Sandwich Shop', ''),
 3625: ("Auntie Freeze's Radiator Supply", ''),
 3627: ('St. Bernard Kennel Club', ''),
 3629: ('Pea Soup Cafe', ''),
 3630: ('Icy London, Icy France Travel Agency', ''),
 3634: ('Easy Chair Lifts', ''),
 3635: ('Used Firewood', ''),
 3636: ('Affordable Goosebumps', ''),
 3637: ("Kate's Skates", ''),
 3638: ('Toboggan or Not Toboggan', ''),
 3641: ("Fred's Red Sled Beds", ''),
 3642: ('Eye of the Storm Optics', ''),
 3643: ('Snowball Hall', ''),
 3644: ('Melted Ice Cubes', ''),
 3647: ('The Sanguine Penguin Tuxedo Shop', ''),
 3648: ('Instant Ice', ''),
 3649: ('Hambrrrgers', ''),
 3650: ('Antarctic Antiques', ''),
 3651: ("Frosty Freddy's Frozen Frankfurters", ''),
 3653: ('Ice House Jewelry', ''),
 3654: ('', ''),
 3702: ('Winter Storage', ''),
 3703: ('', ''),
 3705: ('Icicles Built for Two', ''),
 3706: ("Shiverin' Shakes Malt Shop", ''),
 3707: ('Snowplace Like Home', ''),
 3708: ("Pluto's Place", ''),
 3710: ('Dropping Degrees Diner', ''),
 3711: ('', ''),
 3712: ('Go With the Floe', ''),
 3713: ('Chattering Teeth, Subzero Dentist', ''),
 3715: ("Aunt Arctic's Soup Shop", ''),
 3716: ('Road Salt and Pepper', ''),
 3717: ('Juneau What I Mean?', ''),
 3718: ('Designer Inner Tubes', ''),
 3719: ('Ice Cube on a Stick', ''),
 3721: ("Noggin's Toboggan Bargains", ''),
 3722: ('Snow Bunny Ski Shop', ''),
 3723: ("Shakey's Snow Globes", ''),
 3724: ('The Chattering Chronicle', ''),
 3725: ('You Sleigh Me', ''),
 3726: ('Solar Powered Blankets', ''),
 3728: ('Lowbrow Snowplows', ''),
 3729: ('', ''),
 3730: ('Snowmen Bought & Sold', ''),
 3731: ('Portable Fireplaces', ''),
 3732: ('The Frozen Nose', ''),
 3734: ('Icy Fine, Do You? Optometry', ''),
 3735: ('Polar Ice Caps', ''),
 3736: ('Diced Ice at a Nice Price', ''),
 3737: ('Downhill Diner', ''),
 3738: ("Heat-Get It While It's Hot", ''),
 3739: ('', ''),
 3801: ('Toon HQ', ''),
 3806: ('Alpine Chow Line', ''),
 3807: ('Used Groundhog Shadows', ''),
 3808: ('The Sweater Lodge', ''),
 3809: ('Ice Saw It Too', ''),
 3810: ('A Better Built Quilt', ''),
 3811: ('Your Snow Angel', ''),
 3812: ('Mittens for Kittens', ''),
 3813: ("Snowshoes You Can't Refuse", ''),
 3814: ('Malt in Your Mouth Soda Fountain', ''),
 3815: ('The Toupee Chalet', ''),
 3816: ('Just So Mistletoe', ''),
 3817: ('Winter Wonderland Walking Club', ''),
 3818: ('The Shovel Hovel', ''),
 3819: ('Clean Sweep Chimney Service', ''),
 3820: ('Snow Whitening', ''),
 3821: ('Hibernation Vacations', ''),
 3823: ('Precipitation Foundation', ''),
 3824: ('Open Fire Chestnut Roasting', ''),
 3825: ('Cool Cat Hats', ''),
 3826: ('Oh My Galoshes!', ''),
 3827: ('Choral Wreaths', ''),
 3828: ("Snowman's Land", ''),
 3829: ('Pinecone Zone', ''),
 3830: ('Wait and See Goggle Defogging', ''),
 9802: ("Barbra's Bohemian Art Supplies", ''),
 9804: ("Angry Dan's Garden Sprinklers", ''),
 9806: ("Nacib Niri", ''),
 9808: ("Ori-O's Creamery and Dairy", ''),
 9809: ('Rave of the Forks', ''),
 9812: ('Louds Silent-Shop', ''),
 9813: ('Bedpost Bakery', ''),
 9814: ("Amazing Angler's Silly Shop", ''),
 9815: ("Nattie's Catties", ''),
 9816: ('Carlos Carpentry BunkBeds Inc.', ''),
 9817: ('The Psyche-Ologist', ''),
 9819: ("Toony Bob's Fluffy Pillows", ''),
 9820: ("Batty's Bat Supply", ''),
 9821: ("Milk or Sugar? Tea Shop", ''),
 9822: ("Zedd's Pasta", ''),
 9824: ("Joe's Burnt Biscuits", ''),
 9826: ("Juste-A-Cote Taxi Service", ''),
 9827: ("Frekly Fred's Storage Shack", ''),
 9828: ("Barden Betty's Clingy Clothing", ''),
 9829: (lToonHQ, ''),
}
ClosetTimeoutMessage = 'Sorry, you ran out\n of time.'
ClosetNotOwnerMessage = "This isn't your closet, but you may try on the clothes."
ClosetPopupOK = lOK
ClosetPopupCancel = lCancel
ClosetDiscardButton = 'Remove'
ClosetAreYouSureMessage = 'You have deleted some clothes.  Do you really want to delete them?'
ClosetYes = lYes
ClosetNo = lNo
ClosetVerifyDelete = 'Really delete %s?'
ClosetShirt = 'this shirt'
ClosetShorts = 'these shorts'
ClosetSkirt = 'this skirt'
ClosetDeleteShirt = 'Delete\nshirt'
ClosetDeleteShorts = 'Delete\nshorts'
ClosetDeleteSkirt = 'Delete\nskirt'
TrunkNotOwnerMessage = "This isn't your trunk, but you may try on the accessories."
TrunkAreYouSureMessage = 'You have deleted some accessories.  Do you really want to delete them?'
TrunkHat = 'this hat'
TrunkGlasses = 'these glasses'
TrunkBackpack = 'this backpack'
TrunkShoes = 'these shoes'
TrunkDeleteHat = 'Delete\nhat'
TrunkDeleteGlasses = 'Delete\nglasses'
TrunkDeleteBackpack = 'Delete\nbackpack'
TrunkDeleteShoes = 'Delete\nshoes'
EstateOwnerLeftMessage = "Sorry, the owner of this estate left.  You'll be sent to the playground in %s seconds"
EstatePopupOK = lOK
EstateTeleportFailed = "Couldn't go home. Try again!"
EstateTeleportFailedNotFriends = "Sorry, %s is in a toon's estate that you are not friends with."
EstateTargetGameStart = 'The Toon-up Target game has started!'
EstateTargetGameInst = "The more you hit the red target, the more you'll get Tooned up."
EstateTargetGameEnd = 'The Toon-up Target game is now over...'
AvatarsHouse = '%s\n House'
BankGuiCancel = lCancel
BankGuiOk = lOK
DistributedBankNoOwner = 'Sorry, this is not your bank.'
DistributedBankNotOwner = 'Sorry, this is not your bank.'
FishGuiCancel = lCancel
FishGuiOk = 'Sell All'
FishTankValue = 'Hi, %(name)s! You have %(num)s fish in your bucket worth a total of %(value)s Jellybeans. Do you want to sell them all?'
FlowerGuiCancel = lCancel
FlowerGuiOk = 'Sell All'
FlowerBasketValue = '%(name)s, you have %(num)s flowers in your basket worth a total of %(value)s Jellybeans. Do you want to sell them all?'

def GetPossesive(name):
    if name[-1:] == 's':
        possesive = name + "'"
    else:
        possesive = name + "'s"
    return possesive


PetTrait2descriptions = {'hungerThreshold': ('Always Hungry',
                     'Often Hungry',
                     'Sometimes Hungry',
                     'Rarely Hungry'),
 'boredomThreshold': ('Always Bored',
                      'Often Bored',
                      'Sometimes Bored',
                      'Rarely Bored'),
 'angerThreshold': ('Always Grumpy',
                    'Often Grumpy',
                    'Sometimes Grumpy',
                    'Rarely Grumpy'),
 'forgetfulness': ('Always Forgets',
                   'Often Forgets',
                   'Sometimes Forgets',
                   'Rarely Forgets'),
 'excitementThreshold': ('Very Calm',
                         'Pretty Calm',
                         'Pretty Excitable',
                         'Very Excitable'),
 'sadnessThreshold': ('Always Sad',
                      'Often Sad',
                      'Sometimes Sad',
                      'Rarely Sad'),
 'restlessnessThreshold': ('Always Restless',
                           'Often Restless',
                           'Sometimes Restless',
                           'Rarely Restless'),
 'playfulnessThreshold': ('Rarely Playful',
                          'Sometimes Playful',
                          'Often Playful',
                          'Always Playful'),
 'lonelinessThreshold': ('Always Lonely',
                         'Often Lonely',
                         'Sometimes Lonely',
                         'Rarely Lonely'),
 'fatigueThreshold': ('Always Tired',
                      'Often Tired',
                      'Sometimes Tired',
                      'Rarely Tired'),
 'confusionThreshold': ('Always Confused',
                        'Often Confused',
                        'Sometimes Confused',
                        'Rarely Confused'),
 'surpriseThreshold': ('Always Surprised',
                       'Often Surprised',
                       'Sometimes Surprised',
                       'Rarely Surprised'),
 'affectionThreshold': ('Rarely Affectionate',
                        'Sometimes Affectionate',
                        'Often Affectionate',
                        'Always Affectionate')}
FireworksInstructions = lToonHQ + ': Hit the "Page Up" key to see the show!'
FireworksJuly4Beginning = lToonHQ + ': Welcome to summer fireworks! Enjoy the show!'
FireworksJuly4Ending = lToonHQ + ': Hope you enjoyed the show! Have a great summer!'
FireworksNewYearsEveBeginning = lToonHQ + ': Happy New Year! Enjoy the fireworks show, sponsored by Flippy!'
FireworksNewYearsEveEnding = lToonHQ + ': Hope you enjoyed the show! Have a Toontastic New Year!'
FireworksComboBeginning = lToonHQ + ': Enjoy lots of Laffs with Toon fireworks!'
FireworksComboEnding = lToonHQ + ': Thank you, Toons! Hope you enjoyed the show!'
TIP_NONE = 0
TIP_GENERAL = 1
TIP_STREET = 2
TIP_MINIGAME = 3
TIP_COGHQ = 4
TIP_ESTATE = 5
TIP_KARTING = 6
TIP_GOLF = 7
TipTitle = 'TOON TIP:'
TipDict = {TIP_NONE: ('',),
 TIP_GENERAL: ('The Royalbots go up to level 20.',
               'The Courtbots go up to level 18.',
               'Carebots go up to level 16.',
               'Fashionbots go up to 15.',
               'If you need any guidence, ask Master Cool Cat.',
               'Use ~maxtoon to max your Toon.',
               "Use ~unlimitedgags so you don't lose your gags if you use one.",
               "~immortal helps so you don't go sad by the Cogs.",
               "~unites restocks your unites for you.",
               '~fires gets you pinkslips.',
               "The Cog facilities are random, don't expect them to be easy.",
               'There is a chance for 2.0s and 3.0s to be in facilities, be aware!',
               'The gags have been balanced, but the Cogs have been balanced too.',
               'The game has been modified so well that you can experience a new game.'),
 TIP_STREET: ('There are four types of Cogs: Royalbots, Carebots, Fashionbots, and Courtbots.'),
 TIP_MINIGAME: ('THERE IS NOTHING TO SEE HERE!!!!!!!!!!!!!!!!!!!!!!!!!!'),
 TIP_COGHQ: ('You must complete your Fashionbot Disguise before visiting the Fashion Designer.',
             'You must complete your Carebot Disguise before visiting the C.F.O.',
             'You must complete your Royalbot Disguise before visiting KingShine.',
             'You must complete your Courtbot Disguise before visiting the Chief.',
             "The bosses have their own challenge, enjoy them. ^-^"),
 TIP_ESTATE: ("DOODLES ARE THE BEST! GO BUY ONE OR YOU'RE A HEARTLESS DOODLE HATER!!!!!!!!!!!!!!!!!! >:("),
 TIP_KARTING: ("Buy a kart, get out there, AND RACE!"),
 TIP_GOLF: ('GROUNDED GROUNDED GROUNDED GROUNDED GROUNDED!')}
FishGenusNames = {0: 'Balloon Fish',
 2: 'Cat Fish',
 4: 'Clown Fish',
 6: 'Frozen Fish',
 8: 'Star Fish',
 10: 'Holey Mackerel',
 12: 'Dog Fish',
 14: 'Amore Eel',
 16: 'Nurse Shark',
 18: 'King Crab',
 20: 'Moon Fish',
 22: 'Sea Horse',
 24: 'Pool Shark',
 26: 'Bear Acuda',
 28: 'Cutthroat Trout',
 30: 'Piano Tuna',
 32: 'Peanut Butter & Jellyfish',
 34: 'Devil Ray'}
FishSpeciesNames = {0: ('Balloon Fish',
     'Hot Air Balloon Fish',
     'Weather Balloon Fish',
     'Water Balloon Fish',
     'Red Balloon Fish'),
 2: ('Cat Fish',
     'Siamese Cat Fish',
     'Alley Cat Fish',
     'Tabby Cat Fish',
     'Tom Cat Fish'),
 4: ('Clown Fish',
     'Sad Clown Fish',
     'Party Clown Fish',
     'Circus Clown Fish'),
 6: ('Frozen Fish',),
 8: ('Star Fish',
     'Five Star Fish',
     'Rock Star Fish',
     'Shining Star Fish',
     'All Star Fish'),
 10: ('Holey Mackerel',),
 12: ('Dog Fish',
      'Bull Dog Fish',
      'Hot Dog Fish',
      'Dalmatian Dog Fish',
      'Puppy Dog Fish'),
 14: ('Amore Eel', 'Electric Amore Eel'),
 16: ('Nurse Shark', 'Clara Nurse Shark', 'Florence Nurse Shark'),
 18: ('King Crab', 'Alaskan King Crab', 'Old King Crab'),
 20: ('Moon Fish',
      'Full Moon Fish',
      'Half Moon Fish',
      'New Moon Fish',
      'Crescent Moon Fish',
      'Harvest Moon Fish'),
 22: ('Sea Horse',
      'Rocking Sea Horse',
      'Clydesdale Sea Horse',
      'Arabian Sea Horse'),
 24: ('Pool Shark',
      'Kiddie Pool Shark',
      'Swimming Pool Shark',
      'Olympic Pool Shark'),
 26: ('Brown Bear Acuda',
      'Black Bear Acuda',
      'Koala Bear Acuda',
      'Honey Bear Acuda',
      'Polar Bear Acuda',
      'Panda Bear Acuda',
      'Kodiac Bear Acuda',
      'Grizzly Bear Acuda'),
 28: ('Cutthroat Trout', 'Captain Cutthroat Trout', 'Scurvy Cutthroat Trout'),
 30: ('Piano Tuna',
      'Grand Piano Tuna',
      'Baby Grand Piano Tuna',
      'Upright Piano Tuna',
      'Player Piano Tuna'),
 32: ('Peanut Butter & Jellyfish',
      'Grape PB&J Fish',
      'Crunchy PB&J Fish',
      'Strawberry PB&J Fish',
      'Concord Grape PB&J Fish'),
 34: ('Devil Ray',)}
CogPartNames = ('Upper Left Leg',
 'Lower Left Leg',
 'Left Foot',
 'Upper Right Leg',
 'Lower Right Leg',
 'Right Foot',
 'Left Shoulder',
 'Right Shoulder',
 'Chest',
 'Health Meter',
 'Pelvis',
 'Upper Left Arm',
 'Lower Left Arm',
 'Left Hand',
 'Upper Right Arm',
 'Lower Right Arm',
 'Right Hand')
CogPartNamesSimple = ('Upper Torso',)
SellbotLegFactorySpecMainEntrance = 'Factory Entrance'
SellbotLegFactorySpecLobby = 'Lobby'
SellbotLegFactorySpecLobbyHallway = 'Gag Room'
SellbotLegFactorySpecGearRoom = 'Gear Room'
SellbotLegFactorySpecBoilerRoom = 'Boiler Room'
SellbotLegFactorySpecEastCatwalk = 'East Pathway Catwalk'
SellbotLegFactorySpecPaintMixer = 'Paint & Gag Mixer Room'
SellbotLegFactorySpecPaintMixerStorageRoom = 'Paint Mixer Gag Room'
SellbotLegFactorySpecWestSiloCatwalk = 'West Silo Catwalk'
SellbotLegFactorySpecPipeRoom = 'Pipe Room'
SellbotLegFactorySpecDuctRoom = 'Duct Room'
SellbotLegFactorySpecSideEntrance = 'Side Entrance'
SellbotLegFactorySpecStomperAlley = 'Stomper Alley'
SellbotLegFactorySpecLavaRoomFoyer = 'Lava Room Foyer'
SellbotLegFactorySpecLavaRoom = 'Lava Room'
SellbotLegFactorySpecLavaStorageRoom = 'Lava Storage Room'
SellbotLegFactorySpecWestCatwalk = 'West Catwalk'
SellbotLegFactorySpecOilRoom = 'Oil Room'
SellbotLegFactorySpecLookout = 'Lookout'
SellbotLegFactorySpecWarehouse = 'Warehouse'
SellbotLegFactorySpecOilRoomHallway = 'Oil Room Hallway'
SellbotLegFactorySpecEastSiloControlRoom = 'East Silo Control Room'
SellbotLegFactorySpecWestSiloControlRoom = 'West Silo Control Room'
SellbotLegFactorySpecCenterSiloControlRoom = 'Center Silo Control Room'
SellbotLegFactorySpecEastSilo = 'East Silo'
SellbotLegFactorySpecWestSilo = 'West Silo'
SellbotLegFactorySpecCenterSilo = 'Center Silo'
SellbotLegFactorySpecEastSiloCatwalk = 'East Silo Catwalk'
SellbotLegFactorySpecWestElevatorShaft = 'West Elevator Shaft'
SellbotLegFactorySpecEastElevatorShaft = 'East Elevator Shaft'
FishBingoBingo = 'BINGO!'
FishBingoVictory = 'VICTORY!!'
FishBingoJackpot = 'JACKPOT!'
FishBingoGameOver = 'GAME OVER'
FishBingoIntermission = 'Intermission\nEnds In:'
FishBingoNextGame = 'Next Game\nStarts In:'
FishBingoTypeNormal = 'Classic'
FishBingoTypeCorners = 'Four Corners'
FishBingoTypeDiagonal = 'Diagonals'
FishBingoTypeThreeway = 'Three Way'
FishBingoTypeBlockout = 'BLOCKOUT!'
SillySaturdayStart = "It's time for Silly Saturday! Saturdays are silly with Fish Bingo and Grand Prix throughout the day!"
SillySaturdayOngoing = 'Welcome! Silly Saturday is currently in progress.'
SillySaturdayEnd = 'Silly Saturday is over. Hope you had fun. See you next week!'
AprilToonsWeekStart = "It's April Toons Week!"
AprilToonsWeekEnd = 'April Toons Week is over. See you next year!'
FishBingoStart = "It's time for Fish Bingo!  Go to any available pier to play!"
FishBingoOngoing = 'Welcome! Fish Bingo is currently in progress.'
FishBingoEnd = 'Hope you had fun playing Fish Bingo.'
FishBingoHelpMain = 'Welcome to Toontown Fish Bingo!  Everyone at the pond works together to fill the card before time runs out.'
FishBingoHelpFlash = 'When you catch a fish, click on one of the flashing squares to mark the card.'
FishBingoHelpNormal = 'This is a Classic Bingo card.  Mark any row down, across or diagonally to win.'
FishBingoHelpDiagonals = 'Mark both of the diagonals to win.'
FishBingoHelpCorners = 'An easy Corners card.  Mark all four corners to win.'
FishBingoHelpThreeway = "Three-way.  Mark both diagonals and the middle row to win.  This one isn't easy!"
FishBingoHelpBingo = 'Bingo!'
FishBingoHelpBlockout = 'Blockout!.  Mark the entire card to win.  You are competing against all the other ponds for a huge jackpot!'
FishBingoOfferToSellFish = 'Your fish bucket is full. Would you like to sell your fish?'
FishBingoJackpotWin = 'Win %s Jellybeans!'
ResistanceToonupMenu = 'Heals'
ResistanceToonupItem = '%s Heals'
ResistanceToonupItemMax = 'Full'
ResistanceToonupChat = 'Toons of the World, Heal Up!'
ResistanceRestockMenu = 'Restock'
ResistanceRestockItem = 'Restock %s'
ResistanceRestockItemAll = 'EVERYTHING YOU GOT!!!!!!!!!!!!'
ResistanceRestockChat = 'Toons of the World, Restock!'
ResistanceMeritsMenu = 'Promotions'
ResistanceMeritsItem = 'Promotions %s'
ResistanceMeritsChat = 'Toons of the World, PROMOTIONS!!'
ResistanceMoneyMenu = 'Money'
ResistanceMoneyItem = '%s Money'
ResistanceMoneyChat = 'Toons of the World, FINANCIAL STUFF!!'
ResistanceTicketsMenu = 'Tickets'
ResistanceTicketsItem = '%s Tickets'
ResistanceTicketsChat = 'Toons of the World, Go Race!'
ResistanceEmote1 = NPCToonNames[9228] + ': Welcome to the Resistance!'
ResistanceEmote2 = NPCToonNames[9228] + ': Use your new emote to identify yourself to other members.'
ResistanceEmote3 = NPCToonNames[9228] + ': Good luck!'
KartUIExit = 'Leave Kart'
KartShop_Cancel = lCancel
KartShop_BuyKart = 'Buy Kart'
KartShop_BuyAccessories = 'Buy Accessories'
KartShop_BuyAccessory = 'Buy Accessory'
KartShop_Cost = 'Cost: %d Tickets'
KartShop_ConfirmBuy = 'Buy the %s for %d Tickets?'
KartShop_NoAvailableAcc = 'No available accessories of this type'
KartShop_FullTrunk = 'Your trunk is full.'
KartShop_ConfirmReturnKart = 'Are you sure you want to return your current Kart?'
KartShop_ConfirmBoughtTitle = 'Congratulations!'
KartShop_NotEnoughTickets = 'Not Enough Tickets!'
KartView_Rotate = 'Rotate'
KartView_Right = 'Right'
KartView_Left = 'Left'
StartingBlock_NotEnoughTickets = "You don't have enough tickets! Try a practice race instead."
StartingBlock_NoBoard = 'Boarding has ended for this race. Please wait for the next race to begin.'
StartingBlock_NoKart = 'You need a kart first! Try asking one of the clerks in the Kart Shop.'
StartingBlock_Occupied = 'This block is currently occupied! Please try another spot.'
StartingBlock_TrackClosed = 'Sorry, this track is closed for remodeling.'
StartingBlock_EnterPractice = 'Would you like to enter a practice race?'
StartingBlock_EnterNonPractice = 'Would you like to enter a %s race for %s tickets?'
StartingBlock_EnterShowPad = 'Would you like to park your car here?'
StartingBlock_KickSoloRacer = 'Toon Battle and Grand Prix races require two or more racers.'
StartingBlock_Loading = 'Goofy Speedway'
LeaderBoard_Time = 'Time'
LeaderBoard_Name = 'Racer Name'
LeaderBoard_Daily = 'Daily Scores'
LeaderBoard_Weekly = 'Weekly Scores'
LeaderBoard_AllTime = 'All Time Best Scores'
RecordPeriodStrings = [LeaderBoard_Daily, LeaderBoard_Weekly, LeaderBoard_AllTime]
KartRace_RaceNames = ['Practice', 'Toon Battle', 'Grand Prix']
from toontown.racing import RaceGlobals
KartRace_Go = 'Go!'
KartRace_Reverse = ' Rev'
KartRace_TrackNames = {RaceGlobals.RT_Speedway_1: 'Screwball Stadium',
 RaceGlobals.RT_Speedway_1_rev: 'Screwball Stadium' + KartRace_Reverse,
 RaceGlobals.RT_Rural_1: 'Rustic Raceway',
 RaceGlobals.RT_Rural_1_rev: 'Rustic Raceway' + KartRace_Reverse,
 RaceGlobals.RT_Urban_1: 'City Circuit',
 RaceGlobals.RT_Urban_1_rev: 'City Circuit' + KartRace_Reverse,
 RaceGlobals.RT_Speedway_2: 'Corkscrew Coliseum',
 RaceGlobals.RT_Speedway_2_rev: 'Corkscrew Coliseum' + KartRace_Reverse,
 RaceGlobals.RT_Rural_2: 'Airborne Acres',
 RaceGlobals.RT_Rural_2_rev: 'Airborne Acres' + KartRace_Reverse,
 RaceGlobals.RT_Urban_2: 'Blizzard Boulevard',
 RaceGlobals.RT_Urban_2_rev: 'Blizzard Boulevard' + KartRace_Reverse}
KartRace_Unraced = 'N/A'
KartDNA_KartNames = {0: 'Cruiser',
 1: 'Roadster',
 2: 'Toon Utility Vehicle'}
KartDNA_AccNames = {1000: 'Air Cleaner',
 1001: 'Four Barrel',
 1002: 'Flying Eagle',
 1003: 'Steer Horns',
 1004: 'Straight Six',
 1005: 'Small Scoop',
 1006: 'Single Overhead',
 1007: 'Medium Scoop',
 1008: 'Single Barrel',
 1009: 'Flugle Horn',
 1010: 'Striped Scoop',
 2000: 'Space Wing',
 2001: 'Patched Spare',
 2002: 'Roll Cage',
 2003: 'Single Fin',
 2004: 'Double-decker Wing',
 2005: 'Single Wing',
 2006: 'Standard Spare',
 2007: 'Single Fin',
 2008: 'sp9',
 2009: 'sp10',
 3000: 'Dueling Horns',
 3001: "Freddie's Fenders",
 3002: 'Cobalt Running Boards',
 3003: 'Cobra Sidepipes',
 3004: 'Straight Sidepipes',
 3005: 'Scalloped Fenders',
 3006: 'Carbon Running Boards',
 3007: 'Wood Running Boards',
 3008: 'fw9',
 3009: 'fw10',
 4000: 'Curly Tailpipes',
 4001: 'Splash Fenders',
 4002: 'Dual Exhaust',
 4003: 'Plain Dual Fins',
 4004: 'Plain Mudflaps',
 4005: 'Quad Exhaust',
 4006: 'Dual Flares',
 4007: 'Mega Exhaust',
 4008: 'Striped Dual Fins',
 4009: 'Bubble Duals Fins',
 4010: 'Striped Mudflaps',
 4011: 'Mickey Mudflaps',
 4012: 'Scalloped Mudflaps',
 5000: 'Turbo',
 5001: 'Moon',
 5002: 'Patched',
 5003: 'Three Spoke',
 5004: 'Paint Lid',
 5005: 'Heart',
 5006: 'Mickey',
 5007: 'Five Bolt',
 5008: 'Daisy',
 5009: 'Basketball',
 5010: 'Hypno',
 5011: 'Tribal',
 5012: 'Gemstone',
 5013: 'Five Spoke',
 5014: 'Knockoff',
 6000: 'Number Five',
 6001: 'Splatter',
 6002: 'Checkerboard',
 6003: 'Flames',
 6004: 'Hearts',
 6005: 'Bubbles',
 6006: 'Tiger',
 6007: 'Flowers',
 6008: 'Lightning',
 6009: 'Angel',
 7000: 'Chartreuse',
 7001: 'Peach',
 7002: 'Bright Red',
 7003: 'Red',
 7004: 'Maroon',
 7005: 'Sienna',
 7006: 'Brown',
 7007: 'Tan',
 7008: 'Coral',
 7009: 'Orange',
 7010: 'Yellow',
 7011: 'Cream',
 7012: 'Citrine',
 7013: 'Lime',
 7014: 'Sea Green',
 7015: 'Green',
 7016: 'Light Blue',
 7017: 'Aqua',
 7018: 'Blue',
 7019: 'Periwinkle',
 7020: 'Royal Blue',
 7021: 'Slate Blue',
 7022: 'Purple',
 7023: 'Lavender',
 7024: 'Pink',
 7025: 'Plum',
 7026: 'Black'}
RaceHoodSpeedway = 'Speedway'
RaceHoodRural = 'Rural'
RaceHoodUrban = 'Urban'
RaceTypeCircuit = 'Tournament'
RaceQualified = 'qualified'
RaceSwept = 'swept'
RaceWon = 'won'
Race = 'race'
Races = 'races'
Total = 'total'
GrandTouring = 'Grand Touring'

def getTrackGenreString(genreId):
    genreStrings = ['Speedway', 'Country', 'City']
    return genreStrings[genreId].lower()


def getTunnelSignName(trackId, padId):
    if trackId == 2 and padId == 0:
        return 'tunne1l_citysign'
    elif trackId == 1 and padId == 0:
        return 'tunnel_countrysign1'
    else:
        genreId = RaceGlobals.getTrackGenre(trackId)
        return 'tunnel%s_%ssign' % (padId + 1, RaceGlobals.getTrackGenreString(genreId))


KartTrophyDescriptions = [str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodSpeedway + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodRural + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodUrban + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.TotalQualifiedRaces) + ' ' + Total + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodSpeedway + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodRural + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodUrban + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.TotalWonRaces) + ' ' + Total + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.SweptCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceSwept,
 str(RaceGlobals.SweptCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
 str(RaceGlobals.SweptCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
 GrandTouring,
 str(RaceGlobals.TrophiesPerCup) + ' Kart Racing trophies won! Laff point boost!',
 str(RaceGlobals.TrophiesPerCup * 2) + ' Kart Racing trophies won! Laff point boost!',
 str(RaceGlobals.TrophiesPerCup * 3) + ' Kart Racing trophies won! Laff point boost!']
KartRace_TitleInfo = 'Get Ready to Race'
KartRace_SSInfo = 'Welcome to Screwball Stadium!\nPut the pedal to the metal and hang on tight!\n'
KartRace_CoCoInfo = 'Welcome to Corkscrew Coliseum!\nUse the banked turns to keep your speed up!\n'
KartRace_RRInfo = 'Welcome to Rustic Raceway!\nPlease be kind to the fauna and stay on the track!\n'
KartRace_AAInfo = 'Welcome to Airborne Acres!\nHold onto your hats! It looks bumpy up ahead...\n'
KartRace_CCInfo = 'Welcome to City Circuit!\nWatch out for pedestrians as you speed through downtown!\n'
KartRace_BBInfo = 'Welcome to Blizzard Boulevard!\nWatch your speed. There might be ice out there.\n'
KartRace_GeneralInfo = 'Use Control to throw gags you pick up on the track, and the arrow keys to control your kart.'
KartRace_TrackInfo = {RaceGlobals.RT_Speedway_1: KartRace_SSInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_1_rev: KartRace_SSInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_2: KartRace_CoCoInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_2_rev: KartRace_CoCoInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_1: KartRace_RRInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_1_rev: KartRace_RRInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_2: KartRace_AAInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_2_rev: KartRace_AAInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_1: KartRace_CCInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_1_rev: KartRace_CCInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_2: KartRace_BBInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_2_rev: KartRace_BBInfo + KartRace_GeneralInfo}
KartRecordStrings = {RaceGlobals.Daily: 'daily',
 RaceGlobals.Weekly: 'weekly',
 RaceGlobals.AllTime: 'all time'}
KartRace_FirstSuffix = 'st'
KartRace_SecondSuffix = '    nd'
KartRace_ThirdSuffix = '  rd'
KartRace_FourthSuffix = '   th'
KartRace_WrongWay = 'Wrong\nWay!'
KartRace_LapText = 'Lap %s'
KartRace_FinalLapText = 'Final Lap!'
KartRace_Exit = 'Exit Race'
KartRace_NextRace = 'Next Race'
KartRace_Leave = 'Leave Race'
KartRace_Qualified = 'Qualified!'
KartRace_Record = 'Record!'
KartRace_RecordString = 'You have set a new %s record for %s! Your bonus is %s tickets.'
KartRace_Tickets = 'Tickets'
KartRace_Exclamations = '!'
KartRace_Deposit = 'Deposit'
KartRace_Winnings = 'Winnings'
KartRace_Bonus = 'Bonus'
KartRace_RaceTotal = 'Race Total'
KartRace_CircuitTotal = 'Circuit Total'
KartRace_Trophies = 'Trophies'
KartRace_Zero = '0'
KartRace_Colon = ':'
KartRace_TicketPhrase = '%s ' + KartRace_Tickets
KartRace_DepositPhrase = KartRace_Deposit + KartRace_Colon + '\n'
KartRace_QualifyPhrase = 'Qualify:\n'
KartRace_RaceTimeout = 'You timed out of that race.  Your tickets have been refunded.  Keep trying!'
KartRace_RaceTimeoutNoRefund = 'You timed out of that race.  Your tickets have not been refunded because the Grand Prix had already started.  Keep trying!'
KartRace_RacerTooSlow = 'You took too long to finish the race.  Your tickets have not been refunded.  Keep trying!'
KartRace_PhotoFinish = 'Photo Finish!'
KartRace_CircuitPoints = 'Circuit Points'
CircuitRaceStart = 'The Toontown Grand Prix at Goofy Speedway is about to begin!  To win, collect the most points in three consecutive races!'
CircuitRaceOngoing = 'Welcome! The Toontown Grand Prix is currently in progress.'
CircuitRaceEnd = "That's all for today's Toontown Grand Prix at Goofy Speedway.  See you next week!"
TrickOrTreatMsg = 'You have already\nfound this treat!'
WinterCarolingMsg = 'You have already been caroling here!'
LawbotBossTempIntro0 = "Welcome, Cogs! It's a pleasure to meet you."
LawbotBossTempIntro1 = "You see here, we have new guests on the elevator and I'm coming."
LawbotBossTempIntro2 = "I am still coming."
LawbotBossTempIntro3 = 'Ok, I am here.'
LawbotBossTempIntro4 = "Oh, welcome, new Cogs."
LawbotBossTempIntro5 = "I see you're here for the new grand, eh?"
LawbotBossTempIntro6 = "Wait a minute, you look funny..."
LawbotBossTempIntro7 = "And you smell funny..."
LawbotBossTempIntro8 = "Wait a minute, you're Toons!"
LawbotBossTempIntro9 = "Get them!"
LawbotBossTempJury1 = 'Okay Cogs, End this!'
LawbotBossHowToGetEvidence = 'Touch the witness stand to get evidence.'
LawbotBossTrialChat1 = 'Court is now in session'
LawbotBossHowToThrowPies = 'Press the Delete key to throw the evidence\n at the lawyers or into the scale!'
LawbotBossNeedMoreEvidence = 'You need to get more evidence!'
LawbotBossDefenseWins1 = 'What! How did the defence win?'
LawbotBossDefenseWins2 = 'I demand a rematch!'
LawbotBossDefenseWins3 = "Bah, who cares? I'll just send in Classic Noah for repairs."
LawbotBossProsecutionWins = 'I find in favor of the plaintiff!'
LawbotBossReward = 'I award a promotion and the ability to summon Cogs'
LawbotBossLeaveCannon = 'Leave cannon'
LawbotBossPassExam = 'Bah, so you passed the bar exam.'
LawbotBossTaunts = ['%s, I find you in contempt of court!',
 'Get them, get them all!',
 'Stop stalking, and destroy them!',
 'Want some food? Order now here.',
 'The Fashionbots will be proud of us.']
WitnessToonPrepareBattleTwo = "Oh no! They're putting only Cogs on the jury!\x07Quick, use the cannons and shoot some Toon jurors into the jury chairs.\x07We need %d to get a balanced scale."
WitnessToonNoJuror = 'Oh oh, no Toon jurors. This will be a tough trial.'
WitnessToonOneJuror = 'Cool! There is 1 Toon in the jury!'
WitnessToonSomeJurors = 'Cool! There are %d Toons in the jury!'
WitnessToonAllJurors = 'Awesome! All the jurors are Toons!'
WitnessToonPrepareBattleThree = 'Hurry, touch the witness stand to get evidence.\x07Press the Delete key to throw the evidence at the lawyers, or at the defense pan.'
WitnessToonCongratulations = "You did it!  Thank you for a spectacular defense!\x07Here, take these papers the Chief Justice left behind.\x07With it you'll be able to summon Cogs from your Cog Gallery page."
WitnessToonLastPromotion = "Wow, you've reached level %s on your Cog Suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog Suit anymore, but you can certainly keep working for the Resistance!"
WitnessToonHPBoost = "You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
WitnessToonMaxed = 'I see that you have a level %s Cog Suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to defend more Toons!'
WitnessToonBonus = 'Wonderful! All the lawyers are stunned. Your evidence weight is %s times heavier for %s seconds'
WitnessToonJuryWeightBonusSingular = {6: 'This is a tough case. You seated %d Toon juror, so your evidence has a bonus weight of %d.',
 7: 'This is a very tough case. You seated %d Toon juror, so your evidence has a bonus weight of %d.',
 8: 'This is the toughest case. You seated %d Toon juror, so your evidence has a bonus weight of %d.'}
WitnessToonJuryWeightBonusPlural = {6: 'This is a tough case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.',
 7: 'This is a very tough case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.',
 8: 'This is the toughest case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.'}
IssueSummons = 'Summon'
SummonDlgTitle = 'Issue a Cog Summon'
SummonDlgButton1 = 'Summon a Cog Building'
SummonDlgButton2 = 'Summon a Cog Invasion'
SummonDlgButton3 = 'Summon a Field Office'
SummonDlgButton4 = 'Summon a Skelecog Invasion'
SummonDlgButton5 = 'Summon a Waiter Invasion'
SummonDlgButton6 = 'Summon a Version 2.0 Invasion'
SummonDlgBuildingConf = 'Would you like to summon a %s to a nearby Toon building?'
SummonDlgInvasionConf = 'Would you like to summon a %s invasion?'
SummonDlgSkelInvasionConf = 'Would you like to summon a %s (Skelecog) invasion?'
SummonDlgWaiterInvasionConf = 'Would you like to summon a %s (Waiter) invasion?'
SummonDlgV2InvasionConf = 'Would you like to summon a Version 2.0 %s invasion?'
SummonDlgNumLeft = 'You have %s left.'
SummonDlgDelivering = 'Delivering Summons...'
SummonDlgBldgSuccess = 'You have successfully summoned the Cogs. %s has agreed to let them temporarily take over %s!'
SummonDlgBldgSuccess2 = 'You have successfully summoned the Cogs. A Shopkeeper has agreed to let them temporarily take over their building!'
SummonDlgBldgBadLoc = 'Sorry, there are no Toon buildings nearby for the Cogs to take over.'
SummonDlgBldgNoCogdos = "Sorry, but you can't summon a Field Office right now. Please try again later."
SummonDlgInvasionSuccess = "You have successfully summoned the Cogs. It's an invasion!"
SummonDlgInvasionBusy = 'A %s cannot be found now.  Try again when the Cog invasion is over.'
SummonDlgInvasionFail = 'Sorry, the Cog invasion has failed.'
SummonDlgShopkeeper = 'The Shopkeeper '
PolarPlaceEffect1 = NPCToonNames[3306] + ': Welcome to Polar Place!'
PolarPlaceEffect2 = NPCToonNames[3306] + ': Try this on for size.'
PolarPlaceEffect3 = NPCToonNames[3306] + ': Your new look will only work in ' + lTheBrrrgh + '.'
GreenToonEffectMsg = NPCToonNames[5312] + ': You look Toontastic in green!'
LaserGameMine = 'Skull Finder!'
LaserGameRoll = 'Matching'
LaserGameAvoid = 'Avoid the Skulls'
LaserGameDrag = 'Drag three of a color in a row'
LaserGameDefault = 'Unknown Game'
PinballHiScore = 'High Score:     %s\n'
PinballHiScoreAbbrev = '...'
PinballYourBestScore = 'Your Best Score:\n'
PinballScore = 'Score:            %d x %d = '
PinballScoreHolder = '%s\n'
GagTreeFeather = 'Feather Gag Tree'
GagTreeJugglingBalls = 'Juggling Balls Gag Tree'
StatuaryFountain = 'Fountain'
StatuaryDonald = 'Donald Statue'
StatuaryMinnie = 'Minnie Statue'
StatuaryMickey1 = 'Mickey Statue'
StatuaryMickey2 = 'Mickey Fountain'
StatuaryToon = 'Toon Statue'
StatuaryToonWave = 'Toon Wave Statue'
StatuaryToonVictory = 'Toon Victory Statue'
StatuaryToonCrossedArms = 'Toon Authority Statue'
StatuaryToonThinking = 'Toon Embrace Statue'
StatuaryMeltingSnowman = 'Melting Snowman'
StatuaryMeltingSnowDoodle = 'Melting SnowDoodle'
StatuaryGardenAccelerator = 'Insta-Grow Fertilizer'
AnimatedStatuaryFlappyCog = 'Flappy Cog'
FlowerColorStrings = ['Red',
 'Orange',
 'Violet',
 'Blue',
 'Pink',
 'Yellow',
 'White',
 'Green']
FlowerSpeciesNames = {49: 'Daisy',
 50: 'Tulip',
 51: 'Carnation',
 52: 'Lily',
 53: 'Daffodil',
 54: 'Pansy',
 55: 'Petunia',
 56: 'Rose'}
FlowerFunnyNames = {49: ('School Daisy',
      'Lazy Daisy',
      'Midsummer Daisy',
      'Freshasa Daisy',
      'Whoopsie Daisy',
      'Upsy Daisy',
      'Crazy Daisy',
      'Hazy Dazy'),
 50: ('Onelip', 'Twolip', 'Threelip'),
 51: ('What-in Carnation',
      'Instant Carnation',
      'Hybrid Carnation',
      'Side Carnation',
      'Model Carnation'),
 52: ('Lily-of-the-Alley',
      'Lily Pad',
      'Tiger Lily',
      'Livered Lily',
      'Chili Lily',
      'Silly Lily',
      'Indubitab Lily',
      'Dilly Lilly'),
 53: ('Laff-o-dil',
      'Daffy Dill',
      'Giraff-o-dil',
      'Time and a half-o-dil'),
 54: ('Dandy Pansy',
      'Chim Pansy',
      'Potsen Pansy',
      'Marzi Pansy',
      'Smarty Pansy'),
 55: ('Car Petunia', 'Platoonia'),
 56: ("Summer's Last Rose",
      'Corn Rose',
      'Tinted Rose',
      'Stinking Rose',
      'Istilla Rose')}
FlowerVarietyNameFormat = '%s %s'
FlowerUnknown = '????'
FloweringNewEntry = 'New Entry'
ShovelNameDict = {0: 'Tin',
 1: 'Bronze',
 2: 'Silver',
 3: 'Gold'}
WateringCanNameDict = {0: 'Small',
 1: 'Medium',
 2: 'Large',
 3: 'Huge'}
GardeningPlant = 'Plant'
GardeningWater = 'Water'
GardeningRemove = 'Remove'
GardeningPick = 'Pick'
GardeningFull = 'Full'
GardeningSkill = 'Skill'
GardeningWaterSkill = 'Water Skill'
GardeningShovelSkill = 'Shovel Skill'
GardeningNoSkill = 'No Skill Up'
GardeningPlantFlower = 'Plant\nFlower'
GardeningPlantTree = 'Plant\nTree'
GardeningPlantItem = 'Plant\nItem'
PlantingGuiOk = 'Plant'
PlantingGuiCancel = 'Cancel'
PlantingGuiReset = 'Reset'
GardeningChooseBeans = 'Choose the Jellybeans you want to plant.'
GardeningChooseBeansItem = 'Choose the Jellybeans / item you want to plant.'
GardeningChooseToonStatue = 'Choose the toon you want to create a statue of.'
GardenShovelLevelUp = "Congratulations you've earned a %(shovel)s! You've mastered the %(oldbeans)d bean flower! To progress you should pick %(newbeans)d bean flowers."
GardenShovelSkillLevelUp = "Congratulations! You've mastered the %(oldbeans)d bean flower! To progress you should pick %(newbeans)d bean flowers."
GardenShovelSkillMaxed = "Amazing! You've maxed out your shovel skill!"
GardenWateringCanLevelUp = "Congratulations you've earned a new watering can!"
GardenMiniGameWon = "Congratulations you've watered the plant!"
ShovelTin = 'Tin Shovel'
ShovelSteel = 'Bronze Shovel'
ShovelSilver = 'Silver Shovel'
ShovelGold = 'Gold Shovel'
WateringCanSmall = 'Small Watering Can'
WateringCanMedium = 'Medium Watering Can'
WateringCanLarge = 'Large Watering Can'
WateringCanHuge = 'Huge Watering Can'
BeanColorWords = ('red',
 'green',
 'orange',
 'violet',
 'blue',
 'pink',
 'yellow',
 'cyan',
 'silver')
PlantItWith = ' Plant with %s.'
MakeSureWatered = ' Make sure all your plants are watered first.'
UseFromSpecialsTab = ' Use from the specials tab of the garden page.'
UseSpecial = 'Use Special'
UseSpecialBadLocation = 'You can only use that in your garden.'
UseSpecialSuccess = 'Success! Your watered plants just grew.'
ConfirmWiltedFlower = '%(plant)s is wilted.  Are you sure you want to remove it?  It will not go into your flower basket, nor will you get an increase in skill.'
ConfirmUnbloomingFlower = '%(plant)s is not blooming.  Are you sure you want to remove it?  It will not go into your flower basket, nor will you get an increase in skill.'
ConfirmNoSkillupFlower = 'Are you sure you want to pick the %(plant)s? It will go into your flower basket, but you will NOT get an increase in skill.'
ConfirmSkillupFlower = 'Are you sure you want to pick the %(plant)s?  It will go into your flower basket. You will also get an increase in skill.'
ConfirmMaxedSkillFlower = "Are you sure you want to pick the %(plant)s?  It will go into your flower basket. You will NOT get an increase in skill since you've maximized it already."
ConfirmBasketFull = 'Your flower basket is full. Sell some flowers first.'
ConfirmRemoveTree = 'Are you sure you want to remove the %(tree)s?'
ConfirmWontBeAbleToHarvest = " If you remove this tree, you won't be able to harvest gags from the higher level trees."
ConfirmRemoveStatuary = 'Are you sure you want to permanently delete the %(item)s?'
ResultPlantedSomething = 'Congratulations! You just planted a %s.'
ResultPlantedSomethingAn = 'Congratulations! You just planted an %s.'
ResultPlantedNothing = "That didn't work.  Please try a different combination of Jellybeans."
GardenGagTree = ' Gag Tree'
GardenUberGag = 'Uber Gag'

def getRecipeBeanText(beanTuple):
    retval = ''
    if not beanTuple:
        return retval
    allTheSame = True
    for index in xrange(len(beanTuple)):
        if index + 1 < len(beanTuple):
            if not beanTuple[index] == beanTuple[index + 1]:
                allTheSame = False
                break

    if allTheSame:
        if len(beanTuple) > 1:
            retval = '%d %s Jellybeans' % (len(beanTuple), BeanColorWords[beanTuple[0]])
        else:
            retval = 'a %s Jellybean' % BeanColorWords[beanTuple[0]]
    else:
        retval += 'a'
        maxBeans = len(beanTuple)
        for index in xrange(maxBeans):
            if index == maxBeans - 1:
                retval += ' and %s Jellybean' % BeanColorWords[beanTuple[index]]
            elif index == 0:
                retval += ' %s' % BeanColorWords[beanTuple[index]]
            else:
                retval += ', %s' % BeanColorWords[beanTuple[index]]

    return retval


GardenTextMagicBeans = 'Magic Beans'
GardenTextMagicBeansB = 'Some Other Beans'
GardenSpecialDiscription = 'This text should explain how to use a certain garden special'
GardenSpecialDiscriptionB = 'This text should explain how to use a certain garden special, in yo face foo!'
GardenTrophyAwarded = 'Wow! You collected %s of %s flowers. That deserves a trophy and a Laff boost!'
GardenTrophyNameDict = {0: 'Wheelbarrow',
 1: 'Shovels',
 2: 'Flower',
 3: 'Watering Can',
 4: 'Shark',
 5: 'Swordfish',
 6: 'Killer Whale'}
SkillTooLow = 'Skill\nToo Low'
NoGarden = 'No\nGarden'

def isVowelStart(str):
    retval = False
    if str and len(str) > 0:
        vowels = ['A',
         'E',
         'I',
         'O',
         'U']
        firstLetter = str.upper()[0:1]
        if firstLetter in vowels:
            retval = True
    return retval


def getResultPlantedSomethingSentence(flowerName):
    if isVowelStart(flowerName):
        retval = ResultPlantedSomethingAn % flowerName
    else:
        retval = ResultPlantedSomething % flowerName
    return retval

VineGameTitle = 'Jungle Vines'
VineGameInstructions = 'Get to the rightmost vine in time. Press Up or Down to climb the vine.  Press Left or Right to change facing and jump.  The lower you are on the vine, the faster you jump off.  Collect the bananas if you can, but avoid the bats and spiders.'
ValentinesDayStart = "Happy ValenToon's Day!"
ValentinesDayEnd = "That's all for ValenToon's Day!"
GolfCourseNames = {0: 'Walk In The Par',
 1: 'Hole Some Fun',
 2: 'The Hole Kit And Caboodle'}
GolfHoleNames = {0: 'Whole In Won',
 1: 'No Putts About It',
 2: 'Down The Hatch',
 3: 'Seeing Green',
 4: 'Hot Links',
 5: 'Peanut Putter',
 6: 'Swing-A-Long',
 7: 'Afternoon Tee',
 8: 'Hole In Fun',
 9: 'Rock And Roll In',
 10: 'Bogey Nights',
 11: 'Tea Off Time',
 12: 'Holey Mackerel!',
 13: 'One Little Birdie',
 14: 'At The Drive In',
 15: 'Swing Time',
 16: 'Hole On The Range',
 17: 'Second Wind',
 18: 'Whole In Won-2',
 19: 'No Putts About It-2',
 20: 'Down The Hatch-2',
 21: 'Seeing Green-2',
 22: 'Hot Links-2',
 23: 'Peanut Putter-2',
 24: 'Swing-A-Long-2',
 25: 'Afternoon Tee-2',
 26: 'Hole In Fun-2',
 27: 'Rock And Roll In-2',
 28: 'Bogey Nights-2',
 29: 'Tea Off Time-2',
 30: 'Holey Mackerel!-2',
 31: 'One Little Birdie-2',
 32: 'At The Drive In-2',
 33: 'Swing Time-2',
 34: 'Hole On The Range-2',
 35: 'Second Wind-2'}
GolfHoleInOne = 'Hole In One'
GolfCondor = 'Condor'
GolfAlbatross = 'Albatross'
GolfEagle = 'Eagle'
GolfBirdie = 'Birdie'
GolfPar = 'Par'
GolfBogey = 'Bogey'
GolfDoubleBogey = 'Double Bogey'
GolfTripleBogey = 'Triple Bogey'
GolfShotDesc = {-4: GolfCondor,
 -3: GolfAlbatross,
 -2: GolfEagle,
 -1: GolfBirdie,
 0: GolfPar,
 1: GolfBogey,
 2: GolfDoubleBogey,
 3: GolfTripleBogey}
from toontown.golf import GolfGlobals
CoursesCompleted = 'Courses Completed'
CoursesUnderPar = 'Courses Under Par'
HoleInOneShots = 'Hole In One Shots'
EagleOrBetterShots = 'Eagle Or Better Shots'
BirdieOrBetterShots = 'Birdie Or Better Shots'
ParOrBetterShots = 'Par Or Better Shots'
MultiPlayerCoursesCompleted = 'Multiplayer Courses Completed'
TwoPlayerWins = 'Two Player Wins'
ThreePlayerWins = 'Three Player Wins'
FourPlayerWins = 'Four Player Wins'
CourseZeroWins = GolfCourseNames[0] + ' Wins'
CourseOneWins = GolfCourseNames[1] + ' Wins'
CourseTwoWins = GolfCourseNames[2] + ' Wins'
GolfHistoryDescriptions = [CoursesCompleted,
 CoursesUnderPar,
 HoleInOneShots,
 EagleOrBetterShots,
 BirdieOrBetterShots,
 ParOrBetterShots,
 MultiPlayerCoursesCompleted,
 CourseZeroWins,
 CourseOneWins,
 CourseTwoWins]
GolfTrophyDescriptions = [str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][0]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][1]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][2]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][0]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][1]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][2]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][0]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][1]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][2]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][0]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][1]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][2]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][0]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][1]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][2]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][0]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][1]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][2]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][0]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][1]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][2]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][0]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][1]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][2]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][0]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][1]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][2]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][0]) + ' ' + CourseTwoWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][1]) + ' ' + CourseTwoWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][2]) + ' ' + CourseTwoWins]
GolfCupDescriptions = [str(GolfGlobals.TrophiesPerCup) + ' Trophies won', str(GolfGlobals.TrophiesPerCup * 2) + ' Trophies won', str(GolfGlobals.TrophiesPerCup * 3) + ' Trophies won']
GolfAvReceivesHoleBest = '%(name)s scored a new hole best at %(hole)s!'
GolfAvReceivesCourseBest = '%(name)s scored a new course best at %(course)s!'
GolfAvReceivesCup = '%(name)s receives the %(cup)s cup!!  Laff point boost!'
GolfAvReceivesTrophy = '%(name)s receives the %(award)s trophy!!'
GolfRanking = 'Ranking: \n'
GolfPowerBarText = '%(power)s%%'
GolfChooseTeeInstructions = 'Press Left or Right to change tee spot.\nPress Control to select.'
GolfWarningMustSwing = 'Warning: You must press Control on your next swing.'
GolfAimInstructions = 'Press Left or Right to aim.\nPress and hold Control to swing.'
GolferExited = '%s has left the golf course.'
GolfPowerReminder = 'Hold Down Control Longer to\nHit the Ball Further'
GolfPar = 'Par'
GolfHole = 'Hole'
GolfTotal = 'Total'
GolfExitCourse = 'Exit Course'
GolfUnknownPlayer = '???'
GolfPageTitle = 'Golf'
GolfPageTitleCustomize = 'Golf Customizer'
GolfPageTitleRecords = 'Personal Best Records'
GolfPageTitleTrophy = 'Golfing Trophies'
GolfPageCustomizeTab = 'Customize'
GolfPageRecordsTab = 'Records'
GolfPageTrophyTab = 'Trophy'
GolfPageTickets = 'Tickets : '
GolfPageConfirmDelete = 'Delete Accessory?'
GolfTrophyTextDisplay = 'Trophy %(number)s : %(desc)s'
GolfCupTextDisplay = 'Cup %(number)s : %(desc)s'
GolfCurrentHistory = 'Current %(historyDesc)s : %(num)s'
GolfTieBreakWinner = '%(name)s wins the random tie breaker!'
GolfSeconds = ' -  %(time).2f seconds'
GolfTimeTieBreakWinner = '%(name)s wins the total aiming time tie breaker!!!'
MoreXpHolidayStart = 'Good news! Exclusive Test Toon double gag experience time has started.'
MoreXpHolidayOngoing = 'Welcome! Exclusive Test Toon double gag experience time is currently ongoing.'
MoreXpHolidayEnd = 'Exclusive Test Toon double gag experience time has ended. Thanks for helping us Test things!'
JellybeanDayHolidayStart = "It's Jellybean Day! Get Double Jellybean rewards at Parties!"
JellybeanDayHolidayEnd = "That's all for Jellybean Day. See you next year."
PartyRewardDoubledJellybean = 'Double Jellybeans!'
GrandPrixWeekendHolidayStart = "It's Grand Prix Weekend at Goofy Speedway! Toons collect the most points in three consecutive races."
GrandPrixWeekendHolidayEnd = "That's all for Grand Prix Weekend. See you next year."
KartRace_DoubleTickets = 'Double Tickets'
SellbotNerfHolidayStart = 'Operation: Storm Sellbot is happening now! Battle the VP today!'
SellbotNerfHolidayEnd = 'Operation: Storm Sellbot has ended. Great work, Toons!'
LawbotNerfHolidayStart = 'Operation: Lawbots Lose is happening now! Battle the CJ today!'
LawbotNerfHolidayEnd = 'Operation: Lawbots Lose has ended. Great work, Toons!'
CashbotNerfHolidayStart = 'Operation: Cashbot Chaos is happening now! Battle the CFO today!'
CashbotNerfHolidayEnd = 'Opeation: Cashbot Chaos has ended. Great work, Toons!'
BossbotNerfHolidayStart = 'Operation: Besiege Bossbot is happening now! Battle the CEO today!'
BossbotNerfHolidayEnd = 'Operation: Besiege Bossbot has ended. Great work, Toons!'
JellybeanTrolleyHolidayStart = 'Double Bean Days for Trolley Games have begun!'
JellybeanTrolleyHolidayEnd = 'Double Bean Days for Trolley Games have ended!'
JellybeanFishingHolidayStart = 'Double Bean Days for Fishing have begun!'
JellybeanFishingHolidayEnd = 'Double Bean Days for Fishing have ended!'
JellybeanPartiesHolidayStart = "It's Jellybean Week! Get Double Jellybean rewards!"
JellybeanPartiesHolidayEnd = "That's all for Jellybean Week. See you next year."
JellybeanMonthHolidayStart = 'Celebrate Toontown with double beans, Cattlelog items and silly surprises!'
BankUpgradeHolidayStart = 'Something Toontastic happened to your Jellybean Bank!'
HalloweenPropsHolidayStart = "It's Halloween in Toontown!"
HalloweenPropsHolidayEnd = 'Halloween has ended. Boo!'
SpookyPropsHolidayStart = 'Silly Meter spins Toontown into spooky mode!'
BlackCatHolidayStart = 'Create a Black Cat - today only!'
BlackCatHolidayEnd = 'Black Cat day has ended!'
SpookyBlackCatHolidayStart = 'Friday 13th means a Black Cat blast!'
TopToonsMarathonStart = "The Top Toons New Year's Day Marathon has begun!"
TopToonsMarathonEnd = "The Top Toons New Year's Day Marathon has ended."
WinterDecorationsStart = "It's Winter Holiday time in Toontown!"
WinterDecorationsEnd = 'Winter Holiday is over - Happy New Year!'
WackyWinterDecorationsStart = 'Brrr! Silly Meter goes from silly to chilly!'
WinterCarolingStart = 'Caroling has come to Toontown. Sing for your Snowman Head - see the Blog for details!'
WinterCarolingEnd = 'Caroling is over. See you next year.'
TrickOrTreatStart = 'Happy Halloween! Trick or treat throughout Toontown to get a nifty Halloween pumpkin head reward!'
TrickOrTreatEnd = 'Halloween is over. See you next year.'
ExpandedClosetsStart = 'Attention Toons: For a limited time, Members can purchase the new 50 item Closet from the Cattlelog for the low price of 50 Jellybeans!'
KartingTicketsHolidayStart = 'Get double tickets from Practice races at Goofy Speedway today!'
IdesOfMarchStart = 'Toons go GREEN!'
IdesOfMarchEnd = 'Hope you had fun being green.'
LogoutForced = 'You have done something wrong\n and are being logged out automatically,\n additionally your account may be frozen.\n Try going on a walk outside, it is fun.'
CountryClubToonEnterElevator = '%s \nhas jumped in the golf kart.'
CountryClubBossConfrontedMsg = '%s is battling the Club President!'
ElevatorBlockedRoom = 'All challenges must be defeated first.'
MolesLeft = 'Moles Left: %d'
MolesInstruction = 'Mole Stomp!\nJump on the red moles!'
MolesFinished = 'Mole Stomp successful!'
MolesPityWin = 'Stomp Failed! But the moles left.'
MolesRestarted = 'Stomp Failed! Restarting...'
BustACogInstruction = 'Remove the cog ball!'
BustACogExit = 'Exit for Now'
BustACogHowto = 'How to Play'
BustACogFailure = 'Out of Time!'
BustACogSuccess = 'Success!'
GolfGreenGameScoreString = 'Puzzles Left: %s'
GolfGreenGamePlayerScore = 'Solved %s'
GolfGreenGameBonusGag = 'You won %s!'
GolfGreenGameGotHelp = '%s solved a Puzzle!'
GolfGreenGameDirections = 'Shoot balls using the the mouse\n\n\nMatching three of a color causes the balls to fall\n\n\nRemove all Cog balls from the board'
enterHedgeMaze = 'Race through the Hedge Maze\n for a laff bonus!'
toonFinishedHedgeMaze = '%s \n  finished in %s place!'
hedgeMazePlaces = ['first',
 'second',
 'third',
 'Fourth']
mazeLabel = 'Maze Race!'
BoardingPartyReadme = 'Boarding Group?'
BoardingGroupHide = 'Hide'
BoardingGroupShow = 'Show Boarding Group'
BoardingPartyInform = 'Create an elevator Boarding Group by clicking on another Toon and Inviting them.\nIn this area Boarding Groups cannot have more than %s Toons.'
BoardingPartyTitle = 'Boarding Group'
BoardingPartyTitleMerge = 'Merge Group'
QuitBoardingPartyLeader = 'Disband'
QuitBoardingPartyNonLeader = 'Leave'
QuitBoardingPartyConfirm = 'Are you sure you want to quit this Boarding Group?'
BoardcodeMissing = 'Something went wrong; try again later.'
BoardcodePromotionLeader = 'Your group cannot board because you do not have enough promotion merits.'
BoardcodePromotionNonLeaderSingular = 'Your group cannot board because %s does not have enough promotion merits.'
BoardcodePromotionNonLeaderPlural = 'Your group cannot board because %s do not have enough promotion merits.'
BoardcodeSpace = 'Your group cannot board because there is not enough space.'
BoardcodeBattleLeader = 'Your group cannot board because you are in battle.'
BoardcodeBattleNonLeaderSingular = 'Your group cannot board because %s is in battle.'
BoardcodeBattleNonLeaderPlural = 'Your group cannot board because %s are in battle.'
BoardingInvitePromotionInviter = 'You need to earn a promotion before being a member of this Boarding Group.'
BoardingInvitePromotionInvitee = '%s needs to earn a promotion before being a member of this Boarding Group.'
BoardingInviteeInDiffGroup = '%s is already in a different Boarding Group.'
BoardingInviteeInKickOutList = '%s had been removed by your leader. Only the leader can re-invite removed members.'
BoardingInviteePendingIvite = '%s has a pending invite; try again later.'
BoardingInviteeInElevator = '%s is currently busy; try again later.'
BoardingInviteGroupFull = 'Your Boarding Group is already full.'
BoardingGroupsTooLarge = '%s is already in a different Boarding Group that is too large to merge.'
BoardingAlreadyInGroup = 'You cannot accept this invitation because you are part of another Boarding Group.'
BoardingGroupAlreadyFull = 'You cannot accept this invitation because the group is already full.'
BoardingKickOutConfirm = 'Are you sure you want to remove %s?'
BoardingPendingInvite = 'You need to deal with the\n pending invitation first.'
BoardingCannotLeaveZone = 'You cannot leave this area because you are part of a Boarding Group.'
BoardingInviteeMessage = '%s would like you to join their Boarding Group.'
BoardingInviteeMergeMessage = '%s would like you merge with their Boarding Group.'
BoardingInvitingMessage = 'Inviting %s to your Boarding Group.'
BoardingInvitationRejected = '%s has rejected to join your Boarding Group.'
BoardingMessageKickedOut = 'You have been removed from the Boarding Group.'
BoardingMessageInvited = '%s has invited %s to the Boarding Group.'
BoardingMessageLeftGroup = '%s has left the Boarding Group.'
BoardingMessageGroupDissolved = 'Your Boarding Group was disbanded by the group leader.'
BoardingMessageGroupDisbandedGeneric = 'Your Boarding Group was disbanded.'
BoardingMessageInvitationFailed = '%s tried to invite you to their Boarding Group.'
BoardingMessageGroupFull = '%s tried to accept your invitation but your group was full.'
BoardingGo = 'GO'
BoardingCancelGo = 'Click Again to\nCancel Go'
And = 'and'
BoardingGoingTo = 'Going To:'
BoardingTimeWarning = 'Boarding the elevator in '
BoardingMore = 'more'
BoardingGoShow = 'Going to\n%s in '
BoardingGoPreShow = 'Confirming...'
BossbotBossName = 'KingShine'
BossbotRTWelcome = "Hello Toons! Welcome to KingShine's Lair!"
BossbotRTRemoveSuit = 'Cog suits...'
BossbotRTFightWaiter = 'You know the drill.'
BossbotRTWearWaiter1 = "Good Job Toons! You defeated the Waiters!"
BossbotRTWearWaiter2 = "Now be aware, the King is inside these chambers."
BossbotRTWearWaiter3 = "The King is very strict, given orders by his Queen."
BossbotRTWearWaiter4 = "We cannot fail, because if we do, we will get kicked out."
BossbotRTWearWaiter5 = "Now let's listen to see what he has to say."
BossbotBossPreTwo1 = "Hello, Cogs. I would like to order."
BossbotBossPreTwo2 = 'Serve my waiters cakes, with no mayo please.'
BossbotRTServeFood1 = "Well, it looks like you're the new waiter."
BossbotRTServeFood2 = "So, my friend Marco baked me some cake."
BossbotRTServeFood3 = "They contain a special ingredient called Mayonnaise."
BossbotRTServeFood4 = "Serve a Cog with two cakes in a row, and they will explode."
BossbotRTServeFood5 = "But keep in mind, if they get angry, then you will have to restart that Cog."
BossbotRTServeFood6 = 'Alright, I said enough, now get out there!'
BossbotPhase3Speech1 = "I SPECIFICALLY SAID NO MAYO ON THE CAKES!!!!!!!"
BossbotPhase3Speech2 = 'WHY! DO THE CAKES! HAVE! MAYO!??!?!'
BossbotPhase3Speech3 = 'Eliminate them from this office!!!'
BossbotPhase4Speech1 = 'OH that does it! I had enough!'
BossbotPhase4Speech2 = "This battle ends here! And now!! I'll send you straight to the Cog HQS!"
BossbotRTPhase4Speech1 = "Oh no, he's very angry now..."
BossbotRTPhase4Speech2 = 'Listen, we have no time to talk, finish him with anything you got! I know you can do it!'
BossbotRTPhase4Speech3 = 'Use the seltzer bottles to damage him.'
BossbotRTPhase4Speech4 = 'Or use Golf balls to slow him down.'
BossbotRTPhase4Speech5 = 'This will take some skill, so good luck Toons!'
BossbotPitcherLeave = 'Leave Bottle'
BossbotPitcherLeaving = 'Leaving Bottle'
BossbotPitcherAdvice = 'Use the left and right keys to rotate.\nHold down Ctrl increase power.\nRelease Ctrl to fire.'
BossbotGolfSpotLeave = 'Leave Golf Ball'
BossbotGolfSpotLeaving = 'Leaving Golf Ball'
BossbotGolfSpotAdvice = 'Use the left and right keys to rotate.\nCtrl to fire.'
BossbotRewardSpeech1 = "WHAT! NO! NOT THIS!"
BossbotRewardSpeech2 = 'YOU STINK!!!!!!!'
BossbotRTCongratulations = "You did it!  You've demoted the C.E.O.!\x07Here, take these pink slips the C.E.O. left behind.\x07With it you'll be able to fire Cogs in a battle."
BossbotRTHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
BossbotRTMaxed = '\x07I see that you have a level %s Cog Suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to defend more Toons!'
BossbotRTLastPromotion = "\x07Wow, you've reached level %s on your Cog Suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog Suit anymore, but you can certainly keep working for the Resistance!"
BossRTKeyReward = '\x07By the way, thanks to your exquisite performance, the Toon Council has decided to offer to you a Cog Nation Crate key!\x07Using this, you will be able to open the crates you have earned in the cog factories.'
GolfAreaAttackTaunt = 'AHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
OvertimeAttackTaunts = ["You asked for it, time to disable room A.", "You have nothing, room B is going bye bye!"]
ElevatorBossBotBoss = "Darth Noah's House"
ElevatorBossBotCourse0 = 'Easy Room'
ElevatorBossBotCourse1 = 'Medium Room'
ElevatorBossBotCourse2 = 'Hard Maze'
ElevatorCashBotBoss = 'Carebot Kindness'
ElevatorCashBotMint0 = 'Cheap Mint'
ElevatorCashBotMint1 = 'Expensive Mint'
ElevatorCashBotMint2 = 'Finance Mint'
ElevatorSellBotBoss = 'Fashionbot Designers Mall'
ElevatorSellBotFactory0 = 'Factory Entrance'
ElevatorSellBotFactory1 = 'Back Entrance'
ElevatorSellBotFactory2 = 'Master Mode Entrance'
ElevatorLawBotBoss = 'DefenderBot Room'
ElevatorLawBotCourse0 = 'Office A'
ElevatorLawBotCourse1 = 'Office B'
ElevatorLawBotCourse2 = 'Office C'
ElevatorLawBotCourse3 = 'Office D'
IceGameTitle = 'Ice Slide'
IceGameInstructions = 'Get as close to the center by the end of the second round. Use arrow keys to change direction and force. Press Ctrl to launch your toon.  Hit barrels for extra points and avoid the TNT!'
IceGameInstructionsNoTnt = 'Get as close to the center by the end of the second round. Use arrow keys to change direction and force. Press Ctrl to launch your toon.  Hit barrels for extra points.'
IceGameInfo = 'Match %(curMatch)d/%(numMatch)d, Round %(curRound)d/%(numRound)d'
IceGameControlKeyWarning = 'Remember to press the Ctrl key!'
PicnicTableJoinButton = 'Join'
PicnicTableObserveButton = 'Observe'
PicnicTableCancelButton = 'Cancel'
PicnicTableTutorial = 'How To Play'
PicnicTableMenuTutorial = 'What game do you want to learn?'
PicnicTableMenuSelect = 'What game do you want to play?'
ChineseCheckersGetUpButton = 'Get Up'
ChineseCheckersStartButton = 'Start Game'
ChineseCheckersQuitButton = 'Quit Game'
ChineseCheckersIts = "It's "
ChineseCheckersYourTurn = 'Your Turn'
ChineseCheckersGreenTurn = "Green's Turn"
ChineseCheckersYellowTurn = "Yellow's Turn"
ChineseCheckersPurpleTurn = "Purple's Turn"
ChineseCheckersBlueTurn = "Blue's Turn"
ChineseCheckersPinkTurn = "Pink's Turn"
ChineseCheckersRedTurn = "Red's Turn"
ChineseCheckersColorG = 'You are Green'
ChineseCheckersColorY = 'You are Yellow'
ChineseCheckersColorP = 'You are Purple'
ChineseCheckersColorB = 'You are Blue'
ChineseCheckersColorPink = 'You are Pink'
ChineseCheckersColorR = 'You are Red'
ChineseCheckersColorO = 'You are Observing'
ChineseCheckersYouWon = 'You just won a game of Chinese Checkers!'
ChineseCheckers = 'Chinese Checkers.'
ChineseCheckersGameOf = ' has just won a game of '
ChineseTutorialTitle1 = 'Objective'
ChineseTutorialTitle2 = 'How to Play'
ChineseTutorialPrev = 'Previous Page'
ChineseTutorialNext = 'Next Page'
ChineseTutorialDone = 'Done'
ChinesePage1 = 'The goal of Chinese Checkers is to be the first  toon to move all of your marbles from the bottom triangle across the board and into the triangle at the top. The first toon to do so wins!'
ChinesePage2 = 'Toons take turns moving any marble of their own color.  A marble can move into an adjacent hole or it can hop over other marbles. Hops must go over a marble and end in an empty hole. It is possible to chain hops together for longer moves!'
CheckersPage1 = 'The goal of Checkers is to leave the opponent without any possible moves. To do this you can either capture all of his peices or block them in such that he has no available moves.'
CheckersPage2 = 'Toons take turns moving any peice of their own color. A peice can move one square diagonal and forward. A peice can only move into a square that is not occupied by another peice. Kings follow the same rules but are allowed to move backwards.'
CheckersPage3 = 'To capture an opponents peice your peice must jump over it diagonally into the vacant square beyond it. If you have any jump moves during a turn, you must do one of them. You can chain jump moves together as long as it is with the same peice.'
CheckersPage4 = 'A peice becomes a king when it reaches the last row on the board. A peice that has just become a king cannot continue jumping until the next turn. Additionally, kings are allowed to move all directions and are allowed to change directions while jumping.'
CheckersGetUpButton = 'Get Up'
CheckersStartButton = 'Start Game'
CheckersQuitButton = 'Quit Game'
CheckersIts = "It's "
CheckersYourTurn = 'Your Turn'
CheckersWhiteTurn = "White's Turn"
CheckersBlackTurn = "Black's Turn"
CheckersColorWhite = 'You are White'
CheckersColorBlack = 'You are Black'
CheckersObserver = 'You are Observing'
RegularCheckers = 'Checkers.'
RegularCheckersGameOf = ' has just won a game of '
RegularCheckersYouWon = 'You just won a game of Checkers!'
GardenDropTitle = 'Garden Drop'
GardenDropExitGame = 'Exit Mini Game'
GardenDropHelpTitle = 'Instructions:'
GardenDropInstructions = "Match the ghost balls with the normal balls! But beware of the cog ball, it will try to block you off!"
GardenDropBackToGame = "Back to Game"
GardenDropButtonTitle = 'Garden\nDrop'
GardenDropCongradulations = 'Super Congratulations!!'
GardenDropProgressLevels = "Click 'Next' to go to the next level!"
GardenDropWinGame = 'You have won the Garden Drop Game!'
GardenDropExit = 'Exit'
MailNotifyNewItems = "You've got mail!"
MailNewMailButton = 'Mail'
MailSimpleMail = 'Note'
MailFromTag = 'Note From: %s'
AwardNotifyNewItems = 'You have a new award in your mailbox!'
AwardNotifyOldItems = 'There are still awards waiting in your mailbox for you to pick up!'
InviteInvitation = 'the invitation'
InviteAcceptInvalidError = 'The invitation is no longer valid.'
InviteAcceptPartyInvalid = 'That party has been cancelled.'
InviteAcceptAllOk = 'The host has been informed of your reply.'
InviteRejectAllOk = 'The host has been informed that you declined the invitation.'
Months = {1: 'JANUARY',
 2: 'FEBRUARY',
 3: 'MARCH',
 4: 'APRIL',
 5: 'MAY',
 6: 'JUNE',
 7: 'JULY',
 8: 'AUGUST',
 9: 'SEPTEMBER',
 10: 'OCTOBER',
 11: 'NOVEMBER',
 12: 'DECEMBER'}
DayNames = ('Monday',
 'Tuesday',
 'Wednesday',
 'Thursday',
 'Friday',
 'Saturday',
 'Sunday')
DayNamesAbbrev = ('MON',
 'TUE',
 'WED',
 'THU',
 'FRI',
 'SAT',
 'SUN')
SummerFireworksStart = 'Celebrate Summer with a fireworks show every hour in each playground!'
SummerFireworksEnd = 'Summer Fireworks are over. Hope you had fun.'
NewYearFireworksStart = 'Happy New Year! Enjoy a fireworks show every hour in each playground!'
NewYearFireworksEnd = 'New Year Fireworks are over. See you next year!'
HolidayNamesInCalendar = {1: ('Summer Fireworks', 'Celebrate Summer with a fireworks show every hour in each playground!'),
 2: ('New Year Fireworks', 'Happy New Year! Enjoy a fireworks show every hour in each playground!'),
 3: ('Halloween', 'Happy Halloween! Trick or treat throughout Toontown to get a nifty Halloween pumpkin head reward!'),
 4: ('Winter Holiday', 'Celebrate the Winter Holiday with Toontastic decorations, party and Cattlelog items, and more!'),
 5: ('Skelecog Invasion', 'Stop the Skelecogs from invading Toontown!'),
 6: ('Mr. Hollywood Invasion', 'Stop the Mr. Hollywood Cogs from invading Toontown!'),
 8: ('Toon Species Election', 'Vote on the new Toon species! Will it be Goat? Will it be Pig?'),
 9: ('Black Cat Day', 'Create a Toontastic Black Cat Toon - today only!'),
 16: ('Grand Prix', 'Grand Prix Monday at Goofy Speedway! To win, collect the most points in three consecutive races!'),
 17: ('Fish Bingo', 'Fish Bingo Wednesday! Everyone at the pond works together to complete the card before time runs out.'),
 18: ('Silly Saturdays', 'Saturdays are silly with Fish Bingo and Grand Prix throughout the day!'),
 24: ('Ides of March', 'Beware the Ides of March! Stop the Backstabber Cogs from invading Toontown!'),
 26: ('Halloween Decor', 'Celebrate Halloween as spooky trees and streetlights transform Toontown!'),
 28: ('Winter Invasion', 'The sellbots are on the loose spreading their cold sales tactics!'),
 29: ("April Toons' Week", "Celebrate April Toons' Week - a holiday built by Toons for Toons!"),
 33: ('Sellbot Surprise 1', 'Sellbot Surprise! Stop the Cold Caller Cogs from invading Toontown!'),
 34: ('Sellbot Surprise 2', 'Sellbot Surprise! Stop the Name Dropper Cogs from invading Toontown!'),
 35: ('Sellbot Surprise 3', 'Sellbot Surprise! Stop the Gladhander Cogs from invading Toontown!'),
 36: ('Sellbot Surprise 4', 'Sellbot Surprise! Stop the Mover & Shaker Cogs from invading Toontown!'),
 37: ('A Cashbot Conundrum 1', 'A Cashbot Conundrum. Stop the Short Change Cogs from invading Toontown!'),
 38: ('A Cashbot Conundrum 2', 'A Cashbot Conundrum. Stop the Penny Pincher Cogs from invading Toontown!'),
 39: ('A Cashbot Conundrum 3', 'A Cashbot Conundrum. Stop the Bean Counter Cogs from invading Toontown!'),
 40: ('A Cashbot Conundrum 4', 'A Cashbot Conundrum. Stop the Number Cruncher Cogs from invading Toontown!'),
 41: ('The Lawbot Gambit 1', 'The Lawbot Gambit. Stop the Bottomfeeder Cogs from invading Toontown!'),
 42: ('The Lawbot Gambit 2', 'The Lawbot Gambit. Stop the Double Talker Cogs from invading Toontown!'),
 43: ('The Lawbot Gambit 3', 'The Lawbot Gambit. Stop the Ambulance Chaser Cogs from invading Toontown!'),
 44: ('The Lawbot Gambit 4', 'The Lawbot Gambit. Stop the Backstabber Cogs from invading Toontown!'),
 45: ('The Trouble With Bossbots 1', 'The Trouble with Bossbots. Stop the Flunky Cogs from invading Toontown!'),
 46: ('The Trouble With Bossbots 2', 'The Trouble with Bossbots. Stop the Pencil Pusher Cogs from invading Toontown!'),
 47: ('The Trouble With Bossbots 3', 'The Trouble with Bossbots. Stop the Micromanager Cogs from invading Toontown!'),
 48: ('The Trouble With Bossbots 4', 'The Trouble with Bossbots. Stop the Downsizer Cogs from invading Toontown!'),
 49: ('Jellybean Day', 'Celebrate Jellybean Day with double Jellybean rewards at parties!'),
 53: ('Cold Caller Invasion', 'Stop the Cold Caller Cogs from invading Toontown!'),
 54: ('Bean Counter Invasion', 'Stop the Bean Counter Cogs from invading Toontown!'),
 55: ('Double Talker Invasion', 'Stop the Double Talker Cogs from invading Toontown!'),
 56: ('Downsizer Invasion', 'Stop the Downsizer Cogs from invading Toontown!'),
 59: ("ValenToon's Day", "Celebrate ValenToon's Day from Feb 09 to Feb 16!"),
 72: ('Yes Men Invasion', 'Stop the Yes Men Cogs from invading Toontown!'),
 73: ('Tightwad Invasion', 'Stop the Tightwad Cogs from invading Toontown!'),
 74: ('Telemarketers Invasion', 'Stop the Telemarketer Cogs from invading Toontown!'),
 75: ('Head Hunter Invasion', 'Stop the Head Hunter Cogs from invading Toontown!'),
 76: ('Spin Doctor Invasion', 'Stop the Spin Doctor Cogs from invading Toontown!'),
 77: ('Moneybags Invasion', 'Stop the Moneybags from invading Toontown!'),
 78: ('Two-faces Invasion', 'Stop the Two-faces from invading Toontown!'),
 79: ('Mingler Invasion', 'Stop the Mingler Cogs from invading Toontown!'),
 80: ('Loan Shark Invasion', 'Stop the Loanshark Cogs from invading Toontown!'),
 81: ('Corporate Raider Invasion', 'Stop the Corporate Raider Cogs from invading Toontown!'),
 82: ('Robber Baron Invasion', 'Stop the Robber Baron Cogs from invading Toontown!'),
 83: ('Legal Eagle Invasion', 'Stop the Legal Eagle Cogs from invading Toontown!'),
 84: ('Big Wig Invasion', 'Stop the Big Wig Cogs from invading Toontown!'),
 85: ('Big Cheese Invasion', 'Stop the Big Cheese from invading Toontown!'),
 86: ('Down Sizer Invasion', 'Stop the Down Sizer Cogs from invading Toontown!'),
 87: ('Mover And Shaker Invasion', 'Stop the Mover and Shaker Cogs from invading Toontown!'),
 88: ('Double Talker Invasion', 'Stop the Double Talkers Cogs from invading Toontown!'),
 89: ('Penny Pincher Invasion', 'Stop the Penny Pinchers Cogs from invading Toontown!'),
 90: ('Name Dropper Invasion', 'Stop the Name Dropper Cogs from invading Toontown!'),
 91: ('Ambulance Chaser Invasion', 'Stop the Ambulance Chaser Cogs from invading Toontown!'),
 92: ('Micro Manager Invasion', 'Stop the Micro Manager Cogs from invading Toontown!'),
 93: ('Number Cruncher Invasion', 'Stop the Number Cruncher Cogs from invading Toontown!'),
 95: ('Victory Parties', 'Celebrate our historic triumph against the Cogs!'),
 96: ('Operation: Storm Sellbot', "Sellbot HQ is open to everyone. Let's go fight the VP!"),
 97: ('Operation: Lawbots Lose', "Lawbot HQ is open to everyone. Let's go fight the CJ!"),
 98: ('Operation: Cashbot Chaos', "Cashbot HQ is open to everyone. Let's go fight the CFO!"),
 99: ('Operation: Besiege Bossbot', "Bossbot HQ is open to everyone. Let's go fight the CEO!"),
 100: ('Double Bean Days - Trolley Games', ''),
 101: ('Double Bean Days - Fishing', ''),
 102: ('Jellybean Week', 'Celebrate Jellybean Week with double Jellybean rewards!'),
 103: ("Top Toons New Year's Day Marathon", "Chances to win every hour! See the What's New Blog for details!"),
 105: ('Toons go GREEN!', 'Toons make a green scene at Green Bean Jeans on Oak Street in Daisy Gardens!'),
 123: ('Day of the Magic Cat', 'Toons gather around to honor the Magic Cat, the creator of the universe!')}
UnknownHoliday = 'Unknown Holiday %d'
HolidayFormat = '%b %d '
HourFormat = '12'
CogdoMemoGuiTitle = 'Memos:'
CogdoMemoNames = 'Barrel-Destruction Memos'
CogdoStomperName = 'Stomp-O-Matic'
BoardroomGameTitle = 'Boardroom Hijinks'
BoardroomGameInstructions = 'The Bossbots are having a meeting to decide what to do with stolen gags. Slide on through and grab as many gag-destruction memos as you can!'
CogdoCraneGameTitle = 'Vend-A-Stomper'
CogdoCraneGameInstructions = 'The Cashbots are using a coin-operated machine to destroy laff barrels. Use the cranes to pick up and throw money bags, in order to prevent barrel destruction!'
CogdoMazeGameTitle = 'Mover & Shaker\nField Office'
CogdoMazeGameInstructions = 'The big Mover & Shaker Cogs have the code to open the door. Defeat them with your water balloons in order to get it!'
CogdoMazeIntroMovieDialogue = (("This is the Toon Resistance! The Movers & Shakers\nhave our Jokes, and they've locked the exit!",), ('Grab water balloons at coolers, and throw them at Cogs!\nSmall Cogs drop Jokes, BIG COGS open the exit.',), ('The more Jokes you rescue, the bigger your Toon-Up\nat the end. Good luck!',))
CogdoMazeGameDoorOpens = 'THE EXIT IS OPEN FOR 60 SECONDS!\nGET THERE FAST FOR A BIGGER TOON-UP'
CogdoMazeGameLocalToonFoundExit = "The exit will open when\nyou've busted all four BIG COGS!"
CogdoMazeGameTimeOut = 'Oh no, time ran out! You lost your jokes.'
CogdoMazeGameTimeAlert = 'Hurry up! 60 seconds to go!'
CogdoMazeGameBossGuiTitle = 'BIG COGS:'
CogdoMazeFindHint = 'Find a Water Cooler'
CogdoMazeThrowHint = "Press 'Ctrl' to throw your water balloon"
CogdoMazeSquashHint = 'Falling objects pop your balloon'
CogdoMazeBossHint = 'Big Cogs take TWO hits to defeat'
CogdoMazeMinionHint = 'Smaller Cogs drop jokes'
CogdoMazeGameElevatorRewardLaff = 'Great job, Toons!\nYou get a Toon-Up from the jokes you saved!'
CogdoFlyingGameTitle = 'Legal Eagle\nField Office'
CogdoFlyingGameInstructions = "Fly through the Legal Eagles' lair. Watch out for obstacles and Cogs along the way, and don't forget to refuel your helicopter!"
CogdoFlyingIntroMovieDialogue = (("You won't ruffle our feathers, Toons! We're destroying barrels of your Laff, and you cannot stop us!", "A flock of Toons! We're crushing barrels of your Laff in our %s, and there's nothing you can do about it!" % CogdoStomperName, "You can't egg us on, Toons! We're powering our offices with your Laff, and you're powerless to stop us!"), ('This is the Toon Resistance! A little bird told me you can use propellers to fly around, grab Barrel Destruction Memos, and keep Laff from being destroyed! Good luck, Toons!', 'Attention Toons! Wing it with a propeller and collect Barrel Destruction Memos to keep our Laff from being stomped! Toon Resistance out!', 'Toon Resistance here! Cause a flap by finding propellers, flying to the Barrel Destruction Memos, and keeping our Laff from being smashed! Have fun!'), ("Squawk! I'm a Silver Sprocket Award winner, I don't need this!", 'Do your best, Toons! You will find us to be quite talon-ted!', "We'll teach you to obey the pecking order, Toons!"))
CogdoFlyingGameFuelLabel = 'Fuel'
CogdoFlyingGameLegalEagleTargeting = 'A Legal Eagle has noticed you!'
CogdoFlyingGameLegalEagleAttacking = 'Incoming Eagle!'
CogdoFlyingGamePickUpAPropeller = 'You need a propeller to fly!'
CogdoFlyingGamePressCtrlToFly = "Press 'Ctrl' to fly up!"
CogdoFlyingGameYouAreInvincible = 'Red Tape protects you!'
CogdoFlyingGameTimeIsRunningOut = 'Time is running out!'
CogdoFlyingGameMinimapIntro = 'This meter shows your progress!\nX marks the finish line.'
CogdoFlyingGameMemoIntro = 'Memos prevent Laff Barrels in\nthe Stomper Room from being destroyed!'
CogdoFlyingGameOutOfTime = 'Oh No! You ran out of time!'
CogdoFlyingGameYouMadeIt = 'Good work, you made it on time!'
CogdoFlyingGameTakingMemos = 'The Legal Eagles took all your memos!'
CogdoBarrelRoomTitle = 'Stomper Room'
CogdoBarrelRoomIntroDialog = 'Good work, Toons! You have haulted the Stomp-O-Matic and are now able to collect some of the stolen Laff barrels, but make sure to hurry before the Cogs come!'
CogdoExecutiveSuiteTitle = 'Executive Suite'
CogdoExecutiveSuiteIntroMessage = "Oh no, they've got the shop keeper!\nDefeat the Cogs and free the captive."
CogdoExecutiveSuiteToonThankYou = 'Thanks for the rescue!\nIf you need help in a fight, use this SOS card to call my friend %s.'
CogdoExecutiveSuiteToonThankYouLawbot = 'Thanks for the rescue!\nThe Lawbots have left behind some sprocket awards that you can use to buy new things in your cattlelog!'
CogdoExecutiveSuiteToonBye = 'Bye!'
SillySurgeTerms = ['Amusing Ascent!',
 'Silly Surge!',
 'Ridiculous Rise!',
 'Giggle Growth!',
 'Funny Fueling!',
 'Batty Boost!',
 'Crazy Climb!',
 'Jolly Jump!',
 'Loony Lift!',
 'Hilarity Hike!',
 'Insanity Increase!',
 'Cracked-Uptick!']
InteractivePropTrackBonusTerms = {0: 'Super Toon-Up!',
 1: '',
 2: '',
 3: '',
 4: 'Super Throw!',
 5: 'Super Squirt!',
 6: ''}
GloveInvalidColorMessage = "That's an unpainted color."
GloveSameColorMessage = "You're already wearing those gloves!"
GloveNoMoneyMessage = "You don't have enough jellybeans!"
GloveMoreMoneyMessage = 'You need %s jellybeans to buy new gloves!'
GloveSuccessMessage = 'Have fun with your new gloves!'
GlovePickColorMessage = 'Feel free to choose!'
GloveGuiTitle = 'Choose a glove color!'
GloveGuiNotice = 'Costs %s jellybeans.'
GloveGuiBuy = 'Buy'
GloveGuiSameColor = 'You already have these!'
LanguageButtonText = 'Language'
LanguageSelectorTitle = 'Choose your language!'
LanguageSelectorCurrent = 'Current language: %s'
LanguageSelectorAvailable = 'Available languages:'
LanguageSelectorBack = 'Back'
LanguageSelectorConfirm = 'Are you sure you want to change your language to %s? This will close your game.'
LanguageSelectorSameLanguage = "You're already using that language!"
CogLevelLabelOn = 'The cog level GUI is on.'
CogLevelLabelOff = 'The cog level GUI is off.'

HouseNames = ("Bungalow", "Tiki", "Teepee", "Castle", "Cupcake", "Cabin")
CatalogPurchaseHouseType = "When you buy a new house type, the current one is replaced by it. To recover the old type, you'll need to buy it back. Continue?"
BugReportButton = 'Report a Bug'
BugReportNotice = 'Attention!\n\nThis button will open a browser which will send you to a third party bug tracker website. This site requires an Ubuntu One account to login. It may ask you to create an account.\n\nAre you sure you want to continue?'
# Buffs

buffIdStrings = {
  0: ('Your movement speed will be slightly increased for the next %d %s.',
      'Reward: Increased movement speed')
}

def getBuffString(buffId, buffTime):
    if buffTime < 60:
        return buffIdStrings[buffId][0] % (buffTime, 'minutes')
    else:
        return buffIdStrings[buffId][0] % (buffTime / 60, 'hours')


def getBuffPosterString(buffId):
    return buffIdStrings[buffId][1]

BoyPetNames = ['Achilles', 'Adolfo', 'Adonis', 'Aesop', 'Agamemnon', 'Ahab', 'Ahmed', 'Ajax', 'Alastair', 'Alberto', 'Alexander', 'Alfonso', 'Alonzo', 'Amadeus', 'Ambrose', 'Andre', 'Angelo', 'Angus', 'Antoine', 'Anton', 'Antonio', 'Archibald', 'Archimedes', 'Arnold', 'Atilla', 'Attaboy', 'Avi', 'Barney', 'Bart', 'Bartleby', 'Basil', 'Baxter', 'Beardsley', 'Beauchamp', 'Beauregard', 'Ben', 'Benny', 'Bernie', 'Billygoat', 'Bluebeard', 'Bo', 'Bogart', 'Bogie', 'Bowser', 'Brando', 'Bruce', 'Bruno', 'Brutus', 'Bubba', 'Buck', 'Buster', 'Butch', 'Cagney', 'Carlton', 'Casanova', 'Casper', 'Cecil', 'Cedric', 'Charlie', 'Chekhov', 'Chico', 'Chief', 'Chip', 'Chuck', 'Chuckie', 'Chucko', 'Clancy', 'Clark', 'Claude', 'Clayton', 'Cliff', 'Clive', 'Clyde', 'Cody', 'Colonel', 'Confucius', 'Conrad', 'Cooper', 'Cowboy', 'Cyril', 'Dagwood', 'Dante', 'Deano', 'Donahue', 'Donatello', 'Drysdale', 'Duke', 'Dweezil', 'Eddie', 'Edgar', 'Edison', 'Eggman', 'Einstein', 'Elmer', 'Elwood', 'Emerson', 'Emmet', 'Errol', 'Ethan', 'Fafnir', 'Farnsworth', 'Felix', 'Fenimore', 'Fenwick', 'Ferdinand', 'Fergus', 'Fido', 'Figaro', 'Filbert', 'Fitzgerald', 'Floyd', 'Frampton', 'Fred', 'Gabriel', 'Garfunkel', 'General', 'Genghis', 'Gershwin', 'Gladiator', 'Gladstone', 'Gorilla', 'Grampa', 'Gramps', 'Groucho', 'Gulliver', 'Gunther', 'Gus', 'Hamlet', 'Harold', 'Harpo', 'Harvey', 'Haseltine', 'Heathcliff', 'Hector', 'Hemingway', 'Hendrix', 'Herbert', 'Hercules', 'Herman', 'Hermes', 'Higgins', 'Hobart', 'Homestar', 'Horace', 'Horatio', 'Horton', 'Houdini', 'Humphrey', 'Ichabod', 'Iggy', 'Ignatius', 'Ignatz', 'Igor', 'Ike', 'Iron Ike', 'Ironside', 'Irving', 'Irwin', 'Isaac', 'Ishmael', 'Ivan', 'Ivanhoe', 'Jack', 'Jake', 'Jasper', 'Jaymo', 'Jerry', 'Jethro', 'Jimmy', 'Jonah', 'Karloff', 'Kasper', 'Keanu', 'Kilroy', 'King', 'Kingfish', 'Kirby', 'Kissinger', 'Lambert', 'Lancelot', 'Lazarus', 'Leonardo', 'Lindbergh', 'Linus', 'Lionel', 'Luigi', 'Macarthur', 'Macbeth', 'Mack', 'Malcolm', 'Mandrake', 'Marcel', 'Marco', 'Mario', 'Marmalade', 'Matador', 'Maurice', 'Maximilian', 'Maxwell', 'Maynard', 'Melville', 'Merlin', 'Michelangelo', 'Milo', 'Moe', 'Morissey', 'Mortimer', 'Mozart', 'Mugsy', 'Muldoon', 'Nabokov', 'Napoleon', 'Narcissus', 'Nelson', 'Nero', 'Nimoy', 'Nimrod', 'Norbert', 'Norman', 'Norris', 'Obadiah', 'Odysseus', 'Ogden', 'Olaf', 'Omar', 'Opie', 'Opus', 'Oswald', 'Othello', 'Otto', 'Pablo', 'Paco', 'Paddington', 'Pancho', 'Paolo', 'Pappy', 'Pavarotti', 'Pavlov', 'Peabody', 'Petey', 'Picasso', 'Pierre', 'Pinkerton', 'Pippin', 'Poindexter', 'Pop', 'Popperton', 'Poseidon', 'Prince', 'Puccini', 'Puck', 'Pugsly', 'Pushkin', 'Quigley', 'Quimby', 'Quincy', 'Reggie', 'Regis', 'Reinhold', 'Rembrandt', 'Renoir', 'Reuben', 'Rex', 'Rhett', 'Ricardo', 'Richter', 'Rocky', 'Roderick', 'Romeo', 'Romulus', 'Roosevelt', 'Rover', 'Rudolph', 'Rudy', 'Rufus', 'Rupert', 'Salvador', 'Sandeep', 'Schubert', 'Scooby', 'Scotty', 'Scruffy', 'Sebastian', 'Seymour', 'Shakespeare', 'Shatner', 'Siegfried', 'Sigmund', 'Simon', 'Sinbad', 'Skyler', 'Snowman', 'Snyder', 'Socrates', 'Sorcerer', 'Spalding', 'Spanky', 'Spencer', 'Spinoza', 'Spock', 'Stallion', 'Steinbeck', 'Stradivarius', 'T Bone', 'Tchaikovsky', 'Terminator', 'Tesla', 'Thaxter', 'Theo', 'Theodore', 'Thessalus', 'Throckmorton', 'Tiberius', 'Tiger', 'Tobias', 'Tolkein', 'Toreador', 'Travis', 'Travolta', 'Triton', 'Ulysses', 'Umberto', 'Victor', 'Vincent', 'Vinnie', 'Virgil', 'Vlad', 'Vladimir', 'Voltaire', 'Vonnegut', 'Wainwright', 'Waldo', 'Waldorf', 'Walter', 'Warhol', 'Watson', 'Wayne', 'Wilbur', 'Wilfred', 'Wilhelm', 'Winston', 'Wiseguy', 'Wolfgang', 'Woodbury', 'Woodrow', 'Wyatt', 'Xanthus', 'Xavier', 'Zeus', 'Zorro']
GirlPetNames = ['Abby', 'Adorabelle', 'Aggie', 'Akiko', 'Allessandria', 'Amaryllis', 'Ambrosia', 'Andrea', 'Anita', 'Annette', 'Annie', 'Antionette', 'April', 'Arabella', 'Ariel', 'Ashley', 'Athena', 'Babette', 'Babs', 'Babydoll', 'Ballerina', 'Beatrice', 'Bertie', 'Beulah', 'Beverly', 'Bianca', 'Blossom', 'Bozette', 'Brittany', 'Buttercup', 'Callalilly', 'Candy', 'Carmen', 'Carnation', 'Cassandra', 'Cece', 'Celeste', 'Chanel', 'Chantilly', 'Charlotte', 'Chelsea', 'Cher', 'Cherry', 'Chickie', 'Chloe', 'Cindy', 'Cinnamon', 'Cissy', 'Claire', 'Clementine', 'Cleopatra', 'Coco', 'Cowgirl', 'Daffodil', 'Dagmar', 'Daisy', 'Daphne', 'Dee Dee', 'Delilah', 'Dixie', 'Dolly', 'Dot', 'Dottie', 'Duchess', 'Edith', 'Electra', 'Elsie', 'Elvira', 'Emerald', 'Europa', 'Fannie', 'Fatima', 'Felicity', 'Fifi', 'Flopsy', 'Flower', 'Funnygirl', 'Gabby', 'Garbo', 'Geranium', 'Gidget', 'Gigi', 'Ginger', 'Goldie', 'Granny', 'Guinevere', 'Gwen', 'Hannah', 'Heidi', 'Henrietta', 'Hera', 'Hermione', 'Hildegard', 'Honey', 'Honeysuckle', 'Hortense', 'Iris', 'Ivy', 'Jade', 'Jaquelin', 'Jasmine', 'Jewel', 'Jo', 'Josephine', 'Joy', 'Juliet', 'June', 'Juniper', 'Kandy', 'Kate', 'Katrina', 'Koko', 'Kornelia', 'Krystal', 'Lacey', 'Lady', 'Lambchop', 'Lapis Lazuli', 'Lassie', 'Laverne', 'Leonora', 'Libby', 'Libra', 'Lilac', 'Lily', 'Lipstick', 'Lisa', 'Lottie', 'Lovebird', 'Lovesong', 'Lucretia', 'Lucy', 'Lulu', 'Luna', 'MK', 'Mabel', 'Magenta', 'Maggie', 'Mamacita', 'Mantissa', 'Maxine', 'Mayflower', 'Medusa', 'Melody', 'Mercedes', 'Meriwether', 'Mermaid', 'Mildred', 'Minerva', 'Missy', 'Mitzi', 'Mocha', 'Molly', 'Mona Lisa', 'Moneypenny', 'Monique', 'Mopsy', 'Nadia', 'Nancy', 'Nannygoat', 'Naomi', 'Nellybelle', 'Nightingale', 'Nikita', 'Odelia', 'Olga', 'Olive', 'Olympia', 'Oona', 'Opal', 'Ophelia', 'Organdy', 'Pandora', 'Patrikia', 'Penelope', 'Penny', 'Petinka', 'Petunia', 'Phoebe', 'Phoenicia', 'Pixie', 'Poinsettia', 'Pookie', 'Precious', 'Prettipaws', 'Primrose', 'Princess', 'Pudgette', 'Queenie', 'Raphael', 'Rapunzel', 'Raquel', 'Rosabelle', 'Rosebud', 'Roxanne', 'Roxy', 'Ruby', 'Sable', 'Sabrina', 'Sadie', 'Saffron', 'Sage', 'Sapphire', 'Sassafras', 'Savannah', 'Scarlett', 'Scheherazade', 'Serenade', 'Sienna', 'Silky', 'Sissy', 'Snoogie', 'Snookie', 'Sonja', 'Sophia', 'Sophie', 'Sorceress', 'Summer', 'Sunbonnet', 'Sunny', 'Sunshine', 'Tabitha', 'Tasha', 'Titania', 'Tootsie', 'Topaz', 'Trixie', 'Truffles', 'Tulip', 'Twiggy', 'Velma', 'Venice', 'Venus', 'Veronica', 'Vicki', 'Victoria', 'Viola', 'Violet', 'Wallflower', 'Winnie', 'Winona', 'Yum Yum', 'Zelda', 'Zsa Zsa']
NeutralPetNames = ['Abner', 'Abracadabra', 'Acacia', 'Ace', 'Admiral', 'Aglet', 'Akimbo', 'Alabaster', 'Alcatraz', 'Alchemy', 'Alfalfa', 'Alien', 'Allegro', 'Alto', 'Amazon', 'Ambassador', 'Amethyst', 'Amnesia', 'Ampersand', 'Anaconda', 'Anchovy', 'Andretti', 'Andromeda', 'Angstrom', 'Animal', 'Antergy', 'Anubus', 'Apogee', 'Apollo', 'Applesauce', 'Apprentice', 'Apricot', 'Aquarius', 'Aramis', 'Archer', 'Arf', 'Argus', 'Argyle', 'Aristotle', 'Arizona', 'Arrow', 'Arsenio', 'Asimov', 'Asparagus', 'Asphalt', 'Astro', 'Atom', 'Augie', 'August', 'Avalanche', 'Avalon', 'Avenger', 'Avis', 'Axel', 'Axle', 'Azalea', 'Aztec', 'Azure', 'Babbit', 'Babble', 'Babbler', 'Baby', 'Babykins', 'Baccarat', 'Backgammon', 'Badger', 'Baggy', 'Bailey', 'Baja', 'Balboa', 'Baldo', 'Baldric', 'Baldy', 'Ballyhoo', 'Bambino', 'Bamboo', 'Bamboozle', 'Bamboozler', 'Banana', 'Bandit', 'Bandito', 'Bangle', 'Banjo', 'Banshee', 'Banzai', 'Barbarian', 'Bargraph', 'Barky', 'Barnacle', 'Barracuda', 'Bashful', 'Bazooka', 'Beaker', 'Bean', 'Beaner', 'Beanstalk', 'Beany', 'Bear', 'Beauty', 'Beaver', 'Beep', 'Beeper', 'Beepy', 'Beethoven', 'Beezneez', 'Begonia', 'Bellyflop', 'Benson', 'Bentley', 'Beppo', 'Bermuda', 'Betatest', 'Bewitched', 'Big Red', 'Big Shot', 'Bigbelly', 'Bigfoot', 'Bijou', 'Bindle', 'Bing', 'Bingo', 'Binky', 'Biscuit', 'Bitsy', 'Bizzy', 'Blackberry', 'Blackbird', 'Blackfoot', 'Blackie', 'Blackjack', 'Blacktop', 'Blanket', 'Blaze', 'Bleary', 'Blimp', 'Blimpo', 'Blimpy', 'Blip Blop', 'Blizzard', 'Blockhead', 'Blondie', 'Blooper', 'Blorange', 'Blot', 'Blotto', 'Bluebell', 'Blueberry', 'Bluegrass', 'Bluenose', 'Blueprint', 'Blunder', 'Blurp', 'Boa', 'Bobbin', 'Bobo', 'Bobtail', 'Bodyguard', 'Boggs', 'Bojangles', 'Bolt', 'Bombshell', 'Bonbon', 'Bones', 'Bongo', 'Bonkers', 'Bono', 'Bonsai', 'Boo Boo', 'Boober', 'Boogeyman', 'Boom Boom', 'Boomer', 'Boots', 'Borax', 'Borg', 'Bosco', 'Bottlecap', 'Bottlenose', 'Boulder', 'Bounce Bounce', 'Bouncer', 'Bouncy', 'Bowtie', 'Bowzer', 'Boyd', 'Bozo', 'Brahms', 'Brainchild', 'Bratwurst', 'Bravo', 'Briar', 'Brie', 'Broadway', 'Broccoli', 'Bronco', 'Brooklyn', 'Brouhaha', 'Brownie', 'Bruiser', 'Bubblegum', 'Bubbles', 'Bubo', 'Buccaneer', 'Buckaroo', 'Buckeye', 'Buckingham', 'Buckle', 'Buckshot', 'Buckskin', 'Buckwheat', 'Budapest', 'Buddy', 'Buffalo', 'Buffoon', 'Bug', 'Bugaboo', 'Bugeye', 'Bugsy', 'Bullet', 'Bullwinkle', 'Bumblebee', 'Bumbler', 'Bumper', 'Bumpkin', 'Bumpus', 'Bumpy', 'Bungee', 'Bunko', 'Bunyan', 'Burbank', 'Butterball', 'Butterscotch', 'Buzz', 'Buzzard', 'Buzzy', 'Byte', 'Caboodle', 'Caboose', 'Cadbury', 'Cadet', 'Caesar', 'Calculus', 'Calico', 'Callisto', 'Calypso', 'Calzone', 'Cambridge', 'Camelot', 'Camembert', 'Cameo', 'Campbell', 'Canoe', 'Cap', 'Cappy', 'Capricorn', 'Captain', 'Caramba', 'Caramel', 'Cargo', 'Carlos', 'Carpool', 'Caruso', 'Casablanca', 'Casbah', 'Casey', 'Cashmere', 'Cassidy', 'Castaway', 'Catamaran', 'Caviar', 'Cayenne', 'Cerebro', 'Cha Cha', 'Challenger', 'Chamberlain', 'Chamomile', 'Champ', 'Chaos', 'Charade', 'Charcoal', 'Charger', 'Charmed', 'Chaser', 'Chasm', 'Checkers', 'Cheesecake', 'Cheesy', 'Cheetah', 'Chester', 'Chewie', 'Chicory', 'Chiffon', 'Chigger', 'Chili', 'Chili Bean', 'Chipmunk', 'Chipper', 'Chips', 'Chocolate', 'Choo Choo', 'Chopin', 'Chopper', 'Chops', 'Chopsticks', 'Chowder', 'Chowderhead', 'Chromium', 'Chubby', 'Chuckles', 'Chutzpah', 'Cinder', 'Citrus', 'Clipper', 'Cloud', 'Cloudy', 'Clover', 'Clue', 'Clueless', 'Clunky', 'Coach', 'Cobol', 'Cobra', 'Cocoa', 'Coconut', 'Cola', 'Colorado', 'Comet', 'Comma', 'Confetti', 'Connecticut', 'Cookie', 'Cooter', 'Copper', 'Coral', 'Corduroy', 'Corky', 'Cornball', 'Corncob', 'Cornelia', 'Cornmo', 'Corny', 'Corona', 'Coronet', 'Cosmo', 'Cottontail', 'Couscous', 'Coyote', 'Crackers', 'Cranberry', 'Crash', 'Crawdad', 'Creamy', 'Creeper', 'Creepy', 'Crescent', 'Cricket', 'Critter', 'Croissant', 'Crouton', 'Crufty', 'Cruiser', 'Crumb', 'Crumbly', 'Cruncher', 'Crunchy', 'Cucamonga', 'Cucaracha', 'Cuckoo', 'Cucumber', 'Cuddles', 'Cupcake', 'Cupid', 'Curmudgeon', 'Curry', 'Cutie', 'Cutie Pie', 'Cypress', 'DJ', 'Dakota', 'Dali', 'Damascus', 'Dancer', 'Dandelion', 'Danger', 'Database', 'Dazzle', 'Dazzler', 'Dazzy', 'December', 'Delaware', 'Delphi', 'Detonator', 'Detour', 'Detroit', 'Deuce', 'Dewfall', 'Diamond', 'Dice', 'Diego', 'Digby', 'Digger', 'Digit', 'Dimples', 'Dingo', 'Dingus', 'Dinky', 'Divot', 'Dizzy', 'Doc', 'Dodger', 'Dodo', 'Dolby', 'Donut', 'Doodad', 'Doodah', 'Doodle', 'Draco', 'Dracula', 'Drawers', 'Dreadnought', 'Dream', 'Dreamer', 'Dreamweaver', 'Dreamy', 'Drippy', 'Droopy', 'Drummer', 'Dumpling', 'Durango', 'Dustmop', 'Dynamite', 'Dynamo', 'Eagle', 'Ebony', 'Eccentric', 'Echo', 'Eclipse', 'Ecstatic', 'Edge', 'Egad', 'Egghead', 'Eggnog', 'Eggtoss', 'Egypt', 'Elderberry', 'Electron', 'Elf', 'Elijah', 'Elvis', 'Email', 'Ember', 'Encore', 'Enoch', 'Epcot', 'Epic', 'Epilog', 'Equinox', 'Ergo', 'Escapade', 'Eskimo', 'Espresso', 'Euclid', 'Euphoria', 'Euphrates', 'Excalibur', 'Exeter', 'Eyespy', 'Faberge', 'Fable', 'Facepuff', 'Fahrenheit', 'Fairbanks', 'Fairfax', 'Faith', 'Faithful', 'Fajita', 'Falafel', 'Falcon', 'Fancy', 'Fandango', 'Fang', 'Fangtastic', 'Fantasia', 'Fats', 'Fatso', 'Fatty', 'Faust', 'Fax', 'Fearless', 'Feather', 'Feedback', 'Fellini', 'Ferrari', 'Fester', 'Fetch', 'Fiddler', 'Fiddlesticks', 'Fiesta', 'Filibuster', 'Fingerprint', 'Fingers', 'Fink', 'Fishbone', 'Fishface', 'Fishhook', 'Fizz', 'Fizzle', 'Fizzy', 'Flabby', 'Flagpole', 'Flame', 'Flannel', 'Flapjack', 'Flash', 'Flatfoot', 'Flicker', 'Fling', 'Flip', 'Flipper', 'Flop', 'Flopper', 'Floppy', 'Florida', 'Fluffster', 'Fluffy', 'Flurry', 'Flute', 'Fog', 'Fogarty', 'Fondue', 'Fortran', 'Fox', 'Foxy', 'Frankfurter', 'Freckles', 'Freebie', 'Freezerburn', 'French Toast', 'Friday', 'Frogface', 'Frogmar', 'Frost', 'Frosty', 'Fruitcake', 'Frump', 'Frumpson', 'Frumpy', 'Fudd', 'Fuddles', 'Fudge', 'Fugitive', 'Fuji', 'Fungus', 'Funky', 'Furball', 'Furface', 'Fusebox', 'Fuzzball', 'Fuzzy', 'Fuzzyface', 'Fuzzykins', 'Gabardine', 'Galaxy', 'Gallop', 'Gambit', 'Gambler', 'Gangway', 'Garlic', 'Garlicbreath', 'Garnet', 'Garth', 'Gavotte', 'Gecko', 'Geewhiz', 'Gem', 'Gemini', 'Gerbil', 'Gewgaw', 'Ghost', 'Giddyup', 'Giggles', 'Gingerbread', 'Gingersnap', 'Glick', 'Gnash', 'Gnasher', 'Gnocchi', 'Gnome', 'Gobbledegook', 'Gobbler', 'Goblet', 'Goblin', 'Gobo', 'Gogo', 'Goiter', 'Goliath', 'Gomer', 'Goober', 'Gooch', 'Gooey', 'Googol', 'Goose', 'Gooseberry', 'Goosebump', 'Gopher', 'Gouda', 'Governor', 'Gracie', 'Graffiti', 'Graham', 'Granite', 'Granola', 'Gravlax', 'Gremlin', 'Grep', 'Grok', 'Grue', 'Grumpus', 'Grumpy', 'Grungy', 'Guffaw', 'Gumbo', 'Gumdrop', 'Gump', 'Gumpus', 'Gumshoe', 'Gypsy', 'Gyro', 'Haggis', 'Haha', 'Hairball', 'Half Pint', 'Halibut', 'Halifax', 'Halloweenie', 'Halo', 'Halogen', 'Hambone', 'Hamburger', 'Hammer', 'Hammerhead', 'Hammerstein', 'Hammy', 'Hamster', 'Happy', 'Harlequin', 'Harley', 'Harmonica', 'Harmony', 'Harvard', 'Havoc', 'Hawk', 'Hawkeye', 'Hayseed', 'Haywire', 'Hazel', 'Heartbreaker', 'Heathrow', 'Heckler', 'Hedgehog', 'Heehee', 'Hemlock', 'Herringbone', 'Hiccup', 'Hifi', 'Hip Hip', 'Hippo', 'Hippodrome', 'Hoagie', 'Hobo', 'Hoho', 'Holmes', 'Honeybee', 'Hooligan', 'Hoops', 'Hoosier', 'Horoscope', 'Hot Dog', 'Hotfoot', 'Hotshot', 'Houston', 'Howard', 'Huckleberry', 'Huffy', 'Huggy', 'Hugo', 'Humdinger', 'Humdrum', 'Hurricane', 'Hydraulic', 'Hypnos', 'IOU', 'Iapyx', 'Ibex', 'Icarus', 'Icky', 'Icon', 'Icy', 'Idiom', 'Idlewild', 'Igloo', 'Iguana', 'Illogical', 'Illusion', 'Imagine', 'Imp', 'Impy', 'Imus', 'Indigo', 'Indy', 'Inferno', 'Infinity', 'Infrared', 'Ingot', 'Inkblot', 'Inkwell', 'Innie', 'Input', 'Insomnia', 'Intro', 'Iodine', 'Iota', 'Itchy', 'Ivory', 'Izzat', 'Izzy', 'Jabber', 'Jabberwock', 'Jackaroo', 'Jackhammer', 'Jackpot', 'Jackrabbit', 'Jacuzzi', 'Jag', 'Jaguar', 'Jalapeno', 'Jambalaya', 'Jamboree', 'January', 'Jargon', 'Java', 'Jaws', 'Jaybird', 'Jester', 'Jet', 'Jicko', 'Jiffy', 'Jigsaw', 'Jimjam', 'Jingle', 'Jinx', 'Jitterbug', 'Jocko', 'Jojo', 'Joker', 'Jokester', 'Joliet', 'Joplin', 'Jordie', 'Jove', 'Joyride', 'Jubilee', 'Jughead', 'Jujitsu', 'Jukebox', 'July', 'Jumbo', 'Jumpy', 'Junior', 'Juno', 'Kabob', 'Kabuki', 'Kafka', 'Kahuna', 'Kalamazoo', 'Kaleidoscope', 'Kalmuk', 'Kansas', 'Kappa', 'Karamazov', 'Karate', 'Karma', 'Katmandu', 'Katsumi', 'Kayak', 'Keepsake', 'Kellogg', 'Kelvin', 'Ketchup', 'Kewpie', 'Keyboard', 'Keyring', 'Khaki', 'Kibbles', 'Kiddo', 'Kielbasa', 'Kilimanjaro', 'Kilowatt', 'Kimono', 'Kinetic', 'Kipling', 'Kismet', 'Kissyface', 'Kitten', 'Klinger', 'Klondike', 'Kludge', 'Klute', 'Klutz', 'Klutzy', 'Knickerbocker', 'Knievel', 'Knish', 'Knock Knock', 'Knockwurst', 'Knoop', 'Knucklebone', 'Knuckles', 'Koala', 'Kodiak', 'Kong', 'Kookaburra', 'Kooky', 'Kool Beanz', 'Kornball', 'Kosmix', 'Krakatoa', 'Kramer', 'Krispy', 'Krooner', 'Lab Rat', 'Labyrinth', 'Lacquer', 'Laddie', 'Ladybug', 'Lambada', 'Lamborghini', 'Lampoon', 'Lamster', 'Landmark', 'Landshark', 'Lanky', 'Lapper', 'Laptop', 'Lasagna', 'Laser', 'Latex', 'Lava', 'Lava Lamp', 'Lavender', 'Layaway', 'Leafy', 'Leaky', 'Lefty', 'Legend', 'Lemming', 'Lemonade', 'Lentil', 'Lettuce', 'Lexy', 'Lickety Split', 'Lickums', 'Licky', 'Licorice', 'Lightning', 'Lima', 'Limbo', 'Limey', 'Linguini', 'Link', 'Lintball', 'Lionheart', 'Lithgow', 'Litmus', 'Littlefoot', 'Liverpool', 'Liverwurst', 'Lizard', 'Lobo', 'Lofty', 'Logan', 'Logical', 'Lollipop', 'London', 'Longfellow', 'Longshot', 'Loofah', 'Looney', 'Loopy', 'Lotus', 'Luau', 'Lucky', 'Ludwig', 'Lullaby', 'Lumpy', 'Lunatic', 'Lynx', 'Lyrical', 'Macaroni', 'Macaroon', 'Macho', 'Macintosh', 'Mackerel', 'Mad Max', 'Madison', 'Maestro', 'Mage', 'Magic', 'Magma', 'Magnet', 'Magnolia', 'Magnus', 'Magoo', 'Magpie', 'Mahogany', 'Majestic', 'Malibu', 'Mambo', 'Mango', 'Manhattan', 'Manitoba', 'Mantra', 'Maple Syrup', 'Maraschino', 'Marathon', 'Mariachi', 'Marquee', 'Marshmallow', 'Martian', 'Marzipan', 'Mascot', 'Matchmaker', 'Matzoh', 'Maverick', 'Max', 'Maybe', 'Mayhem', 'Mazy', 'Meanie', 'Meatball', 'Meatloaf', 'Melange', 'Melbourne', 'Mellifluent', 'Melrose', 'Memo', 'Memphis', 'Menthol', 'Meow Meow', 'Meringue', 'Mesopotamia', 'Mesquite', 'Meta', 'Metric', 'Metro', 'Mezzo', 'Miami', 'Microfilm', 'Microwave', 'Midas', 'Midget', 'Midnight', 'Mikado', 'Milestone', 'Milkshake', 'Minty', 'Minuet', 'Minus', 'Mischief', 'Misery', 'Mist', 'Misty', 'Mittens', 'Mo', 'Mobius', 'Modesta', 'Mohair', 'Mohawk', 'Mojo', 'Molasses', 'Mole', 'Molecule', 'Monday', 'Mongoose', 'Monkey', 'Monogram', 'Montgomery', 'Monty', 'Moocher', 'Moochie', 'Moonbeam', 'Moondancer', 'Moondoggie', 'Moonmist', 'Moose', 'Mooshoo', 'Moptop', 'Mork', 'Morocco', 'Mosaic', 'Moscow', 'Motley', 'Moustache', 'Moxie', 'Mudpie', 'Muffin', 'Mulberry', 'Mumbles', 'Mumford', 'Mumpy', 'Munchkin', 'Murphy', 'Mushmouth', 'Mushroom', 'Mustang', 'Mustard', 'Mutt', 'Muttzie', 'Mylar', 'Nacho', 'Nameless', 'Nardek', 'Nashville', 'Naugahyde', 'Navel', 'Naxos', 'Nectarine', 'Ned', 'Needle', 'Needler', 'Needles', 'Nehru', 'Neon', 'Neptune', 'Network', 'Neuron', 'Neutron', 'Nevada', 'Newt', 'Newton', 'Niagara', 'Nibbler', 'Nibbles', 'Nibbly', 'Niccolo', 'Nickel', 'Nifty', 'Niftykins', 'Nightmare', 'Nim', 'Nimbus', 'Nitro', 'Nix', 'Nixy', 'Noisemaker', 'Nomad', 'Noname', 'Noodles', 'Nooly', 'Norbie', 'Nostrildamus', 'Nosy', 'November', 'Nugget', 'Numbers', 'Nutmeg', 'Oasis', 'Oatcake', 'Oatmeal', 'Oberon', 'Oblong', 'Oboe', 'Obsession', 'Octagon', 'October', 'Oddjob', 'Odzanends', 'Offbeat', 'Ogee', 'Ohio', 'Oink Oink', 'Oinker', 'Okeedoke', 'Okra', 'Oleander', 'Omega', 'Omelet', 'Onion', 'Onionbreath', 'Onionhead', 'Ono', 'Onomatopoeia', 'Onyx', 'Oozy', 'Opaque', 'Opossum', 'Orangeade', 'Orbit', 'Orchid', 'Oregano', 'Original', 'Oriole', 'Orlando', 'Oroonoko', 'Orpheus', 'Orville', 'Oscar', 'Osmosis', 'Ostrich', 'Outie', 'Outlaw', 'Outlet', 'Outrageous', 'Owl', 'Ox', 'Oyster', 'Ozzie', 'PJ', 'Pacemaker', 'Pachyderm', 'Padlock', 'Pagoda', 'Paisley', 'Paladin', 'Palomino', 'Panache', 'Panda', 'Pandemonium', 'Panfried', 'Pantaloon', 'Panther', 'Paprika', 'Papyrus', 'Parachute', 'Paradise', 'Parakeet', 'Parallax', 'Paris', 'Parmesan', 'Parsley', 'Parsnip', 'Pascal', 'Pasternak', 'Patches', 'Patchouli', 'Patchwork', 'Patience', 'Pauper', 'Paws', 'Peachy', 'Peanut', 'Pearl', 'Pebbles', 'Pecan', 'Peck Peck', 'Peepers', 'Peewee', 'Pegasus', 'Pele', 'Pendragon', 'Penguin', 'Peoria', 'Pepper', 'Peppermint', 'Pepperoni', 'Peppy', 'Percival', 'Periwinkle', 'Peroxide', 'Persephone', 'Perseus', 'Persnickety', 'Pesto', 'Pesty', 'Petra', 'Petros', 'Pettibones', 'Phantom', 'Philadelphia', 'Phoenix', 'Phynotaprox', 'Piano', 'Piccolo', 'Pickles', 'Pickwick', 'Pico', 'Piecewise', 'Pigpen', 'Pilaf', 'Pimento', 'Ping', 'Ping Pong', 'Pip', 'Pipsqueak', 'Pistachio', 'Piston', 'Pitabread', 'Pixel', 'Pizza', 'Pizzazz', 'Plato', 'Plumb Bob', 'Plumpy', 'Plunko', 'Pluto', 'Pocket', 'Poco', 'Poe', 'Pointer', 'Pointy', 'Pokey', 'Polaris', 'Polifax', 'Pollywog', 'Poltergeist', 'Pom Pom', 'Poofball', 'Poofy', 'Popcorn', 'Poppy', 'Porcupine', 'Porkchop', 'Portobello', 'Postcard', 'Potbelly', 'Potpie', 'Potzy', 'Pouncer', 'Powder', 'Prancer', 'Preston', 'Pretzel', 'Priscilla', 'Prissy', 'Procyon', 'Prodigy', 'Proton', 'Providence', 'Prowler', 'Proxy', 'Pudding', 'Puddles', 'Pudgy', 'Puff', 'Puffball', 'Puffin', 'Puffy', 'Pugnose', 'Pumpernickel', 'Pumpkin', 'Punch', 'Punky', 'Puree', 'Purrfect', 'Pygmy', 'Pyrex', 'Python', 'Quack Quack', 'Quagmire', 'Quartz', 'Quasar', 'Quasi', 'Queasy', 'Quenby', 'Quesadilla', 'Quester', 'Quetzal', 'Quibbler', 'Quicksand', 'Quicksilver', 'Quinn', 'Quippy', 'Quiqui', 'Quirky', 'Quixote', 'Quizzical', 'Quizzix', 'Rabbit', 'Raccoon', 'Racecar', 'Rachel', 'Radar', 'Radcliffe', 'Radish', 'Radium', 'Radix', 'Radman', 'Raffle', 'Ragamuffin', 'Ragdoll', 'Ragmop', 'Rags', 'Ragtime', 'Ragweed', 'Rainbow', 'Rainstorm', 'Rainwater', 'Raisin', 'Rambler', 'Ramrod', 'Ranger', 'Rascal', 'Raspberry', 'Rathbone', 'Rattler', 'Raven', 'Ravioli', 'Rawhide', 'Raymond', 'Razzmatazz', 'Reactor', 'Recall', 'Recycler', 'Redwood', 'Relay', 'Relic', 'Relish', 'Renegade', 'Repeat', 'Rescuer', 'Retread', 'Rewind', 'Rhapsody', 'Rhinestone', 'Rhino', 'Rhymer', 'Rhythm', 'Ribbons', 'Rickrack', 'Ricochet', 'Riddler', 'Riddles', 'Riffraff', 'Rigatoni', 'Righty', 'Ringleader', 'Ringo', 'Riot', 'Ripley', 'Ripple', 'Ripples', 'Risky', 'Ritz', 'Ritzy', 'Roamer', 'Robin', 'Rocco', 'Rocket', 'Rockhead', 'Rockwell', 'Rococo', 'Rogue', 'Rolex', 'Rollo', 'Roly Poly', 'Ronno', 'Rookie', 'Rooster', 'Roscoe', 'Rosebug', 'Rothchild', 'Rowf', 'Rowser', 'Ruffles', 'Ruggelah', 'Ruggles', 'Rumba', 'Runaway', 'Runt', 'Rushmore', 'Rusty', 'Sabotage', 'Safari', 'Saga', 'Saggy', 'Sagittarius', 'Sahara', 'Salamander', 'Salazar', 'Salinger', 'Salisbury', 'Salsa', 'Salty', 'Sam', 'Samba', 'Sammy', 'Samson', 'Samurai', 'Sandman', 'Sandy', 'Santana', 'Santiago', 'Sasha', 'Sashimi', 'Sasquatch', 'Sassy', 'Satchel', 'Satire', 'Saturn', 'Saucer', 'Saucy', 'Sausage', 'Savage', 'Saxophone', 'Scallop', 'Scamp', 'Scamper', 'Scandal', 'Scarecrow', 'Scary', 'Schlemmer', 'Schmooze', 'Schnook', 'Schnookie', 'Scone', 'Scoops', 'Scoot', 'Scooter', 'Scorpio', 'Scorpion', 'Scoundrel', 'Scout', 'Scrabble', 'Scrambler', 'Scrappy', 'Scrooge', 'Scrumptious', 'Scupper', 'Seagull', 'Seismic', 'Seltzer', 'Seneca', 'September', 'Sepulveda', 'Serengeti', 'Shackles', 'Shamrock', 'Shangri La', 'Sharky', 'Shazam', 'Sheba', 'Shelby', 'Sheldrake', 'Shelley', 'Shelton', 'Shenanigan', 'Shep', 'Sherbet', 'Sherlock', 'Sherwood', 'Shiny', 'Shmunday', 'Shoeless', 'Shogun', 'Shortcake', 'Shortstack', 'Shortstop', 'Shorty', 'Showboat', 'Showoff', 'Shredder', 'Shrimpy', 'Shylock', 'Sideshow', 'Sideways', 'Sidney', 'Silhouette', 'Silverspoon', 'Siren', 'Skeet', 'Skeeter', 'Skelton', 'Skidder', 'Skidoo', 'Skidsy', 'Skinky', 'Skipper', 'Skippy', 'Skunk', 'Skunkmuffin', 'Skunky', 'Sky', 'Skyrocket', 'Slappy', 'Slate', 'Slick', 'Slicker', 'Slippers', 'Sloth', 'Slothful', 'Slugger', 'Sly', 'Smarty', 'Smartypants', 'Smash', 'Smasher', 'Smilestone', 'Smocks', 'Smoke', 'Smoky', 'Smoocher', 'Smoothie', 'Smores', 'Smug', 'Snaggletooth', 'Snapdragon', 'Snappy', 'Snaps', 'Snarly', 'Sneaker', 'Sneakers', 'Sneezer', 'Sneezy', 'Snickers', 'Sniffer', 'Sniffler', 'Sniffles', 'Sniffy', 'Snooker', 'Snookums', 'Snooper', 'Snoots', 'Snooty', 'Snowball', 'Snowberry', 'Snowbunny', 'Snowcap', 'Snowflake', 'Snowpea', 'Snowshoe', 'Snowy', 'Snuffles', 'Snuffy', 'Snugglepot', 'Snuggles', 'Socks', 'Sodapop', 'Soho', 'Sojourner', 'Solo', 'Sonar', 'Sorbet', 'Souffle', 'Soupbowl', 'Soupy', 'Sourball', 'Sourdough', 'Southpaw', 'Spacey', 'Spades', 'Spaghetti', 'Spam', 'Sparkler', 'Sparkplug', 'Sparky', 'Sparrow', 'Sparx', 'Speck', 'Speckles', 'Spectro', 'Spectrum', 'Speedy', 'Spex', 'Sphinx', 'Spicy', 'Spider', 'Spiffy', 'Spike', 'Spiky', 'Spinach', 'Spinner', 'Spiral', 'Spirit', 'Spiro', 'Spitfire', 'Splash', 'Splashy', 'Spoiler', 'Spoof', 'Spooky', 'Sport', 'Sporty', 'Spot', 'Spots', 'Spotty', 'Spring', 'Springbok', 'Springy', 'Sprinkle', 'Sprinkles', 'Spud', 'Spunky', 'Sputnik', 'Spy', 'Squash', 'Squeak', 'Squeaky', 'Squid', 'Squiddly', 'Squidface', 'Squiggle', 'Squiggly', 'Squishy', 'Stalactite', 'Stalagmite', 'Starbuck', 'Stardust', 'Starfire', 'Stargazer', 'Starlight', 'Steamy', 'Steely', 'Stereopsis', 'Sterling', 'Stethoscope', 'Stetson', 'Stewart', 'Sticky', 'Stinger', 'Stingy', 'Stinkwell', 'Stinky', 'Stony', 'Storm', 'Stormy', 'Stowaway', 'Strange', 'Strawberry', 'Strep', 'Stretch', 'Stretchy', 'Stripe', 'Striper', 'Stripes', 'Strudel', 'Stubby', 'Stumpy', 'Sudsy', 'Suede', 'Sugar', 'Sugarbaby', 'Sulfur', 'Sultan', 'Sumo', 'Sundance', 'Sundown', 'Sunflower', 'Sunset', 'Superdoodle', 'Surprise', 'Sushi', 'Swabbie', 'Swampy', 'Sweathog', 'Sweetheart', 'Sweetie Pie', 'Sweetness', 'Sweets', 'Swift', 'Swifty', 'Swizzle', 'Sylvester', 'Synergy', 'Syrup', 'TNT', 'Tablespoon', 'Tabloid', 'Taboo', 'Tacky', 'Taco', 'Tacos', 'Tadpole', 'Taffeta', 'Taffy', 'Tagalong', 'Tags', 'Tahiti', 'Taj', 'Takeout', 'Talisman', 'Tallahassee', 'Tallulah', 'Talon', 'Tamale', 'Tambourine', 'Tandem', 'Tanglewood', 'Tango', 'Tank', 'Tanker', 'Tanner', 'Tantrum', 'Tapestry', 'Tapioca', 'Tapper', 'Tarantula', 'Tardy', 'Target', 'Tarkington', 'Tartan', 'Tasty', 'Tatsu', 'Tatters', 'Tattletale', 'Tattoo', 'Taurus', 'Tawny', 'Taxbreak', 'Taxcut', 'Taxi', 'Taxicab', 'Teacup', 'Teaky', 'Teapot', 'Teaspoon', 'Technicolor', 'Teddy', 'Teehee', 'Teevee', 'Telegram', 'Telepath', 'Telescope', 'Telex', 'Tempest', 'Templeton', 'Tempo', 'Tenderfoot', 'Tennessee', 'Tennisball', 'Tennyson', 'Terence', 'Teriyaki', 'Terror', 'Texas', 'Textbook', 'Thackeray', 'Thaddeus', 'Tharp', 'Tharpo', 'Theoretical', 'Theory', 'Thermos', 'Thickie', 'Thimble', 'Thistle', 'Thorny', 'Thriller', 'Thud', 'Thumbtack', 'Thunder', 'Thunderbird', 'Thurgood', 'Thursday', 'Thyme', 'Tickets', 'Tidbit', 'Tilly', 'Tilted', 'Timbuktu', 'Tinkles', 'Tinsel', 'Tintin', 'Tiny', 'Tipperary', 'Tipsy', 'Titanium', 'Tizzy', 'Toad', 'Toadstool', 'Toady', 'Toaster', 'Toby', 'Toco', 'Toffee', 'Tofu', 'Tokyo', 'Toledo', 'Tomato', 'Tomorrow', 'Tonic', 'Toodleoo', 'Toodles', 'Toot', 'Tooter', 'Toothsome', 'Toothy', 'Tootles', 'Toots', 'Topeka', 'Topper', 'Topsy', 'Tornado', 'Torpedo', 'Tortellini', 'Tortoni', 'Totem', 'Toto', 'Totsy', 'Toucan', 'Toupee', 'Toy', 'Toybox', 'Tracer', 'Trailblazer', 'Tramp', 'Trampoline', 'Trancer', 'Trapper', 'Traveller', 'Treasure', 'Treetop', 'Trekker', 'Trickster', 'Trickstick', 'Tricky', 'Trident', 'Trilogy', 'Trinidad', 'Trinket', 'Trio', 'Tripper', 'Troll', 'Tropix', 'Trouble', 'Trout', 'Trumpet', 'Trusty', 'Tsunami', 'Tuba', 'Tubbo', 'Tubby', 'Tuesday', 'Tuffy', 'Tugboat', 'Tumblebumble', 'Tumbler', 'Tumbleweed', 'Tunafish', 'Tundra', 'Turbo', 'Turkey', 'Turnip', 'Turtleneck', 'Tutu', 'Twaddler', 'Twain', 'Tweezer', 'Twerp', 'Twiggs', 'Twilight', 'Twinkle', 'Twirler', 'Twister', 'Twittery', 'Tycoon', 'Typhoon', 'UFO', 'Ubu', 'Ugly', 'Ukelele', 'Ultimate', 'Ultra', 'Ultrasonic', 'Ultra', 'Umber', 'Umbrella', 'Umpire', 'Underfoot', 'Underwood', 'Unicorn', 'Unique', 'Upbeat', 'Upshot', 'Upside', 'Upstart', 'Uptight', 'Urchin', 'Ursula', 'Utoo', 'Utopia', 'Vacuum', 'Vagabond', 'Valentine', 'Valerie', 'Valiant', 'Vamp', 'Vanderbilt', 'Vanilla', 'Vanity', 'Vaudeville', 'Vegas', 'Velvet', 'Venezuela', 'Vermicelli', 'Vermont', 'Vern', 'Vernon', 'Vertigo', 'Vexy', 'Vibes', 'Victrola', 'Video', 'Viking', 'Vinaigrette', 'Vintage', 'Viper', 'Virtuosity', 'Vivian', 'Voodoo', 'Vulcan', 'Vulture', 'Wabble', 'Wabbler', 'Wacky', 'Waddle', 'Waddler', 'Waddles', 'Wafer', 'Waffle', 'Waffler', 'Waffles', 'Wag', 'Waggles', 'Wags', 'Wagtail', 'Wahoo', 'Waikiki', 'Wallaby', 'Wallaroo', 'Walnut', 'Walnuts', 'Walrus', 'Waltzy', 'Wanderer', 'Warthog', 'Warty', 'Wasco', 'Waterberry', 'Watergate', 'Wavy', 'Waxy', 'Weasel', 'Weaver', 'Webster', 'Wedgewood', 'Wedgie', 'Wednesday', 'Weekend', 'Weepy', 'Weezer', 'Weezie', 'Welcome', 'Wellington', 'Wembly', 'Wendy', 'Wesley', 'Whatchamacallit', 'Whatever', 'Wheatcake', 'Wheedler', 'Whim', 'Whimsy', 'Whipple', 'Whirlwind', 'Whisker', 'Whiskers', 'Whisper', 'Whistler', 'Whistlestop', 'Whittaker', 'Whiz', 'Whizzer', 'Wholesale', 'Whoopdedoo', 'Whoopie', 'Wiggle', 'Wiggler', 'Wiggles', 'Wiggly', 'Wildberry', 'Wildcat', 'Wildflower', 'Wildwood', 'Willy', 'Wily', 'Wimbledon', 'Wimpster', 'Wimpy', 'Windjammer', 'Wing', 'Wink', 'Winker', 'Winkle', 'Winkles', 'Winky', 'Winx', 'Wiretap', 'Wisecrack', 'Wispy', 'Wisteria', 'Wizard', 'Wizkid', 'Wobble', 'Wobbler', 'Wobbles', 'Wobbly', 'Wolverine', 'Wonder', 'Wonderbunny', 'Wonton', 'Wooble', 'Woobles', 'Woobly', 'Woodchuck', 'Woodstock', 'Woodwind', 'Woof Woof', 'Woofer', 'Woolly', 'Woolworth', 'Wordsworth', 'Worm', 'Wormy', 'Wrex', 'Wriggler', 'Wriggles', 'Wriggly', 'Wrinkle', 'Wrinkler', 'Wrinkles', 'Wuggums', 'Wumpus', 'Wuzzie', 'Wyoming', 'Xanadu', 'Xenobia', 'Xifto', 'Xinx', 'Xinxu', 'Xippy', 'Xowie', 'Xoxo', 'Xoxxy', 'Xpresso', 'Yahoo', 'Yammie', 'Yancy', 'Yappy', 'Yardstick', 'Yasu', 'Yeasty', 'Yellowstone', 'Yelper', 'Yertle', 'Yesterday', 'Yeti', 'Yippie', 'Yodeler', 'Yoga', 'Yoko', 'Yonder', 'Yonkers', 'Yorty', 'Yosemite', 'Yukon', 'Yummy', 'Yutu', 'Yvonne', 'Zack', 'Zadok', 'Zaftig', 'Zaire', 'Zapata', 'Zappa', 'Zazen', 'Zebu', 'Zebulon', 'Zen', 'Zenith', 'Zenzen', 'Zepellin', 'Zephyr', 'Zeppo', 'Zero', 'Zesty', 'Zigzag', 'Zilch', 'Zillion', 'Zing', 'Zinger', 'Zingy', 'Zipcode', 'Zircon', 'Zodiac', 'Zoltan', 'Zonk', 'Zoo', 'Zooble', 'Zoom', 'Zoomer', 'Zoomy', 'Zowie', 'Zucchini', 'Zylon']
PetNameDictionary = {}
id = 0

for dictionary in [BoyPetNames, GirlPetNames, NeutralPetNames]:
    for name in dictionary:
        PetNameDictionary[id] = name
        id += 1

def getPetName(uniqueID):
    try:
        return PetNameDictionary[uniqueID]
    except:
        return PetNameDictionary[0]

def getRandomPetName(gender = None, seed = None):
    if seed is not None:
        random.seed(seed)

    nameList = list(NeutralPetNames)

    if gender == 0:
        nameList += BoyPetNames
    else:
        nameList += GirlPetNames

    return random.choice(nameList)

def getPetNameId(name):
    for key, value in PetNameDictionary.items():
        if name == value:
            return key

    return 0

DonaldChatter = ["I'm glad you're here today!",
 "You look like you're having fun.",
 "Oh boy, I'm having a good day.",
 'I hope you are enjoying your ride!',
 'I like meeting new people.',
 'Have fun in my neighborhood.',
 'I like to make people laugh.',
 'Watch out for the Cogs!',
 'Come aboard!',
 "I heard it's snowing at the Brrrgh.",
 'Looks like the trolley is coming!',
 'Sometimes I play trolley games just to eat the fruit pie!',
 'I hope you are enjoying your stay in Toontown!',
 'I like what you are wearing.',
 'I love to play tag. Do you?']
NPCFriendUnavailable = 'Unavailable'
FireTalkMessage = "I'm blowing you up to the Moon!"

RestockAskMessage = "Would you like to\nrestock %s laff for %s jellybeans?"
RestockNoMoneyGuiMessage = "\n\x01WLRed\x01Not enough jellybeans\x02"
RestockFullLaffMessage = "You're already happy!"
RestockLessLaffMessage = "Why would you want to be less happy than you are right now?"
RestockNoMoneyMessage = "You don't have enough jellybeans for that!"
RestockSuccessfulMessage = "You're welcome! Have fun!"
InVP = ' in a V.P. Battle'
InFieldOffice = ' in a Sellbot Field Office'
CogPanelLevel = 'Level %s'
CogPanelSkeleton = 'Skeleton'
CogPanelVirtual = 'Virtual'
CogPanelRevives = 'v%s.0'
CogPanelWaiter = 'Waiter'

def convertSecondsToDate(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    return '%d:%02d:%02d' % (h, m, s)

ToonDefeatedMessage = '%s was defeated!'

BugReportButton = 'Report a Bug'
BugReportNotice = 'Attention!\n\nThis button will open a browser which will send you to a third party bug tracker website. This site requires an Ubuntu One account to login. It may ask you to create an account.\n\nAre you sure you want to continue?'

CodeRedemptionWarning = 'NOTICE: All codes can only be entered once!'

CogInterfaceLabelOn = 'The cog battle interface is on.'
CogInterfaceLabelOff = 'The cog battle interface is off.'
TpTransitionLabelOn = 'The teleport transition is on.'
TpTransitionLabelOff = 'The teleport transition is off.'
FieldOfViewLabel = 'Field of View:'
NametagStyleLabel = 'Nametag Style:'
FishingPoleLabel = 'Fishing Rod:'

BossLocations = {
 'c': '',
 'l': "",
 'm': '',
 's': ''
}
SendCogBossTaunts = {
 's': [
  "",
  "",
  '',
  "",
  "",
  '',
  '',
  '',
  ''
 ],
 'm': [
  "",
  "",
  '',
  "",
  "",
  '',
  '',
  "",
  ''
 ],
 'l': [
  '',
  '',
  '',
  '',
  '',
  '',
  "",
  '',
  ''
 ]
}
VPRampMessage = ""
VPDeathTaunt = ""
DirectedAttackBossTaunts = {
 's': [
  "Take this for design!",
  "Don't you get away from me, you need design!",
  "Going without design eh?",
  "I'm right here for you, Toon!"
 ],
 'm': [
  "Get tested!",
  'I am a professional, let me take care of you.',
  "You look like you're diagnosed with School-ness, let me take care of that.",
  'Follow guidelines.'
 ],
 'c': [
  'You get away from that table!',
  "Swing!",
  'Golf puttz.',
  "You're grinding my machines, Toon!"
 ]
}
VPSpinMessages = [
 "Now let's see, where were we?",
 "All non-fashion must go!",
 'Go away.',
 "The Fashion Designer taught me a lot about you."
]
JumpBossTaunts = {
 's': [
  "Jump one, drop one.",
  'Stop!',
  "Blackpink, in your area!",
  'I am sending you right to the backstage!'
 ],
 'l': [
  "I had enough of you!"
 ],
 'm': [
  "I warned you to get away from the cranes!",
  "Step away from the crane this instant!"
 ]
}
CEOSpeech = [
 "",
 '',
 "",
 "",
 '',
 '',
 '',
 '',
 "",
 "",
 '',
 '',
 ""
] # Len of words + 10

CrateRewardMessage1 = 'Nice! You have earned a crate! It will arrive in your mailbox shortly.'
CrateRewardMessage2 = 'You can open it with keys from boss battles.'
CrateRewardMessages = [CrateRewardMessage1, CrateRewardMessage2]
CrateNotOwner = 'Sorry, this is not your crate.'
CrateNoKeys = 'Sorry, but you have no keys. You can find some in the cog facilities.'
CrateAskToUse = 'Would you like to use a key to open this crate?'
CrateBeanPrize = "Congratulations! You found %s jellybeans. They've been automatically added to your jellybean bank!"
CrateBuffPrize = 'Congratulations! %s'
CrateNametagPrize = "Congratulations! You've received a nametag. Check your mailbox to find out which one!"
CrateEmotePrize = "Congratulations! You've unlocked a new emote. Check your mailbox to pick it up!"
CrateClothingPrize = "Congratulations! You've received a new clothing item. Check your mailbox to check it out!"
CrateAccessoryPrize = 'Congratulations! You found a new accessory for your Toon. Check your mailbox and rock it!'

Stats = [
 'Cogs defeated: %s',
 'V2.0 cogs defeated: %s',
 'Skelecogs defeated: %s',
 'Jellybeans spent: %s',
 'Jellybeans earnt: %s',
 'Tasks completed: %s',
 'Total VP defeats: %s',
 'Total CFO defeats: %s',
 'Total CJ defeats: %s',
 'Total CEO defeats: %s',
 'Gone sad: %s times',
 'Buildings liberated: %s',
 'Offices defeated: %s',
 'Items ordered: %s',
 'Fish caught: %s',
 'Flowers picked: %s',
 'Races completed: %s',
 'Golf holes played: %s',
 'Total SOS cards: %s',
 'Total unites: %s',
 'Total pink slips: %s',
 'Total gags used: %s'
]
StatPageTitle = 'Statistics'
StatPageClear = 'Clear'
StatPageClearAsk = 'Are you sure you want to clear your stats? This is an irreversible action!'
StatPageClearDone = 'Your stats have been cleared.'

ChairAskToUse = 'Would you like to sit on this chair?'

FriendSecretIntro = "If you are playing Toontown Stride with someone you know in the real world, you can become True Friends.  You can chat using the keyboard with your True Friends.  Other Toons won't understand what you're saying.\n\nYou do this by getting a True Friend Code.  Tell the True Friend Code to your friend, but not to anyone else.  When your friend types in your True Friend Code on his or her screen, you'll be True Friends in Toontown!"
FriendSecretGetSecret = 'Get a True Friend Code'
FriendSecretEnterSecret = 'If you have a True Friend Code from someone you know, type it here.'
FriendSecretOK = lOK
FriendSecretEnter = 'Enter True Friend Code'
FriendSecretCancel = lCancel
FriendSecretGettingSecret = 'Getting True Friend Code. . .'
FriendSecretGotSecret = "Here is your new True Friend Code.  Be sure to write it down!\n\nYou may give this True Friend Code to one person only.  Once someone types in your True Friend Code, it will not work for anyone else.  If you want to give a True Friend Code to more than one person, get another True Friend Code.\n\nThe True Friend Code will only work for the next three days.  Your friend will have to type it in before it goes away, or it won't work.\n\nYour True Friend Code is:"
FriendSecretTooMany = "Sorry, you can't have any more True Friend Codes today.  You've already had more than your fair share!\n\nTry again tomorrow."
FriendSecretTryingSecret = 'Trying True Friend Code. . .'
FriendSecretEnteredSecretUnknown = "That's not anyone's True Friend Code.  Are you sure you spelled it correctly?\n\nIf you did type it correctly, it may have expired.  Ask your friend to get a new True Friend Code for you (or get a new one yourself and give it to your friend)."
FriendSecretEnteredSecretFullYou = "You can't be True Friends because you have too many friends on your friends list."
FriendSecretEnteredSecretFullHim = "You can't be True Friends because %s has too many friends on his friends list."
FriendSecretAlreadyFriends = 'You are already True Friends!'
FriendSecretAlreadyFriendsName = 'You are already True Friends with %s!'
FriendSecretEnteredSecretSelf = 'You just typed in your own True Friend Code!'
FriendSecretTooFast = 'You are redeeming codes too fast! Please wait a few seconds.'
FriendSecretNowFriends = 'You are now True Friends with %s!'

GroupAskNoAccess = 'Sorry, but you have no teleport access %s %s.\n\nWould you still like to teleport to %s?'
GroupAskNoAccessSame = 'Sorry, but you have no teleport access %s %s.'
GroupAskAccess = 'Would you like to teleport %s %s in %s?'

TVNotOwner = 'Sorry, but this is not your TV.'
TVInvalidVideo = "Sorry, but we can't play that video. Make sure it is a MP4 video."
TVUnknownVideo = "Oops! Looks like the owner has picked a video to play which isn't currently on your computer!"
TVUnknownVideoPack = 'Oops! Looks like the owner has picked a video to play, but you need to download the %s TV Pack in the launcher.'
TVChooseVideo = 'Choose a video to play!'
TVOK = 'The video you selected is now playing!'
TVPacks = ['QuackityHQ']

GagPopup = '%s: %s\nGags: %s'

ColorfulToon = 'Vibrant'
ColorAdvanced = 'Advanced'
ColorBasic = 'Basic'
ColorAll = 'All'

ShardPagePreferred = 'Preferred'
ShardPageShardTitle = '%s Population: %s'
ShardPageTeleport = 'Teleport to\n%s'

TeleportButton = 'Teleport'
TeleportButtonNoMoney = 'Sorry, but you need %s jellybeans to teleport!'
TeleportButtonConfirm = 'Would you like to spend %s jellybeans to teleport?'
TeleportButtonTakenOver = 'Sorry, but this shop has been taken over by the Cogs!'

BattleCogPopup = '\x01androidGreen\x01Group attacks:\x02\n%s\n\n\x01androidGreen\x01Regular attacks:\x02\n%s'
BattleCogPopupAttack = '%s %s HP'
BattleCogPopupAttackDanger = '\x01red\x01' + BattleCogPopupAttack + '\x02'
BattleCogPopupDanger = '\x01red\x01Dangerous!\x02\n\n'
BattleCogPopupDangerColor = '\x01red'

SuitPageAttackFormat = 'Levels: %s-%s\n\n' + BattleCogPopup
SuitPageNoAttacks = 'None'

BattleGagPopup = '%s: %s\nGags left: %s'
BattleSOSPopup = '\x01azure\x01%s\x02\n%s\n%s%s stars\nSOS left: %s'
BattleSOSPopupHeal = 'Heals'
BattleSOSPopupHarm = 'Deals'
BattleSOSPopupHP = '%s %s HP\n'

DetailPanelSOS = 'SOS Cards'

TeleportLabelOn = 'Accepting teleports.'
TeleportLabelOff = 'Not accepting teleports.'
TeleportPanelNoTeleport = '%s needs some time alone right now.'

InventoryDeleteAll = 'DELETE ALL'
InventoryDeleteConfirm = "Are you sure you want to delete all your gags? Don't worry, your level 7 gags are safe!"

ClothesGUICount = '%s/%s'

FpsMeterLabelOn = 'The frame rate meter is on.'
FpsMeterLabelOff = 'The frame rate meter is off.'

DefaultDoodleName = 'Smiley'

Blacklist = [
 "",
 ""
]

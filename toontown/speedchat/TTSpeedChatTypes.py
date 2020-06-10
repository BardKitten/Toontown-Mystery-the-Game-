from TTSCToontaskMenu import TTSCToontaskMenu
from TTSCFactoryMenu import TTSCFactoryMenu
from TTSCCogMenu import TTSCCogMenu
from TTSCToontaskTerminal import TTSCToontaskTerminal
from TTSCResistanceMenu import TTSCResistanceMenu
from TTSCResistanceTerminal import TTSCResistanceTerminal
from TTSCBoardingMenu import TTSCBoardingMenu

if hasattr(base, 'wantPets') and base.wantPets:
    from TTSCPetTrickMenu import TTSCPetTrickMenu

from otp.otpbase import OTPLocalizer
from SCSpecialMenu import SCSpecialMenu

AprilToonsMenu = [
 (OTPLocalizer.AprilToonsMenuSections[1], [30100]),
 (OTPLocalizer.AprilToonsMenuSections[2], [30130, 30131, 30132, 30133]),
 (OTPLocalizer.AprilToonsMenuSections[0], [30140, 30141])
]

GolfMenu = [
 (OTPLocalizer.GolfMenuSections[1], [4100, 4101, 4102, 4103, 4104, 4105]),
 (OTPLocalizer.GolfMenuSections[2], [4200, 4201, 4202, 4203, 4204, 4205, 4206, 4207]),
 (OTPLocalizer.GolfMenuSections[3], [4300, 4301, 4302, 4303, 4304, 4305, 4306, 4307]),
 (OTPLocalizer.GolfMenuSections[0], [4000, 4001, 4002])
]

JellybeanJamMenu = [
 (OTPLocalizer.JellybeanJamMenuSections[0], [30180, 30181, 30182, 30183, 30184, 30185]),
 (OTPLocalizer.JellybeanJamMenuSections[1], [30186, 30187, 30188, 30189, 30190])
]

KartRacingMenu = [
 (OTPLocalizer.KartRacingMenuSections[1], [3130, 3160, 3190, 3170, 3180, 3150, 3110]),
 (OTPLocalizer.KartRacingMenuSections[2], [3200, 3201, 3210, 3211, 3220, 3221, 3222, 3223, 3224, 3225, 3230, 3231, 3232, 3233, 3234, 3235]),
 (OTPLocalizer.KartRacingMenuSections[3], [3600, 3601, 3602, 3603, 3640, 3641, 3642, 3643, 3660, 3661, 3662, 3663]),
 (OTPLocalizer.KartRacingMenuSections[4], [3300, 3301, 3310, 3320, 3330, 3340, 3350, 3360]),
 (OTPLocalizer.KartRacingMenuSections[5], [3410, 3400, 3430, 3450, 3451, 3452, 3453, 3460, 3461, 3462, 3470]),
 (OTPLocalizer.KartRacingMenuSections[0], [3010, 3020, 3030, 3040, 3050, 3060, 3061])
]

SellbotFieldOfficeMenu = [
 (OTPLocalizer.SellbotFieldOfficeMenuSections[1], range(30409, 30419)),
 (OTPLocalizer.SellbotFieldOfficeMenuSections[0], range(30404, 30409))
]

SellbotNerfMenu = [
 (OTPLocalizer.SellbotNerfMenuSections[1], [30157, 30158, 30159, 30160, 30161, 30162, 30163, 30164]),
 (OTPLocalizer.SellbotNerfMenuSections[2], [30165, 30166, 30167, 30168, 30169, 30170, 30171, 30172, 30173, 30174, 30175]),
 (OTPLocalizer.SellbotNerfMenuSections[0], [30150, 30151, 30152, 30153, 30154, 30155, 30156]),
]

SillyPhaseFiveMenu = [
 (OTPLocalizer.SillyHolidayMenuSections[1], [30325, 30326, 30327]),
 (OTPLocalizer.SillyHolidayMenuSections[2], [30328, 30329, 30330, 30331, 30332])
]

SillyPhaseFourMenu = [
 (OTPLocalizer.SillyHolidayMenuSections[1], [30325, 30326, 30327]),
 (OTPLocalizer.SillyHolidayMenuSections[2], [30329, 30330, 30331, 30332])
]

SillyPhaseThreeMenu = [
 (OTPLocalizer.SillyHolidayMenuSections[1], [30323, 30324, 30325, 30326, 30327]),
 (OTPLocalizer.SillyHolidayMenuSections[2], [30318, 30319, 30320, 30321, 30322])
]

SillyPhaseTwoMenu = [
 (OTPLocalizer.SillyHolidayMenuSections[1], [30310, 30311, 30312, 30313, 30314, 30315]),
 (OTPLocalizer.SillyHolidayMenuSections[2], [30316, 30317]),
 (OTPLocalizer.SillyHolidayMenuSections[0], [30309])
]

SillyPhaseOneMenu = [
 (OTPLocalizer.SillyHolidayMenuSections[1], [30303, 30304, 30305, 30306]),
 (OTPLocalizer.SillyHolidayMenuSections[2], [30307, 30308]),
 (OTPLocalizer.SillyHolidayMenuSections[0], [30301, 30302])
]

VictoryPartiesMenu = [
 (OTPLocalizer.VictoryPartiesMenuSections[1], [30350, 30351, 30352, 30353, 30354]),
 (OTPLocalizer.VictoryPartiesMenuSections[2], [30355, 30356, 30357, 30358, 30359, 30360, 30361])
]

WinterMenu = [
 (OTPLocalizer.WinterMenuSections[0], range(30200, 30206)),
 (OTPLocalizer.WinterMenuSections[1], [30275, 30276, 30277])
]

HalloweenMenu = [(OTPLocalizer.HalloweenMenuSections[0], [30250, 30251, 30252, 10003])]
IdesOfMarchMenu = [(OTPLocalizer.IdesOfMarchMenuSections[0], [30450, 30451, 30452])]
SellbotInvasionMenu = [(OTPLocalizer.SellbotInvasionMenuSections[0], range(30400, 30404))]

# SuitGlobals are used to set the appearance of Cogs.
from toontown.suit import SuitDNA
from pandac.PandaModules import VBase4

SCALE_INDEX = 0 # The scale of the cog
HAND_COLOR_INDEX = 1 # The hand color
HEADS_INDEX = 2 # A list of heads
HEAD_TEXTURE_INDEX = 3 # The texture to use for the head
HEIGHT_INDEX = 4 # The height of the cog

aSize = 6.06 # Size of body type 'a'
bSize = 5.29 # Size of body type 'b'
cSize = 4.14 # Size of body type 'c'

ColdCallerHead = VBase4(0.25, 0.35, 1.0, 1.0) # Head used by Cold Caller

            # Bossbots
suitProperties = {'f': (4.0 / cSize, SuitDNA.corpPolyColor, ['gladhander'], '', 4.88),
                  'p': (3.35 / bSize, SuitDNA.corpPolyColor, ['pencilpusher'], '', 5.0),
                  'ym': (4.125 / aSize, SuitDNA.corpPolyColor, ['yesman'], '', 5.28),
                  'mm': (4.5 / bSize, SuitDNA.corpPolyColor, ['downsizer'], '', 5.25),
                  'ds': (4.5 / aSize, VBase4(0.8, 0.7, 0.7, 1.0), ['twoface'], '', 6.08),
                  'hh': (6.5 / bSize, SuitDNA.corpPolyColor, ['telemarketer'], 'spin-doctor.jpg', 7.45),
                  'cr': (6.75 / aSize, VBase4(0.85, 0.55, 0.55, 1.0), ['twoface'], 'halloween_mingler.jpg', 8.23),
                  'tbc': (7.0 / aSize, VBase4(0.75, 0.95, 0.75, 1.0), ['bigcheese'], '', 9.34),
                  # Lawbots
                  'bf': (4.0 / cSize, SuitDNA.legalPolyColor, ['flunky', 'bottom-feeder.jpg'], '', 4.81),
                  'b': (4.375 / bSize, VBase4(0, 0, 0, 0), ['movershaker'], 'halloween_blood-sucker.jpg', 6.17),
                  'dt': (4.25 / aSize, SuitDNA.legalPolyColor, ['yesman'], 'double-talker.jpg', 5.63),
                  'ac': (4.35 / cSize, SuitDNA.legalPolyColor, ['micromanager'], '', 6.39),
                  'bs': (4.5 / bSize, SuitDNA.legalPolyColor, ['beancounter'], '', 6.71),
                  'sd': (5.65 / aSize, VBase4(0.7, 0.7, 0.2, 0.3), ['numbercruncher'], 'software_simian.jpg', 7.9),
                  'le': (7.125 / aSize, VBase4(0, 0, 0, 0), ['legaleagle'], '', 8.27),
                  'bw': (7.0 / aSize, SuitDNA.legalPolyColor, ['bigwig'], '', 8.69),
                  # Cashbots
                  'sc': (3.6 / cSize, SuitDNA.moneyPolyColor, ['coldcaller'], 'conartist.jpg', 4.77),
                  'pp': (3.55 / bSize, VBase4(0, 0, 0, 0), ['telemarketer'], '', 5.26),
                  'tw': (4.5 / aSize, SuitDNA.moneyPolyColor, ['numbercruncher'], 'name-dropper.jpg', 5.41),
                  'bc': (4.4 / bSize, SuitDNA.moneyPolyColor, ['movershaker'], '', 5.95),
                  'nc': (5.25 / aSize, SuitDNA.moneyPolyColor, ['numbercruncher'], '', 7.22),
                  'mb': (5.3 / aSize, SuitDNA.moneyPolyColor, ['twoface'], 'law-keeper.jpg', 6.97),
                  'ls': (6.5 / cSize, VBase4(0, 0, 0, 0), ['flunky'], 'corporate-raider.jpg', 8.58),
                  'rb': (7.0 / aSize, SuitDNA.moneyPolyColor, ['yesman'], 'middleman2.jpg', 8.95),
                  # Sellbots
                  'cc': (3.5 / cSize, VBase4(0.5, 0.4, 0.3, 0.1), ['coldcaller'], '', 4.63),
                  'tm': (3.75 / bSize, VBase4(0.2, 0.1, 0.5, 0.2), ['telemarketer', ''], '', 5.24),
                  'nd': (4.35 / aSize, VBase4(0.55, 0.65, 1.0, 1.0), ['twoface'], 'mingler.jpg', 5.98),
                  'gh': (4.75 / bSize, SuitDNA.salesPolyColor, ['movershaker'], 'installation-wizard.jpg', 6.4),
                  'ms': (4.75 / aSize, SuitDNA.salesPolyColor, ['numbercruncher'], 'halloween_name-dropper.jpg', 6.7),
                  'tf': (5.25 / aSize, SuitDNA.salesPolyColor, ['twoface'], 'middleman.jpg', 6.95),
                  'm': (5.75 / aSize, SuitDNA.salesPolyColor, ['yesman'], 'blood-sucker.jpg', 7.61),
                  'mh': (7.0 / aSize, SuitDNA.salesPolyColor, ['yesman', 'glasses_shades'], '', 8.95),
                  }

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
suitProperties = {'f': (4.0 / cSize, VBase4(1.0, 0, 0, 1.0), ['gladhander'], '', 4.88),
                  'p': (3.35 / bSize, SuitDNA.corpPolyColor, ['pencilpusher'], '', 5.0),
                  'ym': (4.125 / aSize, VBase4(1.0, 1.0, 0, 1.0), ['backstabber'], '', 5.28),
                  'mm': (4.5 / bSize, VBase4(1.0, 0, 0.2, 0.5), ['downsizer'], '', 5.25),
                  'ds': (4.5 / aSize, VBase4(0.8, 0.7, 0.7, 1.0), ['headhunter'], '', 6.08),
                  'hh': (6.5 / bSize, VBase4(0, 1.0, 0, 1.0), ['telemarketer'], 'spin-doctor.jpg', 7.45),
                  'cr': (6.75 / aSize, VBase4(1.0, 0, 0, 1.0), ['twoface'], 'halloween_mingler.jpg', 8.23),
                  'tbc': (7.0 / aSize, VBase4(0.95, 0.95, 1.0, 1.0), ['bigcheese'], '', 9.34),
                  # Lawbots
                  'bf': (4.0 / cSize, SuitDNA.legalPolyColor, ['flunky', 'bottom-feeder.jpg'], '', 4.81),
                  'b': (4.375 / bSize, VBase4(0.95, 0.95, 1.0, 1.0), ['movershaker'], 'halloween_blood-sucker.jpg', 6.17),
                  'dt': (4.25 / aSize, VBase4(1.0, 0.2, 0.4, 0.3), ['yesman'], 'double-talker.jpg', 5.63),
                  'ac': (1.25 / cSize, SuitDNA.legalPolyColor, ['micromanager'], '', 1.89),
                  'bs': (4.5 / bSize, VBase4(0, 1.0, 0.2, 1.0), ['beancounter'], '', 6.71),
                  'sd': (5.65 / aSize, VBase4(1.0, 0, 1.0, 1.0), ['numbercruncher'], 'software_simian.jpg', 7.9),
                  'le': (7.125 / aSize, VBase4(0, 0, 0, 0), ['legaleagle'], '', 8.27),
                  'bw': (7.0 / aSize, SuitDNA.legalPolyColor, ['bigwig'], '', 8.69),
                  # Cashbots
                  'sc': (2.0 / cSize, VBase4(1.0, 1.0, 0, 1.0), ['coldcaller'], 'conartist.jpg', 3.37),
                  'pp': (3.55 / bSize, VBase4(1.0, 0.6, 0.5, 1.0), ['loanshark'], '', 5.26),
                  'tw': (4.5 / aSize, VBase4(0, 1.0, 0, 1.0), ['numbercruncher'], 'name-dropper.jpg', 5.41),
                  'bc': (4.4 / bSize, VBase4(1, 0.6, 0, 1.0), ['movershaker'], '', 5.95),
                  'nc': (5.25 / aSize, VBase4(1.0, 0, 0, 1.0), ['numbercruncher'], '', 7.22),
                  'mb': (5.3 / aSize, VBase4(0, 1.0, 0, 1.0), ['twoface'], 'law-keeper.jpg', 6.97),
                  'ls': (6.5 / cSize, VBase4(0.95, 0.95, 1.0, 1.0), ['flunky'], 'corporate-raider.jpg', 8.58),
                  'rb': (7.0 / aSize, VBase4(1.0, 0, 0, 1.0), ['yesman'], 'middleman2.jpg', 8.95),
                  # Sellbots
                  'cc': (3.5 / cSize, VBase4(0.5, 0.4, 0.3, 0.1), ['coldcaller'], '', 4.63),
                  'tm': (3.75 / bSize, VBase4(0, 1.0, 0, 1.0), ['telemarketer'], '', 5.24),
                  'nd': (4.35 / aSize, VBase4(0.55, 0.65, 1.0, 1.0), ['twoface'], 'mingler.jpg', 5.98),
                  'gh': (4.75 / bSize, VBase4(0.4, 0.1, 0, 0.3), ['movershaker'], 'installation-wizard.jpg', 6.4),
                  'ms': (4.75 / aSize, VBase4(0, 0, 0, 0), ['numbercruncher'], 'halloween_name-dropper.jpg', 6.7),
                  'tf': (5.25 / aSize, VBase4(0, 0.1, 0, 0.1), ['twoface'], 'middleman.jpg', 6.95),
                  'm': (5.75 / aSize, VBase4(1.0, 1.0, 0, 1.0), ['yesman'], 'blood-sucker.jpg', 7.61),
                  'mh': (7.0 / aSize, VBase4(1.0, 0.3, 0.2, 0.6), ['yesman', 'glasses_shades'], '', 8.95),
                  }

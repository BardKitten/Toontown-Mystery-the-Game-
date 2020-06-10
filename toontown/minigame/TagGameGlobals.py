from toontown.toonbase import ToontownGlobals

DURATION = 90
DEFAULT_SKY = 'phase_3.5/models/props/TT_sky'
DEFAULT_GROUND = 'phase_4/models/minigames/tag_arena'

DEFAULT_TREASURE_POINTS = [
 (0, 0, 0.1),
 (5, 20, 0.1),
 (0, 40, 0.1),
 (-5, -20, 0.1),
 (0, -40, 0.1),
 (20, 0, 0.1),
 (40, 5, 0.1),
 (-20, -5, 0.1),
 (-40, 0, 0.1),
 (22, 20, 0.1),
 (-20, 22, 0.1),
 (20, -20, 0.1),
 (-25, -20, 0.1),
 (20, 40, 0.1),
 (20, -44, 0.1),
 (-24, 40, 0.1),
 (-20, -40, 0.1)]

DEFAULT_DROP_POINTS = (
 (0, 10, 0.25, 180, 0, 0),
 (10, 0, 0.25, 90, 0, 0),
 (0, -10, 0.25, 0, 0, 0),
 (-10, 0, 0.25, -90, 0, 0)
)

SKY = {
 ToontownGlobals.TheBrrrgh: 'phase_3.5/models/props/BR_sky'
}

GROUND = {
 ToontownGlobals.TheBrrrgh: 'phase_8/models/minigames/tag_arena_BR',
 ToontownGlobals.DaisyGardens: 'phase_8/models/minigames/tag_arena_DG'
}

TREASURE_POINTS = {
 ToontownGlobals.TheBrrrgh: [
  (-27, -30.7, 10.4),
  (0.2, -33.6, 2.5),
  (-60.9, -36.6, 2.7),
  (-59.3, -9.04, 0.31),
  (-78.4, 2.7, 4.2),
  (-37.8, 2.1, 3.7),
  (-28.6, 35.8, 11.6),
  (7.7, 5.8, 2.4),
  (41.5, -30.1, 14.2),
  (37.8, 32.1, 11.7),
  (2.8, 51.1, 3),
  (-16.8, 0.6, 2.2),
  (-72.4, 37.7, 5)
 ],
 ToontownGlobals.DaisyGardens: [
  (21.3, 27.6, 0.025),
  (30.4, -8.4, 0.025),
  (0.5, -36.3, 0.025),
  (-34.9, -10.4, 0.025),
  (-35.3, -34.3, 0.025),
  (-33.3, -54, 0.025),
  (41.6, -39.4, 0.025),
  (19.0, -41.2, 0.025),
  (0.5, 61.3, 0.025),
  (-24.4, 52.1, 0.025),
  (-49.9, 24.2, 0.025),
  (-43.8, 8.4, 0.025)
 ]
}

DROP_POINTS = {
 ToontownGlobals.TheBrrrgh: (
  (-30.4, 37.5, 11.1, 2006, 0, 0),
  (34.7, -21.5, 12.5, 1875, 0, 0),
  (-31.9, -29.4, 10, 1774),
  (-74.1, -30.5, 5.3, 1720)
 ),
 ToontownGlobals.DaisyGardens: (
  (38.6, -55.1, 0.025, 396, 0, 0),
  (3.1, 54, 0.025, 898, 0, 0),
  (-37.8, -49.4, 0.025, 685, 0, 0),
  (-55.9, 21, 0.025, 608, 0, 0)
 )
}

SNOW_HOODS = [ToontownGlobals.TheBrrrgh]

def getSky(safezoneId):
    return SKY.get(safezoneId, DEFAULT_SKY)

def getGround(safezoneId):
    return GROUND.get(safezoneId, DEFAULT_GROUND)

def getTreasurePoints(safezoneId):
    return TREASURE_POINTS.get(safezoneId, DEFAULT_TREASURE_POINTS)

def getDropPoints(safezoneId):
    return DROP_POINTS.get(safezoneId, DEFAULT_DROP_POINTS)

def isSnowHood(safezoneId):
    return safezoneId in SNOW_HOODS

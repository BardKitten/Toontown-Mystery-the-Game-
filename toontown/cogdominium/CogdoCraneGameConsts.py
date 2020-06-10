from direct.fsm.StatePush import StateVar
from otp.level.EntityStateVarSet import EntityStateVarSet
from CogdoUtil import VariableContainer
from toontown.cogdominium.CogdoEntityTypes import CogdoCraneGameSettings, CogdoCraneCogSettings
Gameplay = VariableContainer()
Gameplay.SecondsUntilGameOver = 60.0 * 3.0
Gameplay.TimeRunningOutSeconds = 45.0
Audio = VariableContainer()
Audio.MusicFiles = {'normal': 'phase_9/audio/bgm/CHQ_FACT_bg.ogg',
 'end': 'phase_7/audio/bgm/encntr_toon_winning_indoor.ogg',
 'timeRunningOut': 'phase_7/audio/bgm/encntr_suit_winning_indoor.ogg'}
Settings = EntityStateVarSet(CogdoCraneGameSettings)
CogSettings = EntityStateVarSet(CogdoCraneCogSettings)
CranePosHprs = [(13.4, -136.6, 6, -45, 0, 0),
 (13.4, -91.4, 6, -135, 0, 0),
 (58.6, -91.4, 6, 135, 0, 0),
 (58.6, -136.6, 6, 45, 0, 0)]
MoneyBagPosHprs = [[77.2 - 84,
  -329.3 + 201,
  0,
  -90,
  0,
  0],
 [77.1 - 84,
  -302.7 + 201,
  0,
  -90,
  0,
  0],
 [165.7 - 84,
  -326.4 + 201,
  0,
  90,
  0,
  0],
 [165.5 - 84,
  -302.4 + 201,
  0,
  90,
  0,
  0],
 [107.8 - 84,
  -359.1 + 201,
  0,
  0,
  0,
  0],
 [133.9 - 84,
  -359.1 + 201,
  0,
  0,
  0,
  0],
 [107.0 - 84,
  -274.7 + 201,
  0,
  180,
  0,
  0],
 [134.2 - 84,
  -274.7 + 201,
  0,
  180,
  0,
  0]]
for i in xrange(len(MoneyBagPosHprs)):
    MoneyBagPosHprs[i][2] += 6

from SpecImports import *
import random
LobbyParent = 10014
BoilerParent = 10030
PipeLeftParent = 10023
PipeRightParent = 10032
OilParent = 10034
ControlParent = 10037
DuctParent = 10036
PaintMixerStorageParent = 10660
EastCatwalkParent = 10661
WestCatwalkParent = 10662
CenterSiloOutsideBattleCellParent = 10663
CenterSiloBattleCellParent = 10064
CenterSiloParent = 20095
SigRoomParent = 20058
WestSiloParent = 20094
WestSiloBattleCellParent = 10047
EastSiloParent = 20096
EastSiloBattleCellParent = 10068
LobbyCell = 0
BoilerCell = 1
PipeLeftCell = 2
PipeRightCell = 3
OilCell = 4
ControlCell = 5
DuctCell = 6
CenterSiloCell = 7
SigRoomCell = 8
WestSiloCell = 9
EastSiloCell = 10
CenterSiloOutsideCell = 11
PaintMixerStorageCell = 12
EastCatwalkCell = 13
WestCatwalkCell = 14
BattleCells = {LobbyCell: {'parentEntId': LobbyParent,
             'pos': Point3(0, 0, 0)},
 BoilerCell: {'parentEntId': BoilerParent,
              'pos': Point3(0, 0, 0)},
 OilCell: {'parentEntId': OilParent,
           'pos': Point3(0, 0, 0)},
 ControlCell: {'parentEntId': ControlParent,
               'pos': Point3(0, 0, 0)},
 CenterSiloCell: {'parentEntId': CenterSiloBattleCellParent,
                  'pos': Point3(0, 0, 0)},
 PipeLeftCell: {'parentEntId': PipeLeftParent,
                'pos': Point3(0, 0, 0)},
 PipeRightCell: {'parentEntId': PipeRightParent,
                 'pos': Point3(0, 0, 0)},
 DuctCell: {'parentEntId': DuctParent,
            'pos': Point3(0, 0, 0)},
 SigRoomCell: {'parentEntId': SigRoomParent,
               'pos': Point3(0, 0, 0)},
 WestSiloCell: {'parentEntId': WestSiloBattleCellParent,
                'pos': Point3(0, 0, 0)},
 EastSiloCell: {'parentEntId': EastSiloBattleCellParent,
                'pos': Point3(-20, -10, 0)},
 CenterSiloOutsideCell: {'parentEntId': CenterSiloOutsideBattleCellParent,
                'pos': Point3(0, 0, 0)},
 PaintMixerStorageCell: {'parentEntId': PaintMixerStorageParent,
                'pos': Point3(0, 0, 0)},
 EastCatwalkCell: {'parentEntId': EastCatwalkParent,
                'pos': Point3(0, 0, 0)},
 WestCatwalkCell: {'parentEntId': WestCatwalkParent,
                'pos': Point3(0, 0, 0)}}
CogData = [{'type': 'rb',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 29,
  'battleCell': LobbyCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 29,
  'battleCell': LobbyCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'bw',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 29,
  'battleCell': LobbyCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'tbc',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 29,
  'battleCell': LobbyCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'tf',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 29,
  'battleCell': BoilerCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'walk',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 29,
  'battleCell': BoilerCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'walk',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 29,
  'battleCell': BoilerCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'walk',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'tf',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 29,
  'battleCell': BoilerCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 29,
  'battleCell': OilCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 29,
  'battleCell': OilCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 29,
  'battleCell': OilCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 29,
  'battleCell': OilCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 29,
  'battleCell': ControlCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 29,
  'battleCell': ControlCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'tf',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 29,
  'battleCell': ControlCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'tf',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 29,
  'battleCell': ControlCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 30,
  'battleCell': CenterSiloCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'tf',
  'parentEntId': CenterSiloParent,
  'boss': 1,
  'level': 30,
  'battleCell': CenterSiloCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': 4},
 {'type': 'tf',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 30,
  'battleCell': CenterSiloCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 30,
  'battleCell': CenterSiloCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 29,
  'battleCell': WestSiloCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'tf',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 29,
  'battleCell': WestSiloCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'tf',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 29,
  'battleCell': WestSiloCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 29,
  'battleCell': WestSiloCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 29,
  'battleCell': EastSiloCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 29,
  'battleCell': EastSiloCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 29,
  'battleCell': EastSiloCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 29,
  'battleCell': EastSiloCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 29,
  'battleCell': PipeLeftCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 29,
  'battleCell': PipeLeftCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 29,
  'battleCell': PipeLeftCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 29,
  'battleCell': PipeLeftCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 29,
  'battleCell': PipeRightCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 29,
  'battleCell': PipeRightCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 29,
  'battleCell': PipeRightCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 29,
  'battleCell': PipeRightCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 29,
  'battleCell': DuctCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'ms',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 29,
  'battleCell': DuctCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'ms',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 29,
  'battleCell': DuctCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'ms',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 29,
  'battleCell': DuctCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 29,
  'battleCell': SigRoomCell,
  'pos': Point3(5, -10.75, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'tf',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 29,
  'battleCell': SigRoomCell,
  'pos': Point3(5, -3.25, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 29,
  'battleCell': SigRoomCell,
  'pos': Point3(5, 3.25, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 29,
  'battleCell': SigRoomCell,
  'pos': Point3(5, 10.75, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': CenterSiloOutsideBattleCellParent,
  'boss': 0,
  'level': 30,
  'battleCell': CenterSiloOutsideCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId':CenterSiloOutsideBattleCellParent,
  'boss': 0,
  'level': 30,
  'battleCell': CenterSiloOutsideCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': CenterSiloOutsideBattleCellParent,
  'boss': 0,
  'level': 30,
  'battleCell': CenterSiloOutsideCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': CenterSiloOutsideBattleCellParent,
  'boss': 0,
  'level': 30,
  'battleCell': CenterSiloOutsideCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': PaintMixerStorageParent,
  'boss': 0,
  'level': 30,
  'battleCell': PaintMixerStorageCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': PaintMixerStorageParent,
  'boss': 0,
  'level': 30,
  'battleCell': PaintMixerStorageCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': PaintMixerStorageParent,
  'boss': 0,
  'level': 30,
  'battleCell': PaintMixerStorageCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': PaintMixerStorageParent,
  'boss': 0,
  'level': 30,
  'battleCell': PaintMixerStorageCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': EastCatwalkParent,
  'boss': 0,
  'level': 30,
  'battleCell': EastCatwalkCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': EastCatwalkParent,
  'boss': 0,
  'level': 30,
  'battleCell': EastCatwalkCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': EastCatwalkParent,
  'boss': 0,
  'level': 30,
  'battleCell': EastCatwalkCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'mh',
  'parentEntId': EastCatwalkParent,
  'boss': 0,
  'level': 30,
  'battleCell': EastCatwalkCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': WestCatwalkParent,
  'boss': 0,
  'level': 30,
  'battleCell': WestCatwalkCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': WestCatwalkParent,
  'boss': 0,
  'level': 30,
  'battleCell': WestCatwalkCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': WestCatwalkParent,
  'boss': 0,
  'level': 30,
  'battleCell': WestCatwalkCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2])},
 {'type': 'm',
  'parentEntId': WestCatwalkParent,
  'boss': 0,
  'level': 30,
  'battleCell': WestCatwalkCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': 2}]
ReserveCogData = [{}]

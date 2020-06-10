from pandac.PandaModules import BitMask32
from pandac.PandaModules import Point3, VBase4
from direct.showbase import PythonUtil
from toontown.toonbase import TTLocalizer
KICK_TO_PLAYGROUND_EVENT = 'lobbies_kickToPlayground'
UberdogCheckLobbyStartFrequency = 5.0
UberdogPurgeLobbyPeriod = 24.0
UberdogLobbiesSanityCheckFrequency = 60
MaxToonsAtALobby = 8
ActivityRequestStatus = PythonUtil.Enum(('Joining', 'Exiting'))
InviteStatus = PythonUtil.Enum(('NotRead',
 'ReadButNotReplied',
 'Accepted',
 'Rejected'))
PartyStatus = PythonUtil.Enum(('Pending',
 'Cancelled',
 'Finished',
 'CanStart',
 'Started',
 'NeverStarted'))
AddPartyErrorCode = PythonUtil.Enum(('AllOk',
 'ValidationError',
 'DatabaseError',
 'TooManyHostedParties'))

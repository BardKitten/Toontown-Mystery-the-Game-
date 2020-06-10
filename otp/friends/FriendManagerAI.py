from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from otp.otpbase import OTPGlobals
from toontown.toonbase import ToontownGlobals
import datetime, uuid, time, string, random

AVAILABLE_CHARS = string.ascii_lowercase + string.digits

class AddTrueFriend:

    def __init__(self, manager, av, targetId, code):
        self.air = manager.air
        self.manager = manager
        self.av = av
        self.targetId = targetId
        self.code = code

    def start(self):
        self.air.dbInterface.queryObject(self.air.dbId, self.targetId, self.__gotAvatar)
    
    def __gotAvatar(self, dclass, fields):
        dclasses = self.air.dclassesByName['DistributedToonAI']

        if dclass != dclasses:
            return
        
        friendsList = fields['setFriendsList'][0]
        trueFriendsList = fields['setTrueFriends'][0]
        name = fields['setName'][0]
        avId = self.av.doId
        
        if avId in trueFriendsList:
            self.manager.sendUpdateToAvatarId(avId, 'tfResponse', [ToontownGlobals.TF_ALREADY_FRIENDS_NAME, name])
            return
        elif avId not in friendsList:
            if len(friendsList) >= OTPGlobals.MaxFriends:
                self.manager.sendUpdateToAvatarId(avId, 'tfResponse', [ToontownGlobals.TF_FRIENDS_LIST_FULL_HIM, name])
                return
            
            friendsList.append(avId)
        
        if self.targetId not in self.av.getFriendsList():
            self.av.extendFriendsList(self.targetId)
        
        if hasattr(self.manager, 'data'):
            del self.manager.data[self.code]
        else:
            self.air.dbGlobalCursor.tfCodes.remove({'_id': self.code})

        self.av.addTrueFriend(self.targetId)
        trueFriendsList.append(avId)
        self.air.send(dclasses.aiFormatUpdate('setFriendsList', self.targetId, self.targetId, self.air.ourChannel, [friendsList]))
        self.air.send(dclasses.aiFormatUpdate('setTrueFriends', self.targetId, self.targetId, self.air.ourChannel, [trueFriendsList]))
        self.manager.sendUpdateToAvatarId(avId, 'tfResponse', [ToontownGlobals.TF_SUCCESS, name])
        del self.manager.tfFsms[avId]

class FriendManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("FriendManagerAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air
        self.currentContext = 0
        self.requests = {}
        self.tfFsms = {}
        self.connectToDatabase()
    
    def connectToDatabase(self):
        if not self.air.dbConn:
            self.notify.warning('Not using mongodb, true friends will be non-persistent')
            self.data = {}
        else:
            self.air.dbGlobalCursor.tfCodes.ensure_index('date', expireAfterSeconds=ToontownGlobals.TF_EXPIRE_SECS)

    def friendQuery(self, requested):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)

        if not av:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to friend a player that does not exist!')
            return

        context = self.currentContext
        self.requests[context] = [ [ avId, requested ], 'friendQuery']
        self.currentContext += 1
        self.sendUpdateToAvatarId(requested, 'inviteeFriendQuery', [avId, av.getName(), av.getDNAString(), context])

    def cancelFriendQuery(self, context):
        avId = self.air.getAvatarIdFromSender()

        if not context in self.requests:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to cancel a request that doesn\'t exist!')
            return

        if avId != self.requests[context][0][0]:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to cancel someone elses request!')
            return

        self.requests[context][1] = 'cancelled'
        self.sendUpdateToAvatarId(self.requests[context][0][1], 'inviteeCancelFriendQuery', [context])

    def inviteeFriendConsidering(self, yesNo, context):
        avId = self.air.getAvatarIdFromSender()

        if not context in self.requests:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to consider a friend request that doesn\'t exist!')
            return

        if avId != self.requests[context][0][1]:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to consider for someone else!')
            return

        if self.requests[context][1] != 'friendQuery':
            self.air.writeServerEvent('suspicious', avId, 'Player tried to reconsider friend request!')
            return

        if yesNo != 1:
            self.sendUpdateToAvatarId(self.requests[context][0][0], 'friendConsidering', [yesNo, context])
            del self.requests[context]
            return

        self.requests[context][1] = 'friendConsidering'
        self.sendUpdateToAvatarId(self.requests[context][0][0], 'friendConsidering', [yesNo, context])

    def inviteeFriendResponse(self, response, context):
        avId = self.air.getAvatarIdFromSender()

        if not context in self.requests:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to respond to a friend request that doesn\'t exist!')
            return

        if avId != self.requests[context][0][1]:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to respond to someone else\'s request!')
            return

        if self.requests[context][1] == 'cancelled':
            self.air.writeServerEvent('suspicious', avId, 'Player tried to respond to non-active friend request!')
            return

        self.sendUpdateToAvatarId(self.requests[context][0][0], 'friendResponse', [response, context])

        if response == 1:
            requested = self.requests[context][0][1]

            if requested in self.air.doId2do:
                requested = self.air.doId2do[requested]
            else:
                del self.requests[context]
                return

            requester = self.requests[context][0][0]

            if requester in self.air.doId2do:
                requester = self.air.doId2do[requester]
            else:
                del self.requests[context]
                return

            requested.extendFriendsList(requester.getDoId())
            requester.extendFriendsList(requested.getDoId())

            requested.d_setFriendsList(requested.getFriendsList())
            requester.d_setFriendsList(requester.getFriendsList())

        del self.requests[context]

    def inviteeAcknowledgeCancel(self, context):
        avId = self.air.getAvatarIdFromSender()

        if not context in self.requests:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to acknowledge the cancel of a friend request that doesn\'t exist!')
            return

        if avId != self.requests[context][0][1]:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to acknowledge someone else\'s cancel!')
            return

        if self.requests[context][1] != 'cancelled':
            self.air.writeServerEvent('suspicious', avId, 'Player tried to cancel non-cancelled request!')
            return

        del self.requests[context]
    
    def getRandomCharSequence(self, count):
        return ''.join(random.choice(AVAILABLE_CHARS) for i in xrange(count))
    
    def getTFCode(self, tryNumber):
        if tryNumber == ToontownGlobals.MAX_TF_TRIES:
            return str(uuid.uuid4())
        
        code = 'TT %s %s' % (self.getRandomCharSequence(3), self.getRandomCharSequence(3))
        
        if (hasattr(self, 'data') and code in self.data) or (self.air.dbConn and self.air.dbGlobalCursor.tfCodes.find({'_id': code}).count() > 0):
            return self.getTFCode(tryNumber + 1)
        
        return code
    
    def requestTFCode(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        
        if not av:
            return
        
        tfRequest = av.getTFRequest()
        
        if tfRequest[1] >= ToontownGlobals.MAX_TF_TRIES and tfRequest[0] >= time.time():
            self.sendUpdateToAvatarId(avId, 'tfResponse', [ToontownGlobals.TF_COOLDOWN, ''])
            return
        
        code = self.getTFCode(0)
        
        if hasattr(self, 'data'):
            self.data[code] = avId
        else:
            self.air.dbGlobalCursor.tfCodes.insert({'_id': code, 'date': datetime.datetime.utcnow(), 'avId': avId})
        
        av.b_setTFRequest((time.time() + ToontownGlobals.TF_COOLDOWN_SECS, tfRequest[1] + 1))
        self.sendUpdateToAvatarId(avId, 'tfResponse', [ToontownGlobals.TF_SUCCESS, code])
    
    def redeemTFCode(self, code):
        avId = self.air.getAvatarIdFromSender()

        if avId in self.tfFsms:
            self.sendUpdateToAvatarId(avId, 'tfResponse', [ToontownGlobals.TF_TOO_FAST, ''])
            return

        av = self.air.doId2do.get(avId)
        
        if not av:
            return
        
        if hasattr(self, 'data'):
            if code not in self.data:
                self.sendUpdateToAvatarId(avId, 'tfResponse', [ToontownGlobals.TF_UNKNOWN_SECRET, ''])
                return
            
            targetId = self.data[code]
        else:
            fields = self.air.dbGlobalCursor.tfCodes.find_one({'_id': code})
            
            if not fields:
                self.sendUpdateToAvatarId(avId, 'tfResponse', [ToontownGlobals.TF_UNKNOWN_SECRET, ''])
                return
            
            targetId = fields['avId']
        
        if avId == targetId:
            self.sendUpdateToAvatarId(avId, 'tfResponse', [ToontownGlobals.TF_SELF_SECRET, ''])
            return
        elif av.isTrueFriends(targetId):
            self.sendUpdateToAvatarId(avId, 'tfResponse', [ToontownGlobals.TF_ALREADY_FRIENDS, ''])
            return
        elif targetId not in av.getFriendsList() and len(av.getFriendsList()) >= OTPGlobals.MaxFriends:
            self.sendUpdateToAvatarId(avId, 'tfResponse', [ToontownGlobals.TF_FRIENDS_LIST_FULL_YOU, ''])
            return
        
        tfOperation = AddTrueFriend(self, av, targetId, code)
        tfOperation.start()
        self.tfFsms[avId] = tfOperation
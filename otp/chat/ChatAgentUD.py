from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *
from otp.distributed import OtpDoGlobals
from toontown.toonbase import TTLocalizer
 
BLACKLIST = TTLocalizer.Blacklist
OFFENSE_MSGS = ('-- DEV CHAT -- word blocked: %s', 'Watch your language! This is your first offense. You said "%s".',
                'Watch your language! This is your second offense. Next offense you\'ll get banned for 24 hours. You said "%s".')
 
class ChatAgentUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('ChatAgentUD')
    wantWhitelist = config.GetBool('want-whitelist', True)
   
    chatMode2channel = {
            1 : OtpDoGlobals.OTP_MOD_CHANNEL,
            2 : OtpDoGlobals.OTP_ADMIN_CHANNEL,
            3 : OtpDoGlobals.OTP_SYSADMIN_CHANNEL,
    }
    chatMode2prefix = {
            1 : "[MOD] ",
            2 : "[ADMIN] ",
            3 : "[SYSADMIN] ",
    }
   
    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)
 
        self.offenses = {}
 
    def chatMessage(self, message, chatMode):
        sender = self.air.getAvatarIdFromSender()
        if sender == 0:
            self.air.writeServerEvent('suspicious', self.air.getAccountIdFromSender(),
                                      'Account sent chat without an avatar', message)
            return
 
        if chatMode == 0 and self.wantWhitelist:
            if self.detectBadWords(self.air.getMsgSender(), message):
                return
 
        self.air.writeServerEvent('chat-said', sender, message)
        self.air.send(self.air.dclassesByName['DistributedAvatarUD'].aiFormatUpdate('setTalk', sender, sender, self.air.ourChannel, [message]))
 
    def detectBadWords(self, sender, message):
        words = message.split()
        print words
        for word in words:
            if word.lower() in BLACKLIST:
                accountId = (sender >> 32) & 0xFFFFFFFF
                avId = sender & 0xFFFFFFFF
               
                if not sender in self.offenses:
                    self.offenses[sender] = 0
                   
                if self.air.friendsManager.getToonAccess(avId) < 300:
                    self.offenses[sender] += 1
               
                if self.offenses[sender] >= 3:
                    msg = 'Banned'    
                   
                else:
                    msg = OFFENSE_MSGS[self.offenses[sender]] % word
                    dclass = self.air.dclassesByName['ClientServicesManagerUD']
                    dg = dclass.aiFormatUpdate('systemMessage',
                               OtpDoGlobals.OTP_DO_ID_CLIENT_SERVICES_MANAGER,
                               sender, 1000000, [msg])
                    self.air.send(dg)
                    #self.air.banManager.ban(sender, 2, 'language')
                   
                self.air.writeServerEvent('chat-offense', accountId, word=word, num=self.offenses[sender], msg=msg)
                if self.offenses[sender] >= 3:
                    del self.offenses[sender]
                   
                return 1
               
        return 0
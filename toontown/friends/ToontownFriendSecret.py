from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer, ToontownGlobals
from otp.otpbase import OTPGlobals

globalFriendSecret = None

def showFriendSecret():
    global globalFriendSecret
    if not base.cr.wantTrueFriends():
        chatMgr = base.localAvatar.chatMgr
        chatMgr.fsm.request('noTrueFriends')
    else:
        if globalFriendSecret != None:
            globalFriendSecret.unload()
        globalFriendSecret = ToontownFriendSecret()
        globalFriendSecret.enter()

def hideFriendSecret():
    if globalFriendSecret != None:
        globalFriendSecret.exit()

def unloadFriendSecret():
    global globalFriendSecret
    if globalFriendSecret != None:
        globalFriendSecret.unload()
        globalFriendSecret = None
    return

class ToontownFriendSecret(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownFriendSecret')

    def __init__(self):
        DirectFrame.__init__(self, parent=aspect2dp, pos=(0, 0, 0.3), relief=None, image=DGG.getDefaultDialogGeom(), image_scale=(1.6, 1, 1.4), image_pos=(0, 0, -0.05), image_color=OTPGlobals.GlobalDialogColor, borderWidth=(0.01, 0.01))
        self.initialiseoptions(ToontownFriendSecret)
        self.isLoaded = 0
        self.isEntered = 0

    def unload(self):
        if self.isLoaded == 0:
            return None
        self.isLoaded = 0
        self.exit()
        del self.introText
        del self.getSecret
        del self.enterSecretText
        del self.enterSecret
        del self.ok1
        del self.ok2
        del self.cancel
        del self.secretText
        DirectFrame.destroy(self)

    def load(self):
        if self.isLoaded == 1:
            return None
        self.isLoaded = 1
        self.introText = DirectLabel(parent=self, relief=None, pos=(0, 0, 0.4), scale=0.05, text=TTLocalizer.FriendSecretIntro, text_fg=(0, 0, 0, 1), text_wordwrap=30)
        self.introText.hide()
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        self.getSecret = DirectButton(parent=self, relief=None, pos=(0, 0, -0.11), image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=TTLocalizer.FSgetSecret, text=TTLocalizer.FriendSecretGetSecret, text_scale=TTLocalizer.FSgetSecretButton, text_pos=(0, -0.02), command=self.__getSecret)
        self.getSecret.hide()
        self.enterSecretText = DirectLabel(parent=self, relief=None, pos=TTLocalizer.FSenterSecretTextPos, scale=0.05, text=TTLocalizer.FriendSecretEnterSecret, text_fg=(0, 0, 0, 1), text_wordwrap=30)
        self.enterSecretText.hide()
        self.enterSecret = DirectEntry(parent=self, relief=DGG.SUNKEN, scale=0.06, pos=(-0.6, 0, -0.38), frameColor=(0.8, 0.8, 0.5, 1), borderWidth=(0.1, 0.1), numLines=1, width=20, frameSize=(-0.4,
         20.4,
         -0.4,
         1.1), command=self.__enterSecret)
        self.enterSecret.resetFrameSize()
        self.enterSecret.hide()
        self.ok1 = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=TTLocalizer.FSok1, text=TTLocalizer.FriendSecretEnter, text_scale=0.06, text_pos=(0, -0.02), pos=(0, 0, -0.5), command=self.__ok1)
        self.ok1.hide()
        self.ok2 = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=TTLocalizer.FSok2, text=TTLocalizer.FriendSecretOK, text_scale=0.06, text_pos=(0, -0.02), pos=(0, 0, -0.57), command=self.__ok2)
        self.ok2.hide()
        self.cancel = DirectButton(parent=self, relief=None, text=TTLocalizer.FriendSecretCancel, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=TTLocalizer.FScancel, text_scale=0.06, text_pos=(0, -0.02), pos=(0, 0, -0.57), command=self.__cancel)
        self.cancel.hide()
        self.nextText = DirectLabel(parent=self, relief=None, pos=(0, 0, 0.3), scale=0.06, text='', text_scale=TTLocalizer.FSnextText, text_fg=(0, 0, 0, 1), text_wordwrap=25.5)
        self.nextText.hide()
        self.secretText = DirectLabel(parent=self, relief=None, pos=(0, 0, -0.42), scale=0.08, text='', text_fg=(0, 0, 0, 1), text_wordwrap=30)
        self.secretText.hide()
        guiButton.removeNode()

    def enter(self):
        if self.isEntered == 1:
            return
        self.isEntered = 1
        if self.isLoaded == 0:
            self.load()
        self.show()
        self.introText.show()
        self.getSecret.show()
        self.enterSecretText.show()
        self.enterSecret.show()
        self.ok1.show()
        self.ok2.hide()
        self.cancel.hide()
        self.nextText.hide()
        self.secretText.hide()
        base.localAvatar.chatMgr.fsm.request('otherDialog')
        self.enterSecret['focus'] = 1

    def exit(self):
        if self.isEntered == 0:
            return
        self.isEntered = 0
        self.__cleanupFirstPage()
        self.hide()

    def __getSecret(self):
        self.__cleanupFirstPage()
        self.nextText['text'] = TTLocalizer.FriendSecretGettingSecret
        self.nextText.setPos(0, 0, 0.3)
        self.nextText.show()
        self.ok1.hide()
        self.cancel.show()
        base.cr.friendManager.requestTFCode(self.gotSecret)
    
    def gotSecret(self, response, code):
        if response == ToontownGlobals.TF_COOLDOWN:
            self.rejectGetSecret(TTLocalizer.FriendSecretTooMany)
        elif response == ToontownGlobals.TF_SUCCESS:
            self.successGetSecret(code)
    
    def rejectGetSecret(self, reason):
        self.nextText['text'] = reason
        self.nextText.show()
        self.secretText.show()
        self.cancel.hide()
        self.ok1.hide()
        self.ok2.show()

    def successGetSecret(self, code):
        self.nextText['text'] = TTLocalizer.FriendSecretGotSecret
        self.nextText.setPos(*TTLocalizer.FSgotSecretPos)
        self.secretText['text'] = code
        self.secretText.setScale(0.1 if code.startswith('TT') else 0.08)
        self.nextText.show()
        self.secretText.show()
        self.cancel.hide()
        self.ok1.hide()
        self.ok2.show()

    def __enterSecret(self, secret):
        self.enterSecret.set('')
        secret = secret.strip()
        
        if not secret:
            self.exit()
            return
        
        self.__cleanupFirstPage()
        self.nextText['text'] = TTLocalizer.FriendSecretTryingSecret
        base.cr.friendManager.redeemTFCode(secret, self.gotResponse)
        self.nextText.setPos(0, 0, 0.3)
        self.nextText.show()
        self.cancel.hide()
        self.ok1.hide()
        self.ok2.show()

    def gotResponse(self, response, name):
        if response == ToontownGlobals.TF_UNKNOWN_SECRET:
            self.nextText['text'] = TTLocalizer.FriendSecretEnteredSecretUnknown
        elif response == ToontownGlobals.TF_SELF_SECRET:
            self.nextText['text'] = TTLocalizer.FriendSecretEnteredSecretSelf
        elif response == ToontownGlobals.TF_TOO_FAST:
            self.nextText['text'] = TTLocalizer.FriendSecretTooFast
        elif response == ToontownGlobals.TF_FRIENDS_LIST_FULL_YOU:
            self.nextText['text'] = TTLocalizer.FriendSecretEnteredSecretFullYou
        elif response == ToontownGlobals.TF_FRIENDS_LIST_FULL_HIM:
            self.nextText['text'] = TTLocalizer.FriendSecretEnteredSecretFullHim % name
        elif response == ToontownGlobals.TF_ALREADY_FRIENDS:
            self.nextText['text'] = TTLocalizer.FriendSecretAlreadyFriends
        elif response == ToontownGlobals.TF_ALREADY_FRIENDS_NAME:
            self.nextText['text'] = TTLocalizer.FriendSecretAlreadyFriendsName % name
        elif response == ToontownGlobals.TF_SUCCESS:
            self.nextText['text'] = TTLocalizer.FriendSecretNowFriends % name
        self.nextText.show()
        self.cancel.hide()
        self.ok1.hide()
        self.ok2.show()

    def __ok1(self):
        secret = self.enterSecret.get()
        self.__enterSecret(secret)

    def __ok2(self):
        self.exit()

    def __cancel(self):
        self.exit()

    def __cleanupFirstPage(self):
        self.introText.hide()
        self.getSecret.hide()
        self.enterSecretText.hide()
        self.enterSecret.hide()
        base.localAvatar.chatMgr.fsm.request('mainMenu')

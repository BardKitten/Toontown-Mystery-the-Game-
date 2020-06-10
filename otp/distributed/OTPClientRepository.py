from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed import DistributedSmoothNode
from direct.distributed.ClientRepositoryBase import ClientRepositoryBase
from direct.distributed.MsgTypes import *
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.gui.DirectGui import *
from direct.task import Task
from panda3d.core import *
from otp.avatar import Avatar, DistributedAvatar
from otp.avatar.DistributedPlayer import DistributedPlayer
from otp.distributed import OtpDoGlobals
from otp.distributed.OtpDoGlobals import *
from otp.distributed.TelemetryLimiter import TelemetryLimiter
from otp.otpbase import OTPGlobals, OTPLocalizer
from otp.otpgui import OTPDialog
from otp.nametag.NametagConstants import *
import sys, time, types, random
import __builtin__

class OTPClientRepository(ClientRepositoryBase):
    notify = directNotify.newCategory('OTPClientRepository')
    avatarLimit = 6

    def __init__(self, serverVersion, playGame = None):
        ClientRepositoryBase.__init__(self)
        self.handler = None
        self.__currentAvId = 0
        self.createAvatarClass = None
        self.systemMessageSfx = None
        self.playToken = launcher.getPlayToken()

        self.parentMgr.registerParent(OTPGlobals.SPRender, base.render)
        self.parentMgr.registerParent(OTPGlobals.SPHidden, NodePath())
        self.timeManager = None

        self._proactiveLeakChecks = config.GetBool('crash-on-proactive-leak-detect', 1)
        self.activeDistrictMap = {}
        self.telemetryLimiter = TelemetryLimiter()
        self.serverVersion = serverVersion
        self.waitingForDatabase = None
        self.loginFSM = ClassicFSM('loginFSM', [
            State('loginOff',
                  self.enterLoginOff,
                  self.exitLoginOff, [
                      'connect']),
            State('connect',
                  self.enterConnect,
                  self.exitConnect, [
                      'noConnection',
                      'login',
                      'failedToConnect']),
            State('login',
                  self.enterLogin,
                  self.exitLogin, [
                      'noConnection',
                      'waitForGameList',
                      'reject',
                      'failedToConnect',
                      'shutdown']),
            State('failedToConnect',
                  self.enterFailedToConnect,
                  self.exitFailedToConnect, [
                      'connect',
                      'shutdown']),
            State('shutdown',
                  self.enterShutdown,
                  self.exitShutdown, [
                      'loginOff']),
            State('waitForGameList',
                  self.enterWaitForGameList,
                  self.exitWaitForGameList, [
                      'noConnection',
                      'waitForShardList']),
            State('waitForShardList',
                  self.enterWaitForShardList,
                  self.exitWaitForShardList, [
                      'noConnection',
                      'waitForAvatarList',
                      'noShards']),
            State('noShards',
                  self.enterNoShards,
                  self.exitNoShards, [
                      'noConnection',
                      'noShardsWait',
                      'shutdown']),
            State('noShardsWait',
                  self.enterNoShardsWait,
                  self.exitNoShardsWait, [
                      'noConnection',
                      'waitForShardList',
                      'shutdown']),
            State('reject',
                  self.enterReject,
                  self.exitReject, []),
            State('noConnection',
                  self.enterNoConnection,
                  self.exitNoConnection, [
                      'login',
                      'connect',
                      'shutdown']),
            State('afkTimeout',
                  self.enterAfkTimeout,
                  self.exitAfkTimeout, [
                      'waitForAvatarList',
                      'shutdown']),
            State('waitForAvatarList',
                  self.enterWaitForAvatarList,
                  self.exitWaitForAvatarList, [
                      'noConnection',
                      'chooseAvatar',
                      'shutdown']),
            State('chooseAvatar',
                  self.enterChooseAvatar,
                  self.exitChooseAvatar, [
                      'noConnection',
                      'createAvatar',
                      'waitForAvatarList',
                      'waitForSetAvatarResponse',
                      'waitForDeleteAvatarResponse',
                      'shutdown',
                      'login']),
            State('createAvatar',
                  self.enterCreateAvatar,
                  self.exitCreateAvatar, [
                      'noConnection',
                      'chooseAvatar',
                      'waitForSetAvatarResponse',
                      'shutdown']),
            State('waitForDeleteAvatarResponse',
                  self.enterWaitForDeleteAvatarResponse,
                  self.exitWaitForDeleteAvatarResponse, [
                      'noConnection',
                      'chooseAvatar',
                      'shutdown']),
            State('rejectRemoveAvatar',
                  self.enterRejectRemoveAvatar,
                  self.exitRejectRemoveAvatar, [
                      'noConnection',
                      'chooseAvatar',
                      'shutdown']),
            State('waitForSetAvatarResponse',
                  self.enterWaitForSetAvatarResponse,
                  self.exitWaitForSetAvatarResponse, [
                      'noConnection',
                      'playingGame',
                      'shutdown']),
            State('playingGame',
                  self.enterPlayingGame,
                  self.exitPlayingGame, [
                      'noConnection',
                      'waitForAvatarList',
                      'login',
                      'shutdown',
                      'afkTimeout',
                      'noShards'])],
            'loginOff', 'loginOff')
        self.gameFSM = ClassicFSM('gameFSM', [
            State('gameOff',
                  self.enterGameOff,
                  self.exitGameOff, [
                      'waitOnEnterResponses']),
            State('waitOnEnterResponses',
                  self.enterWaitOnEnterResponses,
                  self.exitWaitOnEnterResponses, [
                      'playGame',
                      'tutorialQuestion',
                      'gameOff']),
            State('tutorialQuestion',
                  self.enterTutorialQuestion,
                  self.exitTutorialQuestion, [
                      'playGame',
                      'gameOff']),
            State('playGame',
                  self.enterPlayGame,
                  self.exitPlayGame, [
                      'gameOff',
                      'closeShard',
                      'switchShards']),
            State('switchShards',
                  self.enterSwitchShards,
                  self.exitSwitchShards, [
                      'gameOff',
                      'waitOnEnterResponses']),
            State('closeShard',
                  self.enterCloseShard,
                  self.exitCloseShard, [
                      'gameOff',
                      'waitOnEnterResponses'])],
            'gameOff', 'gameOff')
        self.loginFSM.getStateNamed('playingGame').addChild(self.gameFSM)
        self.loginFSM.enterInitialState()
        self.music = None
        self.gameDoneEvent = 'playGameDone'
        self.playGame = playGame(self.gameFSM, self.gameDoneEvent)
        self.shardListHandle = None
        self.uberZoneInterest = None

        self.__pendingGenerates = {}
        self.__pendingMessages = {}
        self.__doId2pendingInterest = {}

        self.chatAgent = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_CHAT_MANAGER, 'ChatAgent')
        self.csm = None # To be set by subclass.

    def hasPlayToken():
        return self.playToken != None

    def readDCFile(self, dcFileNames=None):
        dcFile = self.getDcFile()
        dcFile.clear()
        self.dclassesByName = {}
        self.dclassesByNumber = {}
        self.hashVal = 0

        if isinstance(dcFileNames, types.StringTypes):
            # If we were given a single string, make it a list.
            dcFileNames = [dcFileNames]

        dcImports = {}
        if dcFileNames == None:
            try:
                # For Nirai
                readResult = dcFile.read(dcStream, '__dc__')
                del __builtin__.dcStream

            except NameError:
                readResult = dcFile.readAll()

            if not readResult:
                self.notify.error("Could not read dc file.")

        else:
            searchPath = getModelPath().getValue()
            for dcFileName in dcFileNames:
                pathname = Filename(dcFileName)
                vfs.resolveFilename(pathname, searchPath)
                readResult = dcFile.read(pathname)
                if not readResult:
                    self.notify.error("Could not read dc file: %s" % (pathname))

        self.hashVal = dcFile.getHash()

        # Now import all of the modules required by the DC file.
        for n in xrange(dcFile.getNumImportModules()):
            moduleName = dcFile.getImportModule(n)[:]

            # Maybe the module name is represented as "moduleName/AI".
            suffix = moduleName.split('/')
            moduleName = suffix[0]
            suffix=suffix[1:]
            if self.dcSuffix in suffix:
                moduleName += self.dcSuffix
            elif self.dcSuffix == 'UD' and 'AI' in suffix: #HACK:
                moduleName += 'AI'

            importSymbols = []
            for i in xrange(dcFile.getNumImportSymbols(n)):
                symbolName = dcFile.getImportSymbol(n, i)

                # Maybe the symbol name is represented as "symbolName/AI".
                suffix = symbolName.split('/')
                symbolName = suffix[0]
                suffix=suffix[1:]
                if self.dcSuffix in suffix:
                    symbolName += self.dcSuffix
                elif self.dcSuffix == 'UD' and 'AI' in suffix: #HACK:
                    symbolName += 'AI'

                importSymbols.append(symbolName)

            self.importModule(dcImports, moduleName, importSymbols)

        # Now get the class definition for the classes named in the DC
        # file.
        for i in xrange(dcFile.getNumClasses()):
            dclass = dcFile.getClass(i)
            number = dclass.getNumber()
            className = dclass.getName() + self.dcSuffix

            # Does the class have a definition defined in the newly
            # imported namespace?
            classDef = dcImports.get(className)
            if classDef is None and self.dcSuffix == 'UD': #HACK:
                className = dclass.getName() + 'AI'
                classDef = dcImports.get(className)

            # Also try it without the dcSuffix.
            if classDef == None:
                className = dclass.getName()
                classDef = dcImports.get(className)
            if classDef is None:
                self.notify.debug("No class definition for %s." % (className))
            else:
                if type(classDef) == types.ModuleType:
                    if not hasattr(classDef, className):
                        self.notify.warning("Module %s does not define class %s." % (className, className))
                        continue
                    classDef = getattr(classDef, className)

                if type(classDef) != types.ClassType and type(classDef) != types.TypeType:
                    self.notify.error("Symbol %s is not a class name." % (className))
                else:
                    dclass.setClassDef(classDef)

            self.dclassesByName[className] = dclass
            if number >= 0:
                self.dclassesByNumber[number] = dclass

        # Owner Views
        if self.hasOwnerView():
            ownerDcSuffix = self.dcSuffix + 'OV'
            # dict of class names (without 'OV') that have owner views
            ownerImportSymbols = {}

            # Now import all of the modules required by the DC file.
            for n in xrange(dcFile.getNumImportModules()):
                moduleName = dcFile.getImportModule(n)

                # Maybe the module name is represented as "moduleName/AI".
                suffix = moduleName.split('/')
                moduleName = suffix[0]
                suffix=suffix[1:]
                if ownerDcSuffix in suffix:
                    moduleName = moduleName + ownerDcSuffix

                importSymbols = []
                for i in xrange(dcFile.getNumImportSymbols(n)):
                    symbolName = dcFile.getImportSymbol(n, i)

                    # Check for the OV suffix
                    suffix = symbolName.split('/')
                    symbolName = suffix[0]
                    suffix=suffix[1:]
                    if ownerDcSuffix in suffix:
                        symbolName += ownerDcSuffix
                    importSymbols.append(symbolName)
                    ownerImportSymbols[symbolName] = None

                self.importModule(dcImports, moduleName, importSymbols)

            # Now get the class definition for the owner classes named
            # in the DC file.
            for i in xrange(dcFile.getNumClasses()):
                dclass = dcFile.getClass(i)
                if ((dclass.getName()+ownerDcSuffix) in ownerImportSymbols):
                    number = dclass.getNumber()
                    className = dclass.getName() + ownerDcSuffix

                    # Does the class have a definition defined in the newly
                    # imported namespace?
                    classDef = dcImports.get(className)
                    if classDef is None:
                        self.notify.error("No class definition for %s." % className)
                    else:
                        if type(classDef) == types.ModuleType:
                            if not hasattr(classDef, className):
                                self.notify.error("Module %s does not define class %s." % (className, className))
                            classDef = getattr(classDef, className)
                        dclass.setOwnerClassDef(classDef)
                        self.dclassesByName[className] = dclass

    def getGameDoId(self):
        return self.GameGlobalsId

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterLoginOff(self):
        self.handler = self.handleMessageType
        self.shardListHandle = None
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitLoginOff(self):
        self.handler = None
        return

    def getServerVersion(self):
        return self.serverVersion

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterConnect(self, serverList):
        self.serverList = serverList
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.connectingBox = dialogClass(message=OTPLocalizer.CRConnecting)
        self.connectingBox.show()
        self.renderFrame()
        self.handler = self.handleConnecting
        self.connect(self.serverList, successCallback=self._sendHello, failureCallback=self.failedToConnect)

    def _sendHello(self):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_HELLO)
        datagram.addUint32(self.hashVal)
        datagram.addString(self.serverVersion)
        self.send(datagram)

    def handleConnecting(self, msgtype, di):
        if msgtype == CLIENT_HELLO_RESP:
            self._handleConnected()
        else:
            self.handleMessageType(msgtype, di)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def failedToConnect(self, statusCode, statusString):
        self.loginFSM.request('failedToConnect', [statusCode, statusString])

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitConnect(self):
        self.connectingBox.cleanup()
        del self.connectingBox

    def handleSystemMessage(self, di):
        message = ClientRepositoryBase.handleSystemMessage(self, di)
        whisper = WhisperPopup(message, OTPGlobals.getInterfaceFont(), WTSystem)
        whisper.manage(base.marginManager)
        if not self.systemMessageSfx:
            self.systemMessageSfx = base.loadSfx('phase_3/audio/sfx/clock03.ogg')
        if self.systemMessageSfx:
            base.playSfx(self.systemMessageSfx)

    def getConnectedEvent(self):
        return 'OTPClientRepository-connected'

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def _handleConnected(self):
        launcher.setDisconnectDetailsNormal()
        messenger.send(self.getConnectedEvent())
        self.gotoFirstScreen()

    def gotoFirstScreen(self):
        self.startReaderPollTask()
        #self.startHeartbeat()
        self.loginFSM.request('login')

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterLogin(self):
        self.sendSetAvatarIdMsg(0)
        self.loginDoneEvent = 'loginDone'
        self.accept(self.loginDoneEvent, self.__handleLoginDone)
        self.csm.performLogin(self.loginDoneEvent)
        self.waitForDatabaseTimeout(requestName='WaitOnCSMLoginResponse')

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def __handleLoginDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'success':
            self.loginFSM.request('waitForGameList')
        elif mode == 'reject':
            self.loginFSM.request('reject')
        elif mode == 'quit':
            self.loginFSM.request('shutdown')
        elif mode == 'failure':
            self.loginFSM.request('failedToConnect', [-1, '?'])
        else:
            self.notify.error('Invalid doneStatus mode from ClientServicesManager: ' + str(mode))

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitLogin(self):
        self.cleanupWaitingForDatabase()
        self.ignore(self.loginDoneEvent)
        del self.loginDoneEvent
        self.handler = None
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterFailedToConnect(self, statusCode, statusString):
        self.handler = self.handleMessageType
        messenger.send('connectionIssue')
        url = self.serverList[0]
        self.notify.warning('Failed to connect to %s (%s %s).  Notifying user.' % (url.cStr(), statusCode, statusString))
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.failedToConnectBox = dialogClass(message=OTPLocalizer.CRNoConnectTryAgain % (url.getServer(), url.getPort()), doneEvent='failedToConnectAck', text_wordwrap=18, style=OTPDialog.TwoChoice)
        self.failedToConnectBox.show()
        self.accept('failedToConnectAck', self.__handleFailedToConnectAck)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def __handleFailedToConnectAck(self):
        doneStatus = self.failedToConnectBox.doneStatus
        if doneStatus == 'ok':
            self.loginFSM.request('connect', [self.serverList])
            messenger.send('connectionRetrying')
        elif doneStatus == 'cancel':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitFailedToConnect(self):
        self.handler = None
        self.ignore('failedToConnectAck')
        self.failedToConnectBox.cleanup()
        del self.failedToConnectBox
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterShutdown(self, errorCode = None):
        self.handler = self.handleMessageType
        self.sendDisconnect()
        self.notify.info('Exiting cleanly')
        base.exitShow(errorCode)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitShutdown(self):
        self.handler = None
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterWaitForGameList(self):
        self.gameDoDirectory = self.addTaggedInterest(self.GameGlobalsId, OTP_ZONE_ID_MANAGEMENT, self.ITAG_PERM, 'game directory', event='GameList_Complete')
        self.acceptOnce('GameList_Complete', self.loginFSM.request, ['waitForShardList'])

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitWaitForGameList(self):
        self.handler = None
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterWaitForShardList(self):
        if not self.isValidInterestHandle(self.shardListHandle):
            self.shardListHandle = self.addTaggedInterest(self.GameGlobalsId, OTP_ZONE_ID_DISTRICTS, self.ITAG_PERM, 'LocalShardList', event='ShardList_Complete')
            self.acceptOnce('ShardList_Complete', self._wantShardListComplete)
        else:
            self._wantShardListComplete()

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def _wantShardListComplete(self):
        if self._shardsAreReady():
            self.loginFSM.request('waitForAvatarList')
        else:
            self.loginFSM.request('noShards')

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def _shardsAreReady(self):
        maxPop = config.GetInt('shard-mid-pop', 300)
        for shard in self.activeDistrictMap.values():
            if shard.available:
                if shard.avatarCount < maxPop:
                    return True
        else:
            return False

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitWaitForShardList(self):
        self.ignore('ShardList_Complete')
        self.handler = None
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterNoShards(self):
        messenger.send('connectionIssue')
        self.handler = self.handleMessageType
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.noShardsBox = dialogClass(message=OTPLocalizer.CRNoDistrictsTryAgain, doneEvent='noShardsAck', style=OTPDialog.TwoChoice)
        self.noShardsBox.show()
        self.accept('noShardsAck', self.__handleNoShardsAck)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def __handleNoShardsAck(self):
        doneStatus = self.noShardsBox.doneStatus
        if doneStatus == 'ok':
            messenger.send('connectionRetrying')
            self.loginFSM.request('noShardsWait')
        elif doneStatus == 'cancel':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitNoShards(self):
        self.handler = None
        self.ignore('noShardsAck')
        self.noShardsBox.cleanup()
        del self.noShardsBox
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterNoShardsWait(self):
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.connectingBox = dialogClass(message=OTPLocalizer.CRConnecting)
        self.connectingBox.show()
        self.renderFrame()
        self.noShardsWaitTaskName = 'noShardsWait'

        def doneWait(task, self = self):
            self.loginFSM.request('waitForShardList')

        delay = 6.5 + random.random() * 2.0
        taskMgr.doMethodLater(delay, doneWait, self.noShardsWaitTaskName)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitNoShardsWait(self):
        taskMgr.remove(self.noShardsWaitTaskName)
        del self.noShardsWaitTaskName
        self.connectingBox.cleanup()
        del self.connectingBox

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterReject(self):
        self.handler = self.handleMessageType
        self.notify.warning('Connection Rejected')
        sys.exit()

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitReject(self):
        self.handler = None
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterNoConnection(self):
        messenger.send('connectionIssue')
        self.resetInterestStateForConnectionLoss()
        self.shardListHandle = None
        self.handler = self.handleMessageType
        self.__currentAvId = 0
        self.stopHeartbeat()
        self.stopReaderPollTask()
        if (self.bootedIndex is not None) and (self.bootedIndex in OTPLocalizer.CRBootedReasons):
            message = OTPLocalizer.CRBootedReasons[self.bootedIndex]
        elif self.bootedIndex == 155:
            message = self.bootedText
        elif self.bootedText is not None:
            message = OTPLocalizer.CRBootedReasonUnknownCode % self.bootedIndex
        else:
            message = OTPLocalizer.CRLostConnection
        reconnect = 1
        if self.bootedIndex in (152, 127, 124, 101, 102, 103):
            reconnect = 0
        if self.bootedIndex == 152:
            message = message % {'name': self.bootedText}
        launcher.setDisconnectDetails(self.bootedIndex, message)
        style = OTPDialog.Acknowledge
        if reconnect:
            message += OTPLocalizer.CRTryConnectAgain
            style = OTPDialog.TwoChoice
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.lostConnectionBox = dialogClass(doneEvent='lostConnectionAck', message=message, text_wordwrap=18, style=style)
        self.lostConnectionBox.show()
        self.accept('lostConnectionAck', self.__handleLostConnectionAck)
        self.notify.warning('Lost connection to server. Notifying user.')
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def __handleLostConnectionAck(self):
        if self.lostConnectionBox.doneStatus == 'ok':
            self.loginFSM.request('connect', [self.serverList])
        else:
            self.loginFSM.request('shutdown')

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitNoConnection(self):
        self.handler = None
        self.ignore('lostConnectionAck')
        self.lostConnectionBox.cleanup()
        messenger.send('connectionRetrying')
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterAfkTimeout(self):
        self.sendSetAvatarIdMsg(0)
        msg = OTPLocalizer.AfkForceAcknowledgeMessage
        dialogClass = OTPGlobals.getDialogClass()
        self.afkDialog = dialogClass(text=msg, command=self.__handleAfkOk, style=OTPDialog.Acknowledge)
        self.handler = self.handleMessageType

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def __handleAfkOk(self, value):
        self.loginFSM.request('waitForAvatarList')

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitAfkTimeout(self):
        if self.afkDialog:
            self.afkDialog.cleanup()
            self.afkDialog = None
        self.handler = None
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterWaitForAvatarList(self):
        self._requestAvatarList()

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def _requestAvatarList(self):
        self.csm.requestAvatars()
        self.waitForDatabaseTimeout(requestName='WaitForAvatarList')

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitWaitForAvatarList(self):
        self.cleanupWaitingForDatabase()
        self.handler = None
        return

    def handleAvatarsList(self, avatars):
        self.avList = avatars
        self.loginFSM.request('chooseAvatar', [self.avList])
    
    def handleChatSettings(self, chatSettings):
        self.chatSettings = chatSettings
    
    def wantSpeedchatPlus(self):
        return self.chatSettings[0]
    
    def wantTrueFriends(self):
        return self.chatSettings[1]
    
    def wantTypedChat(self):
        return self.wantSpeedchatPlus() or self.wantTrueFriends()

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterChooseAvatar(self, avList):
        pass

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitChooseAvatar(self):
        pass

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterCreateAvatar(self, avList, index, newDNA = None):
        pass

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitCreateAvatar(self):
        pass

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterWaitForDeleteAvatarResponse(self, potAv):
        self.csm.sendDeleteAvatar(potAv.id)
        self.waitForDatabaseTimeout(requestName='WaitForDeleteAvatarResponse')

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitWaitForDeleteAvatarResponse(self):
        self.cleanupWaitingForDatabase()

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterRejectRemoveAvatar(self, reasonCode):
        self.notify.warning('Rejected removed avatar. (%s)' % (reasonCode,))
        self.handler = self.handleMessageType
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.rejectRemoveAvatarBox = dialogClass(message='%s\n(%s)' % (OTPLocalizer.CRRejectRemoveAvatar, reasonCode), doneEvent='rejectRemoveAvatarAck', style=OTPDialog.Acknowledge)
        self.rejectRemoveAvatarBox.show()
        self.accept('rejectRemoveAvatarAck', self.__handleRejectRemoveAvatar)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def __handleRejectRemoveAvatar(self):
        self.loginFSM.request('chooseAvatar')

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitRejectRemoveAvatar(self):
        self.handler = None
        self.ignore('rejectRemoveAvatarAck')
        self.rejectRemoveAvatarBox.cleanup()
        del self.rejectRemoveAvatarBox
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterWaitForSetAvatarResponse(self, potAv):
        self.sendSetAvatarMsg(potAv)
        self.waitForDatabaseTimeout(requestName='WaitForSetAvatarResponse')

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitWaitForSetAvatarResponse(self):
        self.cleanupWaitingForDatabase()
        self.handler = None
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def sendSetAvatarMsg(self, potAv):
        self.sendSetAvatarIdMsg(potAv.id)
        self.avData = potAv

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def sendSetAvatarIdMsg(self, avId):
        if avId != self.__currentAvId:
            self.__currentAvId = avId
            self.csm.sendChooseAvatar(avId)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def handleAvatarResponseMsg(self, avatarId, di):
        pass

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterPlayingGame(self):
        pass

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitPlayingGame(self):
        self.notify.info('sending clientLogout')
        messenger.send('clientLogout')

    def _abandonShard(self):
        self.notify.error('%s must override _abandonShard' % self.__class__.__name__)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterGameOff(self):
        self.uberZoneInterest = None
        if not hasattr(self, 'cleanGameExit'):
            self.cleanGameExit = True
        if self.cleanGameExit:
            if self.isShardInterestOpen():
                self.notify.error('enterGameOff: shard interest is still open')
        elif self.isShardInterestOpen():
            self.notify.warning('unclean exit, abandoning shard')
            self._abandonShard()
        self.cleanupWaitAllInterestsComplete()
        del self.cleanGameExit
        self.cache.flush()
        self.doDataCache.flush()
        self.handler = self.handleMessageType
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitGameOff(self):
        self.handler = None
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterWaitOnEnterResponses(self, shardId, hoodId, zoneId, avId):
        self.cleanGameExit = False
        self.handlerArgs = {'hoodId': hoodId,
         'zoneId': zoneId,
         'avId': avId}
        if shardId is not None:
            district = self.activeDistrictMap.get(shardId)
        else:
            district = None
        if not district:
            self.distributedDistrict = self.getStartingDistrict()
            if not self.distributedDistrict:
                self.loginFSM.request('noShards')
                return
            shardId = self.distributedDistrict.doId
        else:
            self.distributedDistrict = district
        self.notify.info('Entering shard %s' % shardId)
        localAvatar.setLocation(shardId, zoneId)
        base.localAvatar.defaultShard = shardId
        self.waitForDatabaseTimeout(requestName='WaitOnEnterResponses')
        self.handleSetShardComplete()
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def handleSetShardComplete(self):
        hoodId = self.handlerArgs['hoodId']
        zoneId = self.handlerArgs['zoneId']
        avId = self.handlerArgs['avId']
        self.uberZoneInterest = self.addInterest(base.localAvatar.defaultShard, OTPGlobals.UberZone, 'uberZone', 'uberZoneInterestComplete')
        self.acceptOnce('uberZoneInterestComplete', self.uberZoneInterestComplete)
        self.waitForDatabaseTimeout(20, requestName='waitingForUberZone')

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def uberZoneInterestComplete(self):
        self.__gotTimeSync = 0
        self.cleanupWaitingForDatabase()
        if self.timeManager == None:
            self.notify.info('TimeManager is not present.')
            DistributedSmoothNode.globalActivateSmoothing(0, 0)
            self.gotTimeSync()
        else:
            DistributedSmoothNode.globalActivateSmoothing(1, 0)
            if self.timeManager.synchronize('startup'):
                self.accept('gotTimeSync', self.gotTimeSync)
                self.waitForDatabaseTimeout(requestName='uberZoneInterest-timeSync')
            else:
                self.notify.info('No sync from TimeManager.')
                self.gotTimeSync()
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitWaitOnEnterResponses(self):
        self.ignore('uberZoneInterestComplete')
        self.cleanupWaitingForDatabase()
        self.handler = None
        self.handlerArgs = None
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterCloseShard(self, loginState = None):
        self.notify.info('Exiting shard')
        if loginState is None:
            loginState = 'waitForAvatarList'
        self._closeShardLoginState = loginState
        base.cr.setNoNewInterests(True)
        return

    def _removeLocalAvFromStateServer(self):
        self.sendSetAvatarIdMsg(0)
        self._removeAllOV()
        self.removeShardInterest(Functor(self.loginFSM.request, self._closeShardLoginState))

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def _removeAllOV(self):
        ownerDoIds = self.doId2ownerView.keys()
        for doId in ownerDoIds:
            self.disableDoId(doId, ownerView=True)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def isShardInterestOpen(self):
        self.notify.error('%s must override isShardInterestOpen' % self.__class__.__name__)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def removeShardInterest(self, callback, task = None):
        self._removeCurrentShardInterest(Functor(self._removeShardInterestComplete, callback))

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def _removeShardInterestComplete(self, callback):
        self.cleanGameExit = True
        self.cache.flush()
        self.doDataCache.flush()
        callback()

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def _removeCurrentShardInterest(self, callback):
        self.notify.error('%s must override _removeCurrentShardInterest' % self.__class__.__name__)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitCloseShard(self):
        del self._closeShardLoginState
        base.cr.setNoNewInterests(False)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterTutorialQuestion(self, hoodId, zoneId, avId):
        pass

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitTutorialQuestion(self):
        pass

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterPlayGame(self, hoodId, zoneId, avId):
        if self.music:
            self.music.stop()
            self.music = None
        self.handler = self.handlePlayGame
        self.accept(self.gameDoneEvent, self.handleGameDone)
        base.transitions.noFade()
        self.playGame.load()
        try:
            loader.endBulkLoad('localAvatarPlayGame')
        except:
            pass

        self.playGame.enter(hoodId, zoneId, avId)

        def checkScale(task):
            return Task.cont

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def handleGameDone(self):
        if self.timeManager:
            self.timeManager.setDisconnectReason(OTPGlobals.DisconnectSwitchShards)
        doneStatus = self.playGame.getDoneStatus()
        how = doneStatus['how']
        shardId = doneStatus['shardId']
        hoodId = doneStatus['hoodId']
        zoneId = doneStatus['zoneId']
        avId = doneStatus['avId']
        if how == 'teleportIn':
            self.gameFSM.request('switchShards', [shardId,
             hoodId,
             zoneId,
             avId])
        else:
            self.notify.error('Exited shard with unexpected mode %s' % how)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitPlayGame(self):
        taskMgr.remove('globalScaleCheck')
        self.handler = None
        self.playGame.exit()
        self.playGame.unload()
        self.ignore(self.gameDoneEvent)
        return

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def gotTimeSync(self):
        self.notify.info('gotTimeSync')
        self.ignore('gotTimeSync')
        self.__gotTimeSync = 1
        self.moveOnFromUberZone()

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def moveOnFromUberZone(self):
        if not self.__gotTimeSync:
            self.notify.info('Waiting for time sync.')
            return
        hoodId = self.handlerArgs['hoodId']
        zoneId = self.handlerArgs['zoneId']
        avId = self.handlerArgs['avId']

        if not self.SupportTutorial or base.localAvatar.tutorialAck:
            self.gameFSM.request('playGame', [hoodId, zoneId, avId])
            return
        if base.config.GetBool('force-tutorial', 0):
            self.gameFSM.request('tutorialQuestion', [hoodId, zoneId, avId])
            return
        else:
            if hasattr(self, 'skipTutorialRequest') and self.skipTutorialRequest:
                self.skipTutorialRequest = None
                self.gameFSM.request('skipTutorialRequest', [hoodId, zoneId, avId])
                return
            else:
                self.gameFSM.request('tutorialQuestion', [hoodId, zoneId, avId])
                return

        self.gameFSM.request('playGame', [hoodId, zoneId, avId])

    def handlePlayGame(self, msgType, di):
        if self.notify.getDebug():
            self.notify.debug('handle play game got message type: ' + `msgType`)
        if self.__recordObjectMessage(msgType, di):
            return
        if msgType == CLIENT_ENTER_OBJECT_REQUIRED:
            self.handleGenerateWithRequired(di)
        elif msgType == CLIENT_ENTER_OBJECT_REQUIRED_OTHER:
            self.handleGenerateWithRequired(di, other=True)
        elif msgType == CLIENT_OBJECT_SET_FIELD:
            # TODO: Properly fix this:
            try:
                self.handleUpdateField(di)
            except:
                pass
        elif msgType == CLIENT_OBJECT_LEAVING:
            self.handleDelete(di)
        else:
            self.handleMessageType(msgType, di)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def enterSwitchShards(self, shardId, hoodId, zoneId, avId):
        self._switchShardParams = [shardId,
         hoodId,
         zoneId,
         avId]
        localAvatar.setLeftDistrict()
        self.removeShardInterest(self._handleOldShardGone)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def _handleOldShardGone(self):
        self.gameFSM.request('waitOnEnterResponses', self._switchShardParams)

    @report(types=['args', 'deltaStamp'], dConfigParam='teleport')
    def exitSwitchShards(self):
        pass

    def getStartingDistrict(self):
        if not self.activeDistrictMap:
            self.notify.info('no shards')
            return

        maxPop = config.GetInt('shard-mid-pop', 300)
        preferred = settings.get('preferredShard', None)
        
        if preferred:
            for shard in self.activeDistrictMap.values():
                if shard.available and shard.name == preferred and shard.avatarCount < maxPop:
                    return shard

        for shard in self.activeDistrictMap.values():
            if shard.available and shard.avatarCount < maxPop:
                district = shard
                maxPop = district.avatarCount

        if district:
            self.notify.debug('chose %s: pop %s' % (district.name, district.avatarCount))

        return district

    def getShardName(self, shardId):
        try:
            return self.activeDistrictMap[shardId].name
        except:
            return None

        return None

    def isShardAvailable(self, shardId):
        try:
            return self.activeDistrictMap[shardId].available
        except:
            return 0

    def listActiveShards(self):
        list = []

        for s in self.activeDistrictMap.values():
            if s.available:
                list.append((s.doId, s.name, s.avatarCount, s.invasionStatus, s.groupAvCount))

        return list

    def getPlayerAvatars(self):
        return [i for i in self.doId2do.values() if isinstance(i, DistributedPlayer)]

    def queryObjectField(self, dclassName, fieldName, doId, context = 0):
        dclass = self.dclassesByName.get(dclassName)
        if dclass is not None:
            fieldId = dclass.getFieldByName(fieldName).getNumber()
            self.queryObjectFieldId(doId, fieldId, context)
        return

    def lostConnection(self):
        ClientRepositoryBase.lostConnection(self)
        self.loginFSM.request('noConnection')

    def waitForDatabaseTimeout(self, extraTimeout = 0, requestName = 'unknown'):
        OTPClientRepository.notify.debug('waiting for database timeout %s at %s' % (requestName, globalClock.getFrameTime()))
        self.cleanupWaitingForDatabase()
        globalClock.tick()
        taskMgr.doMethodLater((OTPGlobals.DatabaseDialogTimeout + extraTimeout) * choice(0, 10, 1), self.__showWaitingForDatabase, 'waitingForDatabase', extraArgs=[requestName])

    def cleanupWaitingForDatabase(self):
        if self.waitingForDatabase:
            self.waitingForDatabase.hide()
            self.waitingForDatabase.cleanup()
            self.waitingForDatabase = None
        taskMgr.remove('waitingForDatabase')
        return

    def __showWaitingForDatabase(self, requestName):
        messenger.send('connectionIssue')
        OTPClientRepository.notify.info('timed out waiting for %s at %s' % (requestName, globalClock.getFrameTime()))
        dialogClass = OTPGlobals.getDialogClass()
        self.waitingForDatabase = dialogClass(text=OTPLocalizer.CRToontownUnavailable, dialogName='WaitingForDatabase', buttonTextList=[OTPLocalizer.CRToontownUnavailableCancel], style=OTPDialog.CancelOnly, command=self.__handleCancelWaiting)
        self.waitingForDatabase.show()
        taskMgr.remove('waitingForDatabase')
        taskMgr.doMethodLater(OTPGlobals.DatabaseGiveupTimeout, self.__giveUpWaitingForDatabase, 'waitingForDatabase', extraArgs=[requestName])
        return Task.done

    def __giveUpWaitingForDatabase(self, requestName):
        OTPClientRepository.notify.info('giving up waiting for %s at %s' % (requestName, globalClock.getFrameTime()))
        self.cleanupWaitingForDatabase()
        self.loginFSM.request('noConnection')
        return Task.done

    def __handleCancelWaiting(self, value):
        self.loginFSM.request('shutdown')

    def renderFrame(self):
        gsg = base.win.getGsg()
        if gsg:
            render2d.prepareScene(gsg)
        base.graphicsEngine.renderFrame()

    def handleMessageType(self, msgType, di):
        if self.__recordObjectMessage(msgType, di):
            return
        if msgType == CLIENT_EJECT:
            self.handleGoGetLost(di)
        elif msgType == CLIENT_HEARTBEAT:
            self.handleServerHeartbeat(di)
        elif msgType == CLIENT_ENTER_OBJECT_REQUIRED:
            self.handleGenerateWithRequired(di)
        elif msgType == CLIENT_ENTER_OBJECT_REQUIRED_OTHER:
            self.handleGenerateWithRequired(di, other=True)
        elif msgType == CLIENT_ENTER_OBJECT_REQUIRED_OTHER_OWNER:
            self.handleGenerateWithRequiredOtherOwner(di)
        elif msgType == CLIENT_OBJECT_SET_FIELD:
            self.handleUpdateField(di)
        elif msgType == CLIENT_OBJECT_LEAVING:
            self.handleDisable(di)
        elif msgType == CLIENT_OBJECT_LEAVING_OWNER:
            self.handleDisable(di, ownerView=True)
        elif msgType == CLIENT_DONE_INTEREST_RESP:
            self.gotInterestDoneMessage(di)
        elif msgType == CLIENT_OBJECT_LOCATION:
            self.gotObjectLocationMessage(di)
        else:
            currentLoginState = self.loginFSM.getCurrentState()
            if currentLoginState:
                currentLoginStateName = currentLoginState.getName()
            else:
                currentLoginStateName = 'None'
            currentGameState = self.gameFSM.getCurrentState()
            if currentGameState:
                currentGameStateName = currentGameState.getName()
            else:
                currentGameStateName = 'None'

    def gotInterestDoneMessage(self, di):
        if self.deferredGenerates:
            dg = Datagram(di.getDatagram())
            di = DatagramIterator(dg, di.getCurrentIndex())
            self.deferredGenerates.append((CLIENT_DONE_INTEREST_RESP, (dg, di)))
        else:
            di2 = DatagramIterator(di.getDatagram(), di.getCurrentIndex())
            di2.getUint32()  # Ignore the context.
            handle = di2.getUint16()
            self.__playBackGenerates(handle)

            self.handleInterestDoneMessage(di)

    def gotObjectLocationMessage(self, di):
        if self.deferredGenerates:
            dg = Datagram(di.getDatagram())
            di = DatagramIterator(dg, di.getCurrentIndex())
            di2 = DatagramIterator(dg, di.getCurrentIndex())
            doId = di2.getUint32()
            if doId in self.deferredDoIds:
                self.deferredDoIds[doId][3].append((CLIENT_OBJECT_LOCATION, (dg, di)))
            else:
                self.handleObjectLocation(di)
        else:
            self.handleObjectLocation(di)

    def replayDeferredGenerate(self, msgType, extra):
        if msgType == CLIENT_DONE_INTEREST_RESP:
            dg, di = extra
            self.handleInterestDoneMessage(di)
        elif msgType == CLIENT_OBJECT_LOCATION:
            dg, di = extra
            self.handleObjectLocation(di)
        else:
            ClientRepositoryBase.replayDeferredGenerate(self, msgType, extra)

    @exceptionLogged(append=False)
    def handleDatagram(self, di):
        msgType = self.getMsgType()
        if msgType == 65535:
            self.lostConnection()
            return
        if self.handler == None:
            self.handleMessageType(msgType, di)
        else:
            self.handler(msgType, di)
        self.considerHeartbeat()
        return

    def identifyFriend(self, doId):
        return self.identifyAvatar(doId)

    def identifyAvatar(self, doId):
        info = self.doId2do.get(doId)

        return info if info else self.identifyFriend(doId)

    def sendDisconnect(self):
        if self.isConnected():
            datagram = PyDatagram()
            datagram.addUint16(CLIENT_DISCONNECT)
            self.send(datagram)
            self.notify.info('Sent disconnect message to server')
            self.disconnect()
        self.stopHeartbeat()

    def _isPlayerDclass(self, dclass):
        return False

    def _isValidPlayerLocation(self, parentId, zoneId):
        return True

    def _isInvalidPlayerAvatarGenerate(self, doId, dclass, parentId, zoneId):
        if self._isPlayerDclass(dclass):
            if not self._isValidPlayerLocation(parentId, zoneId):
                return True
        return False

    def handleGenerateWithRequired(self, di, other=False):
        doId = di.getUint32()
        parentId = di.getUint32()
        zoneId = di.getUint32()
        classId = di.getUint16()

        # Decide whether we should add this to the interest's pending
        # generates, or process it right away:
        for handle, interest in self._interests.items():
            if parentId != interest.parentId:
                continue

            if isinstance(interest.zoneIdList, list):
                if zoneId not in interest.zoneIdList:
                    continue
            else:
                if zoneId != interest.zoneIdList:
                    continue

            break
        else:
            interest = None

        if (not interest) or (not interest.events):
            # This object can be generated right away:
            return self.__doGenerate(doId, parentId, zoneId, classId, di, other)

        # This object must be generated when the operation completes:
        pending = self.__pendingGenerates.setdefault(handle, [])
        pending.append((doId, parentId, zoneId, classId, Datagram(di.getDatagram()), other))
        self.__doId2pendingInterest[doId] = handle

    def __playBackGenerates(self, handle):
        if handle not in self.__pendingGenerates:
            return

        # This interest has pending generates! Play them:
        generates = self.__pendingGenerates[handle]
        del self.__pendingGenerates[handle]
        generates.sort(key=lambda i: i[3])  # Sort by classId.
        for doId, parentId, zoneId, classId, dg, other in generates:
            di = DatagramIterator(dg)
            di.skipBytes(16)
            self.__doGenerate(doId, parentId, zoneId, classId, di, other)
            if doId in self.__doId2pendingInterest:
                del self.__doId2pendingInterest[doId]

        # Also play back any messages we missed:
        self.__playBackMessages(handle)

    def __playBackMessages(self, handle):
        if handle not in self.__pendingMessages:
            return

        # Any pending messages? Play them:
        for dg in self.__pendingMessages[handle]:
            di = DatagramIterator(dg)
            msgType = di.getUint16()
            if self.handler is None:
                self.handleMessageType(msgType, di)
            else:
                self.handler(msgType, di)

        del self.__pendingMessages[handle]

    def __recordObjectMessage(self, msgType, di):
        if msgType not in (CLIENT_OBJECT_SET_FIELD, CLIENT_OBJECT_LEAVING,
                           CLIENT_OBJECT_LOCATION):
            return False

        di2 = DatagramIterator(di.getDatagram(), di.getCurrentIndex())
        doId = di2.getUint32()

        if doId not in self.__doId2pendingInterest:
            return False

        pending = self.__pendingMessages.setdefault(self.__doId2pendingInterest[doId], [])
        pending.append(Datagram(di.getDatagram()))

        return True

    def __doGenerate(self, doId, parentId, zoneId, classId, di, other):
        dclass = self.dclassesByNumber[classId]
        if self._isInvalidPlayerAvatarGenerate(doId, dclass, parentId, zoneId):
            return
        dclass.startGenerate()
        if other:
            self.generateWithRequiredOtherFields(dclass, doId, di, parentId, zoneId)
        else:
            self.generateWithRequiredFields(dclass, doId, di, parentId, zoneId)
        dclass.stopGenerate()

    def handleGenerateWithRequiredOtherOwner(self, di):
        doId = di.getUint32()
        parentId = di.getUint32()
        zoneId = di.getUint32()
        classId = di.getUint16()
        dclass = self.dclassesByNumber[classId]
        dclass.startGenerate()
        distObj = self.generateWithRequiredOtherFieldsOwner(dclass, doId, di)
        dclass.stopGenerate()

    def handleQuietZoneGenerateWithRequired(self, di):
        doId = di.getUint32()
        parentId = di.getUint32()
        zoneId = di.getUint32()
        classId = di.getUint16()
        dclass = self.dclassesByNumber[classId]
        dclass.startGenerate()
        distObj = self.generateWithRequiredFields(dclass, doId, di, parentId, zoneId)
        dclass.stopGenerate()

    def handleQuietZoneGenerateWithRequiredOther(self, di):
        doId = di.getUint32()
        parentId = di.getUint32()
        zoneId = di.getUint32()
        classId = di.getUint16()
        dclass = self.dclassesByNumber[classId]
        dclass.startGenerate()
        distObj = self.generateWithRequiredOtherFields(dclass, doId, di, parentId, zoneId)
        dclass.stopGenerate()

    def handleDisable(self, di, ownerView = False):
        doId = di.getUint32()
        if not self.isLocalId(doId):
            self.disableDoId(doId, ownerView)

        if doId == self.__currentAvId:
            self.bootedIndex = 153
            self.bootedText = ''

            self.notify.warning("Avatar deleted! Closing connection...")

            # disconnect now, don't wait for send/recv to fail
            self.stopReaderPollTask()
            self.lostConnection()

    def sendSetLocation(self, doId, parentId, zoneId):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_OBJECT_LOCATION)
        datagram.addUint32(doId)
        datagram.addUint32(parentId)
        datagram.addUint32(zoneId)
        self.send(datagram)

    def sendHeartbeat(self):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_HEARTBEAT)
        self.send(datagram)
        self.lastHeartbeat = globalClock.getRealTime()
        self.considerFlush()

    def isLocalId(self, id):
        try:
            return localAvatar.doId == id
        except:
            self.notify.debug('In isLocalId(), localAvatar not created yet')
            return False

    ITAG_PERM = 'perm'
    ITAG_AVATAR = 'avatar'
    ITAG_SHARD = 'shard'
    ITAG_WORLD = 'world'
    ITAG_GAME = 'game'

    def addTaggedInterest(self, parentId, zoneId, mainTag, desc, otherTags = [], event = None):
        return self.addInterest(parentId, zoneId, desc, event)

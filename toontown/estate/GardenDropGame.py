import math, random, GameSprite, GardenGameGlobals
from math import pi
from direct.gui.DirectGui import *
from direct.distributed.ClockDelta import *
from toontown.toonbase import TTLocalizer

LevelNumber = 1

class GardenDropGame:

    def __init__(self):
        self.inHelp = False
        self.sprites = []
        self.lastTime = []
        self.grid = []
        print ('Grid Dimensions X%s Z%s' % (GardenGameGlobals.gX,
         GardenGameGlobals.gZ))
        base.gardenGame = self
        self.matchList = []
        self.massCount = 0
        self.foundCount = 0

        return None

    def reinitialize(self):
        self.inHelp = False
        self.sprites = []
        self.lastTime = []
        self.grid = []
        self.matchList = []
        self.massCount = 0
        self.foundCount = 0

        return None

    def load(self):
        model = loader.loadModel('phase_5.5/models/gui/package_delivery_panel.bam')
        model1 = loader.loadModel('phase_3.5/models/gui/matching_game_gui.bam')

        self.model = model
        self.model1 = model1

        background = model.find('**/bg')
        itemBoard = model.find('**/item_board')

        self.frame = DirectFrame(scale=1.1000000000000001, relief=DGG.FLAT, frameSize=(-0.5,
         0.5,
         -0.45000000000000001,
         -0.050000000000000003), frameColor=(0.73699999999999999, 0.57299999999999995, 0.34499999999999997, 1.0))

        self.background = DirectFrame(self.frame, image=background, image_scale=0.050000000000000003, relief=None, pos=(0, 1, 0))
        self.itemBoard = DirectFrame(parent=self.frame, image=itemBoard, image_scale=0.050000000000000003, image_color=(0.92200000000000004, 0.92200000000000004, 0.753, 1), relief=None, pos=(0, 1, 0))
        gui2 = loader.loadModel('phase_3/models/gui/quit_button.bam')

        self.font = loader.loadFont("phase_3/models/fonts/MickeyFont.bam")
        self.gardenDropText = OnscreenText(parent=self.frame, text=TTLocalizer.GardenDropTitle,scale=(0.17,0.17,0.17), font=self.font, pos=(0,0.685,0), fg=(1,1,1,1))

        self.quitButton = DirectButton(parent=self.frame, relief=None, image=(gui2.find('**/QuitBtn_UP'),
         gui2.find('**/QuitBtn_DN'),
         gui2.find('**/QuitBtn_RLVR')), pos=(0.5,
         1.0,
         -0.41999999999999998), scale=0.90000000000000002, text=TTLocalizer.GardenDropExitGame, text_font=self.font, text0_fg=(1, 1, 1, 1), text1_fg=(1, 1, 1, 1), text2_fg=(1, 1, 1, 1), text_scale=0.044999999999999998, text_pos=(0,
         -0.01), command=self._GardenDropGame__handleExit)

        if LevelNumber == 1:
            self.helpButton = DirectButton(parent=self.frame, relief=None, image=(gui2.find('**/QuitBtn_UP'),
             gui2.find('**/QuitBtn_DN'),
             gui2.find('**/QuitBtn_RLVR')), pos=(-0.5,
             1.0,
             -0.41999999999999998), scale=0.90000000000000002, text=TTLocalizer.PicnicTableTutorial, text_font=self.font, text0_fg=(1, 1, 1, 1), text1_fg=(1, 1, 1, 1), text2_fg=(1, 1, 1, 1), text_scale=0.044999999999999998, text_pos=(0,
             -0.01), command=self._GardenDropGame__openHelp)

    def help(self):
        self.inHelp = True

        frameGui = loader.loadModel('phase_3/models/gui/dialog_box_gui.bam')
        self.helpFrame = DirectFrame(scale=1.1, relief=None, image=frameGui, image_scale=(1.75, 1, 0.75), image_color=(1,1,1,1), frameSize=(-0.5,
         0.5,
         -0.45,
         -0.05))

        self.font = loader.loadFont("phase_3/models/fonts/MickeyFont.bam")
        self.helpText = DirectLabel(scale=1.1, relief=None, text_pos=(0, 0.2), text_wordwrap=16, text=TTLocalizer.GardenDropHelpTitle, text_font=self.font, pos=(0.0, 0.0, 0.0), text_scale=0.1, text0_fg=(1, 1, 1, 1), parent=self.helpFrame)

        self.font2 = loader.loadFont("phase_3/models/fonts/Comedy.bam")
        self.helpText2 = DirectLabel(scale=1.1, relief=None, text_pos=(-0.6, 0.1), text_wordwrap=15, text=TTLocalizer.GardenDropInstructions, text_font=self.font2, pos=(0.0, 0.0, 0.0), text_scale=0.085, text0_fg=(0, 0, 0, 1), parent=self.helpFrame, text_align=TextNode.ALeft)

        gui2 = loader.loadModel('phase_3/models/gui/quit_button.bam')
        self.backButton = DirectButton(parent=self.helpFrame, relief=None, image=(gui2.find('**/QuitBtn_UP'), gui2.find('**/QuitBtn_DN'), gui2.find('**/QuitBtn_RLVR')), pos=(0.5, 1.0, -0.32), scale=0.9, text=TTLocalizer.GardenDropBackToGame, text_font=self.font, text0_fg=(1, 1, 1, 1), text1_fg=(1, 1, 1, 1), text2_fg=(1, 1, 1, 1), text_scale=0.045, text_pos=(0, -0.01), command=self.unloadHelp)

        return True

    def addSprite(self, image, size = 0.5, posX = 0, posZ = 0, found = 0):
        nodeObj = DirectLabel(parent=self.frame, relief=None, image=image, pos=(posX, 0.0, posZ), scale=size, image_color=(1.0, 1.0, 1.0, 1))
        if LevelNumber == 1 or LevelNumber == 2:
            colorChoice = random.choice(range(0, 3))
        if LevelNumber == 3 or LevelNumber == 4:
            colorChoice = random.choice(range(0, 4))
        if LevelNumber == 5:
            colorChoice = random.choice(range(0, 5))

        newSprite = GameSprite.GameSprite(nodeObj, colorChoice, found)
        self.sprites.append(newSprite)

        if found:
            self.foundCount += 1

        return newSprite

    def addUnSprite(self, image, size = 0.5, posX = 0, posZ = 0):
        nodeObj = DirectLabel(parent=self.frame, relief=None, image=image, pos=(posX, 0.0, posZ), scale=size, image_color=(1.0, 1.0, 1.0, 1))

        newSprite = GameSprite.GameSprite(nodeObj)
        newSprite = GameSprite.GameSprite(nodeObj)

        return newSprite

    def testPointDistanceSquare(self, x1, z1, x2, z2):
        distX = x1 - x2
        distZ = z1 - z2
        distC = distX * distX + distZ * distZ

        if distC == 0:
            distC = 1e-10

        return distC

    def testDistance(self, nodeA, nodeB):
        distX = nodeA.getX() - nodeB.getX()
        distZ = nodeA.getZ() - nodeB.getZ()
        distC = distX * distX + distZ * distZ
        dist = math.sqrt(distC)

        return dist

    def testGridfull(self, cell):
        if not cell:
            return 0
        elif cell[0] != None:
            return 1
        else:
            return 0

        returnTrue

    def getValidGrid(self, x, z):
        if x < 0 or x >= GardenGameGlobals.gridDimX:
            return None
        elif z < 0 or z >= GardenGameGlobals.gridDimZ:
            return None
        else:
            return self.grid[x][z]

        return None

    def getColorType(self, x, z):
        if x < 0 or x >= GardenGameGlobals.gridDimX:
            return -1
        elif z < 0 or z >= GardenGameGlobals.gridDimZ:
            return -1
        elif self.grid[x][z][0] == None:
            return -1
        else:
            return self.grid[x][z][0].colorType

        return True

    def getSprite(self, spriteIndex):
        if spriteIndex >= len(self.sprites) or self.sprites[spriteIndex].markedForDeath:
            return None
        else:
            return self.sprites[spriteIndex]

        return None

    def findGrid(self, x, z, force = 0):
        currentClosest = None
        currentDist = 10000000

        for countX in xrange(GardenGameGlobals.gridDimX):
            for countZ in xrange(GardenGameGlobals.gridDimZ):
                testDist = self.testPointDistanceSquare(x, z, self.grid[countX][countZ][1], self.grid[countX][countZ][2])
                if self.grid[countX][countZ][0] == None and testDist < currentDist and (force or self.hasNeighbor(countX, countZ)):
                    currentClosest = self.grid[countX][countZ]
                    self.closestX = countX
                    self.closestZ = countZ
                    currentDist = testDist

        return currentClosest

    def findGridCog(self):
        GardenGameGlobals.cogX = 0
        GardenGameGlobals.cogZ = 0
        self.massCount = 0

        for row in self.grid:
            for cell in row:
                if cell[0] != None:
                    GardenGameGlobals.cogX += cell[1]
                    GardenGameGlobals.cogZ += cell[2]
                    self.massCount += 1

        if self.massCount > 0:
            self.cogX = (GardenGameGlobals.cogX / self.massCount)
            self.cogZ = (GardenGameGlobals.cogZ / self.massCount)
            self.cogSprite.setX(self.cogX)
            self.cogSprite.setZ(self.cogZ)
        else:
            self.doOnClearGrid()

        return True

    def stickInGrid(self, sprite, force = 0):
        if sprite.isActive and not sprite.isQue:
            gridCell = self.findGrid(sprite.getX(), sprite.getZ(), force)

            if gridCell:
                gridCell[0] = sprite
                sprite.setActive(0)
                sprite.setX(gridCell[1])
                sprite.setZ(gridCell[2])
                self.createMatchList(self.closestX, self.closestZ)

                if len(self.matchList) >= 3:
                    self.clearMatchList()
                self.findGridCog()

    def fillMatchList(self, cellX, cellZ):
        if (cellX, cellZ) in self.matchList:
            return True

        self.matchList.append((cellX, cellZ))
        colorType = self.grid[cellX][cellZ][0].colorType

        if cellZ % 2 == 0:
            if self.getColorType(cellX - 1, cellZ) == colorType:
                self.fillMatchList(cellX - 1, cellZ)

            if self.getColorType(cellX + 1, cellZ) == colorType:
                self.fillMatchList(cellX + 1, cellZ)

            if self.getColorType(cellX, cellZ + 1) == colorType:
                self.fillMatchList(cellX, cellZ + 1)

            if self.getColorType(cellX + 1, cellZ + 1) == colorType:
                self.fillMatchList(cellX + 1, cellZ + 1)

            if self.getColorType(cellX, cellZ - 1) == colorType:
                self.fillMatchList(cellX, cellZ - 1)

            if self.getColorType(cellX + 1, cellZ - 1) == colorType:
                self.fillMatchList(cellX + 1, cellZ - 1)
        else:
            if self.getColorType(cellX - 1, cellZ) == colorType:
                self.fillMatchList(cellX - 1, cellZ)

            if self.getColorType(cellX + 1, cellZ) == colorType:
                self.fillMatchList(cellX + 1, cellZ)

            if self.getColorType(cellX, cellZ + 1) == colorType:
                self.fillMatchList(cellX, cellZ + 1)

            if self.getColorType(cellX - 1, cellZ + 1) == colorType:
                self.fillMatchList(cellX - 1, cellZ + 1)

            if self.getColorType(cellX, cellZ - 1) == colorType:
                self.fillMatchList(cellX, cellZ - 1)

            if self.getColorType(cellX - 1, cellZ - 1) == colorType:
                self.fillMatchList(cellX - 1, cellZ - 1)

    def createMatchList(self, x, z):
        self.matchList = []
        self.fillMatchList(x, z)

    def clearMatchList(self):
        for entry in self.matchList:
            gridEntry = self.grid[entry[0]][entry[1]]
            sprite = gridEntry[0]
            gridEntry[0] = None
            sprite.markedForDeath = 1

        return True

    def hasNeighbor(self, cellX, cellZ):
        gotNeighbor = 0

        if cellZ % 2 == 0:
            if self.testGridfull(self.getValidGrid(cellX - 1, cellZ)):
                gotNeighbor = 1
            elif self.testGridfull(self.getValidGrid(cellX + 1, cellZ)):
                gotNeighbor = 1
            elif self.testGridfull(self.getValidGrid(cellX, cellZ + 1)):
                gotNeighbor = 1
            elif self.testGridfull(self.getValidGrid(cellX + 1, cellZ + 1)):
                gotNeighbor = 1
            elif self.testGridfull(self.getValidGrid(cellX, cellZ - 1)):
                gotNeighbor = 1
            elif self.testGridfull(self.getValidGrid(cellX + 1, cellZ - 1)):
                gotNeighbor = 1
        elif self.testGridfull(self.getValidGrid(cellX - 1, cellZ)):
            gotNeighbor = 1
        elif self.testGridfull(self.getValidGrid(cellX + 1, cellZ)):
            gotNeighbor = 1
        elif self.testGridfull(self.getValidGrid(cellX, cellZ + 1)):
            gotNeighbor = 1
        elif self.testGridfull(self.getValidGrid(cellX - 1, cellZ + 1)):
            gotNeighbor = 1
        elif self.testGridfull(self.getValidGrid(cellX, cellZ - 1)):
            gotNeighbor = 1
        elif self.testGridfull(self.getValidGrid(cellX - 1, cellZ - 1)):
            gotNeighbor = 1

        return gotNeighbor

    def __colTest(self):
        if not hasattr(self, 'tick'):
            self.tick = 0

        self.tick += 1

        if self.tick > 5:
            self.tick = 0
        sizeSprites = len(self.sprites)

        for movingSpriteIndex in xrange(len(self.sprites)):
            for testSpriteIndex in xrange(movingSpriteIndex, len(self.sprites)):
                movingSprite = self.getSprite(movingSpriteIndex)
                testSprite = self.getSprite(testSpriteIndex)

                if testSprite and movingSprite:
                    if movingSpriteIndex != testSpriteIndex and (movingSprite.isActive or testSprite.isActive):
                        if movingSprite.isQue or testSprite.isQue:
                            if self.testDistance(movingSprite.nodeObj, testSprite.nodeObj) < GardenGameGlobals.queExtent * (movingSprite.size + testSprite.size):
                                self.push(movingSprite, testSprite)
                        elif self.testDistance(movingSprite.nodeObj, testSprite.nodeObj) < movingSprite.size + testSprite.size:
                            if movingSprite.isActive:
                                testSprite.isActive or self.__collide(movingSprite, testSprite)

                        if self.testDistance(self.cogSprite.nodeObj, testSprite.nodeObj) < (self.cogSprite.size + testSprite.size):
                            if movingSprite.isActive:
                                self.stickInGrid(testSprite, 1)

                        if self.tick == 5:
                            pass

    def __collide(self, move, test):
        queHit = 0

        if move.isQue:
            que = move
            hit = test
            queHit = 1
        elif test.isQue:
            que = test
            hit = move
            queHit = 1
        else:
            test.velX = 0
            test.velZ = 0
            move.velX = 0
            move.velZ = 0
            test.collide()
            move.collide()
            self.stickInGrid(move,1)
            self.stickInGrid(test,1)

        if queHit:
            forceM = 0.1
            distX = que.getX() - hit.getX()
            distZ = que.getZ() - hit.getZ()
            self.stickInGrid(move,1)
            self.stickInGrid(test,1)

    def push(self, move, test):
        queHit = 0

        if move.isQue:
            que = move
            hit = test
            queHit = 1
        elif test.isQue:
            que = test
            hit = move
            queHit = 1

        if queHit:
            forceM = 0.1
            dist = self.testDistance(move.nodeObj, test.nodeObj)

            if abs(dist) < GardenGameGlobals.queExtent * que.size and abs(dist) > 0:
                scaleSize = GardenGameGlobals.queExtent * que.size * 0.5
                distFromPara = abs(abs(dist) - scaleSize)
                force = (scaleSize - distFromPara) / scaleSize * (dist / abs(dist))
                angle = self.angleTwoSprites(que, hit)

                if angle < 0:
                    angle = angle + 2 * pi

                if angle > pi * 2.0:
                    angle = angle - 2 * pi

                newAngle = pi * 1.0

                if angle > pi * 1.5 or angle < pi * 0.5:
                    newAngle = pi * 0.0

                hit.addForce(forceM * force, newAngle)

    def angleTwoSprites(self, sprite1, sprite2):
        x1 = sprite1.getX()
        z1 = sprite1.getZ()
        x2 = sprite2.getX()
        z2 = sprite2.getZ()
        x = x2 - x1
        z = z2 - z1
        angle = math.atan2(-x, z)

        return angle + pi * 0.5

    def doOnClearGrid(self):
        secondSprite = self.addSprite(self.block, posX=GardenGameGlobals.newBallX, posZ=0.0, found=1)
        secondSprite.addForce(0, 1.55 * pi)
        self.stickInGrid(secondSprite, 1)

    def __run(self, Task):
        if self.lastTime == None:
            self.lastTime = globalClock.getRealTime()

        timeDelta = 0.0265
        self.lastTime = globalClock.getRealTime()
        GardenGameGlobals.newBallCountUp += timeDelta

        if base.mouseWatcherNode.hasMouse():
            x = base.mouseWatcherNode.getMouseX()
            y = base.mouseWatcherNode.getMouseY()
            self.queBall.setX(x)
            self.queBall.setZ(y)

        for sprite in self.sprites:
            sprite.run(timeDelta)
            if sprite.getX() > GardenGameGlobals.maxX:
                sprite.setX(GardenGameGlobals.maxX)
                sprite.velX = -sprite.velX

            if sprite.getX() < GardenGameGlobals.minX:
                sprite.setX(GardenGameGlobals.minX)
                sprite.velX = -sprite.velX

            if sprite.getZ() > GardenGameGlobals.maxZ:
                sprite.setZ(GardenGameGlobals.maxZ)
                sprite.velZ = -sprite.velZ

            if sprite.getZ() < GardenGameGlobals.minZ:
                self.stickInGrid(sprite, 1)

            if sprite.isActive:
                sprite.addForce(timeDelta * 0.9, pi * 1.5)

        self.queBall.velX = (self.queBall.getX() - self.queBall.prevX) / timeDelta
        self.queBall.velZ = (self.queBall.getZ() - self.queBall.prevZ) / timeDelta
        self.__colTest()

        for sprite in self.sprites:
            if sprite.markedForDeath:
                if sprite.foundation:
                    self.foundCount -= 1

                self.sprites.remove(sprite)
                sprite.delete()

        if GardenGameGlobals.controlSprite == None:
            self.addControlSprite(GardenGameGlobals.newBallX, GardenGameGlobals.newBallZ)
            GardenGameGlobals.newBallCountUp = 0.0

        if GardenGameGlobals.newBallCountUp >= GardenGameGlobals.newBallTime:
            self.addControlSprite(GardenGameGlobals.newBallX, GardenGameGlobals.newBallZ)
            GardenGameGlobals.newBallCountUp = 0.0

        if not GardenGameGlobals.controlSprite.isActive:
            GardenGameGlobals.controlSprite = None

        if self.foundCount <= 0:
            self.__handleWin()

        return Task.cont

    def loadStartingSprites(self, levelNum):
        self.queBall = self.addSprite(self.block, posX=0.25, posZ=0.5, found=0)
        self.queBall.setColor(GardenGameGlobals.colorWhite)
        self.queBall.isQue = 1

        GardenGameGlobals.controlSprite = None
        self.cogSprite = self.addUnSprite(self.block, posX=0.25, posZ=0.5)
        self.cogSprite.setColor(GardenGameGlobals.colorBlack)

        for ball in xrange(0, levelNum):
            place = random.random() * GardenGameGlobals.rangeX
            self.newSprite = self.addSprite(self.block, size=0.5, posX=GardenGameGlobals.minX + place, posZ=0.0, found=1)
            self.stickInGrid(self.newSprite, 1)

    def __handlePlay(self):
        if hasattr(base, 'localAvatar'):
            base.cr.playGame.getPlace().fsm.forceTransition('stopped')

        self.reinitialize()
        self.load()

        self.itemboard = self.model.find('**/item_board')
        self.block = self.model1.find('**/minnieCircle')

        size = 0.085
        sizeZ = size * 0.8

        for countX in xrange(GardenGameGlobals.gridDimX):
            newRow = []
            for countZ in xrange(GardenGameGlobals.gridDimZ):
                offset = 0
                if countZ % 2 == 0:
                    offset = size / 2
                newRow.append([None, countX * size + GardenGameGlobals.minX + offset, countZ * sizeZ + GardenGameGlobals.minZ])

            self.grid.append(newRow)

        if LevelNumber == 1:
            self.loadStartingSprites(3)
        elif LevelNumber == 2:
            self.loadStartingSprites(5)
        elif LevelNumber == 3:
            self.loadStartingSprites(7)
        elif LevelNumber == 4:
            self.loadStartingSprites(10)
        elif LevelNumber == 5:
            self.loadStartingSprites(15)
        base.taskMgr.add(self._GardenDropGame__run,"MouseCheck")

        if hasattr(self, 'victoryFrame'):
            self.victoryFrame.removeNode()
            del self.victoryFrame

    def addControlSprite(self, x = 0.0, z = 0.0):
        newSprite = self.addSprite(self.block, posX=x, posZ=z)
        GardenGameGlobals.controlSprite = newSprite

    def playGardenDrop(self):
        self.GDButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.font = loader.loadFont("phase_3/models/fonts/MickeyFont.bam")
        self.yellowButton = (self.GDButtonImage.find('**/QuitBtn_UP'), self.GDButtonImage.find('**/QuitBtn_DN'), self.GDButtonImage.find('**/QuitBtn_RLVR'))

        self.GardenGameButton = DirectButton(frameSize=(0), text=TTLocalizer.GardenDropButtonTitle, image=self.yellowButton, text_pos=(0,0.01), relief=None, text_fg=(1, 1, 1, 1), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, command=self.deleteGDButton, pos=(0.49, 0, 0.115), text_font=self.font, text_scale=(0.083,0.040,0.049), borderWidth=(0.13, 0.01), scale=(0.8,1,1.8))
        self.GardenGameButton.reparentTo(base.a2dBottomLeft)
        base.localAvatar.gardenGameButton = self.GardenGameButton

    def __openHelp(self):
        self.unload()
        self.help()
        base.taskMgr.remove('MouseCheck')

    def unload(self):
        self.frame.destroy()
        del self.frame

        if (GardenGameGlobals.acceptErrorDialog and GardenGameGlobals.acceptErrorDialog.cleanup()):
            GardenGameGlobals.acceptErrorDialog = 1

    def unloadHelp(self):
        self.helpFrame.removeNode()
        self._GardenDropGame__handlePlay()

    def deleteGDButton(self):
        self.GardenGameButton.removeNode()
        self.__handlePlay()

    def __handleExit(self):
        self._GardenDropGame__acceptExit()

    def __acceptExit(self, buttonValue = None):
        global LevelNumber
        if hasattr(base, 'localAvatar'):
            base.cr.playGame.getPlace().fsm.forceTransition('walk')

        self.playGardenDrop()
        if (hasattr(self, 'frame') and self.frame.hide()):
            self.unload()
            messenger.send(GardenGameGlobals.doneEvent)

        LevelNumber = 1
        base.taskMgr.remove('MouseCheck')

    def __handleWin(self):
        global LevelNumber
        self.unload()
        self.loadWin()
        LevelNumber += 1
        base.taskMgr.remove('MouseCheck')

    def loadWin(self):
        model = loader.loadModel('phase_5.5/models/gui/package_delivery_panel.bam')
        model1 = loader.loadModel('phase_3.5/models/gui/matching_game_gui.bam')

        self.model = model
        self.model1 = model1

        background = model.find('**/bg')
        itemBoard = model.find('**/item_board')

        frameGui = loader.loadModel('phase_3/models/gui/dialog_box_gui.bam')
        self.victoryFrame = DirectFrame(scale=1.1, relief=None, image=frameGui, image_scale=(1.75, 1, 0.75), image_color=(1,1,1,1), frameSize=(-0.5,
         0.5,
         -0.45,
         -0.05))

        frameGui2 = loader.loadModel('phase_3.5/models/gui/jar_gui.bam')
        self.jar = DirectFrame(parent=self.victoryFrame, scale=(0.65,1.4,1.3), relief=None, image=frameGui2, image_scale=(1.75, 1, 0.75), image_color=(1,1,1,1), pos=(-0.5,-0.15,-0.075), frameSize=(-0.5,
         0.45,
         -0.45,
         -0.05))

        gui2 = loader.loadModel('phase_3/models/gui/quit_button.bam')
        self.font = loader.loadFont("phase_3/models/fonts/MickeyFont.bam")

        if LevelNumber == 5:
            congratsMessage = TTLocalizer.GardenDropWinGame
        else:
            congratsMessage = TTLocalizer.GardenDropProgressLevels
            self.nextButton = DirectButton(parent=self.victoryFrame, relief=None, image=(gui2.find('**/QuitBtn_UP'), gui2.find('**/QuitBtn_DN'), gui2.find('**/QuitBtn_RLVR')), pos=(0, 1.0, -0.32), scale=0.9, text=TTLocalizer.lNext, text_font=self.font, text0_fg=(1, 1, 1, 1), text1_fg=(1, 1, 1, 1), text2_fg=(1, 1, 1, 1), text_scale=0.045, text_pos=(0, -0.01), command=self._GardenDropGame__handlePlay)

        self.congratsText = DirectLabel(scale=1.1, relief=None, text_pos=(0, 0.2), text_wordwrap=16, text=TTLocalizer.GardenDropCongradulations, text_font=self.font, pos=(0.0, 0.0, 0.0), text_scale=0.1, text0_fg=(1, 1, 1, 1), parent=self.victoryFrame)

        self.font2 = loader.loadFont("phase_3/models/fonts/Comedy.bam")
        self.congratsText2 = DirectLabel(scale=1.1, relief=None, text_pos=(0.2, 0.025), text_wordwrap=10, text=congratsMessage, text_font=self.font2, pos=(0.0, 0.0, 0.0), text_scale=0.085, text0_fg=(0, 0, 0, 1), parent=self.victoryFrame)

        self.quitButton = DirectButton(parent=self.victoryFrame, relief=None, image=(gui2.find('**/QuitBtn_UP'), gui2.find('**/QuitBtn_DN'), gui2.find('**/QuitBtn_RLVR')), pos=(0.5, 1.0, -0.32), scale=0.9, text=TTLocalizer.GardenDropExit, text_font=self.font, text0_fg=(1, 1, 1, 1), text1_fg=(1, 1, 1, 1), text2_fg=(1, 1, 1, 1), text_scale=0.045, text_pos=(0, -0.01), command=self.__handleExitWin)

        return True

    def unloadWin(self):
        self.victoryFrame.removeNode()
        del self.victoryFrame

        if GardenGameGlobals.acceptErrorDialog:
            GardenGameGlobals.acceptErrorDialog.cleanup()
            GardenGameGlobals.acceptErrorDialog = None

        self.playGardenDrop()
        base.taskMgr.remove('gameTask')

        return True

    def __handleExitWin(self):
        global LevelNumber
        self._GardenDropGame__acceptExitWin()
        LevelNumber = 1

    def __acceptExitWin(self, buttonValue = None):
        if hasattr(base, 'localAvatar'):
            base.cr.playGame.getPlace().fsm.forceTransition('walk')

        if hasattr(self, 'victoryFrame'):
            self.unloadWin()
            messenger.send(GardenGameGlobals.doneEvent)

    def endGame(self):
        if hasattr(base, 'localAvatar'):
            base.localAvatar.gardenGameButton.removeNode()

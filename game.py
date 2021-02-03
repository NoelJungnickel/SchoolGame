import pygame, sys
from pygame.locals import *
from shapeCreator import Entry, Label, Button
from characterCreator import Character
from fightingScreen import Fight

pygame.init()

icon = pygame.image.load(r'C:\Users\Noel\Pictures\Kochium2.png')

winName = "Start"
winWidth = 1600
winHeight = 900
#winWidth = 1920
#winHeight = 1080

pygame.display.set_caption(winName)
win = pygame.display.set_mode((winWidth, winHeight))
#win = pygame.display.set_mode((winWidth, winHeight), pygame.FULLSCREEN)
pygame.display.set_icon(icon)
            
class Game():
    def __init__(self):
        self.win = win
        self.winName = winName
        self.gameRun = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.click = False
        self.gridX = 1
        self.gridY = 1
        self.vel = 5
        self.characterX = 100
        self.characterY = 100
        self.character = Character(self.win, self.characterX, self.characterY, r'C:\Users\Noel\Pictures\Kochium2.png')

    """def creator(self):
        self.createOptionsScreen()"""
        
    def mainloopGame1(self):
        self.createOptionsScreen()

        while self.gameRun:
            self.clock.tick(self.FPS)
            self.win.fill((204, 204, 204))
            self.placeGame()
            self.keyPressGame()
            self.screen1 = Label(self.win, "1", 500, 500, (255, 0, 0), 200)
            self.screen1.drawLetter()

            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.startRun = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.escScreen()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    def mainloopGame2(self):

        while self.gameRun:
            self.clock.tick(self.FPS)
            self.win.fill((204, 204, 204))
            self.placeGame()
            self.keyPressGame()
            self.screen2 = Label(self.win, "2", 500, 500, (255, 0, 0), 200)
            self.screen2.drawLetter()

            self.triggerFight = Button(self.win, (255, 255, 255), 600, 600, 80, 50, text = 'FIGHT', textColor = (0, 0, 255), textSize = 50)
            self.triggerFight.drawButton()

            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.startRun = False
                if self.triggerFight.checkCollisionRect(self.character.characterToRect()) and event.type == KEYDOWN:
                    if event.key == K_m:
                        Fight().fightLoop()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.escScreen()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    def mainloopGame3(self):

        while self.gameRun:
            self.clock.tick(self.FPS)
            self.win.fill((204, 204, 204))
            self.placeGame()
            self.keyPressGame()
            self.screen3 = Label(self.win, "3", 500, 500, (255, 0, 0), 200)
            self.screen3.drawLetter()

            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.startRun = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.escScreen()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    def mainloopGame4(self):

        while self.gameRun:
            self.clock.tick(self.FPS)
            self.win.fill((204, 204, 204))
            self.placeGame()
            self.keyPressGame()
            self.screen4= Label(self.win, "4", 500, 500, (255, 0, 0), 200)
            self.screen4.drawLetter()

            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.startRun = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.escScreen()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    def mainloopGame5(self):

        while self.gameRun:
            self.clock.tick(self.FPS)
            self.win.fill((204, 204, 204))
            self.placeGame()
            self.keyPressGame()
            self.screen5 = Label(self.win, "5", 500, 500, (255, 0, 0), 200)
            self.screen5.drawLetter()

            self.levelUp = Button(self.win, (255, 255, 255), 300, 300, 80, 50, text = 'levelUp', textColor = (0, 0, 255), textSize = 50)
            self.levelUp.drawButton()
            self.level = Label(self.win, str(self.character.level), 800, 500, (0, 255, 0), 200)
            self.level.drawLetter()
            if self.levelUp.checkCollisionRect(self.character.characterToRect()):
                self.character.levelUp()

            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.startRun = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.escScreen()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    def mainloopGame6(self):

        while self.gameRun:
            self.clock.tick(self.FPS)
            self.win.fill((204, 204, 204))
            self.placeGame()
            self.keyPressGame()
            self.screen6 = Label(self.win, "6", 500, 500, (255, 0, 0), 200)
            self.screen6.drawLetter()

            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.startRun = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.escScreen()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    def mainloopGame7(self):

        while self.gameRun:
            self.clock.tick(self.FPS)
            self.win.fill((204, 204, 204))
            self.placeGame()
            self.keyPressGame()
            self.screen7 = Label(self.win, "7", 500, 500, (255, 0, 0), 200)
            self.screen7.drawLetter()

            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.startRun = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.escScreen()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    def mainloopGame8(self):

        while self.gameRun:
            self.clock.tick(self.FPS)
            self.win.fill((204, 204, 204))
            self.placeGame()
            self.keyPressGame()
            self.screen8 = Label(self.win, "8", 500, 500, (255, 0, 0), 200)
            self.screen8.drawLetter()

            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.startRun = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.escScreen()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    def mainloopGame9(self):
  
        while self.gameRun:
            self.clock.tick(self.FPS)
            self.win.fill((204, 204, 204))
            self.placeGame()
            self.keyPressGame()
            self.screen9 = Label(self.win, "9", 500, 500, (255, 0, 0), 200)
            self.screen9.drawLetter()

            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.startRun = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.escScreen()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    def placeGame(self):
        self.character.drawCharacter()

    def loadMainloop(self):
        if self.gridX == 1 and self.gridY == 1:
            self.mainloopGame1()
        elif self.gridX == 2 and self.gridY == 1:
            self.mainloopGame2()
        elif self.gridX == 3 and self.gridY == 1:
            self.mainloopGame3()
        elif self.gridX == 1 and self.gridY == 2:
            self.mainloopGame4()
        elif self.gridX == 2 and self.gridY == 2:
            self.mainloopGame5()
        elif self.gridX == 3 and self.gridY == 2:
            self.mainloopGame6()
        elif self.gridX == 1 and self.gridY == 3:
            self.mainloopGame7()
        elif self.gridX == 2 and self.gridY == 3:
            self.mainloopGame8()
        elif self.gridX == 3 and self.gridY == 3:
            self.mainloopGame9()

    def checkEdgesW(self, keys):
        if eval(f'keys[pygame.K_{self.wEntry.text.lower()}]'):
            if self.gridY != 1:
                self.gridY -= 1
                self.character.y += self.winHeight - self.character.getCharacterHeight()
                self.loadMainloop()

    def checkEdgesA(self, keys):
        if eval(f'keys[pygame.K_{self.aEntry.text.lower()}]'):
            if self.gridX != 1:
                self.gridX -= 1
                self.character.x += self.winWidth - self.character.getCharacterWidth()
                self.loadMainloop()

    def checkEdgesS(self, keys):
        if eval(f'keys[pygame.K_{self.sEntry.text.lower()}]'):
            if self.gridY != 3:
                self.gridY += 1
                self.character.y -= self.winHeight - self.character.getCharacterHeight()
                self.loadMainloop()

    def checkEdgesD(self, keys):
        if eval(f'keys[pygame.K_{self.dEntry.text.lower()}]'):
            if self.gridX != 3:
                self.gridX += 1
                self.character.x -= self.winWidth - self.character.getCharacterWidth()
                self.loadMainloop()

    def keyPressGame(self):
        keys = pygame.key.get_pressed()

        if eval(f'keys[pygame.K_{self.wEntry.text.lower()}]'):
            if self.character.y <= 0:
                self.checkEdgesW(keys)
            else:
                if eval(f'keys[pygame.K_{self.kEntry.text.lower()}]'):
                    self.character.y -= self.character.sprintVel
                else:
                    self.character.y -= self.character.vel

        if eval(f'keys[pygame.K_{self.aEntry.text.lower()}]'):
            if self.character.x <= 0:
                self.checkEdgesA(keys)
            else:
                if eval(f'keys[pygame.K_{self.kEntry.text.lower()}]'):
                    self.character.x -= self.character.sprintVel
                else:
                    self.character.x -= self.character.vel

        if eval(f'keys[pygame.K_{self.sEntry.text.lower()}]'):
            if self.character.y >= winHeight - self.character.getCharacterWidth():
                self.checkEdgesS(keys)
            else:
                if eval(f'keys[pygame.K_{self.kEntry.text.lower()}]'):
                    self.character.y += self.character.sprintVel
                else:
                    self.character.y += self.character.vel

        if eval(f'keys[pygame.K_{self.dEntry.text.lower()}]'):
            if self.character.x >= winWidth - self.character.getCharacterHeight():
                self.checkEdgesD(keys)
            else:
                if eval(f'keys[pygame.K_{self.kEntry.text.lower()}]'):
                    self.character.x += self.character.sprintVel
                else:
                    self.character.x += self.character.vel

        if eval(f'keys[pygame.K_{self.lEntry.text.lower()}]'):
            Game().inventoryLoop()

    def escScreen(self):
        self.escRun = True
        self.createEscScreen()

        while self.escRun:
            self.clock.tick(self.FPS)
            self.win.fill((0, 0, 0))
            self.placeEscScreen()
            self.buttonPressEscScreen()
            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.escRun = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    def createEscScreen(self):
        self.continueButton = Button(self.win, (36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 - 100, 200, 50, "CONTINUE")
        self.optionsButton = Button(self.win, (36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 - 25, 200, 50, "OPTIONS")
        self.exitButtonStartScreen = Button(self.win, (36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 + 50, 200, 50, "EXIT")

    def placeEscScreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)
        self.continueButton.drawButton()
        self.optionsButton.drawButton()
        self.exitButtonStartScreen.drawButton()

    def buttonPressEscScreen(self):
        mousePos = pygame.mouse.get_pos()
    
        if self.continueButton.checkCollision(mousePos):
            self.continueButton.color = (0, 255, 0)
            if self.click:
                self.escRun = False
        else:
            self.continueButton.color = (36, 36, 36)
        
        if self.optionsButton.checkCollision(mousePos):
            self.optionsButton.color = (0, 0, 255)
            if self.click:
                self.mainloopOptionsMenu()
        else:
            self.optionsButton.color = (36, 36, 36)

        if self.exitButtonStartScreen.checkCollision(mousePos):
            self.exitButtonStartScreen.color = (255, 0, 0)
            if self.click:
                exit()
        else:
            self.exitButtonStartScreen.color = (36, 36, 36)

    def mainloopOptionsMenu(self):
        self.optionsRun = True
        self.createOptionsScreen()

        while self.optionsRun:
            self.clock.tick(self.FPS)
            self.win.fill((0, 0, 0))
            self.placeOptionsScreen()
            self.buttonPressOptionsScreen()
            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.optionsRun = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                for entry in self.entryList:
                    entry.activateEntry(event)
                    entry.editEntry(event)
    
    def createOptionsScreen(self):
        self.commandsLabel = Label(self.win, "COMMANDS", 60,60)
        self.keysLabel = Label(self.win, "KEYS", self.winWidth/2 + 10, 60)
        self.upKeyLetter = Label(self.win, "MOVE UP", 60, 210)
        self.leftKeyLetter = Label(self.win, "MOVE LEFT", 60, 285)
        self.downKeyLetter = Label(self.win, "MOVE DOWN", 60, 360)
        self.rightKeyLetter = Label(self.win, "MOVE RIGHT", 60, 435)
        self.interactKeyLetter = Label(self.win, "INTERACT", 60, 510)
        self.sprintKeyLetter = Label(self.win, "SPRINT", 60, 585)
        self.inventoryKeyLetter = Label(self.win, "INVENTORY", 60, 660)
        self.labelList = [self.commandsLabel, self.keysLabel, self.upKeyLetter, self.leftKeyLetter, self.downKeyLetter, self.rightKeyLetter, self.interactKeyLetter, self.sprintKeyLetter, self.inventoryKeyLetter]

        self.exitButtonOptionsScreen = Button(self.win, (36, 36, 36), self.winWidth - 250, self.winHeight - 100, 200, 50, "EXIT")
        self.backButtonOptionsScreen = Button(self.win, (36, 36, 36), 50, self.winHeight - 100, 200, 50, "BACK")
        self.topBarLabel = Button(self.win, (36, 36, 36), 50, 50, self.winWidth - 100, 50)
        self.wKeyLabel = Button(self.win, (36, 36, 36), 50, 200, self.winWidth - 100, 50, "|")
        self.aKeyLabel = Button(self.win, (36, 36, 36), 50, 275, self.winWidth - 100, 50, "|")
        self.sKeyLabel = Button(self.win, (36, 36, 36), 50, 350, self.winWidth - 100, 50, "|")
        self.dKeyLabel = Button(self.win, (36, 36, 36), 50, 425, self.winWidth - 100, 50, "|")
        self.mKeyLabel = Button(self.win, (36, 36, 36), 50, 500, self.winWidth - 100, 50, "|")
        self.kKeyLabel = Button(self.win, (36, 36, 36), 50, 575, self.winWidth - 100, 50, "|")
        self.lKeyLabel = Button(self.win, (36, 36, 36), 50, 650, self.winWidth - 100, 50, "|")
        self.buttonList = [self.exitButtonOptionsScreen, self.backButtonOptionsScreen, self.topBarLabel, self.wKeyLabel, self.aKeyLabel, self.sKeyLabel, self.dKeyLabel, self.mKeyLabel, self.kKeyLabel, self.lKeyLabel]

        self.wEntry = Entry(self.win, self.winWidth/2 + 8, 208, 35, 33, (36, 36, 36), "W")
        self.aEntry = Entry(self.win, self.winWidth/2 + 8, 283, 35, 33, (36, 36, 36), "A")
        self.sEntry = Entry(self.win, self.winWidth/2 + 8, 358, 35, 33, (36, 36, 36), "S")
        self.dEntry = Entry(self.win, self.winWidth/2 + 8, 433, 35, 33, (36, 36, 36), "D")
        self.mEntry = Entry(self.win, self.winWidth/2 + 8, 508, 35, 33, (36, 36, 36), "M")
        self.kEntry = Entry(self.win, self.winWidth/2 + 8, 583, 35, 33, (36, 36, 36), "K")
        self.lEntry = Entry(self.win, self.winWidth/2 + 8, 658, 35, 33, (36, 36, 36), "L")
        self.entryList = [self.wEntry, self.aEntry, self.sEntry, self.dEntry, self.mEntry, self.kEntry, self.lEntry]

    def placeOptionsScreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)

        for button in self.buttonList:
            button.drawButton()

        for label in self.labelList:
            label.drawLetter()

        for entry in self.entryList:
            entry.drawEntry()
        

    def buttonPressOptionsScreen(self):
        mousePos = pygame.mouse.get_pos()

        if self.exitButtonOptionsScreen.checkCollision(mousePos):
            self.exitButtonOptionsScreen.color = (255, 0, 0)
            if self.click:
                exit()
        else:
            self.exitButtonOptionsScreen.color = (36, 36, 36)

        if self.backButtonOptionsScreen.checkCollision(mousePos):
            self.backButtonOptionsScreen.color = (255, 0, 0)
            if self.click:
                self.optionsRun = False
        else:
            self.backButtonOptionsScreen.color = (36, 36, 36)

    def inventoryLoop(self):
        self.inventoryRun = True
        self.createInventoryScreen()

        while self.inventoryRun:
            self.clock.tick(self.FPS)
            self.win.fill((0, 0, 0))
            self.placeInventoryScreen()
            self.buttonPressInventoryScreen()
            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.inventoryRun = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    def createInventoryScreen(self):
        self.exitButtonInventoryScreen = Button(self.win, (36, 36, 36), self.winWidth - 250, self.winHeight - 100, 200, 50, "EXIT")
        self.backButtonInventoryScreen = Button(self.win, (36, 36, 36), 50, self.winHeight - 100, 200, 50, "BACK")

    def placeInventoryScreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)
        self.exitButtonInventoryScreen.drawButton()
        self.backButtonInventoryScreen.drawButton()
    
    def buttonPressInventoryScreen(self):
        mousePos = pygame.mouse.get_pos()

        if self.exitButtonInventoryScreen.checkCollision(mousePos):
            self.exitButtonInventoryScreen.color = (255, 0, 0)
            if self.click:
                exit()
        else:
            self.exitButtonInventoryScreen.color = (36, 36, 36)

        if self.backButtonInventoryScreen.checkCollision(mousePos):
            self.backButtonInventoryScreen.color = (255, 0, 0)
            if self.click:
                self.inventoryRun = False
        else:
            self.backButtonInventoryScreen.color = (36, 36, 36)
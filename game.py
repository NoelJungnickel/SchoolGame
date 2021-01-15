import pygame, sys
from pygame.locals import *
from shapeCreator import Input, Label, Button
from characterCreator import Character

pygame.init()

icon = pygame.image.load(r'C:\Users\Ozzy\Desktop\Bilder von Leuten\Surzher.png')

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
        self.characterX = 100
        self.characterY = 100

    def mainloopGame1(self):
        self.createGame()

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
        self.createGame()

        while self.gameRun:
            self.clock.tick(self.FPS)
            self.win.fill((204, 204, 204))
            self.placeGame()
            self.keyPressGame()
            self.screen2 = Label(self.win, "2", 500, 500, (255, 0, 0), 200)
            self.screen2.drawLetter()

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

    def mainloopGame3(self):
        self.createGame()

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
        self.createGame()

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
        self.createGame()

        while self.gameRun:
            self.clock.tick(self.FPS)
            self.win.fill((204, 204, 204))
            self.placeGame()
            self.keyPressGame()
            self.screen5 = Label(self.win, "5", 500, 500, (255, 0, 0), 200)
            self.screen5.drawLetter()
            self.LevelUp = Button(self.win, (255, 255, 255), 300, 300, 80, 50, text = 'LevelUp', textColor = (0, 0, 255), textSize = 50)
            self.LevelUp.drawButton()
            self.Level = Label(self.win, str(self.character.Level), 800, 500, (0, 255, 0), 200)
            self.Level.drawLetter()
            if self.LevelUp.checkCollisionRect(self.character.characterToRect()):
                self.character.LevelUp()
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
        self.createGame()

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
        self.createGame()

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
        self.createGame()

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
        self.createGame()

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
    def createGame(self):
        self.character = Character(self.win, self.characterX, self.characterY, r'C:\Users\Ozzy\Desktop\Bilder von Leuten\Surzher.png')

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

    def checkEdgesW(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if self.gridY != 1:
                self.gridY -= 1
                self.loadMainloop()

    def checkEdgesA(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if self.gridX != 1:
                self.gridX -= 1
                self.loadMainloop()

    def checkEdgesS(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            if self.gridY != 3:
                self.gridY += 1
                self.loadMainloop()

    def checkEdgesD(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            if self.gridX != 3:
                self.gridX += 1
                self.loadMainloop()
                        
    def keyPressGame(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if self.character.y <= 0:
                self.checkEdgesW()
            else:
                self.character.y -= self.character.vel

        if keys[pygame.K_a]:
            if self.character.x <= 0:
                self.checkEdgesA()
            else:
                self.character.x -= self.character.vel

        if keys[pygame.K_s]:
            if self.character.y >= winHeight - self.character.getCharacterWidth():
                self.checkEdgesS()
            else:
                self.character.y += self.character.vel

        if keys[pygame.K_d]:
            if self.character.x >= winWidth - self.character.getCharacterHeight():
                self.checkEdgesD()
            else:
                self.character.x += self.character.vel

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
    
    def createOptionsScreen(self):
        self.exitButtonOptionsScreen = Button(self.win, (36, 36, 36), self.winWidth - 250, self.winHeight - 100, 200, 50, "EXIT")
        self.backButtonOptionsScreen = Button(self.win, (36, 36, 36), 50, self.winHeight - 100, 200, 50, "BACK")
        self.topBarLabel = Button(self.win, (36, 36, 36), 50, 50, self.winWidth - 100, 50)
        self.commandsLabel = Label(self.win, "COMMANDS", 60,60)
        self.keysLabel = Label(self.win, "KEYS", self.winWidth/2 + 10, 60)
        self.wKeyLabel = Button(self.win, (36, 36, 36), 50, 200, self.winWidth - 100, 50, "|")
        self.upKeyLetter = Label(self.win, "MOVE UP", 60, 210)
        self.wKeyLetter = Label(self.win, "W", self.winWidth/2 + 10, 210)
        self.aKeyLabel = Button(self.win, (36, 36, 36), 50, 275, self.winWidth - 100, 50, "|")
        self.leftKeyLetter = Label(self.win, "MOVE LEFT", 60, 285)
        self.aKeyLetter = Label(self.win, "A", self.winWidth/2 + 10, 285)
        self.sKeyLabel = Button(self.win, (36, 36, 36), 50, 350, self.winWidth - 100, 50, "|")
        self.downKeyLetter = Label(self.win, "MOVE DOWN", 60, 360)
        self.sKeyLetter = Label(self.win, "S", self.winWidth/2 + 10, 360)
        self.dKeyLabel = Button(self.win, (36, 36, 36), 50, 425, self.winWidth - 100, 50, "|")
        self.rightKeyLetter = Label(self.win, "MOVE RIGHT", 60, 435)
        self.dKeyLetter = Label(self.win, "D", self.winWidth/2 + 10, 435)
        self.mKeyLabel = Button(self.win, (36, 36, 36), 50, 500, self.winWidth - 100, 50, "|")
        self.interactKeyLetter = Label(self.win, "INTERACT", 60, 510)
        self.mKeyLetter = Label(self.win, "M", self.winWidth/2 + 10, 510)
        self.kKeyLabel = Button(self.win, (36, 36, 36), 50, 575, self.winWidth - 100, 50, "|")
        self.sprintKeyLetter = Label(self.win, "SPRINT", 60, 585)
        self.kKeyLetter = Label(self.win, "K", self.winWidth/2 + 10, 585)
        self.lKeyLabel = Button(self.win, (36, 36, 36), 50, 650, self.winWidth - 100, 50, "|")
        self.inventoryKeyLetter = Label(self.win, "INVENTORY", 60, 660)
        self.lKeyLetter = Label(self.win, "L", self.winWidth/2 + 10, 660)

    def placeOptionsScreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)
        self.exitButtonOptionsScreen.drawButton()
        self.backButtonOptionsScreen.drawButton()
        self.topBarLabel.drawButton()
        self.commandsLabel.drawLetter()
        self.keysLabel.drawLetter()
        self.wKeyLabel.drawButton()
        self.upKeyLetter.drawLetter()
        self.wKeyLetter.drawLetter()
        self.aKeyLabel.drawButton()
        self.leftKeyLetter.drawLetter()
        self.aKeyLetter.drawLetter()
        self.sKeyLabel.drawButton()
        self.downKeyLetter.drawLetter()
        self.sKeyLetter.drawLetter()
        self.dKeyLabel.drawButton()
        self.rightKeyLetter.drawLetter()
        self.dKeyLetter.drawLetter()
        self.mKeyLabel.drawButton()
        self.interactKeyLetter.drawLetter()
        self.mKeyLetter.drawLetter()
        self.kKeyLabel.drawButton()
        self.sprintKeyLetter.drawLetter()
        self.kKeyLetter.drawLetter()
        self.lKeyLabel.drawButton()
        self.inventoryKeyLetter.drawLetter()
        self.lKeyLetter.drawLetter()
        

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
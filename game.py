import pygame, sys
from pygame.locals import *
from shapeCreator import Input, Label, Button

pygame.init()

icon = pygame.image.load(r'C:\Users\Noel\Pictures\Kochium.png')

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
        
    def mainloopGame1(self):
        self.createGame()

        while self.gameRun:
            self.clock.tick(self.FPS)
            self.win.fill((204, 204, 204))
            self.placeGame()
            self.keyPressGame()

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
        self.character = Button(self.win, (255, 0, 0), self.winWidth/2 - 50, self.winHeight/2 - 50, 100, 100)

    def placeGame(self):
        self.character.drawButton()

    def keyPressGame(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if self.character.y <= 0:
                pass
            else:
                self.character.y -= 10

        if keys[pygame.K_a]:
            if self.character.x <= 0:
                pass
            else:
                self.character.x -= 10

        if keys[pygame.K_s]:
            if self.character.y >= winHeight - self.character.height:
                pass
            else:
                self.character.y += 10

        if keys[pygame.K_d]:
            if self.character.x >= winWidth - self.character.width:
                pass
            else:
                self.character.x += 10

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
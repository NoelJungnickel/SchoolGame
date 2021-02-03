import pygame, sys
from pygame.locals import *
from shapeCreator import Entry, Label, Button


pygame.init()

icon = pygame.image.load(r'C:\Users\Noel\Pictures\Kochium.png')
placeholder1 = pygame.image.load(r'C:\Users\Noel\Pictures\Dc10.png')
placeholder2 = pygame.image.load(r'C:\Users\Noel\Pictures\Avatar.png')

winName = "Start"
winWidth = 1600
winHeight = 900
#winWidth = 1920
#winHeight = 1080

pygame.display.set_caption(winName)
win = pygame.display.set_mode((winWidth, winHeight))
#win = pygame.display.set_mode((winWidth, winHeight), pygame.FULLSCREEN)
pygame.display.set_icon(icon)

class Fight():
    def __init__(self):
        self.win = win
        self.winName = winName
        self.gameRun = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.click = False

    def fightLoop(self):
        self.fightRun = True
        self.createFight()

        while self.fightRun:
            self.clock.tick(self.FPS)
            self.win.fill((0, 0, 0))
            self.buttonPressFightScreen()
            self.placeFight()

            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.escScreen()
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.click = True

    def createFight(self):
        self.enemyHpBar = Button(self.win, (255, 0, 0), 50, 45, 300, 60, "Enemy HP")
        self.playerHpBar = Button(self.win, (0, 255, 0), self.winWidth - 790, 425, 300, 60, "Player HP")
        self.chooseAction = Button(self.win, (36, 36, 36), 50, self.winHeight - 180, 750, 150)
        self.chooseAttack = Button(self.win, (36, 36, 36), 810, self.winHeight - 180, 750, 150)
        self.distictionLine = Button(self.win, (0, 0, 255), 0, 360, 2000, 10, "")
        self.attackButton = Button(self.win, (10, 10, 10), 60, self.winHeight - 170, 730, 60, "Attack")
        self.statsButton = Button(self.win, (10, 10, 10), 60, self.winHeight - 100, 360, 60, "Stats")
        self.escapeButton = Button(self.win, (10, 10, 10), 430, self.winHeight - 100, 360, 60, "Escape")

    def placeFight(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)
        pygame.draw.rect(self.win, (0, 0, 255), (150, self.winHeight - 510, 550, 300), 10)
        pygame.draw.rect(self.win, (0, 0, 255), (910, self.winHeight - 870, 550, 300), 10)
        self.enemyHpBar.drawButton()
        self.playerHpBar.drawButton()
        self.chooseAction.drawButton()
        self.chooseAttack.drawButton()
        self.distictionLine.drawButton()
        self.attackButton.drawButton()
        self.escapeButton.drawButton()
        self.statsButton.drawButton()

    def buttonPressFightScreen(self):
        mousePos = pygame.mouse.get_pos()

        if self.attackButton.checkCollision(mousePos):
            self.attackButton.color = (255, 0, 0)
            if self.click:
                exit()
        else:
            self.attackButton.color = (10, 10, 10)

        if self.escapeButton.checkCollision(mousePos):
            self.escapeButton.color = (0, 255, 255)
            if self.click:
                self.fightRun = False
        else:
            self.escapeButton.color = (10, 10, 10)

        if self.statsButton.checkCollision(mousePos):
            self.statsButton.color = (255, 0, 255)
            if self.click:
                self.statsScreen()
        else:
            self.statsButton.color = (10, 10, 10)

    def statsScreen(self):
        self.statsRun = True
        self.createStatsScreen()

        while self.statsRun:
            self.clock.tick(self.FPS)
            self.win.fill((0, 0, 0))
            self.placeStatsScreen()
            self.buttonPressStatsScreen()
            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.statsRun = False
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.click = True

    def createStatsScreen(self):
        self.exitButtonStatsScreen = Button(self.win, (36, 36, 36), self.winWidth - 250, self.winHeight - 100, 200, 50, "EXIT")
        self.backButtonStatsScreen = Button(self.win, (36, 36, 36), 50, self.winHeight - 100, 200, 50, "BACK")

    def placeStatsScreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)
        self.exitButtonStatsScreen.drawButton()
        self.backButtonStatsScreen.drawButton()

    def buttonPressStatsScreen(self):
        mousePos = pygame.mouse.get_pos()

        if self.backButtonStatsScreen.checkCollision(mousePos):
            self.backButtonStatsScreen.color = (255, 0, 0)
            if self.click:
                self.statsRun = False
        else:
            self.backButtonStatsScreen.color = (36, 36, 36)

        if self.exitButtonStatsScreen.checkCollision(mousePos):
            self.exitButtonStatsScreen.color = (255, 0, 0)
            if self.click:
                exit()
        else:
            self.exitButtonStatsScreen.color = (36, 36, 36)

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
        self.iEntry = Entry(self.win, self.winWidth/2 + 8, 658, 35, 33, (36, 36, 36), "I")
        self.entryList = [self.wEntry, self.aEntry, self.sEntry, self.dEntry, self.mEntry, self.kEntry, self.iEntry]

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
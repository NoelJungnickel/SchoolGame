import pygame, sys
from pygame.locals import *
from shapeCreator import Entry, Label, Button
from game import Game
from characterCreator import Character
from resource import *

pygame.init()

icon = pygame.image.load(playerPicture) #legt das icon fest

winName = "Start" #legt den Namen fest
#winWidth = 1600
#winHeight = 900
winWidth = 1920 #legt die Breite des windows fest
winHeight = 1080 #legt die Höhe des windows fest

pygame.display.set_caption(winName) #benennt das Window
#win = pygame.display.set_mode((winWidth, winHeight))
win = pygame.display.set_mode((winWidth, winHeight), pygame.FULLSCREEN) #erstellt das window
pygame.display.set_icon(icon) #erstellt das Icon

#Klasse die ein GameMenu erstellt
class GameMenu():
    def __init__(self):
        self.win = win
        self.winName = winName
        self.startRun = True
        self.optionsRun = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.click = False
        self.active = False
    
    #Methode in der die Loop des Startscreens erstellt wird
    def mainloopStartMenu(self):
        self.createStartscreen() #führt die Methode aus, in der die Objekte des Startscreens erstellt werden

        while self.startRun: #überprüft ob der Startscreen angezeigt wird und führt alle Methoden in der loop wärenddessen aus
            self.clock.tick(self.FPS) #legt die framerate fest
            self.win.fill((0, 0, 0)) #füllt den Hintergrund mir der Farbe Schwarz
            self.placeStartscreen() #führt die Methode aus, in der die Objekte des Startscreen platziert werden
            self.buttonPressStartScreen() #führt die Methode aus, in der überprüft wird, ob ein Kopf gedrückt wird
            pygame.display.update() #updatet den screen

            self.click = False
            for event in pygame.event.get(): #überprüft ob ein Event stattfindet
                if event.type == pygame.QUIT: #wenn sich der screen schließt
                    self.startRun = False #wird die loop beendet
                if event.type == KEYDOWN: #wenn man eine Taste and der Tastatur drückt
                    if event.key == K_ESCAPE: #und diese Taste die escape Taste ist
                        exit() #schließt sich ser screen
                if event.type == MOUSEBUTTONDOWN: #wenn man eine Taste and er Maus drückt
                    if event.button == 1: #und diese Taste die linke Maustaste ist
                        self.click = True #wird die Variable click wahr gemacht

    #Methode die das StartMenu erstellt
    def createStartscreen(self):
        self.startButton = Button(self.win, (36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 - 100, 200, 50, "START")
        self.optionsButton = Button(self.win, (36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 - 25, 200, 50, "OPTIONS")
        self.exitButtonStartScreen = Button(self.win, (36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 + 50, 200, 50, "EXIT")

    #Methode die das StartMenu platziert
    def placeStartscreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20) #ein Rechteck wird plaziert
        self.startButton.drawButton() #das eben erstelle Objekt wird platziert
        self.optionsButton.drawButton()
        self.exitButtonStartScreen.drawButton()

    #Methode in der die Funktion der Buttons erstellt wird
    def buttonPressStartScreen(self):
        mousePos = pygame.mouse.get_pos() #die Postition der Maus wird als Varible festgelegt und konstant aktualisiert
    
        if self.startButton.checkCollision(mousePos): #wenn das Objekt "startbutton" mit der eben festgelegten Maupostion kollidiert
            self.startButton.color = (0, 255, 0) #wird die Farbe des "startbuttons" zu Grün geändert
            if self.click: #wenn die eben festgelegte Variable wahr ist
                Game().mainloopGame1() #wird die methode "mainloop1" in der Klasse "Game" ausgeführt
        else: #wenn das Objekt "startbutoon" nicht mit der eben festgelegten Mausposition killidiert
            self.startButton.color = (36, 36, 36) #wird die Farbe des "startbuttons" zu Grau geändert
        
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

    #Methode in der die Loop des Optionscreens erstellt wird
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
                for entry in self.entryList: #für jeden Eingang aus der "entryList" wird überprüft, ob er aktiviert oder verändert wird
                    entry.activateEntry(event)
                    entry.editEntry(event)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.optionsRun = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    #Methode die das OptionsMenu erstellt wird
    def createOptionsScreen(self):
        self.commandsLabel = Label(self.win, "COMMANDS", 60,60) #ein Obejekt der Klasse "Label" wird erstellt
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
        self.tippLabel = Button(self.win, (36, 36, 36), 50, 800, self.winWidth - 100, 50, "TIPP: IF YOU NEED HEALING, TAKE A NAP!")
        self.buttonList = [self.exitButtonOptionsScreen, self.backButtonOptionsScreen, self.topBarLabel, self.wKeyLabel, self.aKeyLabel, self.sKeyLabel, self.dKeyLabel, self.mKeyLabel, self.kKeyLabel, self.lKeyLabel, self.tippLabel]

        self.wEntry = Entry(self.win, self.winWidth/2 + 8, 208, 35, 33, (36, 36, 36), "W") #ein Obejekt der Klasse "Entry" wird erstellt
        self.aEntry = Entry(self.win, self.winWidth/2 + 8, 283, 35, 33, (36, 36, 36), "A")
        self.sEntry = Entry(self.win, self.winWidth/2 + 8, 358, 35, 33, (36, 36, 36), "S")
        self.dEntry = Entry(self.win, self.winWidth/2 + 8, 433, 35, 33, (36, 36, 36), "D")
        self.mEntry = Entry(self.win, self.winWidth/2 + 8, 508, 35, 33, (36, 36, 36), "M")
        self.kEntry = Entry(self.win, self.winWidth/2 + 8, 583, 35, 33, (36, 36, 36), "K")
        self.lEntry = Entry(self.win, self.winWidth/2 + 8, 658, 35, 33, (36, 36, 36), "L")
        self.entryList = [self.wEntry, self.aEntry, self.sEntry, self.dEntry, self.mEntry, self.kEntry, self.lEntry]

    #Methode die das OptionsMenu platziert wird
    def placeOptionsScreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)

        for button in self.buttonList: #alle Köpfe aus der "buttonList" werden platziert
            button.drawButton()

        for label in self.labelList:
            label.drawLetter()

        for entry in self.entryList:
            entry.drawEntry()

    #Methode in der die Funktion der Buttons erstellt wird
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

Menu1 = GameMenu() #ein neues Objekt der Klasse "GameMenu" wird erstellt
Menu1.mainloopStartMenu() #die Methode "mainloopStartMenu" des Objektes "Menu1", welches grade eben erstellt wurde, wird ausgeführt
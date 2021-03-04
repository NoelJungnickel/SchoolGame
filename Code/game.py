import pygame, sys
from pygame.locals import *
from shapeCreator import Entry, Label, Button
from characterCreator import Character
from enemyCreator import Enemy
from random import randint
from resource import *

pygame.init()

icon = pygame.image.load(playerPicture)

winName = "Game"
#winWidth = 1600
#winHeight = 900
winWidth = 1920
winHeight = 1080

pygame.display.set_caption(winName)
#win = pygame.display.set_mode((winWidth, winHeight))
win = pygame.display.set_mode((winWidth, winHeight), pygame.FULLSCREEN)
pygame.display.set_icon(icon)

#Klasse die ein Game erstellt
class Game():
    def __init__(self):
        self.win = win
        self.winName = winName
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.gameRun = True
        self.heal = False
        self.click = False
        self.gridX = 1
        self.gridY = 1
        self.vel = 5
        self.characterX = 450
        self.characterY = 250
        self.character = Character(self.win, self.characterX, self.characterY, characterPicture) #Character wird erstellt
        self.testPicture = pygame.image.load(testPicture) #Bild wird in das Spile geladen
        self.studentPicture = pygame.image.load(studentPicture)
        self.examPicture = pygame.image.load(examPicture)
        self.teacherPicture = pygame.image.load(teacherPicture)
        self.principlePicture = pygame.image.load(principlePicture)
        self.finalsPicture = pygame.image.load(finalsPicture)
        self.createOptionsScreen()
        
    #Methode die den ersten Screen öffnet
    def mainloopGame1(self):
        self.room1Picture = pygame.image.load(room1Picture)
        self.gameRun = True

        self.clock.tick(self.FPS)
        self.win.blit(self.room1Picture, (0, 0)) #das Bild wird auf den Bildschirm platziert
        self.placeGame()
        self.keyPressGame()
        self.Bett = Button(self.win, (0, 0, 0), 150, 50, 800, 400)
        self.healLabel = Label(self.win, "Du wurdest vollständig geheilt", 400, 500, (0, 255, 0), 100)
        
        if self.heal == True:
            self.healLabel.drawLetter()

        pygame.display.update()

        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRun = False
            if self.Bett.checkCollisionRect(self.character.characterToRect()) and event.type == KEYDOWN: #überprüft ob der Character mit dem Bett kolidiert
                if event.key == K_m: #überprüft ob die Taste "M" gedrückt wird
                    self.character.fullHeal() #character wird voll geheilt
                    self.heal = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.escScreen()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    #Methode die den zweiten Screen öffnet
    def mainloopGame2(self):
        self.room2Picture = pygame.image.load(room2Picture)
        self.gameRun = True
        self.heal = False

        self.clock.tick(self.FPS)
        self.win.blit(self.room2Picture, (0, 0))
        self.createEnemies("test") #gegner "test" wird erstellt
        self.placeGame()
        self.keyPressGame()

        #self.triggerFight = Enemy(self.win, 900, 500, testPicture).enemyToRect()
        #self.triggerFight.pygame.draw.rect()


        pygame.display.update()

        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRun = False
            if Enemy(self.win, 900, 500, testPicture).checkCollisionRect(self.character.characterToRect()) and event.type == KEYDOWN: #überprüft ob der Character mit dem Gegner kolidiert
                if event.key == K_m: #überprüft ob die Taste "M" gedrückt wird
                    Fight(self.character,"test").fightLoop() #öffnet den Fightscreen mit dem Gegner "test"
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.escScreen()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    #Methode die den dritten Screen öffnet
    def mainloopGame3(self):
        self.room3Picture = pygame.image.load(room3Picture)
        self.gameRun = True

        self.clock.tick(self.FPS)
        self.win.blit(self.room3Picture, (0, 0))
        self.createEnemies("student")
        self.placeGame()
        self.keyPressGame()

        pygame.display.update()

        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRun = False
            if Enemy(self.win, 900, 500, studentPicture).checkCollisionRect(self.character.characterToRect()) and event.type == KEYDOWN:
                if event.key == K_m:
                    Fight(self.character,"student").fightLoop()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.escScreen()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    #Methode die den vierten Screen öffnet
    def mainloopGame4(self):
        self.room4Picture = pygame.image.load(room4Picture)
        self.gameRun = True
        self.heal = False

        self.clock.tick(self.FPS)
        self.win.blit(self.room4Picture, (0, 0))
        self.createEnemies("test")
        self.placeGame()
        self.keyPressGame()

        pygame.display.update()

        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRun = False
            if Enemy(self.win, 900, 500, testPicture).checkCollisionRect(self.character.characterToRect()) and event.type == KEYDOWN:
                if event.key == K_m:
                    Fight(self.character,"test").fightLoop()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.escScreen()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    #Methode die den fünften Screen öffnet
    def mainloopGame5(self):
        self.room5Picture = pygame.image.load(room5Picture)
        self.gameRun = True

        self.clock.tick(self.FPS)
        self.win.blit(self.room5Picture, (0, 0))
        self.createEnemies("exam")
        self.placeGame()
        self.keyPressGame()          
        
        #self.levelUp = Button(self.win, (255, 255, 255), 300, 300, 80, 50, text = 'levelUp', textColor = (0, 0, 255), textSize = 50)
        #self.levelUp.drawButton()
        #self.level = Label(self.win, str(self.character.level), 800, 500, (0, 255, 0), 200)
        #self.level.drawLetter()
        #if self.levelUp.checkCollisionRect(self.character.characterToRect()):
        #    self.character.levelUp()

        pygame.display.update()

        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRun = False
            if Enemy(self.win, 900, 500, examPicture).checkCollisionRect(self.character.characterToRect()) and event.type == KEYDOWN:
                if event.key == K_m:
                    Fight(self.character,"exam").fightLoop()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.escScreen()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    #Methode die den sechsten Screen öffnet
    def mainloopGame6(self):
        self.room6Picture = pygame.image.load(room6Picture)
        self.gameRun = True

        self.clock.tick(self.FPS)
        self.win.blit(self.room6Picture, (0, 0))
        self.createEnemies("teacher")
        self.placeGame()
        self.keyPressGame()

        pygame.display.update()

        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRun = False
            if Enemy(self.win, 900, 500, teacherPicture).checkCollisionRect(self.character.characterToRect()) and event.type == KEYDOWN:
                if event.key == K_m:
                    Fight(self.character,"teacher").fightLoop()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.escScreen()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    #Methode die den siebten Screen öffnet
    def mainloopGame7(self):
        self.room7Picture = pygame.image.load(room7Picture)
        self.gameRun = True

        self.clock.tick(self.FPS)
        self.win.blit(self.room7Picture, (0, 0))
        self.createEnemies("student")
        self.placeGame()
        self.keyPressGame()

        pygame.display.update()

        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRun = False
            if Enemy(self.win, 900, 500, studentPicture).checkCollisionRect(self.character.characterToRect()) and event.type == KEYDOWN:
                if event.key == K_m:
                    Fight(self.character,"student").fightLoop()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.escScreen()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    #Methode die den achten Screen öffnet
    def mainloopGame8(self):
        self.room8Picture = pygame.image.load(room8Picture)
        self.gameRun = True

        self.clock.tick(self.FPS)
        self.win.blit(self.room8Picture, (0, 0))
        self.createEnemies("teacher")
        self.placeGame()
        self.keyPressGame()

        pygame.display.update()

        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRun = False
            if Enemy(self.win, 900, 500, teacherPicture).checkCollisionRect(self.character.characterToRect()) and event.type == KEYDOWN:
                if event.key == K_m:
                    Fight(self.character,"teacher").fightLoop()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.escScreen()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    #Methode die den neunten Screen öffnet
    def mainloopGame9(self):
        self.room9Picture = pygame.image.load(room9Picture)
        self.gameRun = True
  
        self.clock.tick(self.FPS)
        self.win.blit(self.room9Picture, (0, 0))
        self.createEnemies("principle")
        self.placeGame()
        self.keyPressGame()

        pygame.display.update()

        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRun = False
            if Enemy(self.win, 700, 500, principlePicture).checkCollisionRect(self.character.characterToRect()) and event.type == KEYDOWN:
                if event.key == K_m:
                    Fight(self.character,"principle").fightLoop()
            if Enemy(self.win, 1100, 500, finalsPicture).checkCollisionRect(self.character.characterToRect()) and event.type == KEYDOWN:
                if event.key == K_m:
                    Fight(self.character,"finals").fightLoop()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.escScreen()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    #Methode die den character platziert
    def placeGame(self):
        self.character.drawCharacter(self.character.x, self.character.y)

    #Methode guckt welcher Gegner gemeint ist und ihn dann erstellt
    def createEnemies(self, enemyType):
        if enemyType == "test":
            self.win.blit(self.testPicture, (900, 500))
        elif enemyType == "student":
            self.win.blit(self.studentPicture, (900, 500))
        elif enemyType == "exam":
            self.win.blit(self.examPicture, (900, 500))
        elif enemyType == "teacher":
            self.win.blit(self.teacherPicture, (900, 500))
        elif enemyType == "principle":
            self.win.blit(self.principlePicture, (700, 500))
            self.win.blit(self.finalsPicture, (1100, 500))

    #Methode die entscheidet welcher screen geöffnet werden soll
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
    
    #Methode die überprüft ob das obere Ende des Bildschirmrandes berührt wird
    def checkEdgesW(self, keys):
        if eval(f'keys[pygame.K_{self.wEntry.text.lower()}]'): #wenn die zurzeit festgelegte Taste gedrückt wird
            if self.gridY != 1: #und das "gridY" nicht gleich 1 ist
                self.gridY -= 1 #wird das "girdY" um 1 verkeleinert
                self.character.y += self.winHeight - self.character.getCharacterHeight() #und die Postion des characters verändert
                

    #Methode die überprüft ob das linke Ende des Bildschirmrandes berührt wird
    def checkEdgesA(self, keys):
        if eval(f'keys[pygame.K_{self.aEntry.text.lower()}]'):
            if self.gridX != 1:
                self.gridX -= 1
                self.character.x += self.winWidth - self.character.getCharacterWidth()
                

    #Methode die überprüft ob das untere Ende des Bildschirmrandes berührt wird
    def checkEdgesS(self, keys):
        if eval(f'keys[pygame.K_{self.sEntry.text.lower()}]'):
            if self.gridY != 3:
                self.gridY += 1
                self.character.y -= self.winHeight - self.character.getCharacterHeight()
                

    #Methode die überprüft ob das rechte Ende des Bildschirmrandes berührt wird
    def checkEdgesD(self, keys):
        if eval(f'keys[pygame.K_{self.dEntry.text.lower()}]'):
            if self.gridX != 3:
                self.gridX += 1
                self.character.x -= self.winWidth - self.character.getCharacterWidth()
                
    
    #Methode die den character bewegt und den "statsScreen" öffnet
    def keyPressGame(self):
        keys = pygame.key.get_pressed()
        right = False
        left = False

        if eval(f'keys[pygame.K_{self.wEntry.text.lower()}]'): #wenn die zurzeit festgelegte Taste gedrückt wird
            if self.character.y <= 0: #und die Position des characters kleiner gleich null ist
                self.checkEdgesW(keys) #wird die "checkEdgesW" Methode ausgeführt
            else: #wenn die Position des characters größer als null ist
                right = False
                left = False
                if eval(f'keys[pygame.K_{self.kEntry.text.lower()}]'): #und die zurzeit festgelegte Taste gedrückt wird
                    self.character.y -= self.character.sprintVel #wird die Postition des character schnell verändert
                else: #wenn die zurzeit festgelegte Taste nicht gedrückt wird
                    self.character.y -= self.character.vel #wird die Postition des characters in normaler Geschwindigkeit verändert

        if eval(f'keys[pygame.K_{self.aEntry.text.lower()}]'):
            if self.character.x <= 0:
                self.checkEdgesA(keys)
            else:
                right = False
                left = True
                if eval(f'keys[pygame.K_{self.kEntry.text.lower()}]'):
                    self.character.x -= self.character.sprintVel
                else:
                    self.character.x -= self.character.vel

        if eval(f'keys[pygame.K_{self.sEntry.text.lower()}]'):
            if self.character.y >= winHeight - self.character.getCharacterHeight():
                self.checkEdgesS(keys)
            else:
                right = False
                left = False
                if eval(f'keys[pygame.K_{self.kEntry.text.lower()}]'):
                    self.character.y += self.character.sprintVel
                else:
                    self.character.y += self.character.vel

        if eval(f'keys[pygame.K_{self.dEntry.text.lower()}]'):
            if self.character.x >= winWidth - self.character.getCharacterWidth():
                self.checkEdgesD(keys)
            else:
                right = True
                left = False
                if eval(f'keys[pygame.K_{self.kEntry.text.lower()}]'):
                    self.character.x += self.character.sprintVel
                else:
                    self.character.x += self.character.vel

        if eval(f'keys[pygame.K_{self.lEntry.text.lower()}]'):
            self.inventoryLoop()

    #Methode die den escScreen öffnet
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
    
    #Methode die den escScreen erstellt
    def createEscScreen(self):
        self.continueButton = Button(self.win, (36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 - 100, 200, 50, "CONTINUE")
        self.optionsButton = Button(self.win, (36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 - 25, 200, 50, "OPTIONS")
        self.exitButtonStartScreen = Button(self.win, (36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 + 50, 200, 50, "EXIT")

    #Methode die den escScreen platziert
    def placeEscScreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)
        self.continueButton.drawButton()
        self.optionsButton.drawButton()
        self.exitButtonStartScreen.drawButton()

    #Methode in der die Funktion der Buttons erstellt wird
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

    #Methode die den optionsScreen öffnet
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

    #Methode die optionsScreen erstellt    
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
        self.tippLabel = Button(self.win, (36, 36, 36), 50, 800, self.winWidth - 100, 50, "TIPP: IF YOU NEED HEALING, TAKE A NAP!")
        self.buttonList = [self.exitButtonOptionsScreen, self.backButtonOptionsScreen, self.topBarLabel, self.wKeyLabel, self.aKeyLabel, self.sKeyLabel, self.dKeyLabel, self.mKeyLabel, self.kKeyLabel, self.lKeyLabel, self.tippLabel]

        self.wEntry = Entry(self.win, self.winWidth/2 + 8, 208, 35, 33, (36, 36, 36), "W")
        self.aEntry = Entry(self.win, self.winWidth/2 + 8, 283, 35, 33, (36, 36, 36), "A")
        self.sEntry = Entry(self.win, self.winWidth/2 + 8, 358, 35, 33, (36, 36, 36), "S")
        self.dEntry = Entry(self.win, self.winWidth/2 + 8, 433, 35, 33, (36, 36, 36), "D")
        self.mEntry = Entry(self.win, self.winWidth/2 + 8, 508, 35, 33, (36, 36, 36), "M")
        self.kEntry = Entry(self.win, self.winWidth/2 + 8, 583, 35, 33, (36, 36, 36), "K")
        self.lEntry = Entry(self.win, self.winWidth/2 + 8, 658, 35, 33, (36, 36, 36), "L")
        self.entryList = [self.wEntry, self.aEntry, self.sEntry, self.dEntry, self.mEntry, self.kEntry, self.lEntry]

    #Methode die den optionsScreen platziert
    def placeOptionsScreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)

        for button in self.buttonList:
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
    
    #Methode die den inventorySceen öffnet
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

    #Methode die den inventoryScreen erstllt
    def createInventoryScreen(self):
        self.exitButtonInventoryScreen = Button(self.win, (36, 36, 36), self.winWidth - 250, self.winHeight - 100, 200, 50, "EXIT")
        self.backButtonInventoryScreen = Button(self.win, (36, 36, 36), 50, self.winHeight - 100, 200, 50, "BACK")
        self.nameButton = Button(self.win, (36, 36, 36), 400, 100, 1410, 50, f"Joavrid")
        self.levelButton = Button(self.win, (36, 36, 36), 400, 160, 1410, 50, f"Level: {self.character.level}")
        self.xpButton = Button(self.win, (0, 255, 0), 400, 220, (self.character.aktXP/self.character.maxXP)*1410, 50, f"")
        self.xpButtonFull = Button(self.win, (36, 36, 36), 400, 220, 1410, 50, f"")
        self.xpButtonText = Label(self.win, f"XP: {self.character.aktXP}/{self.character.maxXP}", 1040, 230)
        self.hpButton = Button(self.win, (255, 0, 0), 400, 280, (self.character.aktHP/self.character.maxHP)*1410, 50, f"")
        self.hpButtonFull = Button(self.win, (36, 36, 36), 400, 280, 1410, 50, f"")
        self.hpButtonText = Label(self.win, f"HP: {self.character.aktHP}/{self.character.maxHP}", 1010, 290)
        self.phyDamage = Button(self.win, (36, 36, 36), 400, 340, 1410, 50, f"Physischer Schaden: {self.character.phyDamage}")
        self.defense = Button(self.win, (36, 36, 36), 400, 400, 1410, 50, f"Verteidigung: {self.character.defense}")
        self.vel = Button(self.win, (36, 36, 36), 400, 460, 1410, 50, f"Geschwindigkeit: {self.character.vel}")

    #Methode die den inventoryScreen platziert
    def placeInventoryScreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)
        pygame.draw.rect(self.win, (0, 0, 255), (100, 100, 200, 400), 10)
        self.exitButtonInventoryScreen.drawButton()
        self.backButtonInventoryScreen.drawButton()
        
        self.character.drawCharacter(140, 170)
        self.nameButton.drawButton()
        self.levelButton.drawButton()
        self.xpButtonFull.drawButton()
        self.xpButton.drawButton()
        self.xpButtonText.drawLetter()
        self.hpButtonFull.drawButton()
        self.hpButton.drawButton()
        self.hpButtonText.drawLetter()
        self.phyDamage.drawButton()
        self.defense.drawButton()
        self.vel.drawButton()

    #Methode in der die Funktion der Buttons erstellt wird
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

#Klasse die ein Fight erstellt
class Fight():
    def __init__(self, character, enemyType):
        self.win = win
        self.winName = winName
        self.gameRun = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.click = False
        self.character = character
        self.death = False
        self.deathCounter = 0
        self.enemyType = enemyType
        self.victory = False
        self.winCounter = 0

    #Methode die den fithingScreen öffnet
    def fightLoop(self):
        self.startFight()
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
                        Game().escScreen()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

    #Methode die den fightingScreen erstellt
    def createFight(self):
        self.chooseAction = Button(self.win, (36, 36, 36), 45, self.winHeight - 180, 910, 150)
        self.chooseAttack = Button(self.win, (36, 36, 36), self.chooseAction.getButtonWidth() + 55, self.winHeight - 180, 910, 150)
        self.distictionLine = Button(self.win, (0, 0, 255), 0, 480, 2000, 10, "")
        self.attackButton = Button(self.win, (10, 10, 10), 60, self.winHeight - 170, 880, 60, "Attack")
        self.statsButton = Button(self.win, (10, 10, 10), 60, self.winHeight - 100, 435, 60, "Stats")
        self.escapeButton = Button(self.win, (10, 10, 10), 505, self.winHeight - 100, 435, 60, "Escape")
        self.nameCharacterButton = Button(self.win, (0, 255, 0), self.winWidth - 350, self.winHeight - 560, 300, 60, "Joavrid")
        self.deathLabel = Label(self.win, "Your free trial of life has ended", 400, 500, (255, 0, 0), 100)
        self.victoryLabel = Label(self.win, "VICORTY ROYALE", 650, 500, (255, 255, 0), 100)

    #Methode die den fightingScreen platziert und den Spieler zurücksetzt
    def placeFight(self):
        self.enemyHpBar = Button(self.win, (255, 0, 0), 50, 125, 300, 60, f"{self.enemy1.aktHP}/{self.enemy1.maxHP} HP")
        self.playerHpBar = Button(self.win, (0, 255, 0), self.winWidth - 350, self.winHeight - 485, 300, 60, f"{self.character.aktHP}/{self.character.maxHP} HP")
        self.nameEnemyButton = Button(self.win, (255, 0, 0), 50, 50, 300, 60, self.enemy1.name)
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)
        pygame.draw.rect(self.win, (0, 0, 255), (150, self.winHeight - 510, 550, 300), 10)
        pygame.draw.rect(self.win, (0, 0, 255), (1200, self.winHeight - 1000, 550, 300), 10)
        self.enemyHpBar.drawButton()
        self.playerHpBar.drawButton()
        self.chooseAction.drawButton()
        self.chooseAttack.drawButton()
        self.distictionLine.drawButton()
        self.attackButton.drawButton()
        self.escapeButton.drawButton()
        self.statsButton.drawButton()
        self.nameEnemyButton.drawButton()
        self.nameCharacterButton.drawButton()
        self.enemy1.drawEnemy(1410, 120)
        self.character.drawCharacter(360, 600)
        if self.death == True: #wenn "death" wahr ist
            self.deathLabel.drawLetter() #wird das "deathLabel" angezeigt
            self.deathCounter += 1 #der deathCounter um 1 erhöht
            if self.deathCounter > 180: #wenn der "deathCounter" größer als 180 ist
                self.fightRun = False #wird "fightRun" falsch gesetzt
                exit()
        if self.victory == True:              
            self.victoryLabel.drawLetter()
            self.winCounter += 1
            if self.winCounter > 180:
                self.fightRun = False
                exit()
        
        

    #Methode die den Kampf startet
    def startFight(self):
        self.Test = [testPicture, "Test",                       50, 50, 15, 12, 8]          #alle Gegner werden erstellt
        self.Schüler = [studentPicture, "Schüler",              100, 100, 30, 25, 10]       #alle Gegner werden erstellt
        self.Klausur = [examPicture, "Klausur",                 150, 150, 45, 40, 24]       #alle Gegner werden erstellt
        self.Lehrer = [teacherPicture, "Lehrer",                200, 200, 60, 55, 42]       #alle Gegner werden erstellt
        self.Schulleiter = [principlePicture, "Schulleiter",    300, 300, 300, 80, 56]      #alle Gegner werden erstellt
        self.Abitur = [finalsPicture, "Abitur",                600, 600, 3000, 120, 80]     #alle Gegner werden erstellt
        if self.enemyType == "test":                                                        #if -Statements, die Entscheiden welcher Gegner erstellt wird
            self.enemy1 = Enemy(self.win, 1300, 100, self.Test[0], self.Test[1], self.Test[2], self.Test[3], self.Test[4], self.Test[5], self.Test[6])
        if self.enemyType == "student":
            self.enemy1 = Enemy(self.win, 1300, 100, self.Schüler[0], self.Schüler[1], self.Schüler[2], self.Schüler[3], self.Schüler[4], self.Schüler[5], self.Schüler[6])
        if self.enemyType == "exam":
            self.enemy1 = Enemy(self.win, 1300, 100, self.Klausur[0], self.Klausur[1], self.Klausur[2], self.Klausur[3], self.Klausur[4], self.Klausur[5], self.Klausur[6])
        if self.enemyType == "teacher":
            self.enemy1 = Enemy(self.win, 1300, 100, self.Lehrer[0], self.Lehrer[1], self.Lehrer[2], self.Lehrer[3], self.Lehrer[4], self.Lehrer[5], self.Lehrer[6])
        if self.enemyType == "principle":
            self.enemy1 = Enemy(self.win, 1300, 100, self.Schulleiter[0], self.Schulleiter[1], self.Schulleiter[2], self.Schulleiter[3], self.Schulleiter[4], self.Schulleiter[5], self.Schulleiter[6])
        if self.enemyType == "finals":
            self.enemy1 = Enemy(self.win, 1300, 100, self.Abitur[0], self.Abitur[1], self.Abitur[2], self.Abitur[3], self.Abitur[4], self.Abitur[5], self.Abitur[6])

    #Methode die das Kämpfen definiert
    def fighting(self, damage, enemyDmg): 
        self.enemy1.takeDamage(damage)              #Gegner nimmt Schaden
        if self.enemy1.aktHP <= 0:                  #Es wird gechecked ob der Gegner Tod ist
            self.character.xpGain(self.enemy1.xp)   #Der Spieler erhält die XP des Gegners
            if self.enemyType == "finals":   
                self.victory = True
            else:
                self.fightRun = False
        else:
            self.character.takeDamage(enemyDmg)         #Spieler nimmt Schaden
        if self.character.aktHP <= 0:               #Es wird gechecked ob der Spieler Tod ist
            self.death = True                       #Spieler ist Tod
            self.enemy1.defense = 1000              #Gegner wird unsterblich, weil man noch weiter angreifen köntte
            
    #Methode in der die Funktion der Buttons erstellt wird
    def buttonPressFightScreen(self):
        mousePos = pygame.mouse.get_pos()

        if self.attackButton.checkCollision(mousePos) and self.death == False and self.victory == False:
            self.attackButton.color = (255, 0, 0)
            if self.click:
                self.fighting(self.character.phyDamage, self.enemy1.phyDamage)
        else:
            self.attackButton.color = (10, 10, 10)

        if self.escapeButton.checkCollision(mousePos) and self.death == False and self.victory == False:
            self.escapeButton.color = (0, 255, 255)
            if self.click:
                self.fightRun = False
        else:
            self.escapeButton.color = (10, 10, 10)

        if self.statsButton.checkCollision(mousePos) and self.death == False and self.victory == False:
            self.statsButton.color = (255, 0, 255)
            if self.click:
                self.inventoryLoop()
        else:
            self.statsButton.color = (10, 10, 10)
            
    #Methode die den inventorySceen öffnet
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

    #Methode die den inventoryScreen erstllt
    def createInventoryScreen(self):
        self.exitButtonInventoryScreen = Button(self.win, (36, 36, 36), self.winWidth - 250, self.winHeight - 100, 200, 50, "EXIT")
        self.backButtonInventoryScreen = Button(self.win, (36, 36, 36), 50, self.winHeight - 100, 200, 50, "BACK")
        self.nameButton = Button(self.win, (36, 36, 36), 400, 100, 1410, 50, f"Joavrid")
        self.levelButton = Button(self.win, (36, 36, 36), 400, 160, 1410, 50, f"Level: {self.character.level}")
        self.xpButton = Button(self.win, (0, 255, 0), 400, 220, (self.character.aktXP/self.character.maxXP)*1410, 50, f"")
        self.xpButtonFull = Button(self.win, (36, 36, 36), 400, 220, 1410, 50, f"")
        self.xpButtonText = Label(self.win, f"XP: {self.character.aktXP}/{self.character.maxXP}", 1040, 230)
        self.hpButton = Button(self.win, (255, 0, 0), 400, 280, (self.character.aktHP/self.character.maxHP)*1410, 50, f"")
        self.hpButtonFull = Button(self.win, (36, 36, 36), 400, 280, 1410, 50, f"")
        self.hpButtonText = Label(self.win, f"HP: {self.character.aktHP}/{self.character.maxHP}", 1010, 290)
        self.phyDamage = Button(self.win, (36, 36, 36), 400, 340, 1410, 50, f"Physischer Schaden: {self.character.phyDamage}")
        self.defense = Button(self.win, (36, 36, 36), 400, 400, 1410, 50, f"Verteidigung: {self.character.defense}")
        self.vel = Button(self.win, (36, 36, 36), 400, 460, 1410, 50, f"Geschwindigkeit: {self.character.vel}")

    #Methode die den inventoryScreen platziert
    def placeInventoryScreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)
        pygame.draw.rect(self.win, (0, 0, 255), (100, 100, 200, 400), 10)
        self.exitButtonInventoryScreen.drawButton()
        self.backButtonInventoryScreen.drawButton()
        
        self.character.drawCharacter(140, 170)
        self.nameButton.drawButton()
        self.levelButton.drawButton()
        self.xpButtonFull.drawButton()
        self.xpButton.drawButton()
        self.xpButtonText.drawLetter()
        self.hpButtonFull.drawButton()
        self.hpButton.drawButton()
        self.hpButtonText.drawLetter()
        self.phyDamage.drawButton()
        self.defense.drawButton()
        self.vel.drawButton()

    #Methode in der die Funktion der Knöpfe erstellt wird
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
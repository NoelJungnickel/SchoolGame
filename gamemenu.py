import pygame, sys
from pygame.locals import *
from shapeCreator import Label, Button

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
        
    def mainloopStartMenu(self):
        self.createStartscreen()

        while self.startRun:
            self.clock.tick(self.FPS)
            self.win.fill((0, 0, 0))
            self.placeStartscreen()
            self.buttonPress()
            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.startRun = False
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.click = True

    def createStartscreen(self):
        self.startButton = Button(self.win, (36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 - 100, 200, 50, "START", (255, 255, 255))
        self.optionsButton = Button(self.win, (36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 - 25, 200, 50, "OPTIONS", (255, 255, 255))
        self.exitButton = Button(self.win, (36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 + 50, 200, 50, "EXIT", (255, 255, 255))

    def placeStartscreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)
        self.startButton.drawButton()
        self.optionsButton.drawButton()
        self.exitButton.drawButton()

    def buttonPress(self):
        mousePos = pygame.mouse.get_pos()
    
        if self.startButton.checkCollision(mousePos):
            self.startButton.color = (0, 255, 0)
            if self.click:
                pass
        else:
            self.startButton.color = (36, 36, 36)
        
        if self.optionsButton.checkCollision(mousePos):
            self.optionsButton.color = (0, 0, 255)
            if self.click:
                self.mainloopOptionsMenu()
        else:
            self.optionsButton.color = (36, 36, 36)

        if self.exitButton.checkCollision(mousePos):
            self.exitButton.color = (255, 0, 0)
            if self.click:
                exit()
        else:
            self.exitButton.color = (36, 36, 36)

    def mainloopOptionsMenu(self):
        self.optionsRun = True
        while self.optionsRun:

            self.clock.tick(self.FPS)
            self.win.fill((0, 0, 0))
            self.createOptionsScreen()
            self.placeOptionsScreen()
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
        pass

    def placeOptionsScreen(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)
        
GameMenu().mainloopStartMenu()
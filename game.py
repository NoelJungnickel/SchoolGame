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
                            exit()
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

Game().mainloopGame1()
import pygame, sys
from pygame.locals import *

pygame.init()

icon = pygame.image.load(r'C:\Users\Noel\Pictures\Kochium.png')

winName = "Start"
#winWidth = 1600
#winHeight = 900
winWidth = 1920
winHeight = 1080

pygame.display.set_caption(winName)
#win = pygame.display.set_mode((winWidth, winHeight))
win = pygame.display.set_mode((winWidth, winHeight), pygame.FULLSCREEN)
pygame.display.set_icon(icon)


class Label():
    def __init__(self, text, color, x, y, fontSize = 50):
        pygame.font.init()
        self.mainFont = pygame.font.SysFont('comicsans', fontSize)
        
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.win = win

    def drawLetter(self):
        self.label = self.mainFont.render(self.text, 1, self.color)
        self.win.blit(self.label, (self.x, self.y))

    def getLabelWidth(self):
        return self.labelWidth == self.label.get_rect().size[0]

    def getLabelHeight(self):
        return self.labelHeight == self.label.get_rect().size[1]

class Button():
    def __init__(self, color, x, y, width, height, text = '', textColor = (255, 255, 255), textSize = 50):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.win = win
        self.text = text
        self.textColor = textColor
        self.textSize = textSize

    def checkCollision(self, mousePos):
        col = pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(mousePos)
        if col == 1:
            return True
        else:
            return False
        
    def drawButton(self):
        pygame.font.init()
        font = pygame.font.SysFont('comicsans', self.textSize)
        text = font.render(self.text, 1, self.textColor)
        text_rect = text.get_rect(center=pygame.Rect(self.x, self.y, self.width, self.height).center)
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width, self.height))
        self.win.blit(text, text_rect)

            
class Window():
    def __init__(self):
        
        self.win = win
        self.winName = winName
        self.run = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.click = False
        
    def mainloop(self):

        self.createStartscreen()

        while self.run:

            self.clock.tick(self.FPS)
            self.win.fill((0, 0, 0))
            self.placeStartscreen()
            self.buttonPress()
            self.border()

            pygame.display.update()

            self.click = False
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.click = True
    
    def border(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)

    def createStartscreen(self):
        self.startButton = Button((36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 - 100, 200, 50, "START", (255, 255, 255))
        self.keyButton = Button((36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 - 25, 200, 50, "OPTIONS", (255, 255, 255))
        self.exitButton = Button((36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 + 50, 200, 50, "EXIT", (255, 255, 255))

    def placeStartscreen(self):
        self.startButton.drawButton()
        self.keyButton.drawButton()
        self.exitButton.drawButton()

    def buttonPress(self):
        mousePos = pygame.mouse.get_pos()
    
        if self.startButton.checkCollision(mousePos):
            self.startButton.color = (0, 255, 0)
            if self.click:
                pass
        else:
            self.startButton.color = (36, 36, 36)
        
        if self.keyButton.checkCollision(mousePos):
            self.keyButton.color = (0, 0, 255)
            if self.click:
                pass
        else:
            self.keyButton.color = (36, 36, 36)

        if self.exitButton.checkCollision(mousePos):
            self.exitButton.color = (255, 0, 0)
            if self.click:
                exit()
        else:
            self.exitButton.color = (36, 36, 36)



Window().mainloop()
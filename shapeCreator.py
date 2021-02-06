import pygame, sys
from pygame.locals import *

class Entry():
    def __init__(self, win, x, y, width, height, color = (36, 36, 36), text = "", thickness = 2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.thickness = thickness
        self.win = win
        self.focused = False
    
    def drawEntry(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width, self.height), self.thickness)
        font = pygame.font.Font(None, 50)
        surface = font.render(self.text, True, (255, 255, 255))
        self.win.blit(surface, (self.x + 1, self.y + 1))

    def checkCollision(self, mousePos):
        col = pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(mousePos)
        if col == 1:
            return True
        else:
            return False
        
    def activateEntry(self, event):
        mousePos = pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN:
            if self.checkCollision(mousePos):
                self.focused = True
            else:
                self.focused = False

    def editEntry(self, event):
        if self.focused == True:
            self.color = (255, 255, 255)
        else:
            self.color = (36, 36, 36)

        if event.type == KEYDOWN:
            if self.focused == True:
                if len(self.text) == 0:
                    self.text += event.unicode.upper()
                if event.key == K_BACKSPACE:
                    self.text = self.text[:-1]

class Label():
    def __init__(self, win, text, x, y, color = (255, 255, 255), fontSize = 50):
        
        print("creatingLabel with text: " + text)

        pygame.font.init()
        self.mainFont = pygame.font.SysFont('comicsans', fontSize)
        
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.win = win

    def drawLetter(self):
        self.label = self.mainFont.render(self.text, 1 ,self.color)
        self.win.blit(self.label, (self.x, self.y))


class LabelAlt():
    def __init__(self, text, x, y, color = (255, 255, 255), fontSize = 50):
        
        print("creatingLabel with text: " + text)

        pygame.font.init()
        self.mainFont = pygame.font.SysFont('comicsans', fontSize)
        
        self.text = text
        self.color = color
        self.x = x
        self.y = y 

    def setText(self, text):
        self.text = text

    def render(self, win):
        self.label = self.mainFont.render(self.text, 1 ,self.color)
        win.blit(self.label, (self.x, self.y))

class Button():
    def __init__(self, win, color, x, y, width, height, text = '', textColor = (255, 255, 255), textSize = 50):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.win = win
        self.text = text
        self.textColor = textColor
        self.textSize = textSize
        pygame.font.init()
        self.font = pygame.font.SysFont('comicsans', self.textSize)

    def getButtonWidth(self):
        return self.width

    def checkCollision(self, mousePos):
        col = pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(mousePos)
        if col == 1:
            return True
        else:
            return False

    def checkCollisionRect(self, rectPos):
        col = pygame.Rect(self.x, self.y, self.width, self.height).colliderect(rectPos)
        if col == 1:
            return True
        else:
            return False

    def drawButton(self):

        text = self.font.render(self.text, 1, self.textColor)
        text_rect = text.get_rect(center=pygame.Rect(self.x, self.y, self.width, self.height).center)
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width, self.height))
        self.win.blit(text, text_rect)



class ButtonAlt():
    def __init__(self,   color, x, y, width, height, text = '', textColor = (255, 255, 255), textSize = 50):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color 
        self.text = text
        self.textColor = textColor
        self.textSize = textSize
        pygame.font.init()
        self.font = pygame.font.SysFont('comicsans', self.textSize)

    def getButtonWidth(self):
        return self.width

    def checkCollision(self, mousePos):
        return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(mousePos) == 1 

    def checkCollisionRect(self, rectPos):
        return pygame.Rect(self.x, self.y, self.width, self.height).colliderect(rectPos) == 1 

    def render(self, win): 
        text = self.font.render(self.text, 1, self.textColor)
        text_rect = text.get_rect(center=pygame.Rect(self.x, self.y, self.width, self.height).center)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        win.blit(text, text_rect)
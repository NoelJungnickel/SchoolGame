import pygame, sys
from pygame.locals import *

#Klasse die ein Entry erstellt
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

    #Methode in der die Entrys erstellt werden
    def drawEntry(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width, self.height), self.thickness) #ein Rechteck mit bestimmten Variablen wird gezeichnet
        font = pygame.font.Font(None, 50) #die Schriftart wird festgelegt
        surface = font.render(self.text, True, (255, 255, 255)) #die Schriftart wird gerendert
        self.win.blit(surface, (self.x + 1, self.y + 1)) #die Schriftart wird auf dem Untergrund platziert

    #Methode in die die Killision überprüft wird
    def checkCollision(self, mousePos):
        col = pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(mousePos)
        if col == 1:
            return True
        else:
            return False
    
    #Methode in der überprüft wird, ob das Entry aktiviert ist
    def activateEntry(self, event):
        mousePos = pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN:
            if self.checkCollision(mousePos):
                self.focused = True
            else:
                self.focused = False

    #Methode in der das Entry geändert wird
    def editEntry(self, event):
        if self.focused == True:
            self.color = (255, 255, 255)
        else:
            self.color = (36, 36, 36)

        if event.type == KEYDOWN:
            if self.focused == True:
                if len(self.text) == 0: #überprüft ob die Länge des engegebenen Textes gleich null ist
                    self.text += event.unicode.upper() #macht alle eingegebenen Buchstaben zu Großbuchstaben
                if event.key == K_BACKSPACE:
                    self.text = self.text[:-1] #entfernt das zuletzt hinzugefügte Zeichen

#Klasse die ein Lebel erstellt
class Label():
    def __init__(self, win, text, x, y, color = (255, 255, 255), fontSize = 50):
        pygame.font.init()
        self.mainFont = pygame.font.SysFont('comicsans', fontSize)
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.win = win

    #Methode in der die Letter erstellt werden
    def drawLetter(self):
        self.label = self.mainFont.render(self.text, 1, self.color)
        self.win.blit(self.label, (self.x, self.y))

#Klasse die ein Button erstellt
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

    #Methode die die Breite zurückgibt
    def getButtonWidth(self):
        return self.width

    #Methode die die Kollision von Maus und Button überprüft
    def checkCollision(self, mousePos):
        col = pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(mousePos)
        if col == 1:
            return True
        else:
            return False

    #Methode die die Kollision von Rechteck und Button überprüft
    def checkCollisionRect(self, rectPos):
        col = pygame.Rect(self.x, self.y, self.width, self.height).colliderect(rectPos)
        if col == 1:
            return True
        else:
            return False

    #Methode in der die Buttons erstellt werden
    def drawButton(self):
        text = self.font.render(self.text, 1, self.textColor)
        text_rect = text.get_rect(center=pygame.Rect(self.x, self.y, self.width, self.height).center)
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width, self.height))
        self.win.blit(text, text_rect)
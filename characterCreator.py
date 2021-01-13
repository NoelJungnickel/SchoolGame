import pygame, sys
from pygame.locals import *

class Character():
    def __init__(self, win, x, y, picture):
        self.win = win
        self.x = x
        self.y = y
        self.picture = picture

    def drawCharacter(self):
        self.characterpicture = pygame.image.load(self.picture)
        self.win.blit(self.characterpicture, (self.x, self.y))

    def getCharacterWidth(self):
        return self.characterpicture.get_rect().size[0]

    def getCharacterHeight(self):
        return self.characterpicture.get_rect().size[1]

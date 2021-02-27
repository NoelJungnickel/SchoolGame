import pygame, sys
from pygame.locals import *

class Character():
    def __init__(self, win, x, y, picture):
        self.win = win
        self.x = x
        self.y = y
        self.picture = picture
        self.name = None
        self.maxHP = 100
        self.aktHP = 10
        self.maxEP = 10
        self.aktEP = 10
        self.maxXP = 10
        self.aktXP = 0
        self.level = 1
        self.phyDamage = 15
        self.intDamage = 15
        self.defense = 10
        self.vel = 10
        self.sprintVel = 20
        self.characterpicture = pygame.image.load(self.picture)
        self.characterpicture = pygame.transform.scale(self.characterpicture, (300, 300))

    def levelUp(self):
        self.maxHP += 10
        self.maxEP += 1
        self.maxXP += 10
        if self.level%2 == 0:
            self.phyDamage += 2
            self.intDamage += 2
            self.defense += 2
        self.level += 1

    def xpGain(self, gainedXP):
        self.aktXP += gainedXP 
        if self.aktXP >= self.maxXP:
            self.aktXP -= self.maxXP
            print(1)
            self.levelUp()
    
    def takeDamage(self, damage):
        self.aktHP -= (damage - (self.defense/2))

    def drawCharacter(self, x, y):
        self.win.blit(self.characterpicture, (x, y))

    def getCharacterWidth(self):
        return self.characterpicture.get_rect().size[0]

    def getCharacterHeight(self):
        return self.characterpicture.get_rect().size[1]

    def characterToRect(self):
        filler = pygame.Rect(self.x, self.y, self.getCharacterWidth(), self.getCharacterHeight())
        return filler

import pygame, sys
from pygame.locals import *

#Klasse, die einen Charakter erstellt
class Character():
    def __init__(self, win, x, y, picture):
        self.win = win
        self.x = x
        self.y = y
        self.picture = picture
        self.name = None
        self.maxHP = 100
        self.aktHP = 100
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
        #self.characterpicture = pygame.transform.scale(self.characterpicture, (300, 300))

    #Methode die die Werte des Character erhöht
    def levelUp(self):
        self.maxHP += 10
        self.maxEP += 1
        self.maxXP += 15
        self.aktHP += 10
        self.vel += 1
        self.sprintVel += 2
        if self.level%2 == 0:
            self.phyDamage += 2
            self.intDamage += 2
            self.defense += 2
        self.level += 1

    #Methode die den XP-Wert des Characters erhöht
    def xpGain(self, gainedXP):
        self.aktXP += gainedXP 
        self.checkLevel() #führt die "checkLevel" Methode aus

    #Methode die überprüft welches Level der Character ist
    def checkLevel(self):
        if self.aktXP >= self.maxXP:
            self.aktXP -= self.maxXP
            self.levelUp() #führt die "levelUp" Methode aus
            self.checkLevel() #führt die "checkLevel" Methode aus

    #Methode die den Character Leben verlieren lässt
    def takeDamage(self, damage):
        self.aktHP -= (damage - (self.defense/2))
    
    #Methode die den Character voll heilt
    def fullHeal(self):
        self.aktHP = self.maxHP

    #Methode die den Character platziert
    def drawCharacter(self, x, y):
        self.win.blit(self.characterpicture, (x, y))

    #Methode die die Breite des Characters zurück gibt
    def getCharacterWidth(self):
        return self.characterpicture.get_rect().size[0]

    #Methode die die Höhe des Characters zurück gibt
    def getCharacterHeight(self):
        return self.characterpicture.get_rect().size[1]

    #Methode die den Character zu einen Rechteck konvertiert
    def characterToRect(self):
        filler = pygame.Rect(self.x, self.y, self.getCharacterWidth(), self.getCharacterHeight())
        return filler
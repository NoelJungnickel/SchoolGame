import pygame, sys
from pygame.locals import *
from resource import *

#Klasse die ein Enemy erstellt
class Enemy():
    def __init__(self, win, x, y, picture, name = 0, maxHP = 0, aktHP = 0, xp = 0, phyDamage = 0, defense = 0):
        self.win = win
        self.picture = picture
        self.name = name
        self.maxHP = maxHP
        self.aktHP = aktHP
        self.xp = xp
        self.phyDamage = phyDamage
        self.defense = defense
        self.x = x
        self.y = y
        self.enemypicture = pygame.image.load(self.picture)
    
    #Methode die den Gegenr erstellt
    def drawEnemy(self, x, y):   
        self.win.blit(self.enemypicture, (x, y))
    
    #Methode mit der man Leben verliert
    def takeDamage(self, damage):
        self.aktHP -= (damage - (self.defense/2))

    #Methode die die  Breite zurückgibt
    def getEnemyWidth(self):
        return self.enemypicture.get_rect().size[0]

    #Methode die die  Höhe zurückgibt
    def getEnemyHeight(self):
        return self.enemypicture.get_rect().size[1]

    #Methode die den Gegner zu einem Rechteck konvertiert
    def enemyToRect(self):
        filler = pygame.Rect(self.x, self.y, self.getEnemyWidth(), self.getEnemyHeight())
        return filler
    
    #Methode die die  Kollision von Gegner und Rechteck überprüft
    def checkCollisionRect(self, rectPos):
        col = pygame.Rect(self.x, self.y, self.getEnemyWidth(), self.getEnemyHeight()).colliderect(rectPos)
        if col == 1:
            return True
        else:
            return False
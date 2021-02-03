import pygame, sys
from pygame.locals import *






Schüler = [r'C:\Users\Noel\Pictures\Mika_Buchholz.png', "Schüler", 10, 10, 1, 1]
Lehrer = [r'C:\Users\Noel\Pictures\Koch.png', "Lehrer", 10, 10, 1, 1]
#Test = ()
#Klausur = ()

class Enemy():
    def __init__(self, win, x, y, picture, name, maxHP, aktHP, level, phyDamage):
        self.win = win
        self.picture = picture
        self.name = name
        self.maxHP = maxHP
        self.aktHP = aktHP
        #self.maxEP = 10
        #self.aktEP = 10
        self.level = level
        self.phyDamage = phyDamage
        self.x = x
        self.y = y

    def drawEnemy(self, x, y):
        self.enemypicture = pygame.image.load(self.picture)
        self.win.blit(self.enemypicture, (x, y))
    
    def schadenNehmen(self):
        pass


#enemy1 = Enemy(Schüler[0], Schüler[1], Schüler[2], Schüler[3], Schüler[4], Schüler[5])
#print(enemy1.maxHP)



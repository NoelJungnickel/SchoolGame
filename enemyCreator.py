import pygame, sys
from pygame.locals import *






Schüler = (, "Schüler", 10, 10, 1, phyDamage, intDamage)
Lehrer = (, "Lehrer",)
Test = ()
Klausur = ()

class Enemy():
    def __init__(self, win, picture, name, maxHP, aktHP, level, phyDamage, intDamage):
        self.win = win
        self.picture = picture
        self.name = name
        self.maxHP = maxHP
        self.aktHP = aktHP
        #self.maxEP = 10
        #self.aktEP = 10
        self.level = level
        self.phyDamage = phyDamage
        self.intDamage = intDamage
    
    def schadenNehmen(self)




enemyDictionary = {1: (1, 2, 3)}
print(enemyDictionary[1, 1])
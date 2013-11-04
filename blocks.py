from globalVariables import *
from noise import *
import pygame.gfxdraw
import math
import random

class Nothing:
    def isFemale(self):
        return self.female
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.evolve = False
        self.nRange = 1
        self.lifeCuttof = 0.9
        self.mateCutoff = 0.01
        self.die = False
        self.space = True
        self.isBaby = False
        self.neighbours = None
        self.age = 0
        self.ageCuttoff = pnoise1(random.uniform(0.0,10.0))*100.0
        self.female = False
    def isDead(self):
        return self.die
    def canEvolve(self):
        return self.evolve
    def getNoiseGene(self):
        return pnoise2( self.getGene(), timer.time )
    def getGene(self):
        return self.gene
    def update(self):
        #self.__drawPixel__(white) for showiong what is updated
        value = self.getNoiseGene()
        if value > self.lifeCuttof-pnoise1(timer.time):
            self.evolve = True
    def __drawPixel__(self,color):
        for x in xrange(zoom):
            for y in xrange(zoom):
                pygame.gfxdraw.pixel(screen,self.x*zoom+x,self.y*zoom+y,color)
    def draw(self):
        pass
    def initNeighbours(self):
        self.neighbours = []
        for x in xrange(-self.nRange,self.nRange):
            for y in xrange(-self.nRange,self.nRange):
                if x != 0 or y != 0:
                    self.neighbours.append(entitys[self.x + x][self.y + y])
    def initGenetics(self,x,y):
        incrPix = 80.0
        value = pnoise2(float(x)/incrPix,float(y)/incrPix)
        self.gene = value
    def initGeneticsComplete(self,value):
        self.gene = value
    def initInheritedGenes(self,value):
        self.gene = value
        self.isBaby = True
    def isItABaby(self):
        return self.isBaby
    def getSpace(self):
        return self.space
    def __del__(self):
        pass
cunt = 0
class Life(Nothing):
    def setFemale(self):
        self.female = True
    def update(self):
        self.age +=1
        if self.age>self.ageCuttoff:
            self.die=True
        self.space = False
        value = self.getNoiseGene()
        self.__findMate__()
        pass
    def __findMate__(self):
        highest = 0.0
        oponent = None
        matingMate = None;
        for neighbour in self.neighbours:
            distance = math.fabs(neighbour.getGene()-self.getGene())
            if distance>highest:
                oponent = matingMate
                highest = distance
                matingMate = neighbour
        if matingMate != None:
            dominant = self.getGene() if self.getGene()>matingMate.getGene() else matingMate.getGene()
            nonDominant = self.getGene() if dominant == matingMate.getGene() else matingMate.getGene()
            if oponent != None:
                if self.getGene()> oponent.getGene():
                        oponent.die = True
                        self.__mate__(matingMate,highest,dominant,nonDominant)
                else:
                    self.die = True
    def __mate__(self,matingMate,geneDifference,dominant,nonDominant):
        male = dominant+geneDifference
        female = nonDominant-geneDifference
        desicion = pnoise1(random.uniform(0.0,10.0))
        babyGene = male if desicion >0.0 else female
        for spotsForBaby in self.neighbours:
            if spotsForBaby.space == True:
                spotsForBaby.evolve = True
                spotsForBaby.initInheritedGenes(babyGene)

    def draw(self):
        global screen
        global pygame
        colorGene = max(min(self.getGene()+0.5,1.0),0.0)
        red = int(255-colorGene*255)    #RED = FEMALE
        blue = int(colorGene*255)       #blue = MALE
        selfColor   = (red,0,blue)
        self.__drawPixel__(selfColor)

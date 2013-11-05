from globalVariables import *
from blocks import *
from noise import *

class UniverseUpdater():
    def __init__(self):
        self.rangePerUpdate = int(width/2)
        self.rBeg = int( 0 )
        self.rEnd = int( self.rangePerUpdate/2 )
        self.startRange = [self.rBeg ,self.rEnd]
        self.xRange = [self.rBeg ,self.rEnd]
        self.yRange = [self.rBeg ,self.rEnd]

    def update(self):
        self.__executeRange__()
        self.__controlRange__()

    def __executeRange__(self):
        global entitys
        for x in range(self.xRange[0], self.xRange[1]):
            for y in range(self.yRange[0], self.yRange[1]):
                entitys[x][y].updateNeighbours()
                entitys[x][y].update()
                if entitys[x][y].isDead() == True:
                    gene = entitys[x][y].getGene()
                    exX = entitys[x][y].x
                    exY = entitys[x][y].y
                    entitys[x][y] = Nothing(exX,exY)
                    entitys[x][y].initGeneticsComplete(gene)
                if entitys[x][y].canEvolve() == True:
                    if entitys[x][y].isItABaby() == True:
                        gene = entitys[x][y].getGene()
                        entitys[x][y] = Life(x,y)
                        entitys[x][y].initGeneticsComplete(gene)
                        if gene < 0.0:
                            entitys[x][y].setFemale()
                    else:
                        entitys[x][y] = Life(x,y)
                        entitys[x][y].initGenetics(x,y)
    def __controlRange__(self):
        self.__incrementRange__(self.xRange)
        if self.xRange[1] >= int(width):
            self.xRange = [self.rBeg ,self.rEnd]
            self.__incrementRange__(self.yRange)

        if self.yRange[1] >= int(width):
            self.yRange = [self.rBeg ,self.rEnd]

    def __incrementRange__(self,iRange):
        for x in xrange(2):
            iRange[x] += self.rangePerUpdate/2


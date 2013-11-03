import pygame

class TimeClass:
    def __init__(self):
        self.dt = 0.0
        self.time = 0.0
        self.lastTime = float(pygame.time.get_ticks())/1000.0
    def update(self):
        self.time = float(pygame.time.get_ticks())/1000.0
        self.dt = (self.time-self.lastTime)
        self.lastTime = float(pygame.time.get_ticks())/1000.0

black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

size = [32,32]
width = float(size[0])
height = float(size[1])
zoom = 8
clock = pygame.time.Clock()
screenSize = [size[0]*zoom,size[1]*zoom]
screen = pygame.display.set_mode(screenSize)
entitys = [[None for y in xrange(int(height))] for x in xrange(int(width))]
timer = TimeClass()
done = False

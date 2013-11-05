from blocks import *
from universeUpdater import *
def drawUniverse():
    for x in range(int(width)):
        for y in range(int(height)):
            entitys[x][y].draw()

def initEntitys():
    for x in range(int(width)):
        for y in range(int(height)):
            entitys[x][y] = Nothing(x,y)
            entitys[x][y].initGenetics(x,y)

def keyHandling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    key=pygame.key.get_pressed()
    if key[pygame.K_q]:
        done = True

def gameLoop():
    keyHandling()
    drawUniverse()
    if timer.dt > 0.0:
        pygame.display.set_caption(str(round(1.0/timer.dt)))

def main():
    pygame.init()
    pygame.display.set_caption("PixelsOfLife")
    initEntitys()
    universeUpdater = UniverseUpdater()
    while done == False:
        timer.update()
        screen.fill(black)
        universeUpdater.update()
        gameLoop()
        pygame.display.flip()
        clock.tick(120)
    pygame.quit()
main()

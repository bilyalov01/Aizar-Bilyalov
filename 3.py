import pygame
pygame.init()
screen=pygame.display.set_mode((1020,1020))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))   
background = background.convert()

pygame.draw.arc(background, (0,150,0),(400,10,150,100), 0, 3.14)

screen.blit(background, (0,0))     
 
clock = pygame.time.Clock()
mainloop = True
FPS = 30 
playtime = 0.0

while mainloop:
    milliseconds = clock.tick(FPS) 
    playtime += milliseconds / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False 
    
    screen.fill((255, 255, 255)) 


    pygame.draw.lines(screen, (0,150,0), True, [[150, 250], [250, 300], [350, 250]], 2)
    pygame.draw.lines(screen, (0,150,0), True, [[320, 335], [250, 150], [200, 275]], 2)
    pygame.draw.lines(screen, (0,150,0), True, [[180, 335], [250, 150], [300, 275]], 2)
    pygame.display.set_caption("Frame rate: {:0.2f} frames per second." 
                               " Playtime: {:.2} seconds".format(
                               clock.get_fps(),playtime))
    pygame.display.flip()
print("this 'game' was played for %.2f seconds" % playtime)
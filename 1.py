import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))     
background = background.convert()  

pygame.draw.circle(background, (200,100,150), (300,250), 300)

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
    pygame.display.set_caption("Frame rate: {:0.2f} frames per second." 
                               " Playtime: {:.2} seconds".format(
                               clock.get_fps(),playtime))
    pygame.display.flip()      
print("this 'game' was played for %.2f seconds" % playtime)
import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))   
background = background.convert()  
ballsurface = pygame.Surface((50,50))    

pygame.draw.circle(ballsurface, (0,0,255), (25,25),25)

ballsurface = ballsurface.convert() 
ballx = 320
bally = 240

pygame.draw.rect(background, (0,255,0), (50,50,100,25))

pygame.draw.circle(background, (0,200,0), (200,50), 35)

pygame.draw.polygon(background, (0,180,0), ((250,100),(300,0),(350,50)))

pygame.draw.arc(background, (0,150,0),(400,10,150,100), 0, 3.14) 

screen.blit(background, (0,0))     
#screen.blit(ballsurface, (ballx, bally))  
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
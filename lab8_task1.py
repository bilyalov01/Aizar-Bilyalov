import pygame
pygame.init()

screen=pygame.display.set_mode((500,500))

x=50
y=50
speed=20
running=True
clock = pygame.time.Clock()        #create pygame clock object
FPS = 60                           # desired max. framerate in frames per second. 
playtime = 0
while running:
 milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
 seconds = milliseconds / 1000.0 # seconds passed since last frame (float)
 playtime += seconds
 pygame.time.delay(100)
 for event in pygame.event.get():

     if event.type == pygame.QUIT:
         running = False
     elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_ESCAPE:
             running=False
 
 keys= pygame.key.get_pressed()
 if keys[pygame.K_LEFT] and x>45:
     x-=speed
 if keys[pygame.K_RIGHT] and x<455:
     x+=speed
 if keys[pygame.K_UP] and y>45:
     y-=speed
 if keys[pygame.K_DOWN] and y<455:
     y+=speed
 pygame.display.set_caption("Frame rate: {:0.2f} frames per second." 
                               " Playtime: {:.2} seconds".format(
                               clock.get_fps(),playtime))

 pygame.draw.circle(screen,(255,0,0),(x,y),25)
 pygame.display.update()
 screen.fill((255,255,255))
print("This 'game' was played for {:.2f} seconds".format(playtime))
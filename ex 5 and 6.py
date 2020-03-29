# Simple pygame program
 
 # Import and initialize the pygame library
import pygame
pygame.init()
  
  # Set up the drawing window
screen = pygame.display.set_mode([500, 500])
  
 # Run until the user asks to quit
running = True
while running:
 
     # Did the user click the window close button?
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
 
     # Fill the background with white
     screen.fill((255, 255, 255))
     # Draw a solid blue circle in the center
     
     
     for point in range(0,255,25): # range(start, stop, step)
         pygame.draw.line(screen, (255,0,point), (0,0), (500, point*2), 1)
     for point in range(0,255,50): # range(start, stop, step)
         pygame.draw.line(screen, (point,0,255), (500,0), (point*2, 500), 1)
     for point in range(0,255,50): # range(start, stop, step)
         pygame.draw.line(screen, (255,point,255), (0,500), (point*2, 0), 1)
     for point in range(0,255,50): # range(start, stop, step)
         pygame.draw.line(screen, (255,0,point), (500,500), (0, point*2), 1)
     # Flip the display
     pygame.display.flip()
 
 # Done! Time to quit.
pygame.quit()

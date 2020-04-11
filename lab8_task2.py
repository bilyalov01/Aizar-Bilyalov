#!/usr/bin/env python

"""
002_display_fps_pretty.py

Display framerate and playtime.
Works with Python 2.7 and 3.3+.

URL:     http://thepythongamebook.com/en:part2:pygame:step002
Author:  yipyip
License: Do What The Fuck You Want To Public License (WTFPL)
         See http://sam.zoy.org/wtfpl/
"""

####

import pygame


####

class PygView(object):


    def __init__(self, width=640, height=480, fps=30):
        """Initialize pygame, window, background, font,...
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.screen = pygame.display.set_mode((640, 480))
        self.screenrect = self.screen.get_rect()
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((0, 0, 0))
        self.width = width
        self.height = height
        #self.height = width // 4
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)

        self.screen.blit(self.background, (0, 0))




    def run(self):
        """The mainloop
        """
        self.ballsurface = pygame.Surface((50, 50))
        self.ballrect = self.ballsurface.get_rect() # to use rectrangle's height&width
        self.ballsurface.set_colorkey((0, 0, 0))

        pygame.draw.circle(self.ballsurface, (255, 0, 0), (25, 25), 25)
        self.ballsurface = self.ballsurface.convert_alpha() # ballsurface is ready to be blit

        self.ballx, self.bally = 320, 240 # position of ballsurface on the screen
        self.dx, self.dy = 100, 100
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            milliseconds = self.clock.tick(self.fps)
            seconds = milliseconds / 1000.0            
            self.playtime += milliseconds / 1000.0

            self.show_ball(seconds)
            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()

    def show_ball(self, seconds):
        self.ballx = self.ballx + self.dx * seconds
        self.bally = self.bally + self.dy * seconds 

    

    # check if the ball is outside of the screen
        if self.ballx < 0:
            self.ballx = 0
            self.dx = self.dx * -1
        elif self.ballx + self.ballrect.width > self.screenrect.width:
            self.ballx = self.screenrect.width - self.ballrect.width
            self.dx = self.dx * -1

        if self.bally < 0:
            self.bally = 0
            self.dy = self.dy * -1
        elif self.bally + self.ballrect.height > self.screenrect.height:
            self.bally = self.screenrect.height - self.ballrect.height
            self.dy = self.dy * -1

        self.screen.blit(self.ballsurface, (round(self.ballx, 0), round(self.bally, 0)))
        pygame.display.flip() # refresh the screen

    ####

if __name__ == '__main__':

    # call with width of window and fps
    PygView(640, 480).run()

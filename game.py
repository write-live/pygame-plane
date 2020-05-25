import pygame
from pygame.locals import *
import sys
import random

from start import *
from enermy import *
from down import *
from bullet import *
from hero import *

class game():
    def __init__(self):
        pygame.init()
        self.size = width , height = 480, 700
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('plane battle')  
        self.background = pygame.image.load('images/background.png')
        self.Start = pygame.image.load('images/1.png')
        self.rect = self.Start.get_rect()
        self.rect.left = 115
        self.rect.top = 400
        self.clock = pygame.time.Clock()

    def chushi(self):
        while True:
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed_array = pygame.mouse.get_pressed()
                    for index in range(len(pressed_array)):
                        if pressed_array[index]:
                            if index == 0 and x >= self.rect.left and x <= self.rect.right and y >= self.rect.top and y <= self.rect.bottom:
                                return 1
                        
            
            
            if x >= self.rect.left and x <= self.rect.right and y >= self.rect.top and y <= self.rect.bottom:
                self.Start = pygame.image.load('images/2.png')
            else:
                self.Start = pygame.image.load('images/1.png')

            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.Start,self.rect)
            self.clock.tick(60)
            pygame.display.update()

    def main(self):
        t = self.chushi()
        while t:
            r = start(self.screen)
            t = r.main()

if __name__ == "__main__":
    game = game()
    game.main()
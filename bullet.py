import pygame
from pygame.locals import *
import sys
import random

class bullet(pygame.sprite.Sprite):
    def __init__(self,position,direct,screen):
        super().__init__()
        if direct == -1:
            self.image = pygame.image.load('images/bullet1.png')
        else:
            self.image = pygame.image.load('images/bullet2.png')
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.damage = 25
        self.yspeed = 5 * direct
        self.rect = self.image.get_rect()
        self.rect.left = position[0] - self.image.get_width()//2
        self.rect.top = position[1] - self.image.get_height()//2
        self.mask = pygame.mask.from_surface(self.image)


    def move(self):
        self.rect.top += self.yspeed
        if self.rect.top <= 0 or self.rect.bottom <= self.screen_rect.top:
            self.kill()
            del self

    def update(self):
        self.move()
        self.screen.blit(self.image,self.rect)
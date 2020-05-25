import pygame
from pygame.locals import *
import random

from bullet import *

class enermy(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        i = random.randrange(10)
        # level = 1
        if i >= 9:
            self.level = 3
            self.image = pygame.image.load('images/enemy3.png')
            self.blood = 200
            self.score = 500
        elif i >= 6:
            self.level = 2
            self.image = pygame.image.load('images/enemy2.png')
            self.blood = 100
            self.score = 200
        else:
            self.level = 1
            self.image = pygame.image.load('images/enemy1.png')
            self.blood = 50
            self.score = 50
        # self.level = level
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.xspeed = 1 * random.randint(-1,1)
        self.yspeed = 1
        self.rect.left = random.randint( 0, self.screen.get_width() - self.image.get_width())
        self.rect.top = -self.image.get_height()
        self.active = True
        self.clo = 0
        self.position = self.rect.left , self.rect.top
        self.screen_rect = self.screen.get_rect()

    def move(self):
        self.rect.left += self.xspeed
        self.rect.top += self.yspeed
        if self.rect.right >= self.screen_rect.right or self.rect.left <=0 :
            self.xspeed = -self.xspeed
        if self.rect.top >= self.screen_rect.bottom :
            self.kill()
            del self
            return
        self.position = (self.rect.left + self.rect.right)//2 , (self.rect.top + self.rect.bottom)//2
    
    def shoot(self):
        i = random.randrange(120)
        if i == 0:
            bul = bullet(self.position,1,self.screen)
        else:
            bul = None
        return bul

    def update(self):
        self.clo += 1
        if self.active :
            self.move()
            if self.blood <= 0:
                self.active = False
                self.clo = 0
        else:
            if self.level <= 2 and self.clo <20 :
                self.image = pygame.image.load('images/enemy' + str(self.level) + '_down'+str(self.clo//5 +1)+'.png')
            elif self.level ==3 and self.clo < 30:
                self.image = pygame.image.load('images/enemy3_down'+ str(self.clo//5 +1) +'.png')
            else:
                self.kill()
        self.screen.blit(self.image,self.rect)

import pygame
from pygame.locals import *
import sys
import random

from bullet import *

class hero(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.blood = 100
        self.score = 0
        self.image = pygame.image.load('images/me1.png')
        self.blood_image = pygame.image.load('images/life.png')
        self.boom_image = pygame.image.load('images/bomb.png')
        self.rect = self.image.get_rect()
        self.rect.left = self.screen_rect.right//2
        self.rect.top = self.screen_rect.bottom
        self.clo = 0
        self.boom = 3
        self.dbullet = 18
        self.active = True
        self.over = False
        # pygame.key.set_repeat(1, 1)
        self.position = 500,200
        self.mask = pygame.mask.from_surface(self.image)
        self.font = pygame.font.SysFont('Arial',40)

    def move(self):      #移动       
        x, y = pygame.mouse.get_pos()
        self.rect.top = y - (self.rect.bottom-self.rect.top)//2
        self.rect.left = x - (self.rect.right-self.rect.left)//2
        # if pygame.key.get_pressed()[pygame.K_UP]:
        #     self.rect.top -= 5
        # if pygame.key.get_pressed()[pygame.K_DOWN]:
        #     self.rect.top += 5
        # if pygame.key.get_pressed()[pygame.K_LEFT]:
        #     self.rect.left -= 5
        # if pygame.key.get_pressed()[pygame.K_RIGHT]:
        #     self.rect.left += 5
        if self.rect.right >= self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom
        if self.rect.top <= 0:
            self.rect.top = 0
        x = self.rect.left + (self.rect.right-self.rect.left)//2
        y = self.rect.top + (self.rect.bottom-self.rect.top)//2
        self.position = x , y
        
    # 加血
    def addlife(self):     
        if self.blood + 25 >= 100:
            self.blood = 100
        else:
            self.blood += 25

    # 加载底部血量   
    def loadblood(self):
        if self.blood >= 25:
            self.screen.blit(self.blood_image,(410,630))
            if self.blood >= 50:
                self.screen.blit(self.blood_image,(360,630))
                if self.blood >= 75:
                    self.screen.blit(self.blood_image,(310,630))
                    if self.blood >= 100:
                        self.screen.blit(self.blood_image,(260,630))

    def loadboom(self):
        self.screen.blit(self.boom_image,(20,630))
        text = self.font.render('x'+str(self.boom),True,(255,255,255))
        self.screen.blit(text,(70,650))

    def killed(self):
        # self.rect.left = self.position[0] - self.image.get_width()//2
        # self.rect.top = self.position[1] - self.image.get_height()//2
        if self.clo >= 80:
            self.over = True
            return      
        self.image = pygame.image.load('images/me_destroy_'+ str(self.clo // 20 +1) +'.png')

    def oneshoot(self):
        t = bullet(self.position,-1,self.screen)
        return t

    def doubleshoot(self):
        self.dbullet += 1
        t = bullet([self.position[0]-5,self.position[1]],-1,self.screen)
        r = bullet([self.position[0]+5,self.position[1]],-1,self.screen)
        return t , r

    # 刷新状态
    def update(self):
        self.loadblood()
        self.loadboom()
        if self.active :
            self.move()
            if self.blood <= 0 :
                self.active = False
                self.clo = 0
            if self.clo % 10 < 5 :
                self.image = pygame.image.load('images/me2.png')
            else:
                self.image = pygame.image.load('images/me1.png') 
        else:
            self.killed()
        self.screen.blit(self.image,self.rect)
        self.clo += 1
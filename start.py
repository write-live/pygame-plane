import pygame
from pygame.locals import *
import sys
import random

from hero import *
from bullet import *
from enermy import *
from down import *

class start():
    def __init__(self,screen):
        self.background = pygame.image.load('images/background.png')

        self.mybulletgroup = pygame.sprite.Group()
        self.enermygroup = pygame.sprite.Group()
        self.bulletgroup = pygame.sprite.Group()
        self.bombgroup = pygame.sprite.Group()
        self.lifegroup = pygame.sprite.Group()
        self.killedgroup = pygame.sprite.Group()
        self.dbulletgroup = pygame.sprite.Group()

        self.mine = hero(screen)
        self.clock = pygame.time.Clock()
        self.clo = 0
        self.level = 1
        self.screen = screen
        self.score = 0
        self.font = pygame.font.SysFont('Arial',40)
        self.pause = False
        self.pause_image = pygame.image.load('images/resume_nor.png')
        self.pause_rect = self.pause_image.get_rect()
        self.pause_rect.top = 400
        self.pause_rect.left = 215
        self.again_image = pygame.image.load('images/again.png')
        self.again_rect = self.again_image.get_rect()
        self.again_rect.top = 400
        self.again_rect.left = 95
        self.over_image = pygame.image.load('images/gameover.png')
        self.over_rect = self.over_image.get_rect()
        self.over_rect.top = 450
        self.over_rect.left = 95


    def down_gift(self,enermy):
        self.score += enermy.score
        i = random.randrange(15)
        if i == 6:
            t = life(self.screen,enermy.position)
            self.lifegroup.add(t)
        elif i == 7:
            t = bomb(self.screen,enermy.position)
            self.bombgroup.add(t)
        elif i == 8:
            t = dbullet(self.screen,enermy.position)
            self.dbulletgroup.add(t)

    def collide_check(self):
        for i in self.mybulletgroup.sprites():
            for j in self.enermygroup.sprites():
                if pygame.sprite.collide_mask(i, j):
                    i.kill()
                    j.blood -= 25
                    if j.blood == 0 and j.alive :
                        self.down_gift(j)
                        j.kill()
                        self.killedgroup.add(j)
            for j in self.bulletgroup.sprites():
                if pygame.sprite.collide_mask(i, j):
                    i.kill()
                    j.kill()
                    del j
        for i in self.enermygroup.sprites():
            if pygame.sprite.collide_mask(i , self.mine):
                i.blood = 0
                self.down_gift(i)
                i.kill()
                self.killedgroup.add(i)
                self.mine.blood -= 25
        for i in self.bulletgroup.sprites():
            if pygame.sprite.collide_mask(i,self.mine):
                i.kill()
                del i
                self.mine.blood -= 25
        for i in self.bombgroup.sprites():
            if pygame.sprite.collide_mask(i,self.mine):
                i.kill()
                del i
                self.mine.boom += 1
        for i in self.lifegroup.sprites():
            if pygame.sprite.collide_mask(i,self.mine):
                i.kill()
                del i 
                self.mine.addlife()
        for i in self.dbulletgroup.sprites():
            if pygame.sprite.collide_mask(i,self.mine):
                i.kill()
                del i
                self.mine.dbullet = 0

    def Pause(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index == 0 and x >= self.pause_rect.left and x <= self.pause_rect.right and y >= self.pause_rect.top and y <= self.pause_rect.bottom:
                            self.pause = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    self.pause = False
        if x >= self.pause_rect.left and x <= self.pause_rect.right and y >= self.pause_rect.top and y <= self.pause_rect.bottom:
            self.Start = pygame.image.load('images/resume_pressed.png')
        else:
            self.Start = pygame.image.load('images/resume_nor.png')
        self.screen.blit(self.pause_image,self.pause_rect)


    def over(self):
        over_text = self.font.render('GAME OVER',True,(255,255,255))
        self.screen.blit(over_text,(140,250))
        self.screen.blit(self.over_image,self.over_rect)
        self.screen.blit(self.again_image,self.again_rect)

    def main(self):
        while True:
            if self.mine.over:
                self.over()
                x, y = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pressed_array = pygame.mouse.get_pressed()
                        for index in range(len(pressed_array)):
                            if pressed_array[index]:
                                if index == 0 and x >= self.again_rect.left and x <= self.again_rect.right and y >= self.again_rect.top and y <= self.again_rect.bottom:
                                    return 1
                                if index == 0 and x >= self.over_rect.left and x <= self.over_rect.right and y >= self.over_rect.top and y <= self.over_rect.bottom:
                                    sys.exit()
            elif self.pause:
                self.Pause()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_a:
                            self.pause = True
                        if event.key == K_SPACE and self.mine.boom > 0:
                            self.mine.boom -= 1
                            for i in self.bulletgroup.sprites():
                                i.kill()
                                del i
                            for i in self.enermygroup.sprites():
                                i.blood = 0
                                self.down_gift(i)
                                i.kill()
                                self.killedgroup.add(i)
            
                for each in self.enermygroup.sprites():
                    bul = each.shoot()
                    if bul != None:
                        self.bulletgroup.add(bul)

                if self.clo % 20 == 0 and self.mine.active :
                    if self.mine.dbullet >= 18:
                        t = self.mine.oneshoot()
                        self.mybulletgroup.add(t)
                    else:
                        t , r =self.mine.doubleshoot()
                        self.mybulletgroup.add(t)
                        self.mybulletgroup.add(r)

                level = self.score // 1000
                speed = 120 - level
                speed = speed if speed >=30 else 30
                if self.clo % speed == 0:
                    t = enermy(self.screen)
                    self.enermygroup.add(t)
            
                self.collide_check()

                self.screen.blit(self.background,(0,0))
                self.bombgroup.update()
                self.lifegroup.update()
                self.dbulletgroup.update()
                self.bulletgroup.update()
                self.mybulletgroup.update()
                self.mine.update()
                self.enermygroup.update()
                self.killedgroup.update()

                score_font = self.font.render('score: '+str(self.score),True,(255,255,255))
                self.screen.blit(score_font,(150,20))
        
            self.clo += 1
            self.clock.tick(60)
            pygame.display.update()
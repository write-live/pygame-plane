import pygame

class bomb(pygame.sprite.Sprite):
    def __init__(self ,screen, position):
        super().__init__()
        self.image = pygame.image.load('images/bomb_supply.png')
        self.rect = self.image.get_rect()
        self.rect.left = position[0] - self.image.get_width()//2
        self.rect.top = position[1] - self.image.get_height()//2
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top += 1
        if self.rect.top >= self.screen_rect.bottom:
            self.kill()
            del self

    def update(self):
        self.move()
        self.screen.blit(self.image,self.rect)

class life(pygame.sprite.Sprite):
    def __init__(self ,screen, position):
        super().__init__()
        self.image = pygame.image.load('images/life.png')
        self.rect = self.image.get_rect()
        self.rect.left = position[0] - self.image.get_width()//2
        self.rect.top = position[1] - self.image.get_height()//2
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top += 1
        if self.rect.top >= self.screen_rect.bottom:
            self.kill()
            del self

    def update(self):
        self.move()
        self.screen.blit(self.image,self.rect)

class dbullet(pygame.sprite.Sprite):
    def __init__(self ,screen, position):
        super().__init__()
        self.image = pygame.image.load('images/bullet_supply.png')
        self.rect = self.image.get_rect()
        self.rect.left = position[0] - self.image.get_width()//2
        self.rect.top = position[1] - self.image.get_height()//2
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top += 1
        if self.rect.top >= self.screen_rect.bottom:
            self.kill()
            del self

    def update(self):
        self.move()
        self.screen.blit(self.image,self.rect)
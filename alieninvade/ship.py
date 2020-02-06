import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        '''初始化飞船设置初始位置'''
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        '''将飞船放置底部中央'''
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        '''在飞船的属性center中存储小数值'''
        self.center = float(self.rect.centerx)

        '''移动标志'''
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
            # self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
            # self.rect.centerx -= 1
        # self.rect.centerx = self.center
        # print(self.rect.centerx)

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.center = self.screen_rect.centerx
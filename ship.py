import pygame

class Ship():
    def __init__(self,screen):
        """初始化飞船并设置其初始位置"""
        self.screen=screen
        #确定飞船的外接矩形
        self.image=pygame.image.load("images/ship.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将飞船放在屏幕的底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

    #将飞船绘制到屏幕中
    def blitme(self):
        self.screen.blit(self.image,self.rect)
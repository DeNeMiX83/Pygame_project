import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites
from sprites.player.base_resize_sprite import BaseResize


class BtnShip(BaseResize):
    def __init__(self, rect):
        super(BtnShip, self).__init__(menu_sprites)
        self.image_1 = 'btn_ship_1.png'
        self.image_2 = 'btn_ship_2.png'
        self.put_image()
        self.rect.x = rect.x + rect.w * 0.9655
        self.rect.y = rect.y + rect.h * 0.44 - self.rect.height // 2
        self.x_cur = self.rect.x
        self.y_cur = self.rect.y

    def update(self, *args):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.resize('btn_ship_2.png')
        else:
            self.resize('btn_ship_1.png')
        self.rect.x = self.x_cur

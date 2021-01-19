import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites
from sprites.base_resize_sprite import BaseResize


class BtnSpecific(BaseResize):
    def __init__(self, rect):
        super(BtnSpecific, self).__init__(menu_sprites)
        self.image = load_image(['menu', 'btn_specifications.png'])
        self.put_image()
        self.rect.x = rect.x + rect.w * 0.9655
        self.rect.y = rect.y + rect.h * 0.8 - self.rect.height // 2
        self.x_cur = self.rect.x
        self.y_cur = self.rect.y

    def update(self, *args):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.resize(self.image_2)
        else:
            self.resize(self.image_1)
        self.rect.x = self.x_cur
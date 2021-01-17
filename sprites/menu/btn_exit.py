import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites
from sprites.player.base_resize_sprite import BaseResize


class BtnExit(BaseResize):
    def __init__(self, x, y):
        super(BtnExit, self).__init__(menu_sprites)
        self.image_1 = 'btn_exit_1.png'
        self.image_2 = 'btn_exit_2.png'
        self.put_image()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y * 1.85 - self.rect.height // 2

    def update(self, *args):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.resize('btn_exit_2.png')
        else:
            self.resize('btn_exit_1.png')
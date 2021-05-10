import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites
from sprites.base_zoom_sprite import BaseZoom


class BtnStart(BaseZoom):
    def __init__(self, x, y):
        super(BtnStart, self).__init__(menu_sprites)
        self.image_1 = load_image(['menu', 'btn_start_1.png'])
        self.image_2 = load_image(['menu', 'btn_start_2.png'])
        self.put_image(load=False)
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y * 1.6 - self.rect.height // 2

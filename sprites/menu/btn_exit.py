import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites
from sprites.base_zoom_sprite import BaseZoom


class BtnExit(BaseZoom):
    def __init__(self, x, y, *group):
        super(BtnExit, self).__init__(*group)
        self.image_1 = load_image(['menu', 'btn_exit_1.png'])
        self.image_2 = load_image(['menu', 'btn_exit_2.png'])
        self.put_image(load=False)
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y * 1.85 - self.rect.height // 2

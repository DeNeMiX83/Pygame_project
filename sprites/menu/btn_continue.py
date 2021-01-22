import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites
from sprites.base_zoom_sprite import BaseZoom


class BtnContinue(BaseZoom):
    def __init__(self, x, y, *group):
        super(BtnContinue, self).__init__(*group)
        self.image = load_image(['menu', 'btn_continue.png'])
        self.put_image()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y - self.rect.height // 2

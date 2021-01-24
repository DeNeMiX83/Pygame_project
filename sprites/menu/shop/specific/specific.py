import pygame

from data.images.funk import load_image
from sprites.base_resize_sprite import BaseResize
from sprites.config import menu_sprites, menu_specific_sprites
from sprites.base_zoom_sprite import BaseZoom
from sprites.menu.shop.specific.specific_up import SpecificUp


class Specific(BaseZoom, BaseResize):
    def __init__(self, x, y, type):
        group = [menu_sprites, menu_specific_sprites]
        super(Specific, self).__init__(*group)
        self.image = load_image(['menu', f'specific_{type}.png'])
        self.resize(1)
        self.put_image()
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        self.type = type

    def up(self):
        SpecificUp(*self.rect.center)

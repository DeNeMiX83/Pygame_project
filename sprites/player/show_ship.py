import pygame

from data.images.funk import load_image
from sprites.base_resize_sprite import BaseResize
from sprites.config import menu_sprites, menu_ships_sprites, choice_ship_sprites
from sprites.base_zoom_sprite import BaseZoom


class ShowShip(BaseZoom, BaseResize):
    def __init__(self, x, y, type, enable=True):
        group = [menu_sprites, menu_ships_sprites, choice_ship_sprites]
        super(ShowShip, self).__init__(*group, dir='player')
        self.image = load_image(['player', f'lvl_{type}', f'lvl{type}.png'], -1)
        self.resize(1.5)
        self.put_image()
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        self.enable = enable
        self.ship_type = type
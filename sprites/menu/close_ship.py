import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import menu_sprites, menu_ships_sprites, choice_ship_sprites


class CloseShip(pygame.sprite.Sprite):
    def __init__(self, x, y, ship_type):
        super(CloseShip, self).__init__(menu_sprites, choice_ship_sprites)
        self.image = load_image(['menu', 'close_ship.png'])
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        self.ship_type = ship_type
import pygame

from data.config import width, height
from data.images.funk import load_image
from sprites.base_resize_sprite import BaseResize
from sprites.config import menu_sprites


class MenuSpaceShip(BaseResize):
    def __init__(self, type, x, y):
        super(MenuSpaceShip, self).__init__(menu_sprites)
        self.image = load_image(['player', f'lvl_{type}', f'lvl{type}.png'], -1)
        self.resize(1.5)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y * 1.06 - self.rect.height // 2
        self.type_ship = type

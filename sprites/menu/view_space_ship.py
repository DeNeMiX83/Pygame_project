import pygame
from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites, choice_ship_sprites


class ViewSpaceShip(pygame.sprite.Sprite):
    def __init__(self, type_ship, x=width // 2, y=height * 0.37):
        super(ViewSpaceShip, self).__init__(menu_sprites, choice_ship_sprites)
        self.image = load_image(['menu', 'view_space_ship.png'], -1)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        self.type_ship = type_ship
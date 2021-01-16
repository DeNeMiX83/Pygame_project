import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import menu_sprites, menu_ships_sprites


class Cosmonavt(pygame.sprite.Sprite):
    def __init__(self):
        super(Cosmonavt, self).__init__(menu_sprites)
        self.image = pygame.transform.scale(load_image(['menu', 'косм.png']), (width, height))
        self.rect = self.image.get_rect()
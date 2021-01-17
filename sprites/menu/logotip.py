import pygame
from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import menu_sprites, menu_ships_sprites
from sprites.environment.meteor import Meteor


class Logotip(pygame.sprite.Sprite):
    def __init__(self):
        super(Logotip, self).__init__(menu_sprites)
        self.image = load_image(['menu', 'logotip.png'])
        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect.x = width - self.rect.w
        self.rect.y = height - self.rect.h

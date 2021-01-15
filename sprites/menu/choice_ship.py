import pygame
from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites


class ChoiceShip(pygame.sprite.Sprite):
    def __init__(self):
        super(ChoiceShip, self).__init__(menu_sprites)
        self.image = load_image(['menu', 'choice_ship.png'], -1)
        self.rect = self.image.get_rect()
        self.rect.x = width * 0.03
        self.rect.y = height * 0.05


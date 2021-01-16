from random import choice

import pygame

from data.config import size, width, height
from sprites.config import all_sprites, menu_sprites


class Space(pygame.sprite.Sprite):
    def __init__(self, y):
        super(Space, self).__init__(all_sprites, menu_sprites)
        self.image = self.generate_spase(500)
        self.rect = self.image.get_rect()
        self.rect.y = y

    def generate_spase(self, n):
        screen = pygame.Surface(size)
        for _ in range(n):
            pygame.draw.circle(screen, (255, 255, 255),
                               (choice(range(width)), choice(range(height - 2))), choice(range(1, 3)))
        return screen

    def update(self, *arg):
        self.rect = self.rect.move(0, 1)
        if self.rect.y == height:
            self.rect.y = 0 - height
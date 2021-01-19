import time
from random import choice

import pygame

from data.config import size, width, height
from sprites.base_time import BaseTime
from sprites.config import all_sprites, menu_sprites
from sprites.environment.meteor import Meteor
from sprites.environment.planet import Planet


class Space(BaseTime):
    def __init__(self, y):
        super(Space, self).__init__(all_sprites, menu_sprites)
        self.image = self.generate_spase(500)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.planets = []
        self.meteors = []
        self.time_tik = 0.015
        if y >= 0:
            self.planets = [Planet() for _ in range(3)]
            self.meteors = [Meteor() for _ in range(3)]
        self.put_timer()

    def generate_spase(self, n):
        screen = pygame.Surface(size)
        # pygame.draw.line(screen, (255, 0, 0), (0, height), (width, height), 8)
        for _ in range(n):
            pygame.draw.circle(screen, (255, 255, 255),
                               (choice(range(width)), choice(range(height - 2))), choice(range(1, 4)))
        return screen

    def update(self, *arg):
        if time.time() <= self.time_stop:
            return
        self.rect = self.rect.move(0, 1)
        if self.rect.y == height:
            self.rect.y = 0 - height
        self.put_timer()


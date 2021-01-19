import time
from random import randrange, choice

import pygame

from data.config import width, height
from data.images.funk import load_image
from sprites.base_animate_sprite import BaseAnimateSprite
from sprites.config import all_sprites, planet_sprites, menu_sprites


class Planet(BaseAnimateSprite):
    def __init__(self):
        super(Planet, self).__init__(all_sprites, planet_sprites, menu_sprites)
        columns, rows = 4, 2
        sheet = load_image(['environment', f'planets.png'])
        rect = sheet.get_rect()
        d_size = 0.4
        sheet = pygame.transform.scale(sheet, (int(rect.w * d_size), int(rect.h * d_size)))
        self.cut_sheet(sheet, columns, rows)
        self.place()
        self.time_tik = 0.025
        self.put_timer()

    def place(self):
        sheet = choice(self.frames)
        rect = sheet.get_rect()
        d_size = randrange(1, 4)
        self.delta_y = d_size
        self.image = pygame.transform.scale(sheet, (int(rect.w * d_size), int(rect.h * d_size)))
        yes = True
        while yes:
            self.rect.x = randrange(width - self.rect.w)
            self.rect.y = randrange(-height, -self.rect.h)
            if len(pygame.sprite.spritecollide(self, planet_sprites, False)) == 1:
                yes = False

    def update(self, *args):
        if time.time() <= self.time_stop:
            return
        self.rect.y += self.delta_y
        if self.rect.y > height:
            self.place()
        self.put_timer()
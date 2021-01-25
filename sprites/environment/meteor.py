import time
from random import choice, randrange

import pygame

from data.config import width, height
from data.images.funk import load_image
from sprites.base_animate_sprite import BaseAnimateSprite
from sprites.config import all_sprites, meteors_sprites, player_sprites, shot_sprites, menu_sprites
from sprites.environment.coin import Coin
from sprites.show_hp import ShowHP


class Meteor(BaseAnimateSprite):
    def __init__(self):
        super(Meteor, self).__init__(all_sprites, meteors_sprites, menu_sprites)
        columns, rows = 8, 8
        self.image = load_image(['environment', f'meteors.png'])
        self.resize(2)
        self.cut_sheet(self.image, columns, rows)
        self.image = self.frames[self.cur_frame]
        self.place()
        self.radius = self.rect.w * 0.20
        self.time_tik = 0.1
        self.hp_max = 70
        self.hp = self.hp_max
        self.sprite_hp = ShowHP(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h, self)

    def place(self):
        yes = True
        while yes:
            self.rect.x = randrange(width - self.rect.w)
            self.rect.y = randrange(0 - height, -self.rect.h)
            if len(pygame.sprite.spritecollide(self, meteors_sprites, False)) == 1:
                yes = False

    def show_hp(self):
        self.sprite_hp.move(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        n_frames = []
        frames = []
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
            n_frames.append(frames)
            frames = []
        self.frames = choice(n_frames)

    def update(self, *arg):
        self.rect.y += 2
        if self.rect.y > height + 50:
            self.kill()
            return
        if pygame.sprite.spritecollide(self, player_sprites, False, pygame.sprite.collide_circle):
            self.hp -= 30
        for shot in pygame.sprite.spritecollide(self, shot_sprites, True, pygame.sprite.collide_circle):
            self.hp -= shot.damage
        self.show_hp()
        if self.hp <= 0:
            self.kill()
            Coin(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h // 2)
        if time.time() <= self.time_stop:
            return
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.put_timer()

import time
from time import sleep

import pygame


from data.config import size, width, height, FPS
from data.images.funk import load_image
from sprites.base_time import BaseTime
from sprites.environment.bum import Bum
from sprites.config import all_sprites, menu_sprites, player_sprites, meteors_sprites
from sprites.player.space_ship_shot import SpaceShipShot
from sprites.show_hp import ShowHP


class SpaceShip(BaseTime):
    def __init__(self, type):
        super(SpaceShip, self).__init__(all_sprites, menu_sprites, player_sprites)
        self.image = load_image(['player', f'lvl_{type}', f'lvl{type}.png'])
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.width // 2
        self.rect.y = height * 0.38 - self.rect.height // 2
        self.stop = True
        self.type = type
        self.hp_max = 1000
        self.hp = self.hp_max
        self.sprite_hp = ShowHP(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h, 1)
        self.damage = 40
        self.ship_fire = []
        self.time_tik = 0.2
        self.put_timer()
        self.power_magnet = 50

    def show_hp(self):
        # self.sprite_hp.move(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h, self.hp / self.hp_max)
        x = width // 2
        w = 15
        y = height - w
        prosent_hp = self.hp / self.hp_max
        self.sprite_hp.move(x, y, prosent_hp, w, width)

    def can_shoot(self):
        if time.time() >= self.time_stop:
            x = self.rect.x + self.rect.w // 2
            SpaceShipShot(self.type, x, self.rect.y)
            self.put_timer()

    def follow_the_mouse(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        self.rect.move_ip(0, -self.rect.height // 2)

    def update(self, *args):
        if self.stop:
            return
        self.follow_the_mouse()
        for fire in self.ship_fire:
            fire.move(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h)
        if pygame.sprite.spritecollide(self, meteors_sprites, False, pygame.sprite.collide_circle):
            self.hp -= 50
        self.can_shoot()
        self.show_hp()
        if self.hp <= 0:
            self.stop = True
            Bum(self, self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h // 2)
            self.remove(all_sprites)
            for fire in self.ship_fire:
                fire.kill()


import time
from time import sleep

import pygame

from data.config import size, width, height, FPS
from data.images.funk import load_image
from sprites.base_time import BaseTime
from sprites.config import all_sprites, menu_sprites, player_sprites, meteors_sprites, koin_sprites
from sprites.environment.bum import Bum
from sprites.player.fire import ShipFire
from sprites.player.space_ship_shot import SpaceShipShot
from sprites.show_hp import ShowHP


class SpaceShip(BaseTime):
    def __init__(self, type, damage=100, weapon_damage=100, power_magnet=2, hp_max=100):
        super(SpaceShip, self).__init__(all_sprites,  player_sprites)
        self.hp_max = hp_max
        self.hp = self.hp_max
        self.damage = damage
        self.weapon_damage = weapon_damage
        self.power_magnet = power_magnet
        self.image = load_image(['player', f'lvl_{type}', f'lvl{type}.png'])
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.width // 2
        self.rect.y = height * 0.38 - self.rect.height // 2
        self.type = type
        self.sprite_hp = ShowHP(width // 2, height - 15, self, 15, width)
        self.ship_fire = []
        self.fire_cord = []
        self.time_tik = 0.2
        self.put_timer()
        self.stop = False
        # self.put_fire()
        # self.create_fire()

    def magnit_koin(self):
        collade = pygame.sprite.collide_circle_ratio(self.power_magnet)
        for koin in pygame.sprite.spritecollide(self, koin_sprites, False, collade):
            d_x = (self.rect.x + self.rect.w // 2) - (koin.rect.x + koin.rect.w // 2)
            d_y = (self.rect.y + self.rect.h // 2) - (koin.rect.y + koin.rect.h // 2)
            if d_x >= 0:
                koin.rect.x += 3
            if d_y >= 0:
                koin.rect.y += 3
            if d_x <= 0:
                koin.rect.x -= 3
            if d_y <= 0:
                koin.rect.y -= 3

    def show_hp(self):
        # self.sprite_hp.move(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h, self.hp / self.hp_max)
        x = width // 2
        w = 15
        y = height - w
        prosent_hp = self.hp / self.hp_max
        self.sprite_hp.move(x, y, w, width)

    def can_shoot(self):
        if time.time() >= self.time_stop:
            x = self.rect.x + self.rect.w // 2
            SpaceShipShot(self.type, x, self.rect.y, self.weapon_damage)
            self.put_timer()

    def ship_kill(self):
        self.stop = True
        for fire in self.ship_fire:
            fire.kill()
        self.sprite_hp.kill()
        self.remove(all_sprites)
        Bum(self, self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h // 2)

    def follow_the_mouse(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        self.rect.move_ip(0, -self.rect.height // 2)

    def put_fire(self):
        self.fire_cord = [(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h)]

    def create_fire(self):
        self.ship_fire = [ShipFire(*cord) for cord in self.fire_cord]

    def update(self, *args):
        if self.stop:
            return
        self.follow_the_mouse()
        self.put_fire()
        self.magnit_koin()
        for n, fire in enumerate(self.ship_fire):
            fire.move(*self.fire_cord[n])
        for meteor in pygame.sprite.spritecollide(self, meteors_sprites, True, pygame.sprite.collide_circle):
            self.hp -= 50
            meteor.sprite_hp.kill()
            print(meteor)
        self.can_shoot()
        self.show_hp()
        if self.hp <= 0:
            self.ship_kill()


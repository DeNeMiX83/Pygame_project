import pygame

from data.config import size, width, height, FPS
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites, player_sprites
from sprites.player.space_ship_shot import SpaceShipShot


class ShowHP(pygame.sprite.Sprite):
    def __init__(self, x, y, obj, w=3, l=100):
        super(ShowHP, self).__init__(all_sprites)
        self.obj = obj
        self.move(x, y, w, l)

    def move(self, x, y, w=3, l=100):
        len_hp = int(l * (self.obj.hp / self.obj.hp_max))
        if not self.obj.alive():
            print(1)
        if len_hp < 1 or not self.obj.alive():
            self.kill()
            return
        self.image = pygame.surface.Surface((len_hp, w))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y

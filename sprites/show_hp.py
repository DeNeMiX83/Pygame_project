import pygame

from data.config import size, width, height, FPS
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites, player_sprites
from sprites.player.space_ship_shot import SpaceShipShot


class ShowHP(pygame.sprite.Sprite):
    def __init__(self, x, y, hp_procent, w=3, l=100):
        super(ShowHP, self).__init__(all_sprites)
        self.move(x, y, hp_procent, w, l)

    def move(self, x, y, hp_procent, w=3, l=100):
        len_hp = l * hp_procent
        if len_hp < 1:
            self.kill()
            return
        self.image = pygame.surface.Surface((len_hp, w))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y

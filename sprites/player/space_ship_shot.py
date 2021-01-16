import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import all_sprites, shot_sprites


class SpaceShipShot(pygame.sprite.Sprite):
    def __init__(self, type, x, y, damage=100):
        super(SpaceShipShot, self).__init__(all_sprites, shot_sprites)
        self.image = load_image(['player', f'lvl_{type}', f'shot.png'])
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        self.damage = damage

    def update(self, *arg):
        self.rect.y -= 3
        if (self.rect.y + self.rect.h) < 0:
            self.kill()
import pygame
from sprites.config import all_sprites


class ShowHP(pygame.sprite.Sprite):
    def __init__(self, x, y, obj, w=3, l=100, put_center=True):
        super(ShowHP, self).__init__(all_sprites)
        self.obj = obj
        self.put_center = put_center
        self.move(x, y, w, l)

    def move(self, x, y, w=3, l=100):
        len_hp = int(l * (self.obj.hp / self.obj.hp_max))
        if len_hp <= 0:
            return
        self.image = pygame.surface.Surface((len_hp, w))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x - (self.rect.w // 2 if self.put_center else 0)
        self.rect.y = y

    def update(self, *args):
        if not self.obj.alive() or self.obj.hp <= 0:
            self.kill()

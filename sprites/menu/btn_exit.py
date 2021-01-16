import pygame

from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites


class BtnExit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(BtnExit, self).__init__(menu_sprites)
        self.image = load_image(['menu', 'btn_exit.png'])
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y * 1.85 - self.rect.height // 2
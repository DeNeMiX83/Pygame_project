import pygame
from data.config import size, width, height
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites


class BtnStart(pygame.sprite.Sprite):
    def __init__(self):
        super(BtnStart, self).__init__(menu_sprites)
        self.image = load_image(['menu', 'btn_start.png'], -1)
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.width // 2
        self.rect.y = height * 0.65 - self.rect.height // 2



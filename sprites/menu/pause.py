import pygame
from data.config import width, height
from data.images.funk import load_image
from sprites.config import game_pause_sprites


class Pause(pygame.sprite.Sprite):
    def __init__(self):
        super(Pause, self).__init__(game_pause_sprites)
        self.image = load_image(['menu', 'pause.png'])
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.w // 2
        self.rect.y = height * 0.3 - self.rect.h // 2
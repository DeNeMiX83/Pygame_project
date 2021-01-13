import pygame
from data.config import size, width, height, screen
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super(GameOver, self).__init__(menu_sprites)
        x, y, w, h = screen.get_rect()
        self.image = pygame.transform.scale(load_image(['menu', 'zastavka.jpg'], -1), (w, h))
        self.rect = self.image.get_rect()
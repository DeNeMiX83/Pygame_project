import pygame
from data.config import size, width, height, screen
from data.images.funk import load_image
from game_things import koins
from sprites.config import all_sprites, menu_sprites


class ViewKoins(pygame.sprite.Sprite):
    def __init__(self):
        super(ViewKoins, self).__init__(menu_sprites)
        pass

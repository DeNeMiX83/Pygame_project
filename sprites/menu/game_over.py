import pygame

from data.config import size, width, height
from sprites.config import  game_over_sprites
from sprites.menu.game_over_title import GameOverTitle
from sprites.menu.prizrak import Prizrak


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super(GameOver, self).__init__(game_over_sprites)
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.draw_prizrak()
        self.draw_title()

    def draw_prizrak(self):
        Prizrak(width * 0.5, height * 0.4)

    def draw_title(self):
        GameOverTitle(width * 0.5, height * 0.4)

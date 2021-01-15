import pygame

from data.config import width, height
from data.images.funk import load_image
from sprites.config import menu_sprites


class MenuSpaceShip(pygame.sprite.Sprite):
    def __init__(self, type):
        super(MenuSpaceShip, self).__init__(menu_sprites)
        self.image = load_image(['player', f'lvl_{type}', f'lvl{type}.png'])
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.width // 2
        self.rect.y = height * 0.38 - self.rect.height // 2
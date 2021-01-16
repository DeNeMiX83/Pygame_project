import pygame

from data.config import width, height
from data.images.funk import load_image
from sprites.config import menu_sprites


class MenuSpaceShip(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super(MenuSpaceShip, self).__init__(menu_sprites)
        image = load_image(['player', f'lvl_{type}', f'lvl{type}.png'], -1)
        rect = image.get_rect()
        d_size = 1.5
        self.image = pygame.transform.scale(image, (int(rect.w * d_size), int(rect.h * d_size)))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y * 1.1 - self.rect.height // 2
import pygame

from data.images.funk import load_image
from sprites.config import menu_sprites, menu_specific_sprites
from sprites.base_resize_sprite import BaseResize
from sprites.menu.shop.specific.specific_up import SpecificUp


class Specific(BaseResize):
    def __init__(self, x, y, type):
        group = [menu_sprites, menu_specific_sprites]
        super(Specific, self).__init__(*group, dir='menu')
        image = load_image(['menu', f'specific_{type}.png'])
        rect = image.get_rect()
        d_size = 1
        self.image = pygame.transform.scale(image, (int(rect.w * d_size), int(rect.h * d_size)))
        self.put_image()
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        self.type = type

    def up(self):
        print(1)
        SpecificUp(*self.rect.center)

import pygame
from data.images.funk import load_image


class BaseResize(pygame.sprite.Sprite):
    def __init__(self, *group, dir='menu'):
        super(BaseResize, self).__init__(*group)
        # self.image_1 = 'btn_exit_1.png'
        # self.image_2 = 'btn_exit_2.png'
        self.dir = dir
        # self.put_image()

    def put_image(self):
        if isinstance(self.image_1, str):
            self.image = load_image([self.dir, self.image_1])
        else:
            self.image = self.image_1
        self.rect = self.image.get_rect()

    def resize(self, image):
        center = self.rect.center
        if isinstance(image, str):
            self.image = load_image([self.dir, image])
        else:
            self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self, *args):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.resize(self.image_2)
        else:
            self.resize(self.image_1)
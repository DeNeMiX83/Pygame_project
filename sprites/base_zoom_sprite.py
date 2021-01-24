import pygame
from data.images.funk import load_image
from sprites.base_time import BaseTime


class BaseZoom(BaseTime):
    def __init__(self, *group, d_size=1.1):
        super(BaseZoom, self).__init__(*group)
        # self.image = 'btn_exit.png'
        self.d_size = d_size
        # self.put_image()

    def put_image(self, load=True):
        if load:
            rect = self.image.get_rect()
            self.image_1 = self.image
            self.image_2 = pygame.transform.scale(self.image, (
                int(rect.w * self.d_size), int(rect.h * self.d_size)))
        self.image = self.image_1
        self.rect = self.image.get_rect()

    def zoom(self, image):
        center = self.rect.center
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self, *args):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.zoom(self.image_2)
        else:
            self.zoom(self.image_1)
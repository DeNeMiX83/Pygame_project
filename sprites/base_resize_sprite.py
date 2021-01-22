import pygame


class BaseResize(pygame.sprite.Sprite):
    def __init__(self, *group):
        super(BaseResize, self).__init__(*group)
        # self.image = load_image(['menu', f'prizrak.png'])

    def resize(self, d_size):
        sheet = self.image
        rect = sheet.get_rect()
        self.image = pygame.transform.scale(sheet, (int(rect.w * d_size), int(rect.h * d_size)))
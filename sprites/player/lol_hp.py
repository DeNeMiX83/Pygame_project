import time
import pygame
from data.images.funk import load_image
from sprites.base_time import BaseTime
from sprites.base_zoom_sprite import BaseZoom
from sprites.config import all_sprites


class LolHp(BaseZoom):
    def __init__(self, x, y):
        super(LolHp, self).__init__(all_sprites, d_size=1.1)
        self.image = load_image(['player', 'lol_hp.png'])
        self.resize(0.5)
        self.put_image(load=True)
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        self.time_tik = 0.8
        self.put_timer()

    def update(self, *arg):
        if time.time() < self.time_stop:
            return
        if self.image == self.image_1:
            self.zoom(self.image_2)
        else:
            self.zoom(self.image_1)
        self.put_timer()
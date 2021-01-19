import time

from data.images.funk import load_image
from sprites.base_animate_sprite import BaseAnimateSprite
from sprites.config import all_sprites


class Bum(BaseAnimateSprite):
    def __init__(self, ship, x, y):
        super(Bum, self).__init__(all_sprites)
        columns, rows = 5, 4
        sheet = load_image(['environment', 'bum.png'], -1)
        self.cut_sheet(sheet, columns, rows)
        self.image = self.frames[self.cur_frame]
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        self.time_tik = 0.12
        self.ship = ship

    def update(self, *arg):
        if time.time() <= self.time_stop:
            return
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.put_timer()
        if self.cur_frame == len(self.frames) - 1:
            self.ship.kill()


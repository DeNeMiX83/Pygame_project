import time
from data.images.funk import load_image
from sprites.base_animate_sprite import BaseAnimateSprite
from sprites.config import all_sprites, player_sprites, game_over_sprites


class GameOverTitle(BaseAnimateSprite):
    def __init__(self, x, y):
        super(GameOverTitle, self).__init__(game_over_sprites)
        columns, rows = 2, 1
        self.image = load_image(['menu', f'game_over_title.png'])
        self.resize(0.8)
        self.cut_sheet(self.image, columns, rows)
        self.image = self.frames[self.cur_frame]
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        self.time_tik = 1
        self.put_timer()

    def update(self, *arg):
        if time.time() < self.time_stop:
            return
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.put_timer()
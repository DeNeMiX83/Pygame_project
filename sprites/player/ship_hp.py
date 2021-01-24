import time

from data.config import width, height
from data.images.funk import load_image
from sprites.base_animate_sprite import BaseAnimateSprite
from sprites.config import all_sprites, player_sprites
from sprites.player.lol_hp import LolHp
from sprites.show_hp import ShowHP


class ShipHp(BaseAnimateSprite):
    def __init__(self, x, y, ship):
        super(ShipHp, self).__init__(all_sprites, player_sprites)
        columns, rows = 3, 1
        self.image = load_image(['player', f'view_hp.png'])
        self.resize(0.5)
        self.cut_sheet(self.image, columns, rows)
        self.image = self.frames[self.cur_frame]
        self.rect.x = x - self.rect.w
        self.rect.y = y - self.rect.h
        self.ship = ship
        x = width - self.rect.w // 2
        w = 10
        y = height - self.rect.h // 2
        self.sprite_hp = ShowHP(x, y, self.ship, w, self.rect.w, put_center=False)
        self.view_hp = False

    def show_hp(self):
        x = width - self.rect.w * 0.96
        w = 17
        y = height - self.rect.h * 0.35
        self.sprite_hp.move(x, y, w, self.rect.w * 0.65)

    def update(self, *arg):
        if self.ship.hp / self.ship.hp_max * 100 < 33:
            self.image = self.frames[2]
            if not self.view_hp:
                LolHp(width // 2, height * 0.92)
                self.view_hp = True
        elif self.ship.hp / self.ship.hp_max * 100 < 66:
            self.image = self.frames[1]
        self.show_hp()

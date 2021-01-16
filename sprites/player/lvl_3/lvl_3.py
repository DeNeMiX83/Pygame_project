from sprites.player.fire import ShipFire
from sprites.player.space_ship import SpaceShip


class ShipLevel3(SpaceShip):
    def __init__(self, type, damage=100, weapon_damage=30, power_magnet=2.6, hp_max=3000):
        super(ShipLevel3, self).__init__(type, damage, weapon_damage, power_magnet, hp_max)
        self.time_tik = 0.4
        self.put_fire()
        self.create_fire()

    def put_fire(self):
        self.fire_cord = [(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h * 0.97),
                          (self.rect.x + self.rect.w * 0.28, self.rect.y + self.rect.h * 0.87),
                          (self.rect.x + self.rect.w * 0.74, self.rect.y + self.rect.h * 0.87)]


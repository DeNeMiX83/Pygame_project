from sprites.player.fire import ShipFire
from sprites.player.space_ship import SpaceShip


class ShipLevel4(SpaceShip):
    def __init__(self, type, damage=50, weapon_damage=35, power_magnet=3, hp_max=4000):
        super(ShipLevel4, self).__init__(type, damage, weapon_damage, power_magnet, hp_max)
        self.time_tik = 0.2
        self.put_fire()
        self.create_fire()

    def put_fire(self):
        self.fire_cord = [(self.rect.x + self.rect.w * 0.39, self.rect.y + self.rect.h * 0.98),
                          (self.rect.x + self.rect.w * 0.63, self.rect.y + self.rect.h * 0.98)]


from sprites.player.fire import ShipFire
from sprites.player.space_ship import SpaceShip


class ShipLevel1(SpaceShip):
    def __init__(self, type, damage=30, weapon_damage=8, power_magnet=2, hp_max=1000):
        super(ShipLevel1, self).__init__(type, damage, weapon_damage, power_magnet, hp_max)
        self.time_tik = 0.2
        self.put_fire()
        self.create_fire()

    def put_fire(self):
        self.fire_cord = [(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h * 0.98)]




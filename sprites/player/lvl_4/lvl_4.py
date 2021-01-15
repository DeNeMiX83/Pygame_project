from sprites.player.fire import ShipFire
from sprites.player.space_ship import SpaceShip


class ShipLevel4(SpaceShip):
    def __init__(self, type):
        super(ShipLevel4, self).__init__(type)
        self.hp_max = 4000
        self.hp = self.hp_max
        self.damage = 30
        self.weapon_damage = 35
        self.ship_fire = []
        self.time_tik = 0.2
        self.put_fire()

    def put_fire(self):
        self.ship_fire.append(ShipFire(self.rect.x + self.rect.w, self.rect.y + self.rect.h))

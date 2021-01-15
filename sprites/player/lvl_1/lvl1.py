from sprites.player.fire import ShipFire
from sprites.player.space_ship import SpaceShip


class ShipLevel1(SpaceShip):
    def __init__(self, type):
        super(ShipLevel1, self).__init__(type)
        self.hp_max = 1000
        self.hp = self.hp_max
        self.damage = 30
        self.weapon_damage = 8
        self.time_tik = 0.2
        self.put_fire()
        self.create_fire()

    def put_fire(self):
        self.fire_cord = [(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h)]




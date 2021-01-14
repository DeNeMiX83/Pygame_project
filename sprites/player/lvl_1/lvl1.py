from sprites.player.fire import ShipFire
from sprites.player.space_ship import SpaceShip


class ShipLevel1(SpaceShip):
    def __init__(self, lvl):
        super(ShipLevel1, self).__init__(lvl)
        self.hp_max = 1000
        self.hp = self.hp_max
        self.shot_max = 2
        self.damage = 30
        self.ship_fire = []
        self.put_fire()

    def put_fire(self):
        self.ship_fire.append(ShipFire(self.rect.x + self.rect.w, self.rect.y + self.rect.h))


import pygame


from data.config import size, width, height, FPS
from data.images.funk import load_image
from sprites.config import all_sprites, menu_sprites, player_sprites, meteors_sprites
from sprites.player.space_ship_shot import SpaceShipShot
from sprites.show_hp import ShowHP


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, type):
        super(SpaceShip, self).__init__(all_sprites, menu_sprites, player_sprites)
        self.image = load_image(['player', f'lvl_{type}', f'lvl{type}.png'])
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.width // 2
        self.rect.y = height * 0.38 - self.rect.height // 2
        self.stop = True
        self.shooting = False
        self.type = type
        self.shot_max = 8
        self.shot_cur = 0
        self.hp_max = 1000
        self.hp = self.hp_max
        self.sprite_hp = ShowHP(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h, 1)
        self.damage = 40
        self.ship_fire = []

    def show_hp(self):
        # self.sprite_hp.move(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h, self.hp / self.hp_max)
        x = width // 2
        w = 15
        y = height - w
        prosent_hp = self.hp / self.hp_max
        self.sprite_hp.move(x, y, prosent_hp, w, width)

    def can_shoot(self):
        if self.shooting:
            self.shot_cur += 1
            if self.shot_cur % round(FPS / self.shot_max, 0) == 0:
                x = self.rect.x + self.rect.w // 2
                SpaceShipShot(self.type, x, self.rect.y)

    def follow_the_mouse(self):
        pos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        self.rect.midtop = pos
        self.rect.move_ip(0, -self.rect.height // 2)

    def update(self, *args):
        if self.stop:
            return
        self.follow_the_mouse()
        for fire in self.ship_fire:
            fire.move(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.shooting = True
        if args and args[0].type == pygame.MOUSEBUTTONUP and \
                self.rect.collidepoint(args[0].pos):
            self.shooting = False
        if pygame.sprite.spritecollide(self, meteors_sprites, False, pygame.sprite.collide_circle):
            self.hp -= 50
        self.can_shoot()
        self.show_hp()
        if self.hp <= 0:
            self.stop = True
            self.kill()
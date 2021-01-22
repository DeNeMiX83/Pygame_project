import pygame

from game.game_things import info
from sprites.config import menu_sprites, menu_specific_sprites


class ViewShipSpecific(pygame.sprite.Sprite):
    def __init__(self, x, y, size, type_ship):
        group = [menu_sprites, menu_specific_sprites]
        super(ViewShipSpecific, self).__init__(*group)
        self.fon = pygame.Surface(size)
        self.fon.set_colorkey((0, 0, 0))
        self.font = pygame.font.Font(None, 30)
        self.type_ship = type_ship
        self.image = self.fon
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        self.type_ship = type_ship

    def update(self, *args):
        self.fon.fill((0, 0, 0))
        weapon_damage = info[f'ship_{self.type_ship}']['weapon_damage']
        power_magnet = info[f'ship_{self.type_ship}']['power_magnet']
        hp_max = info[f'ship_{self.type_ship}']['hp_max']
        text_coord = self.fon.get_rect().h // 3
        text = [f'Дамаг: {weapon_damage}',
                f'Сила магнита: {power_magnet}',
                f'Макс здоровье: {hp_max}']
        for line in text:
            string_rendered = self.font.render(line, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.fon.blit(string_rendered, intro_rect)

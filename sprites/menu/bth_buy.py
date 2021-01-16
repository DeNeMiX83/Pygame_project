import pygame

from data.images.funk import load_image
from game_things import info
from sprites.config import menu_sprites, menu_ships_sprites, choice_ship_sprites
from sprites.player.show_ship import ShowShip


class BtnBuyShip(pygame.sprite.Sprite):
    def __init__(self, x, y, prise, ship_type):
        super(BtnBuyShip, self).__init__(menu_sprites, choice_ship_sprites)
        self.image = load_image(['menu', 'buy_ship_5.png'])
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        font = pygame.font.Font(None, 24)
        string_rendered = font.render(f'{prise}', False, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.x = 0 + self.rect.w // 2 - intro_rect.w // 2
        intro_rect.y = 0 + self.rect.h * 0.5
        self.image.blit(string_rendered, intro_rect)
        self.ship_type = ship_type
        self.prise = prise

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if info['koins'] >= self.prise:
                info['koins'] -= self.prise
                info[f'ship_{self.ship_type}']['condition'] = 'open'
                for sprite in choice_ship_sprites:
                    if sprite.ship_type == self.ship_type:
                        if isinstance(sprite, ShowShip):
                            sprite.enable = True
                        else:
                            sprite.kill()

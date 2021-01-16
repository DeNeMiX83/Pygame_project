import pygame
from data.config import size, width, height
from data.images.funk import load_image
from game_things import info
from sprites.config import all_sprites, menu_sprites, view_ship_sprites
from sprites.menu.view_space_ship import ViewSpaceShip


class BtnBuyShip(pygame.sprite.Sprite):
    def __init__(self, x, y, prise, ship_type):
        super(BtnBuyShip, self).__init__(menu_sprites, view_ship_sprites)
        self.image = load_image(['menu', 'buy_ship_2.png'], -1)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w // 2
        self.rect.y = y - self.rect.h // 2
        font = pygame.font.Font(None, 30)
        string_rendered = font.render(f'{prise}', False, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.x = 0 + self.rect.w // 2 - intro_rect.w // 2
        intro_rect.y = 0 + self.rect.h * 0.16
        self.image.blit(string_rendered, intro_rect)
        self.ship_type = ship_type
        self.prise = prise

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if info['koins'] >= self.prise:
                info['koins'] -= self.prise
                info[f'ship_{self.ship_type}'] = 'open'
                for sprite in view_ship_sprites:
                    if sprite.ship_type == self.ship_type:
                        if isinstance(sprite, ViewSpaceShip):
                            sprite.enable = True
                        else:
                            sprite.kill()

import sys
from random import choice
from data.config import width, height, screen
import pygame

from sprites.config import all_sprites, menu_sprites, player_sprites, meteors_sprites, shot_sprites
from sprites.funk.game import create_space, show_space_ship
from sprites.menu.btn_exit import BtnExit
from sprites.menu.btn_start import BtnStart
from sprites.menu.game_over import GameOver
from sprites.menu.view_space_ship import ViewSpaceShip

FPS = 100
running = True


def terminate():
    pygame.quit()
    sys.exit()


def clear_sprites_group():
    all_sprites.empty()
    menu_sprites.empty()
    player_sprites.empty()
    meteors_sprites.empty()
    shot_sprites.empty()


def game_over():
    pygame.mouse.set_visible(True)
    clear_sprites_group()
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    GameOver()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return start_screen(screen)
        menu_sprites.update()
        menu_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def start_screen(screen):
    space_ship_type = 1
    clock = pygame.time.Clock()
    create_space()
    ViewSpaceShip()
    btn_start = BtnStart()
    btn_exit = BtnExit()
    ship = show_space_ship(space_ship_type)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_start.rect.collidepoint(event.pos):
                    ship.stop = False
                    return ship
                if btn_exit.rect.collidepoint(event.pos):
                    terminate()
        menu_sprites.update()
        menu_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)



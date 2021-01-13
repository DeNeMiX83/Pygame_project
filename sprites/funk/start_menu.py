import sys
from random import choice
from data.config import width, height
import pygame

from sprites.config import all_sprites
from sprites.environment.space import Space
from sprites.menu.btn_exit import BtnExit
from sprites.menu.btn_start import BtnStart
from sprites.menu.view_space_ship import ViewSpaceShip
from sprites.player.space_ship import SpaceShip

FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def start_screen(screen):
    clock = pygame.time.Clock()
    create_space()
    ViewSpaceShip()
    BtnStart()
    BtnExit()
    show_space_ship()
    print(1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def create_space():
    Space(0 - height)
    Space(0)


def show_space_ship():
    SpaceShip(1)
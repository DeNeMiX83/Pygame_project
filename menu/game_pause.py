import pygame

import game_things
from data.config import width, height, size, screen, FPS
from game_things import info
from menu.game_over import game_over
from menu.start_menu import terminate, FPS
from sprites.config import game_pause_sprites
from sprites.funk.game import view_koins
from sprites.menu.btn_continue import BtnContinue
from sprites.menu.btn_exit import BtnExit
from sprites.menu.btn_start import BtnStart
from sprites.menu.pause import Pause


def game_pause():
    global FPS
    FPS = 0
    screen_copy = screen.copy()
    fon = pygame.Surface(size)
    fon.set_colorkey((0, 0, 0))
    pygame.mouse.set_visible(True)
    Pause()
    clock = pygame.time.Clock()
    btn_continue = BtnContinue(width // 2, height // 2, game_pause_sprites)
    btn_exit = BtnExit(width // 2, height * 0.32, game_pause_sprites)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_exit.rect.collidepoint(event.pos):
                    game_over()
                    return True
                if btn_continue.rect.collidepoint(event.pos):
                    return
        screen.blit(screen_copy, (0, 0))
        fon.fill((0, 0, 0))
        game_pause_sprites.update()
        game_pause_sprites.draw(fon)
        screen.blit(fon, (0, 0))
        pygame.display.flip()
        clock.tick(100)
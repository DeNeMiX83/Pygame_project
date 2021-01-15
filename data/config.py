import pygame

pygame.init()
surface = pygame.display.Info()
width = int(surface.current_w)
height = int(surface.current_h)
size = width, height
screen = pygame.display.set_mode(size)
max_space_ship_lvl = 3
FPS = 100

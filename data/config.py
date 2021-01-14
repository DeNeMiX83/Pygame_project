import pygame

pygame.init()
surface = pygame.display.Info()
width = int(surface.current_w * 0.5)
height = int(surface.current_h * 0.8)
size = width, height
screen = pygame.display.set_mode(size)
max_space_ship_lvl = 3
FPS = 100

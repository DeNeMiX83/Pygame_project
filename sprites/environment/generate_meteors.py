import time

import pygame

from sprites.config import meteors_sprites
from sprites.environment.meteor import Meteor


class GenerateMeteors():

    def __init__(self):
        super(GenerateMeteors, self).__init__()
        self.new_data()

    def generate(self):
        now = pygame.time.get_ticks()
        time_passed = round(time.time() - self.time_start)
        cold_tick = time_passed // 1
        if now - self.last >= (self.cooldown - cold_tick * 20) and len(meteors_sprites) < 26:
            self.last = now
            Meteor(hp_bost=cold_tick * 15)

    def pause(self):
        self.time_delta = time.time() - self.time_start

    def start(self):
        self.time_start = time.time() - self.time_delta

    def new_data(self):
        self.time_start = time.time()
        self.last = pygame.time.get_ticks()
        self.cooldown = 1000
        self.time_delta = 0

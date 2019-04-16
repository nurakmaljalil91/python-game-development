import pygame
from src.gameobjects.GameObject import GameObject
from src.Settings import *


class Enemy(GameObject):
    def __init__(self, x, y, width, height):
        GameObject.__init__(self, x, y, width, height)
        self.tag = 'Enemy'
        print('Enemy is created')

    def start(self):
        pass

    def handle_events(self, event, delta_time):
        pass

    def update(self, delta_time):
        pass

    def render(self, window):
        pygame.draw.rect(window, RED, (self.x, self.y, self.width, self.height), 2)

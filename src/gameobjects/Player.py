import pygame
from src.Settings import *
from src.gameobjects.GameObject import GameObject


class Player(GameObject):
    def __init__(self, x, y, width, height):
        GameObject.__init__(self, x, y, width, height)

    def handle_events(self, event):
        self.move(event)

    def update(self, delta_time):
        pass

    def render(self, window):

        pygame.draw.rect(
            window, BLUE, (self.x, self.y, self.width, self.height), 0)

    def move(self, event):
        if event.key == pygame.K_w:
            self.y -= 1 * TILESIZE
        if event.key == pygame.K_s:
            self.y += 1 * TILESIZE
        if event.key == pygame.K_d:
            self.x += 1 * TILESIZE
        if event.key == pygame.K_a:
            self.x -= 1 * TILESIZE

    def hitbox(self, x, y, width, height):
        pass

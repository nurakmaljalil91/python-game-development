import pygame
from src.scenes.Scene import Scene
from src.Settings import *


class MenuScene(Scene):
    def __init__(self, name):
        Scene.__init__(self, name)

    def start(self):
        pass

    def handle_events(self, event):
        self.event = event
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_a:
                print('test')

    def update(self, delta_time):
        pass

    def render(self, screen):
        self.draw_grid(screen)

    def clear(self):
        pass

    def quit(self):
        # if the scene is quiting the scene manager will
        # peek the next scene
        pass

    def draw_grid(self, screen):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (x, 0), (x, HEIGHT))

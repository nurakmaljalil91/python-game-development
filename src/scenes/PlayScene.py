# from Scene import Scene
# Because this is 2d game instead of 2d game engine
# this is the class where all player, npc and the enemy
# will be located
from src.Settings import *
from src.scenes.Scene import Scene
from src.gameobjects.Player import *
from src.gameobjects.Enemy import Enemy
import pygame


# import sys
# sys.path.append('home/akmal/Documents/python-game-development/src')
# import sys
# from os import path

# sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class PlayScene(Scene):
    def __init__(self, name):
        Scene.__init__(self, name)

    def start(self):
        # here is where the maps and object is spawn
        # create player
        self.player = Player(0, 0, TILESIZE, TILESIZE)
        self.enemy = Enemy(320, 320, TILESIZE, TILESIZE)

    def handle_events(self, event, delta_time):
        self.player.handle_events(event, delta_time)
        self.enemy.handle_events(event, delta_time)

    def update(self, delta_time):
        self.player.update(delta_time)
        self.enemy.update(delta_time)
        self.player.is_collide(self.enemy)


    def render(self, window):
        window.fill(BLACK)
        self.draw_grid(window)
        self.player.render(window)
        self.enemy.render(window)

    def clear(self):
        pygame.display.flip()

    def draw_grid(self, window):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(window, LIGHTGRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(window, LIGHTGRAY, (0, y), (WIDTH, y))

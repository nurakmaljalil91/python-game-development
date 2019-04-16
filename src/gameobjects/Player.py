import pygame
from src.Settings import *
from src.gameobjects.GameObject import GameObject
from src.gameobjects.Enemy import Enemy


class Player(GameObject):
    def __init__(self, x, y, width, height):
        GameObject.__init__(self, x, y, width, height)
        self.speed = 1000
        self.real_x = 0
        self.real_y = 0
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.tag = 'Player'
        print('Player is created')

    def start(self):
        pass

    def handle_events(self, event, delta_time):
        self.move(event, delta_time)

    def update(self, delta_time):
        # update hitbox here
        # self.hitbox = (self.x, self.y, self.width, self.height)
        pass

    def render(self, window):

        pygame.draw.rect(window, BLUE, self.hitbox, 2)

    def move(self, event, delta_time):
        if event.key == pygame.K_w:
            self.real_y -= self.speed * delta_time
        if event.key == pygame.K_s:
            self.real_y += self.speed * delta_time
        if event.key == pygame.K_d:
            self.real_x += self.speed * delta_time
        if event.key == pygame.K_a:
            self.real_x -= self.speed * delta_time

        self.hitbox = (self.real_x, self.real_y, self.width, self.height)

    def is_collide(self, gameobject):
        if self.real_x < gameobject.x + gameobject.width and self.real_x + self.width \
                > gameobject.x and self.real_y < gameobject.y + gameobject.height and self.real_y\
                + self.height > gameobject.y:
            print(self.tag + ' collide ' + gameobject.tag)

import pygame
import random
import string


# dev-notes:
# because implement the ecs is quiet hard so
# using the traditional oop too make this more
# easy and fast
# id is needed when to find the multiple gameobject


def generate_id():
    random_number = random.randint(100, 999)
    random_string = ''.join(
        [random.choice(string.ascii_letters) for n in range(3)])
    random_id = random_string + str(random_number)
    return random_id


vector2 = pygame.math.Vector2


class GameObject(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.z = 1
        self.width = width
        self.height = height
        self.position = [self.x, self.y]
        self.size = [self.width, self.height]
        self.id = generate_id()
        self.position = vector2(self.x, self.y)
        self.size = vector2(self.width, self.height)

    def start(self):
        pass

    def handle_events(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def clear(self):
        pass

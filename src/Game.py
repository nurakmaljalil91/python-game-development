import pygame
from src.Settings import *
from src.scenes.SceneManager import SceneManager
from src.scenes.PlayScene import PlayScene
from src.scenes.MenuScene import MenuScene


class Game(object):
    def __init__(self, title, width, height, fullscreen):
        # define game attributes
        self.title = title
        self.width = width
        self.height = height
        self.fullscreen = fullscreen
        # Initialize the pygame
        pygame.init()
        # setting the game window
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        print('Game is created')

        # start allow the game to initilize everytihng

    def start(self):
        # starting the game
        self.is_running = True

        # starting the clock
        self.clock = pygame.time.Clock()

        # allow the key press hold
        pygame.key.set_repeat(100, 100)
        # start creating scene manager and put the scene inside it
        self.scene_manager = SceneManager()
        self.menu_scene = MenuScene('menu scene')  # scene 0
        self.play_scene = PlayScene('play scene')  # scene 1
        self.scene_manager.push(self.menu_scene)
        self.scene_manager.push(self.play_scene)
        if self.scene_manager.is_empty() is False:
            self.scene_manager.start()
        self.scene_number = 0  # this for scene changing maybe not included

    # function to handle all the events
    def handle_events(self):
        # set the fps for the game
        self.delta_time = self.clock.tick(FPS) / 1000  # delta time in miliseconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            # end the game if escape key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False
                if self.scene_manager.is_empty() is False:
                    self.scene_manager.handle_events(event)

    def update(self):
        if self.scene_manager.is_empty() is False:
            self.scene_manager.update(self.delta_time)

    def render(self):
        if self.scene_manager.is_empty() is False:
            self.scene_manager.render(self.window)

    def clear(self):
        # self.window.fill(WHITE)
        if self.scene_manager.is_empty() is False:
            self.scene_manager.clear()

        pygame.display.update()

    def quit(self):
        pygame.quit()
        quit()

# end of Game class

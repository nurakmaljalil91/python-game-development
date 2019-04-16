# This is the main file to run the game
from src.Settings import *
from src.Game import Game


def main():
    print('welcome to deween game development')
    print('Game version 0.1.0')
    print('Capglass Studio 2019')

    # create the game
    game = Game(TITLE, WIDTH, HEIGHT, False)
    # init the game
    game.start()
    # game loop
    while (game.is_running is True):
        game.handle_events()
        game.update()
        game.render()
        game.clear()
    game.quit()


# process the main
main()

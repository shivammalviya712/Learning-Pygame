# Author - Shivam Malviya
# Date - 31st May 2019


import pygame
import game_functions as gf
from settings import Settings
from pygame.sprite import Group


def run_game():

    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Rainfall")
    raindrops = Group()

    while True:

        gf.get_events()
        gf.update_screen(screen, settings, raindrops)



run_game()




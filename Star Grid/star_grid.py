# Author - Shivam Malviya
# Date - 29th May 2019


import pygame
from settings import Settings
import game_functions as gf
from pygame.sprite import Group


def run_game():

    pygame.init()
    sg_settings = Settings()
    screen = pygame.display.set_mode((sg_settings.screen_width, sg_settings.screen_height))
    stars = Group()
    gf.create_grid(stars, screen)

    while True:

        gf.get_event()
        gf.update_screen(stars, screen, sg_settings)





run_game()
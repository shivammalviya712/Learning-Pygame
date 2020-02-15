# Author - Shivam Malviya
# Date - 26th May 2019


import pygame
from settings import Settings
import game_functions as gf
from rocket import Rocket
from pygame.sprite import Group


def run_game():

    ss_settings = Settings()
    screen = pygame.display.set_mode((ss_settings.screen_width, ss_settings.screen_height))
    pygame.display.set_caption("Side Shooter")
    rocket = Rocket(screen, ss_settings)
    bullets = Group()

    while True:

        gf.check_events(rocket, bullets, screen, ss_settings)
        rocket.update_rocket()
        gf.update_bullets(bullets, screen)
        gf.update_screen(screen, ss_settings, bullets, rocket)


run_game()




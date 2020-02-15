# Author - Shivam Malviya
# Date - 25th May 2019


import pygame
import sys
from settings import Settings
from rocket import Rocket
import game_functions as gf



pygame.init()
r_settings = Settings()
screen = pygame.display.set_mode((r_settings.screen_width,r_settings.screen_height))
pygame.display.set_caption("Rocket")
rocket = Rocket (screen)


while True:

    gf.check_event(rocket)
    rocket.update(r_settings)
    gf.update_screen(screen,r_settings,rocket)




# Author - Shivam Malviya
# Date - 25th May 2019


import pygame
import sys


def check_event (rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, rocket)

        elif event.type == pygame.KEYUP:
            check_keyup(event, rocket)

def check_keydown(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.right = True

    elif event.key == pygame.K_LEFT:
        rocket.left = True

    elif event.key == pygame.K_DOWN:
        rocket.bottom = True

    elif event.key == pygame.K_UP:
        rocket.top = True

def check_keyup(event,rocket):
    if event.key == pygame.K_RIGHT:
        rocket.right = False

    elif event.key == pygame.K_LEFT:
        rocket.left = False

    elif event.key == pygame.K_DOWN:
        rocket.bottom = False

    elif event.key == pygame.K_UP:
        rocket.top = False

def update_screen (screen,r_settings,rocket):

    screen.fill(r_settings.bg_colour)
    rocket.blitme()
    pygame.display.flip()







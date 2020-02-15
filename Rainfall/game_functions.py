# Author - Shivam Malviya
# Date - 31st May 2019


import pygame
import sys
from raindrop import Raindrop


def get_events():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()


def update_screen(screen, settings, raindrops):

    screen.fill(settings.screen_colour)
    update_raindrops(raindrops)
    create_raindrops(raindrops, settings, screen)
    raindrops.draw(screen)

    pygame.display.flip()


def update_raindrops(raindrops):

    raindrops.update()
    for raindrop in raindrops.copy():
        if raindrop.rect.top >= raindrop.screen_rect.height:
            raindrops.remove(raindrop)


def create_raindrops(raindrops, settings, screen):

    number_rows = get_number_rows(settings, screen)
    number_columns = get_number_column(settings, screen)

    for row in range(number_rows):
        for column in range(number_columns):
            create_raindrop(raindrops, row, column, screen, settings, number_rows, number_columns)


def get_number_rows(settings, screen):

    raindrop = Raindrop(screen, settings)
    rd_height = raindrop.rect.height
    available_space = settings.screen_height
    number_rows = available_space // (2 * rd_height)
    return number_rows


def get_number_column(settings, screen):

    raindrop = Raindrop(screen, settings)
    rd_width = raindrop.rect.width
    available_space = settings.screen_width - 2 * rd_width
    number_column = available_space // (2 * rd_width)
    return number_column


def create_raindrop(raindrops, row, column, screen, settings, number_rows, number_columns):

    if len(raindrops) < number_rows * number_columns:
        raindrop = Raindrop(screen, settings)
        raindrop.rect.x = raindrop.rect.width + 2 * raindrop.rect.width * column
        raindrop.rect.y = 2 * raindrop.rect.height * row
        raindrop.y = raindrop.rect.y
        raindrops.add(raindrop)













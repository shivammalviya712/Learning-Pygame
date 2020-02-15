# Author - Shivam Malviya
# Date - 29th May 2019


import pygame
import sys
from star import Star
from random import randint


def get_event():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(stars, screen, sg_settings):

    screen.fill(sg_settings.screen_colour)
    stars.draw(screen)
    pygame.display.flip()


def create_grid(stars, screen):

    number_rows = get_number_rows(screen)
    number_columns = get_number_column(screen)
    for row in range(number_rows):
        for column in range(number_columns):
            create_star(stars, screen, number_columns, number_rows)


def get_number_rows(screen):
    star = Star(screen)
    star_height = star.rect.height
    available_space = star.screen_rect.height - 2 * star_height
    number_rows = available_space // (2 * star_height)
    return number_rows


def get_number_column(screen):
    star = Star(screen)
    star_width = star.rect.width
    available_space = star.screen_rect.width - 2 * star_width
    number_columns = available_space // (2 * star_width)
    return number_columns


def create_star(stars, screen, column, row):

    star = Star(screen)
    star.rect.x = star.rect.width + randint (1, column) * star.rect.width * 2
    star.rect.y = star.rect.height + randint (1,row) * star.rect.height * 2
    stars.add(star)












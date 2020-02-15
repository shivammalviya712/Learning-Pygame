# Author - Shivam Malviya
# Date - 26th May 2019


import pygame
import sys
from bullet import Bullet


def check_events(rocket, bullets, screen, ss_settings):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, rocket, bullets, screen, ss_settings)

        elif event.type == pygame.KEYUP:
            check_keyup(event, rocket)


def check_keyup(event, rocket):
    if event.key == pygame.K_UP:
        rocket.top = False

    elif event.key == pygame.K_DOWN:
        rocket.bottom = False


def check_keydown(event, rocket, bullets, screen, ss_settings):
    if event.key == pygame.K_UP:
        rocket.top = True

    elif event.key == pygame.K_DOWN:
        rocket.bottom = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, ss_settings, screen, rocket)


def fire_bullet(bullets, ss_settings, screen, rocket):

    if len (bullets) < ss_settings.allowed_bullets:
        new_bullet = Bullet(ss_settings, rocket, screen)
        bullets.add(new_bullet)


def update_bullets(bullets, screen):

    bullets.update()
    screen_rect = screen.get_rect()

    for bullet in bullets.copy():
        if bullet.rect.left >= screen_rect.right:
            bullets.remove(bullet)


def update_screen(screen, ss_settings, bullets, rocket):

    screen.fill(ss_settings.screen_colour)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    rocket.blitme()

    # Redrawing the screen
    pygame.display.flip()

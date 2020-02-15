# Author - Shivam Malviya
# Date - 26th May 2019


import pygame


class Rocket:

    def __init__(self, screen, ss_settings):

        self.screen = screen
        self.image = pygame.image.load("images\\spaceship-s.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = 0
        self.y = self.rect.centery

        self.top = False
        self.bottom = False

        self.settings = ss_settings

    def blitme(self):

        self.screen.blit(self.image, self.rect)

    def update_rocket(self):

        if self.top and self.rect.top > 0:
            self.y -= self.settings.rocket_speed_factor

        if self.bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed_factor

        self.rect.centery = self.y

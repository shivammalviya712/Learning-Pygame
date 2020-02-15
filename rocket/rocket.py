# Author - Shivam Malviya
# Date - 25th May 2019


import pygame


class Rocket():

    def __init__(self,screen):

        filename = "images/spaceship.bmp"
        self.image = pygame.image.load (filename)
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.centery

        self.right = False
        self.left = False
        self.bottom = False
        self.top = False

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit (self.image,self.rect)

    def update(self,r_settings):
        if self.right and self.rect.right < self.screen_rect.right:
            self.centerx += r_settings.rocket_speed

        if self.left and self.rect.left > 0:
            self.centerx -= r_settings.rocket_speed

        if self.bottom and self.rect.bottom < self.screen_rect.bottom:
            self.centery += r_settings.rocket_speed


        if self.top and self.rect.top > 0:
            self.centery -= r_settings.rocket_speed

        # Updating self.rect
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery



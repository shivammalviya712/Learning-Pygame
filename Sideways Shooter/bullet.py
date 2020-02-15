# Author - Shivam Malviya
# Date - 26th May 2019


import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ss_settings, rocket, screen):
        super().__init__()

        self.screen = screen
        self.rect = pygame.Rect(0,0,ss_settings.bullet_width,ss_settings.bullet_height)
        self.rect.centery = rocket.rect.centery
        self.rect.right = rocket.rect.right
        self.x = self.rect.right

        self.speed_factor = ss_settings.bullet_speed_factor
        self.colour = ss_settings.bullet_colour

    def draw_bullet(self):

        pygame.draw.rect(self.screen, self.colour, self.rect)

    def update(self):

        self.x += self.speed_factor
        self.rect.right = self.x

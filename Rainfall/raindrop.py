# Author - Shivam Malviya
# Date - 31st May 2019


import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):

    def __init__(self, screen, settings):

        super().__init__()

        image_file = "images/Rain Drop.bmp"
        self.image = pygame.image.load(image_file)
        self.screen = screen
        self.settings = settings

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = self.rect.y

    def blitme(self):

        self.screen.blit(self.image, self.rect)

    def update(self):

        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
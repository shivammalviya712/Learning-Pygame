# Author - Shivam Malviya
# Date - 29th May 2019


import pygame
from pygame.sprite import Sprite


class Star(Sprite):

    def __init__(self, screen):

        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("images/star.bmp")

        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):

        self.screen.blit(self.image, self.rect)




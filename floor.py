import pygame


class Floor(pygame.sprite.Sprite):
    def __init__(self, image, number, position):
        super().__init__()
        self.number = number
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position


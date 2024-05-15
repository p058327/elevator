import pygame
from timer import Timer
from settings import TIMER_RADIOS


class Floor(pygame.sprite.Sprite):
    def __init__(self, image, number, position):
        super().__init__()
        self.number = number
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.timer = Timer(self.rect.left - 35, self.rect.centery, TIMER_RADIOS, 0)

    def update_timer(self, surface, delta=0, time_to_arrival=None):
        self.timer.update(delta, surface, time_to_arrival)

import pygame
from timer import Timer
from button import Button
from settings import TIMER_RADIOS, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_RADIOS


class Floor(pygame.sprite.Sprite):
    def __init__(self, image, number, position):
        super().__init__()
        self.called = False
        self.number = number
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.button = Button(position, BUTTON_WIDTH, BUTTON_HEIGHT, self.number, "BLACK", BUTTON_RADIOS)
        self.timer = Timer(self.rect.left - TIMER_RADIOS - 5, self.rect.centery, TIMER_RADIOS, 0)

    def update_timer(self, surface, delta=0, time_to_arrival=None):
        self.timer.update(delta, surface, time_to_arrival)

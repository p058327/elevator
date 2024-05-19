import pygame
import math

from settings import LIGHT_GRAY, FONT, GREEN


class Timer(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, initial_time):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.initial_time = initial_time
        self.remaining_time = initial_time

    def update(self, time_delta, surface, new_initial_time=None):
        if new_initial_time is not None:
            self.initial_time = new_initial_time
            self.remaining_time = new_initial_time
        self.remaining_time = max(self.remaining_time - time_delta, 0)
        self.draw(surface)

    def draw(self, surface):
        pygame.draw.circle(surface, GREEN, (self.x, self.y), self.radius, 10)
        pygame.draw.circle(surface, "WHITE", (self.x, self.y), self.radius - 10)

        remaining_fraction = 0 if self.initial_time == 0 else self.remaining_time / self.initial_time
        pygame.draw.arc(surface, "RED", (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2),
                        math.pi * 0, math.pi * remaining_fraction * 2, 10)

        text_color = LIGHT_GRAY if self.remaining_time == 0 else "BLACK"
        font = pygame.font.Font(FONT, 30)
        text = font.render(str(math.ceil(self.remaining_time / 1000)), True, text_color)
        text_rect = text.get_rect(center=(self.x, self.y))
        surface.blit(text, text_rect)

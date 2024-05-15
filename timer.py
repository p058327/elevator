import pygame
import math

from settings import RED, GREEN, LIGHT_GRAY, BLACK


class Timer(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, initial_time):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.initial_time = initial_time
        self.remaining_time = initial_time
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.draw(surface)

    def update(self, time_delta, surface, new_initial_time=None):
        if new_initial_time is not None:
            self.initial_time = new_initial_time
            self.remaining_time = new_initial_time
        self.remaining_time = max(self.remaining_time - time_delta, 0)
        print(f"Timer remaining time: {self.remaining_time / 1000} seconds")

        self.draw(surface)

    def draw(self, surface):
        # self.image.fill((0, 0, 0, 0))  # Clear the image
        pygame.draw.circle(surface, GREEN, (self.rect.x, self.rect.y), self.radius, 10)
        remaining_fraction = 0 if self.initial_time == 0 or self.remaining_time == 0 else self.remaining_time / self.initial_time
        pygame.draw.arc(surface, RED, (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2),
                        math.pi * 0, math.pi * 1.5, 10)
        # pygame.draw.circle(surface, RED, (self.rect.x, self.rect.y), int(self.radius * remaining_fraction), 10)
        text_color = LIGHT_GRAY if self.remaining_time == 0 else BLACK
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render(str(math.ceil(self.remaining_time / 1000)), True, text_color)
        text_rect = text.get_rect(center=(self.rect.x, self.rect.y))
        surface.blit(text, text_rect)

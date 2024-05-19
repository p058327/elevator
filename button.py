import pygame
from settings import GRAY_1, GREEN, FONT


class Button(pygame.sprite.Sprite):
    def __init__(self, position, width, height, number, color, radius=0):
        super().__init__()
        self.x = position[0]
        self.y = position[1]
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.rect.center = position
        self.floor_number = number
        self.color = color
        self.radius = radius
        self.called = False

    def draw(self, surface):
        pygame.draw.rect(surface, GRAY_1, self.rect, 0, self.radius)
        font = pygame.font.Font(FONT, 50)
        text = font.render(str(self.floor_number), True, self.color)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def def_color(self):
        if self.called:
            self.color = GREEN
        else:
            self.color = "BLACK"

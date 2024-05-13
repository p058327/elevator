import pygame
from settings import ELEVATOR_IMAGE, FLOOR_HEIGHT, WINDOW_HEIGHT


# Define the elevator class
class Elevator(pygame.sprite.Sprite):
    def __init__(self, elevator_number):
        super().__init__()
        self.image = ELEVATOR_IMAGE
        self.rect = self.image.get_rect()
        self.number = elevator_number
        self.available = True
        self.availability_time = 0
        self.requested_buttons = []
        self.target_floor = None
        self.lest_floor = None
        self.current_floor = 1
        self.direction = 0
        self.speed = 4  # Pixels per frame

    def move(self):
        if self.target_floor is not None:
            target_y = WINDOW_HEIGHT - (self.target_floor * FLOOR_HEIGHT + 7)
            dist_target = abs(self.rect.y - target_y)
            speed = min(self.speed, dist_target)
            if self.rect.y < target_y:
                self.direction = 1
            elif self.rect.y > target_y:
                self.direction = -1
            else:
                self.direction = 0
                self.target_floor = None
                self.available = True
            self.rect.move_ip(0, self.direction * speed)

    def check_requests(self):
        if not self.target_floor and self.requested_buttons:
            self.target_floor = self.requested_buttons.pop(0)

    def update(self):
        self.move()

    def add_button(self, button):
        self.requested_buttons.append(button)
        self.lest_floor = button

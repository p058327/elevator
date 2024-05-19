import pygame
from settings import ELEVATOR_IMAGE, WINDOW_HEIGHT, INTERNAL_FLOOR_HEIGHT, AWAIT_TIME, FLOOR_TRANSITION_TIME


# Define the elevator class
class Elevator(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ELEVATOR_IMAGE
        self.rect = self.image.get_rect()
        self.requested_floors = []
        self.start_y = None
        self.target_floor = None
        self.target_number = None
        self.current_floor = 1
        self.lest_floor = 1
        self.availability_time = 0
        self.transition_time = 0
        self.elapsed_time = 0
        self.stop_time = 0
        self.different = 0

    def update(self, time):
        if self.target_number is not None:
            self.move(time)
        else:
            self.availability_time = 0

    def move(self, time_delta):
        target_y = WINDOW_HEIGHT - self.target_number * INTERNAL_FLOOR_HEIGHT
        if self.rect.y != target_y:
            self.elapsed_time += time_delta
            fraction = min(self.elapsed_time / self.transition_time, 1)
            if self.rect.y > target_y:
                self.rect.y = self.start_y - self.different * fraction
            elif self.rect.y < target_y:
                self.rect.y = self.start_y + self.different * fraction
            self.availability_time -= time_delta
        else:
            self.stop(time_delta)

    def stop(self, time_delta):
        self.current_floor = self.target_number
        if self.stop_time == 0:
            pygame.mixer.music.play()
        self.stop_time += time_delta
        if self.stop_time >= AWAIT_TIME:
            # The planning decision for this system allows the elevator to be called from a
            # place where an elevator already exists, That's why we make the elevator available.
            self.target_floor.called = False
            self.target_floor.button.called = False
            self.target_number = None
            self.stop_time = 0
            self.elapsed_time = 0
        else:
            self.availability_time -= time_delta

    def check_requests(self):
        if not self.target_number and self.requested_floors:
            self.target_floor = self.requested_floors.pop(0)
            self.target_number = self.target_floor.number
            self.transition_time = self.distance() * FLOOR_TRANSITION_TIME
            self.different = self.distance() * INTERNAL_FLOOR_HEIGHT
            self.start_y = self.rect.y

    def add_button(self, floor):
        self.requested_floors.append(floor)
        self.lest_floor = floor.number

    def distance(self):
        return abs(self.current_floor - self.target_number)

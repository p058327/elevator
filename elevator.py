import pygame
from settings import ELEVATOR_IMAGE, WINDOW_HEIGHT, ELEVATOR_SPEED, INTERNAL_FLOOR_HEIGHT, AWAIT_TIME, \
    FLOOR_TRANSITION_TIME


# Define the elevator class
class Elevator(pygame.sprite.Sprite):
    def __init__(self, elevator_number):
        super().__init__()
        self.stop_time = 0
        self.image = ELEVATOR_IMAGE
        self.rect = self.image.get_rect()
        self.start_y = None
        self.number = elevator_number
        # self.available = True
        # self.previous_availability_time = 0
        self.availability_time = 0
        self.requested_floors = []
        self.target_floor = None
        self.target_number = None
        self.lest_floor = 1
        self.current_floor = 1
        self.speed = ELEVATOR_SPEED  # Pixels per frame
        self.elapsed_time = 0
        self.transition_time = 0
        self.distance = 0

    def move(self, time_delta):
        target_y = WINDOW_HEIGHT - self.target_number * INTERNAL_FLOOR_HEIGHT
        if self.rect.y != target_y:
            self.elapsed_time += time_delta
            fraction = min(self.elapsed_time / self.transition_time, 1)
            if self.rect.y > target_y:
                self.rect.y = self.start_y - self.distance * fraction
            elif self.rect.y < target_y:
                self.rect.y = self.start_y + self.distance * fraction
            self.availability_time -= time_delta
        else:
            self.stop(time_delta)

    def update(self, time):
        if self.target_number is not None:
            self.move(time)
        else:
            self.availability_time = 0

    def check_requests(self):
        if not self.target_number and self.requested_floors:
            self.target_floor = self.requested_floors.pop(0)
            self.target_number = self.target_floor.floor_number
            transition = self.new_transition()
            self.transition_time = transition * FLOOR_TRANSITION_TIME
            self.distance = transition * INTERNAL_FLOOR_HEIGHT
            self.start_y = self.rect.y

    def add_button(self, button):
        self.requested_floors.append(button)
        self.lest_floor = button.floor_number

    def stop(self, passed_time):
        self.current_floor = self.target_number
        if self.stop_time == 0:
            pygame.mixer.music.play()
        self.stop_time += passed_time
        if self.stop_time >= AWAIT_TIME:
            self.target_floor.called = False  # need to note the choice in the document
            self.target_number = None
            self.stop_time = 0
            self.elapsed_time = 0
        else:
            self.availability_time -= passed_time

    def get_time_to_arrival(self):
        return self.availability_time

    def new_transition(self):
        source = self.current_floor
        destination = self.target_number
        transitional_floors = abs(source - destination)
        return transitional_floors

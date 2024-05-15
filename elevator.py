import pygame
from settings import ELEVATOR_IMAGE, FLOOR_HEIGHT, WINDOW_HEIGHT, ELEVATOR_SPEED, INTERNAL_FLOOR_HEIGHT, AWAIT_TIME, \
    FLOOR_TRANSITION_TIME


# Define the elevator class
class Elevator(pygame.sprite.Sprite):
    def __init__(self, elevator_number):
        super().__init__()
        self.stop_time = 0
        self.image = ELEVATOR_IMAGE
        self.rect = self.image.get_rect()
        self.number = elevator_number
        # self.available = True
        # self.previous_availability_time = 0
        self.availability_time = 0
        self.requested_floors = []
        self.target_floor = None
        self.target_number = None
        self.lest_floor = 1
        self.current_floor = 1
        self.direction = 0
        self.speed = ELEVATOR_SPEED  # Pixels per frame

    def move(self, time):
        target_y = WINDOW_HEIGHT - (self.target_number * INTERNAL_FLOOR_HEIGHT)
        dist_target = abs(self.rect.y - target_y)
        speed = min(self.speed, dist_target)
        print(time, self.availability_time)
        if self.rect.y < target_y:
            self.direction = 1
            self.availability_time -= time
        elif self.rect.y > target_y:
            self.direction = -1
            self.availability_time -= time
        else:
            self.stop(time)
            # TODO wait 2 seconds without stop all program
        self.rect.move_ip(0, self.direction * speed)

    def update(self, time):
        if self.target_number is not None:
            self.move(time)
        else:
            self.availability_time = 0

    def check_requests(self):
        if not self.target_number and self.requested_floors:
            self.target_floor = self.requested_floors.pop(0)
            self.target_number = self.target_floor.floor_number

    def add_button(self, button):
        self.requested_floors.append(button)
        self.lest_floor = button.floor_number

    def stop(self, passed_time):
        self.direction = 0
        self.current_floor = self.target_number
        if self.stop_time == 0:
            pygame.mixer.music.play()
        self.stop_time += passed_time
        if self.stop_time >= AWAIT_TIME:
            self.target_floor.called = False  # need to note the choice in the ducomente
            self.target_number = None
            self.stop_time = 0
        else:
            self.availability_time -= passed_time
        print("stop", self.availability_time)

    def get_time_to_arrival(self, floor_number):
        return self.availability_time

# TODO fix the availability_time

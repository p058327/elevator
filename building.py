import pygame
from random import choice

from floor import Floor
from button import Button
from elevator import Elevator
from settings import FLOOR_IMAGE, FLOOR_WIDTH, FLOOR_HEIGHT, \
    ELEVATOR_WIDTH, NUM_ELEVATORS, ELEVATOR_SPEED, AWAIT_TIME, INTERNAL_FLOOR_HEIGHT


class Building(pygame.sprite.Group):
    def __init__(self, num_of_floors, start_point: tuple):
        super().__init__()
        self.floors = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.elevators = pygame.sprite.Group()

        self.start_x = start_point[0]
        self.start_y = start_point[1]

        # TODO self.total_height = num_of_floors * (FLOOR_HEIGHT + 7)

        for floor in range(num_of_floors):
            # determinate the position of the floor according the building position and floor number
            x = self.start_x
            y = self.start_y - floor * INTERNAL_FLOOR_HEIGHT
            floor = Floor(FLOOR_IMAGE, floor + 1, (x, y))
            self.floors.add(floor)
            # Create a button for each floor
            button_position = floor.rect.center
            button_width = 60
            button_height = 60
            button_radius = 20
            button = Button(button_position, button_width, button_height, floor.number,
                            "BLACK", button_radius)
            self.buttons.add(button)
        for i in range(NUM_ELEVATORS):
            elevator = Elevator(i)
            elevator.rect.x = FLOOR_WIDTH + ELEVATOR_WIDTH * (i + 1)
            elevator.rect.y = self.start_y - FLOOR_HEIGHT // 2
            self.elevators.add(elevator)

    def draw_lines(self, surface):
        for floor in self.floors:
            if floor.number < self.floors.sprites()[-1].number:
                pygame.draw.line(surface, "BLACK", (floor.rect.left, floor.rect.top - 3.5),
                                 (floor.rect.right - 1, floor.rect.top - 3.5), 7)

    def call_elevator(self, destination, button: Button):
        min_availability_elevator = self.choose_faster_elevator(destination)

        # update the time of availability for the chosen elevator
        min_availability_elevator.availability_time += AWAIT_TIME

        # update the chosen elevator with the destination
        min_availability_elevator.add_button(button)
        min_availability_elevator.lest_floor = button.floor_number

    def choose_faster_elevator(self, destination):
        choose_elevator = choice(list(self.elevators.sprites()))
        # TODO change to info
        min_availability = 90000000000000000
        for elevator in self.elevators:
            source = elevator.lest_floor
            availability = elevator.availability_time + self.fast_time(source, destination)
            if availability < min_availability:
                choose_elevator = elevator
                min_availability = availability
            # print(elevator.number, elevator.availability_time)
        choose_elevator.availability_time = min_availability
        # print(choose_elevator.number, min_availability)
        return choose_elevator

    def fast_time(self, first_floor, second_floor):
        distance = abs(first_floor - second_floor)
        return distance * 500  # it's not so correct but is hav no affect

    def update(self, clock, surface):
        for elevator in self.elevators:
            elevator.check_requests()
            elevator.update(clock.get_time())
        self.floors.draw(surface)
        self.draw_lines(surface)
        self.elevators.draw(surface)
        for button in self.buttons:
            button.def_color()
            button.draw(surface)



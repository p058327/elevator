from random import choice

import pygame

from elevator import Elevator
from floor import Floor
from button import Button
from settings import FLOOR_IMAGE, FLOOR_WIDTH, FLOOR_HEIGHT, NUM_ELEVATORS, ELEVATOR_WIDTH


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
            # determinate the position of the floor according the building position and floor floor_number
            x = self.start_x + FLOOR_WIDTH // 2
            y = self.start_y - floor * (FLOOR_HEIGHT + 7)
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
                                 (floor.rect.right, floor.rect.top - 3.5), 7)

    def call_elevator(self, destination, button: Button):
        min_availability_time = float('inf')  # Default minimum value so that any value will be less than it
        min_availability_obj = choice(list(self.elevators.sprites()))
        for elevator in self.elevators:
            if elevator.availability_time < min_availability_time:
                min_availability_time = elevator.availability_time
                min_availability_obj = elevator
        min_availability_obj.target_floor = destination
        min_availability_obj.add_button(button)
        add_time = (abs(min_availability_obj.lest_floor - destination) * (FLOOR_HEIGHT + 7) // 4)
        min_availability_obj.availability_time += add_time


# class Buildings(pygame.sprite.Group()):
#     def __init__(self, num_of_buildings):
#         super().__init__()
#         for i in range(num_of_buildings):
#             Buildings.add(Building(i))

import pygame
from random import choice

from floor import Floor
from elevator import Elevator
from settings import (FLOOR_IMAGE, FLOOR_WIDTH, FLOOR_HEIGHT,
                      ELEVATOR_WIDTH, AWAIT_TIME, INTERNAL_FLOOR_HEIGHT, FLOOR_TRANSITION_TIME)


class Building(pygame.sprite.Group):
    def __init__(self, num_of_floors, num_of_elevators, start_point: tuple):
        super().__init__()
        self.floors = pygame.sprite.Group()
        self.elevators = pygame.sprite.Group()

        self.start_x = start_point[0]
        self.start_y = start_point[1]

        for floor in range(num_of_floors):
            # determinate the position of the floor according the building position and floor number
            x = self.start_x
            y = self.start_y - floor * INTERNAL_FLOOR_HEIGHT
            floor = Floor(FLOOR_IMAGE, floor + 1, (x, y))
            self.floors.add(floor)

        for i in range(num_of_elevators):
            elevator = Elevator()
            elevator.rect.x = self.start_x + FLOOR_WIDTH // 2 + ELEVATOR_WIDTH * i
            elevator.rect.y = self.start_y - FLOOR_HEIGHT // 2 + 2
            self.elevators.add(elevator)

    def draw_lines(self, surface):
        for floor in self.floors:
            if floor.number < self.floors.sprites()[-1].number:
                pygame.draw.line(surface, "BLACK", (floor.rect.left, floor.rect.top - 3.5),
                                 (floor.rect.right - 1, floor.rect.top - 3.5), 7)

    def call_elevator(self, destination, floor: Floor, surface):
        min_availability_elevator = self.choose_faster_elevator(destination)

        target = self.floors.sprites()[floor.number - 1]
        self.update_time(destination, min_availability_elevator, target, surface)

        # update the chosen elevator with the destination
        min_availability_elevator.add_button(floor)
        min_availability_elevator.lest_floor = floor.number

    def choose_faster_elevator(self, destination):
        choose_elevator = choice(list(self.elevators.sprites()))
        min_availability = float('inf')
        for elevator in self.elevators:
            source = elevator.lest_floor
            availability = elevator.availability_time + self.transition_time(source, destination)
            if availability < min_availability:
                choose_elevator = elevator
                min_availability = availability
        return choose_elevator

    def update_time(self, destination, chosen_elevator, target_floor, surface):
        # update the time of availability without the 2 seconds of waiting in the destination
        source = chosen_elevator.lest_floor
        chosen_elevator.availability_time += self.transition_time(source, destination)

        time_to_arrival = chosen_elevator.availability_time
        target_floor.update_timer(surface, 0, time_to_arrival)

        # update the time of availability for the 2 seconds of waiting in the destination
        chosen_elevator.availability_time += AWAIT_TIME

    def transition_time(self, first_floor, second_floor):
        distance = abs(first_floor - second_floor)
        return distance * FLOOR_TRANSITION_TIME

    def update(self, clock, surface):
        self.floors.draw(surface)
        self.draw_lines(surface)
        self.elevators.draw(surface)
        for floor in self.floors:
            floor.button.def_color()
            floor.button.draw(surface)
            floor.timer.draw(surface)
            floor.update_timer(surface, clock.get_time())
        for elevator in self.elevators:
            elevator.check_requests()
            elevator.update(clock.get_time())

from buildings import Buildings
from building import Building
from settings import (BUILDING_START_POINT, BUILDING_WIDTH,
                      NUM_FLOORS_1, NUM_ELEVATORS_1, NUM_FLOORS_2, NUM_ELEVATORS_2, NUM_FLOORS_3, NUM_ELEVATORS_3,
                      WINDOW_HEIGHT, INTERNAL_FLOOR_HEIGHT)


def create_building(building_id, num_floors, num_elevators):
    """Creates a Building object based on the provided parameters."""

    max_floors = WINDOW_HEIGHT // INTERNAL_FLOOR_HEIGHT
    num_floors = min(num_floors, max_floors)
    max_elevators = min(num_elevators, num_floors // 2)
    num_elevators = min(num_elevators, max_elevators)
    start_point = BUILDING_START_POINT[0] + building_id * BUILDING_WIDTH, BUILDING_START_POINT[1]

    # Create a Building object with the specified parameters
    building = Building(num_floors, num_elevators, start_point)

    return building


def create_buildings(num_building):
    """Creates a Buildings object."""

    buildings = Buildings()

    # Create a Building object with the specified parameters
    building = create_building(0, NUM_FLOORS_1, NUM_ELEVATORS_1)
    buildings.buildings.append(building)

    if num_building > 1:
        building = create_building(1, NUM_FLOORS_2, NUM_ELEVATORS_2)
        buildings.buildings.append(building)

    if num_building > 2:
        building = create_building(2, NUM_FLOORS_3, NUM_ELEVATORS_3)
        buildings.buildings.append(building)

    return buildings

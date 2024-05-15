from settings import BUILDING_START_POINT, BUILDING_WIDTH
from building import Building


def create_building(building_id, num_floors, num_elevators):
    """Creates a Building object based on the provided parameters."""

    start_point = BUILDING_START_POINT[0] + building_id * BUILDING_WIDTH, BUILDING_START_POINT[1]

    # Create a Building object with the specified parameters
    building = Building(num_floors, num_elevators, start_point)

    return building

class Buildings:
    def __init__(self):
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)

    def update(self, clock, surface):
        for building in self.buildings:
            building.update(clock, surface)

    def call_elevator(self, building_index, destination, button, surface):
        building = self.buildings[building_index]
        building.call_elevator(destination, button, surface)

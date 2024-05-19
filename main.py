import pygame
from building_factory import create_buildings
from settings import FPS, STOP_SOUND, BACKGROUND_IMAGE, NUM_BUILDINGS, DISPLAY

# Initialize Pygame
pygame.init()

# Initialize the clock and limit the frame rate
clock = pygame.time.Clock()
clock.tick(FPS)

# Initialize stopping sound
pygame.mixer.init()
pygame.mixer.music.load(STOP_SOUND)
background = BACKGROUND_IMAGE

# Create the building
buildings = create_buildings(NUM_BUILDINGS)


def check_click():
    for i, building in enumerate(buildings.buildings):
        for floor in building.floors:
            if floor.button.rect.collidepoint(event.pos) and floor.called is False:
                floor.button.called = True
                floor.called = True
                destination = floor.number
                buildings.call_elevator(i, destination, floor, DISPLAY)


# Game loop
running = True
while running:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a call button was clicked
            check_click()

    # Clear the display
    DISPLAY.blit(background, DISPLAY.get_rect())

    # Update all buildings
    buildings.update(clock, DISPLAY)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

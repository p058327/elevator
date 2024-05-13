import pygame

import settings as st
from building import Building
from elevator import Elevator

# Initialize Pygame
pygame.init()

# Create the building
building = Building(st.NUM_FLOORS, (10, (st.WINDOW_HEIGHT - st.FLOOR_HEIGHT // 2)))

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # Limit the frame rate

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a call button was clicked
            for button in building.buttons:
                if button.rect.collidepoint(event.pos):
                    button.called = True
                    destination = button.floor_number
                    building.call_elevator(destination, button)
                if button.called:
                    button.color = st.GREEN
                else:
                    button.color = st.BLACK
            for elevator in building.elevators:
                elevator.check_requests()
                elevator.update()

    # Clear the display
    st.DISPLAY.fill(st.WHITE)

    building.floors.draw(st.DISPLAY)
    building.draw_lines(st.DISPLAY)
    building.elevators.draw(st.DISPLAY)
    for button in building.buttons:
        button.draw(st.DISPLAY)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

# TODO

# from background import Background

# background_object = Background()

# background_object.update()
# background_object.render()
# available_elevator = next((elevator for elevator in elevators if elevator.available), None)


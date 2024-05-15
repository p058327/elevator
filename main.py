import pygame
import settings as st
from building import Building
from timer import Timer

# Initialize Pygame
pygame.init()

# Initialize the sound of the stopping
pygame.mixer.init()
pygame.mixer.music.load(st.STOP_SOUND)
background = st.BACKGROUND_IMAGE

# Create the building
building = Building(st.NUM_FLOORS, st.BUILDING_START_POINT)
# timer = Timer(900, 100, 20, 40)


def check_click(click):
    for button in building.buttons:
        if button.rect.collidepoint(click.pos) and button.called is False:
            button.called = True
            destination = button.floor_number
            building.call_elevator(destination, button, st.DISPLAY)


# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(st.FPS)  # Limit the frame rate
    # print(clock.)

    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a call button was clicked
            check_click(event)

    # Clear the display
    st.DISPLAY.fill(st.WHITE)
    st.DISPLAY.blit(background, st.DISPLAY.get_rect())
    background.blit(st.DISPLAY, st.DISPLAY.get_rect())

    # timer.update(clock.get_time())
    # timer.draw()

    # update the building state
    building.update(clock, st.DISPLAY)

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

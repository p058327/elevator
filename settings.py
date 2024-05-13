import pygame


# Set up the display
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Elevator Challenge")

# Define the floor_number of requested_buttons and elevators
NUM_FLOORS = 7
NUM_ELEVATORS = 2

# Define object size
BUILDING_WIDTH = WINDOW_WIDTH // 3
FLOOR_WIDTH = 300
FLOOR_HEIGHT = 103  # this height is according the project orders
ELEVATOR_WIDTH = 60
ELEVATOR_HEIGHT = FLOOR_HEIGHT

# Define colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 120)
GRAY = (128, 128, 128)
GRAY_1 = (210, 210, 210)
LIGHT_GRAY = (190, 190, 190)

# Load the elevator image
ELEVATOR = pygame.image.load("elv.png")
ELEVATOR_SIZE = ELEVATOR_WIDTH, FLOOR_HEIGHT
ELEVATOR_IMAGE = pygame.transform.scale(ELEVATOR, ELEVATOR_SIZE)

# Load the floor image
FLOOR = pygame.image.load("floor.png")
FLOOR_SIZE = FLOOR_WIDTH, FLOOR_HEIGHT
FLOOR_IMAGE = pygame.transform.scale(FLOOR, FLOOR_SIZE)

SCROLL_SPEED = 10

import pygame


# Set up the display
WINDOW_WIDTH = 1800
WINDOW_HEIGHT = 900
DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Elevator Challenge")

# Define the floor_number of requested_floors and elevators
NUM_FLOORS_1 = 7
NUM_FLOORS_2 = 5
NUM_FLOORS_3 = 6
NUM_ELEVATORS_1 = 2
NUM_ELEVATORS_2 = 3
NUM_ELEVATORS_3 = 1
NUM_BUILDINGS = 7

# Define object size
FLOOR_WIDTH = 300
FLOOR_HEIGHT = 103  # this height is according the project orders
ELEVATOR_WIDTH = 70
ELEVATOR_HEIGHT = FLOOR_HEIGHT
BUTTON_WIDTH = 65
BUTTON_HEIGHT = 65
BUTTON_RADIOS = 25
TIMER_RADIOS = 30
LINE_WIDTH = 7
BUILDING_WIDTH = WINDOW_WIDTH // 3
INTERNAL_FLOOR_HEIGHT = FLOOR_HEIGHT + LINE_WIDTH

FPS = 60
FONT = 'freesansbold.ttf'
STOP_SOUND = "resources/ding.mp3"
BUILDING_START_POINT = (FLOOR_WIDTH // 2 + (TIMER_RADIOS * 2) + 10, (WINDOW_HEIGHT - FLOOR_HEIGHT // 2) - 10)

AWAIT_TIME = 2000  # 2 seconds for awaiting in milliseconds
FLOOR_TRANSITION_TIME = 500

# Define colors
GREEN = (0, 235, 0)
GRAY_1 = (210, 210, 210)
LIGHT_GRAY = (190, 190, 190)

# Load the elevator image
ELEVATOR = pygame.image.load("resources/elv.png")
ELEVATOR_SIZE = ELEVATOR_WIDTH, ELEVATOR_HEIGHT
ELEVATOR_IMAGE = pygame.transform.scale(ELEVATOR, ELEVATOR_SIZE)

# Load the floor image
FLOOR = pygame.image.load("resources/floor.png")
FLOOR_SIZE = FLOOR_WIDTH, FLOOR_HEIGHT
FLOOR_IMAGE = pygame.transform.scale(FLOOR, FLOOR_SIZE)

BACKGROUND = pygame.image.load('resources/background.jpg')
BACKGROUND_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND, BACKGROUND_SIZE)

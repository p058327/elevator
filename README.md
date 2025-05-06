### Elevator System Simulation

This project simulates a building with multiple floors and elevators. Users can call an elevator from any floor by clicking on the call button for that floor. The system then determines the fastest available elevator to service the request and assigns it to that destination floor.

### Installation Steps

1.  **Clone the repository:**

    ```bash
    git clone git@github.com:p058327/elevator.git
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd ./elevator
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Simulation

After completing the installation, you can run the simulation using the following command:

    python3 main.py

**Elevator Calling and Destination Arrival Algorithm:**

1. **Calling an Elevator**: When a user clicks on a floor's call button, the system initiates the elevator calling process. The `check_click` function in `main.py` detects the click event and calls the `call_elevator` method of the corresponding `Building` object.

2. **Choosing the Fastest Elevator**: The `call_elevator` method in `building.py` uses the `choose_faster_elevator` function to determine the elevator with the shortest estimated arrival time to the destination floor. This is done by calculating the availability time and transition time for each elevator and selecting the one with the minimum total time.

3. **Updating Elevator and Floor Timers**: Once the fastest elevator is chosen, the `update_time` method in `building.py` is called. It updates the availability time of the chosen elevator by adding the transition time to the destination floor. It also updates the timer on the destination floor to display the estimated arrival time.

4. **Moving the Elevator**: The `Elevator` class in `elevator.py` handles the actual movement of the elevator. The `update` method is called in each game loop iteration, which triggers the `move` method if the elevator has a target floor. The `move` method updates the elevator's position based on the elapsed time and the transition time to the target floor.

5. **Stopping at the Destination**: When the elevator reaches the target floor, the `stop` method in `elevator.py` is called. This method handles the waiting time at the destination floor (2 seconds by default) before marking the request as completed and resetting the target floor.

6. **Handling Multiple Requests**: The `Elevator` class maintains a list of requested floors (`requested_floors`). The `check_requests` method is called in each game loop iteration to check if there are any pending requests. If there are, and the elevator avilabole, it assigns the next target floor from the list, and the process repeats.

By following this algorithm, the system efficiently manages elevator requests, chooses the fastest available elevator for each request, updates the timers to display the estimated arrival times, and moves the elevators between floors while handling multiple requests and waiting times.


**Building Class**
- Represents the entire building, including all floors and elevators.
- Handles drawing the building, calling elevators, and updating the system.

**Button Class**
- Represents the button on each floor for calling an elevator.
- Draws the button and defines its color based on whether it has been called or not.

**Elevator Class**
- Represents an elevator in the building.
- Moves between floors, handles requests, and updates its availability time.

**Floor Class**
- Represents a single floor in the building.
- Contains a button and a timer for displaying the estimated arrival time of the elevator.

**Timer Class**
- Represents a timer for each floor, displaying the estimated time of arrival for the elevator.
- Updates and draws the timer, including a color-coded progress arc.

**building_factory.py**
- `create_building(building_id, num_floors, num_elevators)`: Creates and returns a `Building` object with the specified number of floors, elevators, and starting position based on the building ID.
- `create_buildings(num_building)`: Creates and returns a `Buildings` object containing one or more `Building` objects based on the specified number of buildings.

**buildings.py**
- `Buildings` class:
    - `__init__(self)`: Initializes an empty list to store `Building` objects.
    - `add_building(self, building)`: Adds a `Building` object to the list of buildings.
    - `update(self, clock, surface)`: Updates all `Building` objects in the list by calling their `update` method.
    - `call_elevator(self, building_index, destination, button, surface)`: Calls the `call_elevator` method of the `Building` object at the specified index, passing the destination, button, and surface.

**main.py**
- Handles the main game loop and event handling.
- Initializes Pygame, loads resources, and creates the `Buildings` object.
- `check_click()`: Checks if a call button on any floor was clicked and calls the corresponding elevator.
- The main game loop handles events (such as quitting or clicking a button), clears the display, updates all buildings, and updates the display.

**settings.py**
- Contains various constants and settings used throughout the program, such as:
    - Window dimensions and display settings
    - Number of floors, elevators, and buildings
    - Object sizes (floors, elevators, buttons, timers)
    - Frame rate, font, and sound settings
    - Colors and image resources

Overall, these files work together to create and manage the building simulation with floors and elevators. The `building_factory.py` module creates `Building` and `Buildings` objects, the `buildings.py` module manages the list of buildings, `main.py` handles the main game loop and event handling, and `settings.py` contains various constants and settings used throughout the program.

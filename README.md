# RTS Build Order App

This is a simple Real-Time Strategy (RTS) build order application. It's a small utility designed to assist players in RTS games by providing them with build orders in a simple and easy-to-navigate interface. Build orders are sequences of actions usually taken at the start of games like StarCraft, Age of Empires, etc. to get a strategic advantage.

The application is built using Python's Tkinter module for GUI and allows the user to select a game, race and build order from the dropdown menus.

## Features

1. Game selection: The user can select a game for which to display the build orders.
2. Race selection: After a game has been selected, the user can select a race for the corresponding game.
3. Build Order selection: Once a race has been selected, a list of build orders for that particular game and race will be displayed.
4. Font Size selection: The user can change the font size of the displayed build order.
5. Overlay feature: The user can opt to overlay the application on top of other windows for ease of viewing while in-game.
6. Lock feature: Locks the position of the overlay to prevent accidental dragging.

## Prerequisites

The project is built using Python 3, so you'll need that to run the script. It uses Tkinter for the GUI which comes pre-installed with Python.

## Installation

1. Clone this repository or download the zip file.
    ```
    git clone https://github.com/username/RTS-Build-Order-App.git
    ```

2. Navigate to the project directory.
    ```
    cd RTS-Build-Order-App
    ```

3. Run the script.
    ```
    python rts_build_order_app.py
    ```

## Usage

After starting the application, follow these steps:

1. Select a game from the 'Select Game' dropdown.
2. Select a race from the 'Select Race' dropdown.
3. Select a build order from the 'Select Build Order' dropdown.
4. The selected build order will now be displayed in the listbox below.

You can also choose to overlay the build order on top of your game by checking the 'Overlay' option. Use the 'Lock' option to prevent the overlay from being accidentally moved.

## Data Source

The build orders are loaded from a JSON file named `builds.json`. Each game has its own set of races and each race has its own set of build orders. You can modify this file to add, remove or update build orders.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

# Tic Tac Toe Game

## Overview
This is a simple graphical implementation of the classic Tic Tac Toe game using Python's `tkinter` library. The game allows two players to take turns marking their respective symbols (X and O) on a 3x3 grid. The game detects wins, ties, and keeps track of scores for each player.

## Features
- Two-player gameplay
- Win detection for horizontal, vertical, and diagonal combinations
- Scorekeeping for Player X and Player O
- Restart functionality to play multiple rounds
- User-friendly graphical interface

## Requirements
- Python 3.x
- `tkinter` library (comes pre-installed with Python)

## Installation
1. Ensure you have Python 3.x installed on your machine.
2. Download or clone the repository containing the `Tic-Tac-Toe.py` file.
3. Navigate to the directory containing the file in your command line or terminal.

## Running the Game
To run the game, execute the following command in your terminal:

```bash
python Tic-Tac-Toe.py
```

## Gameplay Instructions
1. Upon running the game, you will see a 3x3 grid.
2. Player X will start first. Click on any empty cell to place your mark.
3. Players alternate turns until one player wins or the game ends in a tie.
4. The game announces the winner or if it's a tie.
5. Click the "Restart" button to play again without closing the application.

## Code Structure
The code is organized into several functions:
- `set_tile(row, column)`: Handles player moves and updates the board.
- `check_winner()`: Checks for winning conditions after each move.
- `update_score(winner)`: Updates and displays scores based on the winner.
- `new_game()`: Resets the game state for a new round.

### Global Variables
- `playerX`, `playerO`: Symbols used by players.
- `curr_player`: Keeps track of whose turn it is.
- `board`: Represents the state of the game board.
- `scoreX`, `scoreO`: Variables to keep track of scores for each player.

## Customization
You can customize various aspects of the game:
- Change colors by modifying the color variables (`color_blue`, `color_yellow`, etc.).
- Adjust font styles and sizes in label configurations.

## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your improvements or features.

## License
This project is open-source and available under the MIT License.

---

Enjoy playing Tic Tac Toe! If you have any questions or feedback, please reach out!

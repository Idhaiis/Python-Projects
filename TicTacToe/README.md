# Tic-Tac-Toe (Pygame)

A fully-featured Tic-Tac-Toe game built with Python and Pygame, featuring a main menu, local multiplayer, and an unbeatable AI opponent powered by the Minimax algorithm.

## Features

*   **Interactive Main Menu:** Clean GUI with options to resume games, start a new match, or play against an AI bot.
*   **Minimax AI Integration:** Play against a smart AI opponent utilizing the Minimax algorithm ("You Can't Beat Me!" mode).
*   **Audio & Visual Polish:** Includes sound effects for moves, wins/losses, win-line rendering, and dynamic cursor states.
*   **Asset Bundling:** Built-in resource path handling for compiled builds (`sys._MEIPASS`).

## Future Plans (TODO)

*   **Themes:** Add support for different visual color themes and board styles.

## How to Run

1.  Ensure you have Python and Pygame installed:
    ```bash
    pip install pygame
    ```
2.  Make sure your assets (`click.wav`, `game over.mp3`) are placed in the correct directory.
3.  Run the game:
    ```bash
    python main.py
    ```

## Controls

*   **Mouse Click:** Select grid cells to place X or O.
*   **ESC:** Return to the main menu.

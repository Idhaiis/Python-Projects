# Pygame Chess

A functional chess game built with Python and Pygame. Features classic board logic, move validation, and sound effects.

## Features

*   **Standard Chess Rules:** Movement logic for all pieces including pawns, knights, bishops, rooks, queens, and kings.
*   **Move Validation:** Checks for legal moves and prevents illegal maneuvers.
*   **Check Detection:** Notifies players when the king is in check.
*   **Sound Effects:** Includes audio feedback for moves, illegal actions, and checks.
*   **Interactive UI:** Highlighting for mouse cursor and valid move positions.

## Future Plans (TODO)

*   **Machine Learning Integration:** Implement a chess engine using machine learning to provide an AI opponent.
*   **Main Menu:** Add a GUI menu for game settings, mode selection, and difficulty levels.

## How to Run

1.  Ensure you have Python and Pygame installed:
    ```bash
    pip install pygame
    ```
2.  Ensure your assets (`Chess_Pieces_Sprite.png`, `move.mp3`, `illegal.mp3`, `check.mp3`) are in the same directory as the script.
3.  Run the game:
    ```bash
    python main.py
    ```

## Controls

*   **Click:** Select and move pieces.

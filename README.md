# AI-opponent-tic-tac-toe

## Description
This project is a terminal-based Tic Tac Toe game that features an AI opponent. The AI utilizes the Minimax algorithm to provide a challenging game experience. The game is written in Python and uses the `random` and `os` libraries to manage game operations and interactions.

## Technologies Used
- **Python**: Main programming language.
- **Libraries**: `random` for random number generation, `os` for operating system dependent functionality.

## Key Features
- **Terminal-based Interaction**: The game runs directly in the terminal, offering a straightforward text-based interface.
- **AI Opponent Using Minimax Algorithm**: The AI opponent uses the Minimax algorithm, which simulates all possible moves in the game to choose the optimal move. This algorithm is particularly effective in Tic Tac Toe due to the game's limited number of moves and outcomes.
- **Player vs. Player Mode**: Two human players can compete against each other directly.

## Planned Feature Updates
- **Medium Difficulty Level**: Introduce a medium level for the AI that alternates between strategic Minimax moves and random choices, offering a less predictable and moderately challenging opponent.
- **Physical Game Interface using Arduino**: Connect the game to an Arduino with LEDs and buttons to create a physical, interactive version of Tic Tac Toe.
- **Graphical User Interface (GUI)**: Develop a GUI to enhance user interaction, moving away from the terminal-based interface.
- **Online Multiplayer**: Implement online multiplayer capabilities to allow players to compete against each other remotely.
- **Undo Move Option**: Allow players to undo their last move, adding strategy and forgiveness to gameplay.
- **Customizable Player Symbols**: Let players choose their symbols instead of the default 'X' and 'O'.
- **Leaderboard**: Create a leaderboard to track the most wins and winning streaks among players.

## Installation and Running the Game
To run this game, clone the repository to your local machine and run the Python script in your terminal:
```bash
git clone <repository-url>
cd <repository-directory>
python tic_tac_toe.py

# Tic-Tac-Toe with AI

## Description
This project is a Tic-Tac-Toe game built using Python and Pygame, featuring an AI opponent powered by the Minimax algorithm. The AI plays optimally to ensure that it **never loses**, either winning or resulting in a draw. The project demonstrates the use of the minimax strategy in an interactive environment, making it a great example of how AI can be applied in classic board games.

**Technologies Used:**
- Python
- Pygame (for game visuals and interaction)
- Minimax Algorithm (for AI decision-making)

### How it works
The game alternates turns between the player and the AI. The AI uses the Minimax algorithm to evaluate all possible moves and choose the optimal one, making it unbeatable. The algorithm ensures that the AI chooses the move that maximizes its chances of winning while minimizing the player's chances.

### Features
- Minimax AI: The AI implements the Minimax algorithm, ensuring optimal play in every move.
- Pygame Interface: User-friendly graphical interface with easy interactions.

## Setup
To run this project on your local machine, follow these steps:

1. Clone the repository: ```git clone <repository_url>```
2. Navigate to the project directory
3. Install the required dependencies: ```pip install -r requirements.txt```
4. Run the game: ```python main.py```

A Pygame window will open where you can click on the squares to place your move.

## Example
Below are some gifs showcasing the game interface and AI interactions.

_Draw_

![draw](https://github.com/user-attachments/assets/4f3ff9e0-37e5-44a3-8406-6e2745bd0972)

_Player loses_

![loss](https://github.com/user-attachments/assets/cbfa21b3-85c4-4188-b5ca-2dc589f18cf0)

## Future Updates
- Implementing other AI strategies like **Alpha-Beta Pruning** for optimization.
- Exploring advanced AI models such as **Reinforcement Learning** to further enhance decision-making.
- Improving the user interface with additional features like difficulty levels, score tracking, and enhanced visuals.

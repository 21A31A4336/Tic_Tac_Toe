# Tic_Tac_Toe
It is a game developed using dynamic programming in python
************************************************************************
Tic Tac Toe Game
This is a simple implementation of a Tic Tac Toe game in Python. The game is designed for two players who will take turns to mark X and O on a 3x3 board. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
************************************************************************
Features
Display the game board
Check if the board is full
Check for winning conditions
Handle player turns and input
Functions
printboard(board)
Prints the current state of the game board.
***********************************************************************
Parameters:

board (list): A 2D list representing the Tic Tac Toe board.
isfull(board)
Checks if the game board is full.

Parameters:

board (list): A 2D list representing the Tic Tac Toe board.
Returns:

bool: True if the board is full, False otherwise.
check(board, pl)
Checks if a player has won the game.

Parameters:

board (list): A 2D list representing the Tic Tac Toe board.
pl (str): The player to check for a win ('X' or 'O').
Returns:

bool: True if the player has won, False otherwise.
***********************************************************************
How to Play
The game starts with an empty 3x3 board.
Players are prompted to enter their move by specifying the row and column indices (0, 1, or 2).
The current state of the board is displayed after each move.
The game checks for a win or a draw after each move.
The game ends when a player wins or the board is full, resulting in a draw.

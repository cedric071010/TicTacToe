import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Define a simple neural network for the Tic Tac Toe AI
class TicTacToeAI(nn.Module):
    def __init__(self):
        super(TicTacToeAI, self).__init__()
        self.fc1 = nn.Linear(9, 18)  # Input layer with 9 cells, output 18 features
        self.fc2 = nn.Linear(18, 9)  # Hidden layer with 18 features, output layer with 9 cells

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # Apply ReLU activation to the first layer
        x = self.fc2(x)  # Output layer
        return x

# Function to print the Tic Tac Toe board
def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

# Function to get empty positions on the board
def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

# Function to play the Tic Tac Toe game
def play_game():
    # Initialize the game board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Initialize the Tic Tac Toe AI model
    ai_model = TicTacToeAI()
    optimizer = optim.Adam(ai_model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    # Variable to track the player's turn
    player_turn = True  # True for player, False for AI

    while True:
        print_board(board)

        # Player's turn or AI's turn
        if player_turn:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
        else:
            # AI's turn
            empty_positions = get_empty_positions(board)
            input_tensor = torch.tensor([board[i][j] == 'X' for i in range(3) for j in range(3)], dtype=torch.float32)
            input_tensor = input_tensor.view(1, 9)

            with torch.no_grad():
                output = ai_model(input_tensor)
                valid_moves = torch.tensor([i * 3 + j for i, j in empty_positions], dtype=torch.long)
                ai_move = torch.argmax(torch.index_select(output, 1, valid_moves)).item()
                row, col = empty_positions[ai_move]

        # Make a move if the chosen cell is empty
        if board[row][col] == ' ':
            symbol = 'X' if player_turn else 'O'
            board[row][col] = symbol

            # Check if the current move results in a win
            if check_winner(board, symbol):
                print_board(board)
                print(f"{symbol} wins!")
                break
            # Check if the game is a draw
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch turns
            player_turn = not player_turn
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    play_game()

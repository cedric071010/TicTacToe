import random

class RandomPlayer:
    def __init__(self):
        self.name = "Random Player"

    def make_random_move(self, board):
        available_positions = [i for i, cell in enumerate(board) if cell == '0']
        return random.choice(available_positions)

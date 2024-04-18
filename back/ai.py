import random

class RandomPlayer:
    def __init__(self):
        self.name = "Random Player"

    @staticmethod
    def make_move(board):
        available_positions = [i for i, cell in enumerate(board) if cell == '0']
        return random.choice(available_positions)

class Human:
    def __init__(self):
        self.name = "Human Player"

    @staticmethod
    def make_move(board):
        available_positions = [i for i, cell in enumerate(board) if cell == '0']
        print("available positions are " + str(available_positions))
        move = input("enter your move> ")
        while int(move) not in available_positions:
            print(move + " is not available")
            move = input("enter your move> ")
        return int(move)

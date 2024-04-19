import random


class Random:
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

class Data:
    def __init__(self):
        self.name = "Data Player"

    @staticmethod
    def make_move(board):
        #player1
        if board == [ '0', '0', '0', '0', '0', '0', '0', '0', '0' ]:
            pass

        #player2
#doing

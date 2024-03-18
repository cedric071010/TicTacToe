class Game:
    def __init__(self):
        self.board = ['0'] * 9
        self.current_player = '1'

    def make_move(self, position):
        if self.board[position] == '0':
            self.board[position] = self.current_player
            self.current_player = '2' if self.current_player == '1' else '1'
            # simple ui for testing
        else:
            print("Invalid")
        
    def check_win(self):
            win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
            for condition in win_conditions:
                if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != '0':
                    return True
            return False

    # simple ui for testing
    def print_board(self):
            print(''.join(self.board) + '>')

    def play(self):
        while True:
            self.print_board()
            position = int(input()) - 1
            while position < 0 or position > 8:
                # simple ui for testing
                print("Invalid")
                # user input here is 1 to 9 instead of 0 to 8 for easy testing
                # use 0 to 8 when connecting to UI
                position = int(input()-1)
            self.make_move(position)
            if self.check_win():
                # simple ui for testing
                print("Player " + ('2' if self.current_player == '1' else '1') + " win")
                break

# test run
if __name__ == "__main__":
    game = Game()
    game.play()
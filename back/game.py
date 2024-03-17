class TicTacToe:
    def __init__(self):
        self.board = ['0'] * 9
        self.current_player = '1'

    def make_move(self, position):
        if self.board[position] == '0':
            self.board[position] = self.current_player
            self.current_player = '2' if self.current_player == '1' else '1'
        else:
            print("Invalid")

    def print_board(self):
        print(''.join(self.board) + '>')
        
    def check_win(self):
            win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
            for condition in win_conditions:
                if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != '0':
                    return True
            return False

    def play(self):
        while True:
            self.print_board()
            position = int(input()) - 1
            while position < 0 or position > 8:
                print("Invalid")
                position = int(input()-1)
            self.make_move(position)
            if self.check_win():
                print("Player " + ('2' if self.current_player == '1' else '1') + " win")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
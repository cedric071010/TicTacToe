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

    def play(self):
        while True:
            self.print_board()
            position = int(input()) - 1
            while position < 0 or position > 8:
                print("Invalid")
                position = int(input()-1)
            self.make_move(position)

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
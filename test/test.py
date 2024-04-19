import player

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
        win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != '0':
                return True
        return False

    def check_draw(self):
        return '0' not in self.board

    def play(self):
        while True:
            self.print_board()
            position = int(input())
            self.make_move(position)

def main():
    game_play = Game()
    player1 = player.ML
    player2 = player.ML

    while not game_play.check_win():
        if not game_play.check_draw():
            position = player1.make_move(game_play.board)
            game_play.make_move(position)
            print(game_play.board)

            if not game_play.check_win() and 0 in game_play.board:
                position = player2.make_move(game_play.board)
                game_play.make_move(position)
                print(game_play.board)

        else:
            print("draw")
            break

    if game_play.check_win():
        winner = 'Player 2' if game_play.current_player == '1' else 'Player 1'
        print(f"{winner} wins")

if __name__ == "__main__":
    main()
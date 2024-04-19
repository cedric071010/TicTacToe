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
    player1 = player.Random
    player2 = player.ML
    game = 0
    player1_win = 0
    player2_win = 0
    draw = 0
    problem = 0

    while not game_play.check_win():
        if not game_play.check_draw():
            position = player1.make_move(game_play.board)
            game_play.make_move(position)
            print(game_play.board)

            if not game_play.check_win() and '0' in game_play.board:
                position = player2.make_move(game_play.board)
                game_play.make_move(position)
                print(game_play.board)

        else:
            print('-'*50 +"draw")
            draw += 1
            game += 1
            break

    if game_play.check_win():
        game += 1
        winner = 'Player 2' if game_play.current_player == '1' else 'Player 1'
        print('-'*50 + f"{winner} wins")

    if game_play.current_player == '1' and game_play.check_win():
        player2_win += 1
    elif game_play.current_player == '2' and game_play.check_win():
        player1_win += 1
    else:
        problem += 1

    return game, player1_win, player2_win, draw, problem

if __name__ == "__main__":

    tgame = 0
    tplayer1_win = 0
    tplayer2_win = 0
    tdraw = 0
    tproblem = 0

    for i in range(100):

        game, player1_win, player2_win, draw, problem = main()

        tgame += game
        tplayer1_win += player1_win
        tplayer2_win += player2_win
        tdraw += draw
        tproblem += problem

    print(tgame)
    print(tplayer1_win)
    print(tplayer2_win)
    print(tdraw)
    print(problem)

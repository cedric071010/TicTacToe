from game import Game
from ai import RandomPlayer

def main():
    game_play = Game()
    random_player = RandomPlayer()

    if not game_play.check_draw():
        while not game_play.check_win():
            position = random_player.make_random_move(game_play.board)
            game_play.make_move(position)

        game_play.print_board()
        winner = 'Player 2' if game_play.current_player == '1' else 'Player 1'
        print(f"{winner} wins")

if __name__ == "__main__":
    main()
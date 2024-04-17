from game import Game
from ai import RandomPlayer

def main():
    game_play = Game()
    player1 = RandomPlayer()
    player2 = RandomPlayer()


    while not game_play.check_win():
        if not game_play.check_draw():
            position = player1.make_random_move(game_play.board)
            game_play.make_move(position)
            game_play.print_board()
            if not game_play.check_win():
                position = player2.make_random_move(game_play.board)
                game_play.make_move(position)
                game_play.print_board()
        else:
            print("draw")
            break

    if game_play.check_win():
        winner = 'Player 2' if game_play.current_player == '1' else 'Player 1'
        print(f"{winner} wins")


if __name__ == "__main__":
    main()

from game import Game
from ai import RandomPlayer
import copy
import json

def main():
    game_play = Game()
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    history = []

    while not game_play.check_win():
        if not game_play.check_draw():
            position = player1.make_random_move(game_play.board)
            game_play.make_move(position)

            board = copy.deepcopy(game_play.board)
            history.append(board)
            print(board)

            if not game_play.check_win():
                position = player2.make_random_move(game_play.board)
                game_play.make_move(position)

                board = copy.deepcopy(game_play.board)
                history.append(board)
                print(board)

        else:
            print("draw")
            break

    if game_play.check_win():
        winner = 'Player 2' if game_play.current_player == '1' else 'Player 1'
        print(f"{winner} wins")

    print(history)
    with open("history.json", "r") as json_file:
        existing_history = json.load(json_file)
    with open("history.json", "w") as json_file:
        json.dump(existing_history + history, json_file)

if __name__ == "__main__":
    main()

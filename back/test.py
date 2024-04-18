from game import Game
import player
import copy
import json
import time
from front.interface import ApplicationFrontInterface

def main():
    game_play = Game()
    player1 = player.Data
    player2 = player.RandomPlayer
    history = []

    while not game_play.check_win():
        if not game_play.check_draw():
            position = player1.make_random_move(game_play.board)
            game_play.make_move(position)

            board = copy.deepcopy(game_play.board)
            history.append(board)
            print(board)

            if not game_play.check_win() and 0 in game_play.board:
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
    history = {time.asctime(): history}
    print(history)

    existing_history = ApplicationFrontInterface.readFile("history.json")
    existing_history.update(history)
    ApplicationFrontInterface.writeFile("history.json", existing_history)

if __name__ == "__main__":
    main()

x_writen = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 1],
            [1, 2, 0, 0, 2, 0, 0, 0, 1],
            [1, 2, 0, 0, 2, 0, 0, 1, 1],
            [1, 2, 0, 0, 2, 0, 2, 1, 1],
            [1, 2, 1, 0, 2, 0, 2, 1, 1],
            [1, 2, 1, 0, 2, 2, 2, 1, 1],
        ]

y_writen = [0, 4, 8, 2, 7, 6, 2, 5, 3]


import test

import random
import numpy as np
from sklearn.tree import DecisionTreeClassifier


def main():
    x_base = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 1],
            [1, 2, 0, 0, 2, 0, 0, 0, 1],
            [1, 2, 0, 0, 2, 0, 0, 1, 1],
            [1, 2, 0, 0, 2, 0, 2, 1, 1],
            [1, 2, 1, 0, 2, 0, 2, 1, 1],
            [1, 2, 1, 0, 2, 2, 2, 1, 1],
        ]

    y_base = [0, 4, 8, 2, 7, 6, 2, 5, 3]

    x_new = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 2, 0, 0, 0, 0], [1, 0, 0, 0, 2, 0, 0, 0, 1], [1, 2, 0, 0, 2, 0, 0, 0, 1], [1, 2, 0, 0, 2, 0, 0, 1, 1], [1, 2, 0, 0, 2, 0, 2, 1, 1], [1, 2, 1, 0, 2, 0, 2, 1, 1], [1, 2, 1, 0, 2, 2, 2, 1, 1], ['1', '2', '2', '0', '2', '1', '1', '2', '1'], ['1', '2', '2', '0', '2', '1', '1', '2', '1'], ['1', '2', '2', '0', '2', '1', '1', '2', '1'], ['1', '2', '2', '0', '2', '1', '1', '2', '1']]

    y_new = [0, 4, 8, 2, 7, 6, 2, 5, 3, 4, 2, 7, 1]



    def ML_move(board, x, y):
            # Define the training data
            X_train = np.array(x)
            y_train = np.array(y)

            # Create and train the decision tree classifier
            classifier = DecisionTreeClassifier()
            classifier.fit(X_train, y_train)

            #predict the best integer given a list of 9 integers
            integers = np.array(board).reshape(1, -1)  # Reshape input for prediction
            prediction = classifier.predict(integers)

            available_positions = [i for i, cell in enumerate(board) if cell == '0']
            if prediction[0] in available_positions:
                return prediction[0]
            else:
                return random.choice(available_positions)


    player1_x = []
    player1_y = []
    player2_x = []
    player2_y = []

    game_play = test.Game()

    player1_win = False
    player2_win = False
    draw = False
    problem =False


    while not game_play.check_win():
        if not game_play.check_draw():
            position = ML_move(game_play.board, x_new, y_new)
            player1_x.append(game_play.board)
            player1_y.append(position)
            game_play.make_move(position)
            print(game_play.board)

        if not game_play.check_win() and '0' in game_play.board:
            position = ML_move(game_play.board, x_new, y_new)
            player2_x.append(game_play.board)
            player2_y.append(position)
            game_play.make_move(position)
            print(game_play.board)

        else:
            print('-'*50 +"draw")
            draw = True
            break

    if game_play.check_win() and not draw:
        winner = 'Player 2' if game_play.current_player == '1' else 'Player 1'
        print('-'*50 + f"{winner} wins")

    if game_play.current_player == '1' and game_play.check_win():
        player2_win = True
    elif game_play.current_player == '2' and game_play.check_win():
        player1_win = True
    else:
         problem = True
     

    if not problem and not draw:

        if player1_win:
            print(player1_x)
            for data in player1_x:
                x_new.append(data)
            print(player1_y)
            for data in player1_y:
                y_new.append(data)

        if player2_win:
            print(player2_x)
            for data in player2_x:
                x_new.append(data)
            print(player2_y)
            for data in player2_y:
                y_new.append(data)


        print('-'*50)
        print(x_new)
        print(y_new)
       

main()
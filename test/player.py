import random
import numpy as np
from sklearn.tree import DecisionTreeClassifier


class ML:
    def __init__(self):
        self.name = "ML Player"

    @staticmethod
    def make_move(board):
        # Define the training data
        X_train = np.array([

            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 1],
            [1, 2, 0, 0, 2, 0, 0, 0, 1],
            [1, 2, 0, 0, 2, 0, 0, 1, 1],
            [1, 2, 0, 0, 2, 0, 2, 1, 1],
            [1, 2, 1, 0, 2, 0, 2, 1, 1],
            [1, 2, 1, 0, 2, 2, 2, 1, 1],

        ])
        y_train = np.array([0, 4, 8, 2, 7, 6, 2, 5, 3])

        # Create and train the decision tree classifier
        classifier = DecisionTreeClassifier()
        classifier.fit(X_train, y_train)

        #predict the best integer given a list of 9 integers
        integers = np.array(board).reshape(1, -1)  # Reshape input for prediction
        prediction = classifier.predict(integers)

        available_positions = [i for i, cell in enumerate(board) if cell == '0']
        print("available positions are " + str(available_positions))
        if prediction[0] in available_positions:
            return prediction[0]
        else:
            return random.choice(available_positions)


class Random:
    def __init__(self):
        self.name = "Random Player"

    @staticmethod
    def make_move(board):
        available_positions = [i for i, cell in enumerate(board) if cell == '0']
        return random.choice(available_positions)


class Human:
    def __init__(self):
        self.name = "Human Player"

    @staticmethod
    def make_move(board):
        available_positions = [i for i, cell in enumerate(board) if cell == '0']
        print("available positions are " + str(available_positions))
        move = input("enter your move> ")
        while int(move) not in available_positions:
            print(move + " is not available")
            move = input("enter your move> ")
        return int(move)

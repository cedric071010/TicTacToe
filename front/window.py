from PyQt6.QtWidgets import QWidget, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from interface import ApplicationInterface
from random import randint
from subwindows import *


class MainWindow(QMainWindow, ApplicationInterface):

    def __init__(self):
        super().__init__()

        # initialising elements
        self.singleplayerButton = QPushButton()
        self.multiplayerButton = QPushButton()
        self.settingsButton = QPushButton()
        self.quitButton = QPushButton()
        self.button1 = QPushButton("X")
        self.button2 = QPushButton("O")
        self.button3 = QPushButton("X")
        self.button4 = QPushButton("O")
        self.button5 = QPushButton("X")
        self.button6 = QPushButton("O")
        self.button7 = QPushButton("X")
        self.button8 = QPushButton("O")
        self.button9 = QPushButton("X")

        # give elements id for qss
        for button in [self.singleplayerButton, self.multiplayerButton, self.settingsButton, self.quitButton]:
            button.setObjectName("optionButton")
        for button in [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6,
                       self.button7, self.button8, self.button9]:
            button.setObjectName("gameButton")

        # window level configs
        self.setWindowTitle("Tic Tac Toe Remastered")
        self.resize(1750, 1000)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # ----------topLevelLayout---------- level 1
        # --{optionLayout}--{buttonLayout}-- level 2
        self.topLevelLayout = QHBoxLayout()
        self.buttonLayout = QGridLayout()
        self.optionLayout = QVBoxLayout()

        self.buttonLayout.addWidget(self.button1, 0, 0)
        self.buttonLayout.addWidget(self.button2, 0, 1)
        self.buttonLayout.addWidget(self.button3, 0, 2)
        self.buttonLayout.addWidget(self.button4, 1, 0)
        self.buttonLayout.addWidget(self.button5, 1, 1)
        self.buttonLayout.addWidget(self.button6, 1, 2)
        self.buttonLayout.addWidget(self.button7, 2, 0)
        self.buttonLayout.addWidget(self.button8, 2, 1)
        self.buttonLayout.addWidget(self.button9, 2, 2)

        self.topLevelLayout.addLayout(self.optionLayout)
        self.topLevelLayout.addLayout(self.buttonLayout)

        self.createGUI()

    def createGUI(self):
        # link buttons with their functions
        self.singleplayerButton.setText("Singleplayer")
        self.singleplayerButton.clicked.connect(self.singleplayerAction)
        self.multiplayerButton.setText("Multiplayer")
        self.multiplayerButton.clicked.connect(self.multiplayerAction)
        self.settingsButton.setText("Settings")
        self.settingsButton.clicked.connect(self.settingsAction)
        self.quitButton.setText("Quit")
        self.quitButton.clicked.connect(self.quitAction)

        # add widgets to layout
        self.optionLayout.addWidget(self.singleplayerButton)
        self.optionLayout.addWidget(self.multiplayerButton)
        self.optionLayout.addWidget(self.settingsButton)
        self.optionLayout.addWidget(self.quitButton)

        self.centralWidget.setLayout(self.topLevelLayout)

    def singleplayerAction(self):
        pass

    def multiplayerAction(self):
        pass

    def settingsAction(self):
        pass

    def quitAction(self):
        pass

    # dynamically changing menu
    def dynamicUpdate(self):
        for button in [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6,
                       self.button7, self.button8, self.button9]:
            button.setText(["X", "O"][randint(0, 1)])

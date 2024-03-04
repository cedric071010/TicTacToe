from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, \
    QGridLayout
import sys
from QTInterface import ApplicationInterface
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from random import randint
from time import sleep


class MainWindow(QMainWindow, ApplicationInterface):

    def __init__(self):
        super().__init__()

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

        self.button1.setObjectName("gameButton")
        self.button2.setObjectName("gameButton")
        self.button3.setObjectName("gameButton")
        self.button4.setObjectName("gameButton")
        self.button5.setObjectName("gameButton")
        self.button6.setObjectName("gameButton")
        self.button7.setObjectName("gameButton")
        self.button8.setObjectName("gameButton")
        self.button9.setObjectName("gameButton")

        self.setWindowTitle("Tic Tac Toe Remastered")
        self.resize(1750, 1000)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.topLayout = QHBoxLayout()
        self.anotherLayout = QGridLayout()
        self.mainLayout = QVBoxLayout()

        self.anotherLayout.addWidget(self.button1, 0, 0)
        self.anotherLayout.addWidget(self.button2, 0, 1)
        self.anotherLayout.addWidget(self.button3, 0, 2)
        self.anotherLayout.addWidget(self.button4, 1, 0)
        self.anotherLayout.addWidget(self.button5, 1, 1)
        self.anotherLayout.addWidget(self.button6, 1, 2)
        self.anotherLayout.addWidget(self.button7, 2, 0)
        self.anotherLayout.addWidget(self.button8, 2, 1)
        self.anotherLayout.addWidget(self.button9, 2, 2)

        self.topLayout.addLayout(self.mainLayout)
        self.topLayout.addLayout(self.anotherLayout)

        # Todo: multithreading
        self.idle = True

        self.createGUI()

    def createGUI(self):
        self.singleplayerButton.setText("Singleplayer")
        self.singleplayerButton.clicked.connect(self.singleplayerAction)
        self.multiplayerButton.setText("Multiplayer")
        self.multiplayerButton.clicked.connect(self.multiplayerAction)
        self.settingsButton.setText("Settings")
        self.settingsButton.clicked.connect(self.settingsAction)
        self.quitButton.setText("Quit")
        self.quitButton.clicked.connect(self.quitAction)

        self.mainLayout.addWidget(self.singleplayerButton)
        self.mainLayout.addWidget(self.multiplayerButton)
        self.mainLayout.addWidget(self.settingsButton)
        self.mainLayout.addWidget(self.quitButton)

        self.centralWidget.setLayout(self.topLayout)

    def singleplayerAction(self):
        self.idle = False
        pass

    def multiplayerAction(self):
        self.idle = False
        pass

    def settingsAction(self):
        self.idle = False
        pass

    def quitAction(self):
        self.idle = False
        pass

    def idleState(self):
        while self.idle:
            self.button1.setText(["X", "O"][randint(0, 1)])
            self.button2.setText(["X", "O"][randint(0, 1)])
            self.button3.setText(["X", "O"][randint(0, 1)])
            self.button4.setText(["X", "O"][randint(0, 1)])
            self.button5.setText(["X", "O"][randint(0, 1)])
            self.button6.setText(["X", "O"][randint(0, 1)])
            self.button7.setText(["X", "O"][randint(0, 1)])
            self.button8.setText(["X", "O"][randint(0, 1)])
            self.button9.setText(["X", "O"][randint(0, 1)])
            sleep(1)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    with open("QTGlobal.qss", "r") as f:
        stylesheet = str(f.read())
    window.setStyleSheet(stylesheet)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

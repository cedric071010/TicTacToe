from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QProgressBar
from front.interface import ApplicationFrontInterface
from back.interface import ApplicationBackInterface
from PyQt6.QtCore import QTimer
from random import randint


class LocalWindow(QWidget, ApplicationFrontInterface):
    def __init__(self):
        super(LocalWindow, self).__init__()

        self.onClose = False

        self.topLevelLayout = QHBoxLayout()
        self.buttonLayout = QGridLayout()
        self.optionLayout = QVBoxLayout()

        self.button1 = QPushButton("")
        self.button2 = QPushButton("")
        self.button3 = QPushButton("")
        self.button4 = QPushButton("")
        self.button5 = QPushButton("")
        self.button6 = QPushButton("")
        self.button7 = QPushButton("")
        self.button8 = QPushButton("")
        self.button9 = QPushButton("")
        self.allButtons = (self.button1, self.button2, self.button3, self.button4, self.button5, self.button6,
                           self.button7, self.button8, self.button9)
        self.winLabel = QPushButton("")
        self.toggleEvalButton = QPushButton("")
        self.resetButton = QPushButton("")
        self.quitButton = QPushButton("")
        self.evalBar = QProgressBar()
        self.evalBar.setOrientation(Qt.Orientation.Vertical)

        ApplicationFrontInterface.setObjectID(self.button1, self.button2, self.button3, self.button4, self.button5,
                                              self.button6, self.button7, self.button8, self.button9,
                                              ID="gameButton")

        ApplicationFrontInterface.setObjectID(self.winLabel, self.toggleEvalButton, self.resetButton, self.quitButton,
                                              ID="optionButton")

        ApplicationFrontInterface.assignButtons([self.button1, "", lambda: self.buttonAction(self.button1)],
                                                [self.button2, "", lambda: self.buttonAction(self.button2)],
                                                [self.button3, "", lambda: self.buttonAction(self.button3)],
                                                [self.button4, "", lambda: self.buttonAction(self.button4)],
                                                [self.button5, "", lambda: self.buttonAction(self.button5)],
                                                [self.button6, "", lambda: self.buttonAction(self.button6)],
                                                [self.button7, "", lambda: self.buttonAction(self.button7)],
                                                [self.button8, "", lambda: self.buttonAction(self.button8)],
                                                [self.button9, "", lambda: self.buttonAction(self.button9)],
                                                [self.winLabel, "No winner yet", type],
                                                [self.toggleEvalButton, "Toggle Eval.", self.toggleEvalAction],
                                                [self.resetButton, "Reset", self.resetAction],
                                                [self.quitButton, "Quit", self.quitAction])

        self.setLayout(self.topLevelLayout)
        self.topLevelLayout.addWidget(self.evalBar)
        self.topLevelLayout.addLayout(self.buttonLayout)
        self.topLevelLayout.addLayout(self.optionLayout)

        self.buttonLayout.addWidget(self.button1, 0, 0)
        self.buttonLayout.addWidget(self.button2, 0, 1)
        self.buttonLayout.addWidget(self.button3, 0, 2)
        self.buttonLayout.addWidget(self.button4, 1, 0)
        self.buttonLayout.addWidget(self.button5, 1, 1)
        self.buttonLayout.addWidget(self.button6, 1, 2)
        self.buttonLayout.addWidget(self.button7, 2, 0)
        self.buttonLayout.addWidget(self.button8, 2, 1)
        self.buttonLayout.addWidget(self.button9, 2, 2)

        ApplicationFrontInterface.addWidgets(self.winLabel, self.toggleEvalButton, self.resetButton, self.quitButton,
                                             layout=self.optionLayout)

        self.resize(1750, 1000)
        self.setWindowTitle("Tic Tac Toe Remastered - Local Mode")

        with open("front/global.qss", "r") as f:
            stylesheet = str(f.read())
        self.setStyleSheet(stylesheet)

        self.playerMove = "X"
        self.winningMove = False
        self.moves = 0
        self.isLastMoveValid = True
        self.evalValue = 50

        self.timer = QTimer()
        self.timer.timeout.connect(self.refreshEval)
        self.timer.start(10)

    def closeEvent(self, event):
        self.onClose = True
        self.close()

    def buttonAction(self, button):
        if self.winningMove:
            return

        self.playerMove, self.isLastMoveValid = ApplicationBackInterface.makeMove(button, self.playerMove)
        self.winningMove, self.moves = ApplicationBackInterface.checkWin(self.isLastMoveValid, self.allButtons,
                                                                         self.moves)
        if self.winningMove:
            self.winLabel.setText(f"{self.winningMove} wins!")

    def toggleEvalAction(self):
        self.evalBar.show() if self.evalBar.isHidden() else self.evalBar.hide()

    def resetAction(self):
        self.playerMove = "X"
        self.winningMove = False
        self.moves = 0
        for button in [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7,
                       self.button8, self.button9]:
            button.setText("")
        self.winLabel.setText("No winner yet")

    def quitAction(self):
        self.close()

    def refreshEval(self):
        # test values, waiting back integration
        self.evalValue += 1
        if self.evalValue > 100:
            self.evalValue = 50
            if not randint(0, 1):
                self.evalValue = 0

        self.evalBar.setValue(self.evalValue)
        pass


if __name__ == "__main__":
    pass

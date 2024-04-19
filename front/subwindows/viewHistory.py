from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QProgressBar
from front.interface import ApplicationFrontInterface
from back.interface import ApplicationBackInterface
from PyQt6.QtCore import QTimer
from random import randint


class HistoryWindow(QWidget, ApplicationFrontInterface):
    def __init__(self, gameTime):
        super(HistoryWindow, self).__init__()

        self.gameTime = gameTime

        self.settings = ApplicationFrontInterface.readFile("back/settings.json")

        self._ = ApplicationFrontInterface.translation(self.settings["lang"])

        self.onClose = False

        self.gameHistory = ApplicationFrontInterface.readFile("back/settingsTemplate.json")[self.gameTime]
        self.gameHistory[0].update(self.gameHistory[1])
        self.playerInfo = self.gameHistory[0]
        self.gameHistory = self.gameHistory[2:]
        self.winMessage = f"{self.playerInfo['X'][0] if self.playerInfo['X'][1] else self.playerInfo['O'][0]} wins!"
        self.totalMoves = len(self.gameHistory)
        self.moves = -1

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
        self.backwardButton = QPushButton("")
        self.forwardButton = QPushButton("")
        self.quitButton = QPushButton("")
        self.evalBar = QProgressBar()
        self.evalBar.setOrientation(Qt.Orientation.Vertical)

        ApplicationFrontInterface.setObjectID(self.button1, self.button2, self.button3, self.button4, self.button5,
                                              self.button6, self.button7, self.button8, self.button9,
                                              ID="gameButton")

        ApplicationFrontInterface.setObjectID(self.winLabel, self.toggleEvalButton, self.backwardButton,
                                              self.forwardButton, self.quitButton,
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
                                                [self.winLabel, self._("No winner yet"), type],
                                                [self.toggleEvalButton, self._("Toggle Eval."), self.toggleEvalAction],
                                                [self.backwardButton, "←", self.backwardAction],
                                                [self.forwardButton, "→", self.forwardAction],
                                                [self.quitButton, self._("Quit"), self.quitAction])

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
        if self.settings["theme"] != "default":
            self.buttonLayout.addWidget(QLabel(), 3, 0)
            self.buttonLayout.addWidget(QLabel(), 3, 1)
            self.buttonLayout.addWidget(QLabel(), 3, 2)

        ApplicationFrontInterface.addWidgets(self.winLabel, self.toggleEvalButton, self.backwardButton,
                                             self.forwardButton, self.quitButton,
                                             layout=self.optionLayout)

        self.resize(1750, 1000)
        self.setWindowTitle(self._("Tic Tac Toe Remastered - View History"))

        with open("front/global.qss", "r") as f:
            stylesheet = str(f.read())
        self.setStyleSheet(stylesheet)

        self.evalValue = 50

        self.timer = QTimer()
        self.timer.timeout.connect(self.refreshEval)
        self.timer.start(10)


    def closeEvent(self, event):
        self.onClose = True
        self.close()

    def buttonAction(self, button):
        pass

    def toggleEvalAction(self):
        self.evalBar.show() if self.evalBar.isHidden() else self.evalBar.hide()

    def backwardAction(self):
        if self.moves <= 0:
            return
        self.moves -= 1
        self.updateBoard()

    def forwardAction(self):
        if self.moves >= self.totalMoves - 1:
            return
        self.moves += 1
        self.updateBoard()

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

    def updateBoard(self):
        for i, button in enumerate(self.allButtons):
            button.setText({"0": "", "1": "X", "2": "O"}[self.gameHistory[self.moves][i]])
        if self.moves == self.totalMoves - 1:
            self.winLabel.setText(self.winMessage)
        else:
            self.winLabel.setText("No winner yet")


if __name__ == "__main__":
    pass

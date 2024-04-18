from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QProgressBar, QLabel
from front.interface import ApplicationFrontInterface
from back.interface import ApplicationBackInterface
from PyQt6.QtCore import QTimer
from random import randint
from back.player import Random


class SingleplayerWindow(QWidget, ApplicationFrontInterface):
    def __init__(self):
        super(SingleplayerWindow, self).__init__()

        self.settings = ApplicationFrontInterface.readFile("back/settings.json")

        self._ = ApplicationFrontInterface.translation(self.settings["lang"])

        self.ALL_DIFFICULTIES = (self._("Easy"), self._("Normal"), self._("Impossible"), self._("Random"))
        self.ALL_SPEEDS = {0: self._("Instant"),
                           250: self._("Fast"),
                           500: self._("Normal"),
                           750: self._("Slow"),
                           1000: self._("Very Slow")}
        self.difficulty = self._("Random")

        self.firstMove = "X"
        self.playerMove = "X"
        self.winningMove = False
        self.moves = 0
        self.isLastMoveValid = True
        self.evalValue = 50
        self.didLastMoveFinish = True
        self.delayTime = 500

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
        self.difficultyButton = QPushButton("")
        self.playAsButton = QPushButton("")
        self.winLabel = QPushButton("")
        self.toggleEvalButton = QPushButton("")
        self.toggleSpeedButton = QPushButton("")
        self.resetButton = QPushButton("")
        self.quitButton = QPushButton("")
        self.evalBar = QProgressBar()
        self.evalBar.setOrientation(Qt.Orientation.Vertical)

        ApplicationFrontInterface.setObjectID(*self.allButtons,
                                              ID="gameButton")

        ApplicationFrontInterface.setObjectID(self.difficultyButton, self.playAsButton, self.winLabel,
                                              self.toggleEvalButton, self.toggleSpeedButton,
                                              self.resetButton, self.quitButton,
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
                                                [self.difficultyButton, self.difficulty, self.difficultyAction],
                                                [self.playAsButton, self._("Play as: ") + self.firstMove, self.playAsAction],
                                                [self.winLabel, self._("No winner yet"), type],
                                                [self.toggleEvalButton, self._("Toggle Eval."), self.toggleEvalAction],
                                                [self.toggleSpeedButton, self._("Speed: ") + self.ALL_SPEEDS[self.delayTime],
                                                 self.toggleSpeedAction],
                                                [self.resetButton, self._("Reset"), self.resetAction],
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

        ApplicationFrontInterface.addWidgets(self.difficultyButton, self.playAsButton, self.winLabel,
                                             self.toggleEvalButton, self.toggleSpeedButton, self.resetButton,
                                             self.quitButton,
                                             layout=self.optionLayout)

        self.resize(1750, 1000)
        self.setWindowTitle(self._("Tic Tac Toe Remastered - Singleplayer"))

        with open("front/global.qss", "r") as f:
            stylesheet = str(f.read())
        self.setStyleSheet(stylesheet)

        self.timer = QTimer()
        self.timer.timeout.connect(self.refreshEval)
        self.timer.start(10)

        self.botMoveDelayTimer = QTimer()
        self.botMoveDelayTimer.timeout.connect(self.botMove)
        self.botMoveDelayTimer.setSingleShot(True)

    def closeEvent(self, event):
        self.onClose = True
        self.close()

    def buttonAction(self, button):
        if not self.winningMove and self.didLastMoveFinish:
            self.playerMove, self.isLastMoveValid = ApplicationBackInterface.makeMove(button, self.playerMove)
            self.winningMove, self.moves = ApplicationBackInterface.checkWin(self.isLastMoveValid, self.allButtons,
                                                                             self.moves)

            if self.winningMove:
                self.winLabel.setText(self.winningMove + " " + self._("wins!"))
                return

            elif self.moves == 9:
                self.winLabel.setText(self._("No one") + " " + self._("wins!"))
                return

            if self.isLastMoveValid:
                self.didLastMoveFinish = False
                self.botMoveDelayTimer.start(self.delayTime)

    def difficultyAction(self):
        self.difficulty = self.ALL_DIFFICULTIES[(self.ALL_DIFFICULTIES.index(self.difficulty) + 1)
                                                % len(self.ALL_DIFFICULTIES)]
        self.difficultyButton.setText(self.difficulty)
        self.resetAction()

    def playAsAction(self):
        self.firstMove = ('X', 'O')[self.firstMove == 'X']
        self.playAsButton.setText(self._("Play as: ") + self.firstMove)
        self.resetAction()

    def toggleEvalAction(self):
        self.evalBar.show() if self.evalBar.isHidden() else self.evalBar.hide()

    def toggleSpeedAction(self):
        self.delayTime = list(self.ALL_SPEEDS)[(list(self.ALL_SPEEDS).index(self.delayTime) + 1)
                                               % len(list(self.ALL_SPEEDS))]
        self.toggleSpeedButton.setText(self._("Speed: ") + self.ALL_SPEEDS[self.delayTime])

    def resetAction(self):
        self.winningMove = False
        self.moves = 0
        for button in self.allButtons:
            button.setText("")
        self.winLabel.setText(self._("No winner yet"))
        self.playAsButton.setText(self._("Play as: ") + self.firstMove)
        self.playerMove = self.firstMove
        if self.firstMove == 'O':
            self.playerMove = 'X'
            self.didLastMoveFinish = False
            self.botMoveDelayTimer.start(self.delayTime)

    def quitAction(self):
        self.close()

    def refreshEval(self):
        # test values, waiting back integration
        self.evalValue += 1
        if self.evalValue > 100:
            self.evalValue = 50
            if randint(0, 1):
                self.evalValue = 0

        self.evalBar.setValue(self.evalValue)

    def botMove(self):
        if self.difficulty == self._("Random"):
            pos = Random.make_random_move(self.getBoard())
            self.allButtons[pos].setText(self.playerMove)
            self.playerMove = ('X', 'O')[self.playerMove == 'X']
            self.winningMove, self.moves = ApplicationBackInterface.checkWin(self.isLastMoveValid, self.allButtons,
                                                                             self.moves)
            if self.winningMove:
                self.winLabel.setText(self.winningMove + " " + self._("wins!"))

            elif self.moves == 9:
                self.winLabel.setText(self._("No one") + " " + self._("wins!"))

        elif self.difficulty == self._("Easy"):
            pass

        elif self.difficulty == self._("Normal"):
            pass

        elif self.difficulty == self._("Impossible"):
            pass
        self.didLastMoveFinish = True

    def getBoard(self):
        return list(map(lambda button: '0' if button.text() == "" else ('1', '2')[button.text() == 'O'],
                        self.allButtons))


if __name__ == "__main__":
    pass

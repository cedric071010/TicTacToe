from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel
from front.interface import ApplicationInterface


class LocalWindow(QWidget, ApplicationInterface):
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
        self.winLabel = QPushButton("")
        self.resetButton = QPushButton("")
        self.quitButton = QPushButton("")

        ApplicationInterface.setObjectID(self.button1, self.button2, self.button3, self.button4, self.button5,
                                         self.button6, self.button7, self.button8, self.button9,
                                         ID="gameButton")

        ApplicationInterface.setObjectID(self.winLabel, self.resetButton, self.quitButton,
                                         ID="optionButton")

        ApplicationInterface.assignButtons([self.button1, "", self.button1Action],
                                           [self.button2, "", self.button2Action],
                                           [self.button3, "", self.button3Action],
                                           [self.button4, "", self.button4Action],
                                           [self.button5, "", self.button5Action],
                                           [self.button6, "", self.button6Action],
                                           [self.button7, "", self.button7Action],
                                           [self.button8, "", self.button8Action],
                                           [self.button9, "", self.button9Action],
                                           [self.winLabel, "No winner yet", type],
                                           [self.resetButton, "Reset", self.resetAction],
                                           [self.quitButton, "Quit", self.quitAction])

        self.setLayout(self.topLevelLayout)
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

        self.optionLayout.addWidget(self.winLabel)
        self.optionLayout.addWidget(self.resetButton)
        self.optionLayout.addWidget(self.quitButton)

        self.resize(1750, 1000)
        self.setWindowTitle("Tic Tac Toe Remastered - Multiplayer")

        with open("front/global.qss", "r") as f:
            stylesheet = str(f.read())
        self.setStyleSheet(stylesheet)

        self.playerMove = "X"
        self.winningMove = False
        self.moves = 0

    def closeEvent(self, event):
        self.onClose = True
        self.close()

    def button1Action(self):
        if not self.winningMove:
            self.playerMove = ApplicationInterface.makeMove(self.button1, self.playerMove)
            self.winningMove = self.checkWin()
            if self.winningMove:
                self.winLabel.setText(f"{self.winningMove} wins!")

    def button2Action(self):
        if not self.winningMove:
            self.playerMove = ApplicationInterface.makeMove(self.button2, self.playerMove)
            self.winningMove = self.checkWin()
            if self.winningMove:
                self.winLabel.setText(f"{self.winningMove} wins!")

    def button3Action(self):
        if not self.winningMove:
            self.playerMove = ApplicationInterface.makeMove(self.button3, self.playerMove)
            self.winningMove = self.checkWin()
            if self.winningMove:
                self.winLabel.setText(f"{self.winningMove} wins!")

    def button4Action(self):
        if not self.winningMove:
            self.playerMove = ApplicationInterface.makeMove(self.button4, self.playerMove)
            self.winningMove = self.checkWin()
            if self.winningMove:
                self.winLabel.setText(f"{self.winningMove} wins!")

    def button5Action(self):
        if not self.winningMove:
            self.playerMove = ApplicationInterface.makeMove(self.button5, self.playerMove)
            self.winningMove = self.checkWin()
            if self.winningMove:
                self.winLabel.setText(f"{self.winningMove} wins!")

    def button6Action(self):
        if not self.winningMove:
            self.playerMove = ApplicationInterface.makeMove(self.button6, self.playerMove)
            self.winningMove = self.checkWin()
            if self.winningMove:
                self.winLabel.setText(f"{self.winningMove} wins!")

    def button7Action(self):
        if not self.winningMove:
            self.playerMove = ApplicationInterface.makeMove(self.button7, self.playerMove)
            self.winningMove = self.checkWin()
            if self.winningMove:
                self.winLabel.setText(f"{self.winningMove} wins!")

    def button8Action(self):
        if not self.winningMove:
            self.playerMove = ApplicationInterface.makeMove(self.button8, self.playerMove)
            self.winningMove = self.checkWin()
            if self.winningMove:
                self.winLabel.setText(f"{self.winningMove} wins!")

    def button9Action(self):
        if not self.winningMove:
            self.playerMove = ApplicationInterface.makeMove(self.button9, self.playerMove)
            self.winningMove = self.checkWin()
            if self.winningMove:
                self.winLabel.setText(f"{self.winningMove} wins!")

    def checkWin(self) -> str | bool:
        self.moves += 1
        winConditions = [(self.button1, self.button2, self.button3), (self.button4, self.button5, self.button6),
                         (self.button7, self.button8, self.button9), (self.button1, self.button4, self.button7),
                         (self.button2, self.button5, self.button8), (self.button3, self.button6, self.button9),
                         (self.button1, self.button5, self.button9), (self.button3, self.button5, self.button7)]
        for condition in winConditions:
            if condition[0] != "" and all(condition[0].text() == button.text() for button in condition):
                return condition[0].text()

        if self.moves == 9:
            return "No one"

        return False

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


if __name__ == "__main__":
    pass

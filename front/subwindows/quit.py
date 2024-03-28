from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout

from front.interface import ApplicationFrontInterface


class QuitWindow(QWidget, ApplicationFrontInterface):
    def __init__(self):
        super(QuitWindow, self).__init__()

        self.settings = ApplicationFrontInterface.readFile("back/settings.json")
        self._ = ApplicationFrontInterface.translation(self.settings["lang"])

        self.onClose = False

        self.layout = QHBoxLayout()
        self.quitButton = QPushButton()
        self.quitButton.setObjectName("optionButton")
        self.backButton = QPushButton()
        self.backButton.setObjectName("optionButton")

        self.quitButton.setText(self._("Quit"))
        self.backButton.setText(self._("Back"))
        self.quitButton.clicked.connect(quit)
        self.backButton.clicked.connect(self.close)

        self.layout.addWidget(self.quitButton)
        self.layout.addWidget(self.backButton)
        self.setLayout(self.layout)

        self.resize(1750, 1000)
        self.setWindowTitle(self._("Tic Tac Toe Remastered - Confirm Quit"))

        with open("front/global.qss", "r") as f:
            stylesheet = str(f.read())
        self.setStyleSheet(stylesheet)

    def closeEvent(self, event):
        self.onClose = True
        self.close()


if __name__ == "__main__":
    pass

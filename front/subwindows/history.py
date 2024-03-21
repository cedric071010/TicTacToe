from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout
from front.interface import ApplicationFrontInterface


class HistoryWindow(QWidget, ApplicationFrontInterface):
    def __init__(self):
        super(HistoryWindow, self).__init__()

        self.onClose = False

        self.layout = QHBoxLayout()
        self.labelButton = QPushButton()
        self.labelButton.setObjectName("optionButton")

        self.labelButton.setText("Hello World")

        self.layout.addWidget(self.labelButton)
        self.setLayout(self.layout)

        self.resize(1750, 1000)
        self.setWindowTitle("Tic Tac Toe Remastered - History")

        with open("front/global.qss", "r") as f:
            stylesheet = str(f.read())
        self.setStyleSheet(stylesheet)

    def closeEvent(self, event):
        self.onClose = True
        self.close()


if __name__ == "__main__":
    pass

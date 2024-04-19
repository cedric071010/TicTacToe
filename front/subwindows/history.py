import PyQt6
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QFrame, QScrollArea, QSizePolicy
from front.interface import ApplicationFrontInterface
from PyQt6.QtCore import Qt


class HistoryWindow(QWidget, ApplicationFrontInterface):
    def __init__(self):
        super(HistoryWindow, self).__init__()

        self.onClose = False

        self.topLevelLayout = QVBoxLayout()
        self.gameHistoryLayout = QVBoxLayout()
        self.frames = []

        self.container = QWidget()
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.container)
        self.scroll.setWidgetResizable(True)
        self.container.setLayout(self.gameHistoryLayout)

        n = 10
        for i in range(n):
            self.frames.append(QFrame())
            self.frames[i].resize(300, 300)
            self.gameHistoryLayout.addWidget(self.frames[i])
            self.frames[i].setMinimumSize(1000, 100)
            self.frames[i].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.topLevelLayout.addWidget(self.scroll)
        self.setLayout(self.topLevelLayout)

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

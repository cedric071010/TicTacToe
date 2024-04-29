import PyQt6
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QFrame, QScrollArea, QSizePolicy
from front.interface import ApplicationFrontInterface
from PyQt6.QtCore import Qt
from front.subwindows import viewHistory, templateClass


class HistoryWindow(QWidget, ApplicationFrontInterface):
    def __init__(self):
        super(HistoryWindow, self).__init__()

        self.onClose = False

        self.w = templateClass.TemplateClass()

        self.topLevelLayout = QVBoxLayout()
        self.gameHistoryLayout = QVBoxLayout()
        self.label1 = QLabel("hello world")
        self.frames = []
        self.layouts = []
        self.labels = []
        self.buttons = []
        self.history = ApplicationFrontInterface.readFile("back/history.json")

        self.container = QWidget()
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.container)
        self.scroll.setWidgetResizable(True)
        self.container.setLayout(self.gameHistoryLayout)

        for i in range(len(self.history)):
            self.frames.append(QFrame())
            self.layouts.append(QVBoxLayout())
            self.labels.append(QLabel())
            self.buttons.append(QPushButton())

            self.labels[i].setText(f"{list(self.history.keys())[i]}, X: {self.history[list(self.history.keys())[i]][0]['X'][0]}, O: {self.history[list(self.history.keys())[i]][1]['O'][0]}")

            ApplicationFrontInterface.assignButtons([self.buttons[i], "✓",
                                                     lambda button=self.buttons[i],
                                                     gameTime=list(self.history.keys())[i]:
                                                     self.openHistoryWindow(gameTime)])

            self.frames[i].resize(300, 300)
            self.layouts[i].addWidget(self.labels[i])
            self.layouts[i].addWidget(self.buttons[i])
            self.frames[i].setLayout(self.layouts[i])

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

    def openHistoryWindow(self, gameTime):
        if self.w.onClose:
            self.w = viewHistory.HistoryWindow(gameTime)
            self.w.show()


if __name__ == "__main__":
    pass

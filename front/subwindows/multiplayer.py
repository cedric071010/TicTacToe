from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from front.interface import ApplicationInterface
from front.subwindows.multiplayerModes import local
from front.subwindows.templateClass import TemplateClass


class MultiplayerWindow(QWidget, ApplicationInterface):
    def __init__(self):
        super(MultiplayerWindow, self).__init__()

        self.onClose = False

        self.layout = QGridLayout()
        self.localButton = QPushButton()
        self.LANButton = QPushButton()
        self.onlineButton = QPushButton()
        self.quitButton = QPushButton()
        self.w = TemplateClass()

        ApplicationInterface.setObjectID(self.localButton, self.LANButton, self.onlineButton, self.quitButton,
                                         ID="optionButton")

        self.layout.addWidget(self.localButton, 0, 0)
        self.layout.addWidget(self.LANButton, 0, 1)
        self.layout.addWidget(self.onlineButton, 1, 0)
        self.layout.addWidget(self.quitButton, 1, 1)

        self.setLayout(self.layout)

        ApplicationInterface.assignButtons([self.localButton, "Local Mode", self.localAction],
                                           [self.LANButton, "LAN Mode", self.LANAction],
                                           [self.onlineButton, "Online Mode", self.onlineAction],
                                           [self.quitButton, "Back", self.quitAction])

        self.resize(1750, 1000)
        self.setWindowTitle("Tic Tac Toe Remastered - Multiplayer")

        with open("front/global.qss", "r") as f:
            stylesheet = str(f.read())
        self.setStyleSheet(stylesheet)

    def closeEvent(self, event):
        self.onClose = True
        self.close()

    def localAction(self):
        if self.w.onClose:
            self.w = local.LocalWindow()
            self.w.show()

    def LANAction(self):
        pass

    def onlineAction(self):
        pass

    def quitAction(self):
        self.close()


if __name__ == "__main__":
    pass

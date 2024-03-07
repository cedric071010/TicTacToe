from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QLabel
from front.interface import ApplicationInterface
import json
from time import sleep


class SettingsWindow(QWidget, ApplicationInterface):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        self.settingsFile = None

        with open("front/assets/lang/locales.json", "r") as f:
            self.locales = json.loads(f.read())

        with open("back/settings.json", "r") as f:
            self.settings = json.loads(f.read())

        self.onClose = False
        self.lang = self.settings["lang"]
        self.fullScreenState = self.settings["fullscreen"]

        self.topLevelLayout = QHBoxLayout()
        self.layout = QVBoxLayout()
        self.langComboBox = QComboBox()
        self.fullScreenButton = QPushButton()
        self.applyButton = QPushButton()

        self.langComboBox.setObjectName("optionButton")
        self.fullScreenButton.setObjectName("optionButton")
        self.applyButton.setObjectName("optionButton")

        self.fullScreenButton.setText(f"Fullscreen - {['Off', 'On'][self.fullScreenState]}")
        self.fullScreenButton.clicked.connect(self.fullScreenAction)
        if self.fullScreenState:
            self.showFullScreen()

        self.applyButton.setText("Apply")
        self.applyButton.clicked.connect(self.applyAction)

        self.langComboBox.addItems(self.locales.keys())
        self.langComboBox.setCurrentText([i[0] for i in self.locales.items() if i[1] == self.lang][0])

        self.layout.addWidget(self.langComboBox)
        self.layout.addWidget(self.fullScreenButton)
        self.layout.addWidget(self.applyButton)
        # layout bug
        self.topLevelLayout.addLayout(self.layout)
        self.setLayout(self.topLevelLayout)

        self.resize(1440, 900)
        self.setWindowTitle("Tic Tac Toe Remastered - Settings")

        with open("front/global.qss", "r") as f:
            stylesheet = str(f.read())
        self.setStyleSheet(stylesheet)

    def closeEvent(self, event):
        self.onClose = True
        self.close()

    def fullScreenAction(self):
        self.fullScreenState = not self.fullScreenState
        if self.fullScreenState:
            self.showFullScreen()
            self.fullScreenButton.setText("Fullscreen - On")
        else:
            self.showNormal()
            self.fullScreenButton.setText("Fullscreen - Off")

    def applyAction(self):
        self.lang = self.locales[self.langComboBox.currentText()]
        self.settings["lang"] = self.lang
        self.settings["fullscreen"] = int(self.fullScreenState)
        with open("back/settings.json", "w") as f:
            f.write(json.dumps(self.settings, indent=2))


if __name__ == "__main__":
    pass

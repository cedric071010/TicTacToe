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

        with open("front/assets/settings.json", "r") as f:
            self.settings = json.loads(f.read())

        self.onClose = False
        self.lang = self.settings["lang"]

        self.topLevelLayout = QHBoxLayout()
        self.layout = QVBoxLayout()
        self.langComboBox = QComboBox()
        self.langComboBox.setObjectName("optionButton")
        self.applyButton = QPushButton()
        self.applyButton.setObjectName("optionButton")
        self.applyButton.clicked.connect(self.applyAction)
        self.applyButton.setText("Apply")
        self.stateLabel = QLabel()
        self.stateLabel.setText("")
        self.stateLabel.setObjectName("stateLabel")
        self.stateLabel.height = 0

        self.langComboBox.addItems(self.locales.keys())
        self.langComboBox.setCurrentText([i[0] for i in self.locales.items() if i[1] == self.lang][0])

        self.layout.addWidget(self.langComboBox)
        self.layout.addWidget(self.applyButton)
        self.layout.addWidget(self.stateLabel)
        # layout bug
        self.topLevelLayout.addLayout(self.layout)
        self.setLayout(self.topLevelLayout)

        self.resize(1750, 1000)
        self.setWindowTitle("Tic Tac Toe Remastered - Settings")

        with open("front/global.qss", "r") as f:
            stylesheet = str(f.read())
        self.setStyleSheet(stylesheet)

    def closeEvent(self, event):
        self.onClose = True
        self.close()

    def applyAction(self):
        self.lang = self.locales[self.langComboBox.currentText()]
        self.settings["lang"] = self.lang
        with open("front/assets/settings.json", "w") as f:
            f.write(json.dumps(self.settings, indent=2))
        self.stateLabel.setText("Successful")
        # other thread


if __name__ == "__main__":
    pass

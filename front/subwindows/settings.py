from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QLabel, QLineEdit, \
    QGridLayout
from front.interface import ApplicationFrontInterface
from PyQt6.QtCore import Qt
import json
from time import sleep


class SettingsWindow(QWidget, ApplicationFrontInterface):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        self.ALL_THEMES = ['dark_amber.xml',
                           'dark_blue.xml',
                           'dark_cyan.xml',
                           'dark_lightgreen.xml',
                           'dark_pink.xml',
                           'dark_purple.xml',
                           'dark_red.xml',
                           'dark_teal.xml',
                           'dark_yellow.xml',
                           'light_amber.xml',
                           'light_blue.xml',
                           'light_cyan.xml',
                           'light_cyan_500.xml',
                           'light_lightgreen.xml',
                           'light_pink.xml',
                           'light_purple.xml',
                           'light_red.xml',
                           'light_teal.xml',
                           'light_yellow.xml',
                           'default']

        self.settingsFile = None

        self.locales = ApplicationFrontInterface.readFile("front/assets/lang/locales.json")
        self.settings = ApplicationFrontInterface.readFile("back/settings.json")

        self.onClose = False
        self.lang = self.settings["lang"]
        self.fullScreenState = self.settings["fullscreen"]
        self.theme = self.settings["theme"]

        self.lineEditOnFocus = False

        self.topLevelLayout = QHBoxLayout()
        self.layout = QVBoxLayout()
        self.gridLayout = QGridLayout()
        self.langComboBox = QComboBox()
        self.fullScreenButton = QPushButton()
        self.themeButton = QPushButton()
        self.applyButton = QPushButton()
        self.quitButton = QPushButton()

        self.resolutionXLineEdit = QLineEdit()
        self.resolutionXLineEdit.setValidator(QIntValidator())
        self.resolutionXLineEdit.setMaxLength(4)
        self.resolutionXLineEdit.setReadOnly(True)
        self.resolutionXLineEdit.returnPressed.connect(self.resolutionLineEditOnPress)

        self.resolutionYLineEdit = QLineEdit()
        self.resolutionYLineEdit.setValidator(QIntValidator())
        self.resolutionYLineEdit.setMaxLength(4)
        self.resolutionYLineEdit.setReadOnly(True)
        self.resolutionYLineEdit.returnPressed.connect(self.resolutionLineEditOnPress)
        # incomplete, needs save and link slider

        ApplicationFrontInterface.setObjectID(self.langComboBox, self.fullScreenButton, self.themeButton,
                                              self.applyButton, self.quitButton, ID="optionButton")
        ApplicationFrontInterface.setObjectID(self.resolutionXLineEdit,
                                              self.resolutionYLineEdit, ID="resolutionLineEdit")

        self.fullScreenButton.setText(f"Fullscreen - {['Off', 'On'][self.fullScreenState]}")
        self.fullScreenButton.clicked.connect(self.fullScreenAction)
        if self.fullScreenState:
            self.showFullScreen()

        ApplicationFrontInterface.assignButtons([self.themeButton, f"Theme: {self.theme.replace('.xml', '')}",
                                                 self.themeAction],
                                                [self.applyButton, "Apply", self.applyAction],
                                                [self.quitButton, "Back", self.quitAction])

        self.langComboBox.addItems(self.locales.keys())
        self.langComboBox.setCurrentText([i[0] for i in self.locales.items() if i[1] == self.lang][0])

        self.gridLayout.addWidget(self.langComboBox, 0, 0)
        self.gridLayout.addWidget(self.fullScreenButton, 1, 0)
        self.gridLayout.addWidget(self.themeButton, 2, 0)
        self.gridLayout.addWidget(self.applyButton, 3, 0)
        self.gridLayout.addWidget(self.quitButton, 4, 0)
        self.gridLayout.addWidget(self.resolutionXLineEdit, 5, 0)
        self.gridLayout.addWidget(self.resolutionYLineEdit, 6, 0)
        # layout bug
        self.topLevelLayout.addLayout(self.gridLayout)

        self.setLayout(self.topLevelLayout)

        self.resize(1440, 900)
        self.setWindowTitle("Tic Tac Toe Remastered - Settings")

        stylesheet = ApplicationFrontInterface.readFile("front/global.qss", isJSON=False)
        self.setStyleSheet(stylesheet)

    def resolutionLineEditOnPress(self):
        self.lineEditOnFocus = not self.lineEditOnFocus
        self.resolutionXLineEdit.setReadOnly(self.lineEditOnFocus)
        self.resolutionYLineEdit.setReadOnly(self.lineEditOnFocus)

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

    def themeAction(self):
        self.theme = self.ALL_THEMES[(self.ALL_THEMES.index(self.theme) + 1) % len(self.ALL_THEMES)]
        self.themeButton.setText(f"Theme: {self.theme.replace('.xml', '')}")
        # start.py integration

    def applyAction(self):
        self.lang = self.locales[self.langComboBox.currentText()]
        self.settings["lang"] = self.lang
        self.settings["fullscreen"] = int(self.fullScreenState)
        self.settings["theme"] = self.theme
        ApplicationFrontInterface.writeFile("back/settings.json", self.settings)

    def quitAction(self):
        self.onClose = True
        self.close()


if __name__ == "__main__":
    pass

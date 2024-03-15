from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QLabel, QSlider, QLineEdit
from front.interface import ApplicationInterface
from PyQt6.QtCore import Qt
import json
from time import sleep


class SettingsWindow(QWidget, ApplicationInterface):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        self.settingsFile = None

        self.locales = ApplicationInterface.readFile("front/assets/lang/locales.json")
        self.settings = ApplicationInterface.readFile("back/settings.json")

        self.onClose = False
        self.lang = self.settings["lang"]
        self.fullScreenState = self.settings["fullscreen"]

        self.lineEditOnFocus = False

        self.topLevelLayout = QHBoxLayout()
        self.layout = QVBoxLayout()
        self.langComboBox = QComboBox()
        self.fullScreenButton = QPushButton()
        self.applyButton = QPushButton()
        self.resolutionXSlider = QSlider(Qt.Orientation.Horizontal)
        self.resolutionXLineEdit = QLineEdit()
        self.resolutionYSlider = QSlider(Qt.Orientation.Horizontal)
        self.resolutionYLineEdit = QLineEdit()

        self.resolutionXSlider.setMinimum(256)
        self.resolutionXSlider.setMaximum(4096)
        self.resolutionXSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.resolutionXSlider.setSingleStep(256)
        self.resolutionXSlider.setTickInterval(256)
        self.resolutionXSlider.valueChanged.connect(self.displayXSliderAction)
        self.resolutionYSlider.setMinimum(256)
        self.resolutionYSlider.setMaximum(4096)
        self.resolutionYSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.resolutionYSlider.setSingleStep(256)
        self.resolutionYSlider.setTickInterval(256)
        self.resolutionYSlider.valueChanged.connect(self.displayYSliderAction)

        self.resolutionXLineEdit.setValidator(QIntValidator())
        self.resolutionXLineEdit.setMaxLength(4)
        self.resolutionXLineEdit.setReadOnly(True)
        self.resolutionXLineEdit.returnPressed.connect(self.resolutionLineEditOnPress)
        self.resolutionYLineEdit.setValidator(QIntValidator())
        self.resolutionYLineEdit.setMaxLength(4)
        self.resolutionYLineEdit.setReadOnly(True)
        self.resolutionYLineEdit.returnPressed.connect(self.resolutionLineEditOnPress)
        # incomplete, needs save and link slider

        self.langComboBox.setObjectName("optionButton")
        self.fullScreenButton.setObjectName("optionButton")
        self.applyButton.setObjectName("optionButton")
        self.resolutionXSlider.setObjectName("resolutionSlider")
        self.resolutionXLineEdit.setObjectName("resolutionLineEdit")
        self.resolutionYSlider.setObjectName("resolutionSlider")
        self.resolutionYLineEdit.setObjectName("resolutionLineEdit")

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
        self.layout.addWidget(self.resolutionXSlider)
        self.layout.addWidget(self.resolutionXLineEdit)
        self.layout.addWidget(self.resolutionYSlider)
        self.layout.addWidget(self.resolutionYLineEdit)
        # layout bug
        self.topLevelLayout.addLayout(self.layout)
        self.setLayout(self.topLevelLayout)

        self.resize(1440, 900)
        self.setWindowTitle("Tic Tac Toe Remastered - Settings")

        stylesheet = ApplicationInterface.readFile("front/global.qss", isJSON=False)
        self.setStyleSheet(stylesheet)

    def resolutionLineEditOnPress(self):
        self.lineEditOnFocus = not self.lineEditOnFocus
        self.resolutionXLineEdit.setReadOnly(self.lineEditOnFocus)
        self.resolutionYLineEdit.setReadOnly(self.lineEditOnFocus)

    def closeEvent(self, event):
        self.onClose = True
        self.close()

    def displayXSliderAction(self):
        self.resolutionXLineEdit.setText(f"{self.resolutionXSlider.value()}")

    def displayYSliderAction(self):
        self.resolutionYLineEdit.setText(f"{self.resolutionYSlider.value()}")

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
        ApplicationInterface.writeFile("back/settings.json", self.settings)


if __name__ == "__main__":
    pass

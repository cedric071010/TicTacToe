from PyQt6.QtWidgets import QWidget, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtCore import QTimer
from front.interface import ApplicationFrontInterface
from random import randint
from front.subwindows import singleplayer, multiplayer, playUntilWin, history, achievements, settings, quit, \
    templateClass


class MainWindow(QMainWindow, ApplicationFrontInterface):

    def __init__(self):
        super().__init__()

        self.settings = None
        self.lang = None
        self.fullScreenState = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateSettings)
        self.timer.start(1000)

        # initialising elements
        self.singleplayerButton = QPushButton()
        self.multiplayerButton = QPushButton()
        self.playUntilWinButton = QPushButton()
        self.historyButton = QPushButton()
        self.achievementButton = QPushButton()
        self.settingsButton = QPushButton()
        self.quitButton = QPushButton()
        self.button1 = QPushButton("X")
        self.button2 = QPushButton("O")
        self.button3 = QPushButton("X")
        self.button4 = QPushButton("O")
        self.button5 = QPushButton("X")
        self.button6 = QPushButton("O")
        self.button7 = QPushButton("X")
        self.button8 = QPushButton("O")
        self.button9 = QPushButton("X")
        self.w = templateClass.TemplateClass()

        ApplicationFrontInterface.setObjectID(self.singleplayerButton, self.multiplayerButton,
                                              self.playUntilWinButton, self.historyButton, self.achievementButton,
                                              self.settingsButton, self.quitButton,
                                              ID="optionButton")

        ApplicationFrontInterface.setObjectID(self.button1, self.button2, self.button3, self.button4,
                                              self.button5, self.button6, self.button7, self.button8, self.button9,
                                              ID="gameButton")

        # window level configs
        self.setWindowTitle("Tic Tac Toe Remastered")
        self.resize(1440, 900)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # ----------topLevelLayout---------- level 1
        # --{optionLayout}--{buttonLayout}-- level 2
        self.topLevelLayout = QHBoxLayout()
        self.buttonLayout = QGridLayout()
        self.optionLayout = QVBoxLayout()

        self.buttonLayout.addWidget(self.button1, 0, 0)
        self.buttonLayout.addWidget(self.button2, 0, 1)
        self.buttonLayout.addWidget(self.button3, 0, 2)
        self.buttonLayout.addWidget(self.button4, 1, 0)
        self.buttonLayout.addWidget(self.button5, 1, 1)
        self.buttonLayout.addWidget(self.button6, 1, 2)
        self.buttonLayout.addWidget(self.button7, 2, 0)
        self.buttonLayout.addWidget(self.button8, 2, 1)
        self.buttonLayout.addWidget(self.button9, 2, 2)

        self.topLevelLayout.addLayout(self.optionLayout)
        self.topLevelLayout.addLayout(self.buttonLayout)

        self.createGUI()

    def createGUI(self):
        # link buttons with their functions
        ApplicationFrontInterface.assignButtons([self.singleplayerButton, "Singleplayer", self.singleplayerAction],
                                                [self.multiplayerButton, "Multiplayer", self.multiplayerAction],
                                                [self.playUntilWinButton, "Play Until Win", self.playUntilWinAction],
                                                [self.historyButton, "History", self.historyAction],
                                                [self.achievementButton, "Achievements", self.achievementAction],
                                                [self.settingsButton, "Settings", self.settingsAction],
                                                [self.quitButton, "Quit", self.quitAction])

        # add widgets to layout
        ApplicationFrontInterface.addWidgets(self.singleplayerButton, self.multiplayerButton,
                                             self.playUntilWinButton, self.historyButton, self.achievementButton,
                                             self.settingsButton, self.quitButton,
                                             layout=self.optionLayout)

        self.centralWidget.setLayout(self.topLevelLayout)

    def singleplayerAction(self):
        if self.w.onClose:
            self.w = singleplayer.SingleplayerWindow()
            self.w.show()

    def multiplayerAction(self):
        if self.w.onClose:
            self.w = multiplayer.MultiplayerWindow()
            self.w.show()

    def playUntilWinAction(self):
        if self.w.onClose:
            self.w = playUntilWin.PlayUntilWinWindow()
            self.w.show()

    def historyAction(self):
        if self.w.onClose:
            self.w = history.HistoryWindow()
            self.w.show()

    def achievementAction(self):
        if self.w.onClose:
            self.w = achievements.AchievementsWindow()
            self.w.show()

    def settingsAction(self):
        if self.w.onClose:
            self.w = settings.SettingsWindow()
            self.w.show()

    def quitAction(self):
        if self.w.onClose:
            self.w = quit.QuitWindow()
            self.w.show()

    # dynamically changing menu
    def dynamicUpdate(self):
        for button in [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6,
                       self.button7, self.button8, self.button9]:
            button.setText(["X", "O"][randint(0, 1)])

    def updateSettings(self):
        if self.w.onClose:
            self.settings = ApplicationFrontInterface.readFile("back/settings.json")
            self.lang = self.settings["lang"]
            self.fullScreenState = self.settings["fullscreen"]

        # lang
        pass

        # fullscreen
        if self.fullScreenState:
            self.showFullScreen()
        else:
            self.showNormal()


if __name__ == "__main__":
    pass

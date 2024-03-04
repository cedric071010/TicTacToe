from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, \
    QGridLayout
import sys
from ..interface import ApplicationInterface


class SingleplayerWindow(QMainWindow, ApplicationInterface):
    def __init__(self):
        super().__init__()


def main():
    app = QApplication(sys.argv)
    window = SingleplayerWindow()
    with open("global.qss", "r") as f:
        stylesheet = str(f.read())
    window.setStyleSheet(stylesheet)
    window.show()
    sys.exit(app.exec())

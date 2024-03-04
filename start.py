from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from front.window import MainWindow
import sys


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    with open("global.qss", "r") as f:
        stylesheet = str(f.read())
    window.setStyleSheet(stylesheet)
    window.show()

    timer = QTimer()
    timer.timeout.connect(window.dynamicUpdate)
    timer.start(500)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from front.window import MainWindow
import sys
from lib.qt_material import apply_stylesheet


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    with open("front/global.qss", "r") as f:
        stylesheet = str(f.read())
    window.setStyleSheet(stylesheet)

    apply_stylesheet(app, theme='dark_teal.xml')
    window.show()

    timer = QTimer()
    timer.timeout.connect(window.dynamicUpdate)
    timer.start(500)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()

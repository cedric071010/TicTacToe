from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from front.window import MainWindow
import sys
from lib.qt_material import apply_stylesheet
from front.interface import ApplicationFrontInterface


def main():
    settings = ApplicationFrontInterface.readFile("back/settings.json")

    app = QApplication(sys.argv)
    window = MainWindow()
    with open("front/global.qss", "r") as f:
        stylesheet = str(f.read())
    window.setStyleSheet(stylesheet)

    if settings["theme"] != "default":
        apply_stylesheet(app, theme=settings["theme"])
    window.show()

    timer = QTimer()
    timer.timeout.connect(window.dynamicUpdate)
    timer.start(500)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()

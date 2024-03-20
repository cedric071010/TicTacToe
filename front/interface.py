import json
import PyQt6.QtWidgets


class ApplicationInterface:
    @staticmethod
    def readFile(filePath: str, isJSON: bool = True) -> dict | str:
        """
        Returns the contents of a file.
        :param filePath: file path
        :param isJSON: .json file or not
        :return: dict | str
        """

        with open(filePath, "r") as f:
            return json.loads(f.read()) if isJSON else f.read()

    @staticmethod
    def writeFile(filePath: str, msg: dict | str, isJSON: bool = True, indent: int = 2) -> None:
        """
        Write the message to a file.
        :param filePath: file path
        :param msg: content you want to write
        :param isJSON: .json file or not
        :param indent: indentation used in .json files
        :return: None
        """

        with open(filePath, "w") as f:
            if isJSON:
                f.write(json.dumps(msg, indent=indent))
                return
            f.write(msg)

    @staticmethod
    def setObjectID(*args: PyQt6.QtWidgets.QWidget, ID: str) -> None:
        for obj in args:
            obj.setObjectName(ID)

    @staticmethod
    def assignButtons(*args: PyQt6.QtWidgets.QPushButton) -> None:
        for arg in args:
            button = arg[0]
            button.setText(arg[1])
            button.clicked.connect(arg[2])

    @staticmethod
    def addWidgets(*widgets: PyQt6.QtWidgets.QWidget, layout: PyQt6.QtWidgets.QLayout) -> None:
        for widget in widgets:
            layout.addWidget(widget)

    @staticmethod
    def makeMove(button: PyQt6.QtWidgets.QPushButton, playerMove: str) -> tuple[str, bool]:
        if button.text() == "":
            button.setText(playerMove)
            return ("X", "O")[playerMove == "X"], True
        return playerMove, False

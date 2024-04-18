import json
import gettext


class ApplicationFrontInterface:
    @staticmethod
    def readFile(filePath: str, isJSON: bool = True) -> dict | str:
        """
        Returns the contents of a file.
        :param filePath: file path
        :param isJSON: .json file or not
        :return: dict | str
        """

        with open(filePath, "r") as f:
            if isJSON:
                if f.read() in {"", "null"}:
                    return {}
                print(f.read())
                return json.loads(f.read())
            return f.read()

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
    def setObjectID(*args, ID: str):
        for obj in args:
            obj.setObjectName(ID)

    @staticmethod
    def assignButtons(*args):
        for arg in args:
            button = arg[0]
            button.setText(arg[1])
            button.clicked.connect(arg[2])

    @staticmethod
    def addWidgets(*widgets, layout):
        for widget in widgets:
            layout.addWidget(widget)

    @staticmethod
    def translation(language: str = "en"):
        if language == "en":
            return gettext.gettext

        lang = gettext.translation("base", localedir="front/assets/locales", languages=[language])
        lang.install()
        return lang.gettext

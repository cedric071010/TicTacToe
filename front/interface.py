import json


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

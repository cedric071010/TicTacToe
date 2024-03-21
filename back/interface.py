import PyQt6.QtWidgets


class ApplicationBackInterface:
    @staticmethod
    def makeMove(button: PyQt6.QtWidgets.QPushButton, playerMove: str) -> [str, bool]:
        if button.text() == "":
            button.setText(playerMove)
            return ("X", "O")[playerMove == "X"], True
        return playerMove, False

    @staticmethod
    def checkWin(isLastMoveValid, allButtons, moves) -> tuple[str | bool, int]:
        if isLastMoveValid:
            moves += 1
            winConditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
            for condition in winConditions:
                if allButtons[condition[0]] != "" and all(allButtons[condition[0]].text() == button.text() for button
                                                          in (allButtons[condition[0]], allButtons[condition[1]],
                                                              allButtons[condition[2]])):
                    return allButtons[condition[0]].text(), moves

            if moves == 9:
                return "No one", moves

        return False, moves
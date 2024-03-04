import tkinter as tk
from tkinter import messagebox


class OnePlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("1 player")

        setting_message = tk.Label(self, text="No AI yet, try 2 player", font=("Helvetica", 14))
        button_quit_setting = tk.Button(self, text="OK", command=self.destroy)

        setting_message.pack(pady=10)
        button_quit_setting.pack(pady=10)


class TwoPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("2 player")
        self.geometry("300x350")
        self.create_board()
        self.current_player_label = tk.Label(self, text="Current Player: X", font=("Helvetica", 14))
        self.current_player_label.grid(row=3, column=0, columnspan=3)
        self.undo_button = tk.Button(self, text="Undo Move", command=self.undo_move, state=tk.DISABLED)
        self.undo_button.grid(row=4, column=0, columnspan=3)
        self.quit_button = tk.Button(self, text="Quit", command=self.quit_game)
        self.quit_button.grid(row=5, column=0, columnspan=3)

    def create_board(self):
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        self.current_player = "X"
        self.last_move = None

        for i in range(3):
            for j in range(3):
                button = tk.Button(self, text="", width=10, height=5, command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def make_move(self, row, col):
        button = self.buttons[row][col]

        if button["text"] == "":
            button["text"] = self.current_player

            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.current_player_label.config(text=f"Current Player: {self.current_player}")
                self.undo_button.config(state=tk.NORMAL)
                self.last_move = (row, col)

    def undo_move(self):
        if self.last_move:
            row, col = self.last_move
            button = self.buttons[row][col]
            button["text"] = ""
            self.current_player = "O" if self.current_player == "X" else "X"
            self.current_player_label.config(text=f"Current Player: {self.current_player}")
            self.undo_button.config(state=tk.DISABLED)
            self.last_move = None

    def check_winner(self, row, col):
        player = self.current_player

        if all(self.buttons[row][i]["text"] == player for i in range(3)) or \
                all(self.buttons[i][col]["text"] == player for i in range(3)) or \
                all(self.buttons[i][i]["text"] == player for i in range(3)) or \
                all(self.buttons[i][2 - i]["text"] == player for i in range(3)):
            return True

        return False

    def check_draw(self):
        return all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.current_player = "X"
        self.current_player_label.config(text="Current Player: X")
        self.undo_button.config(state=tk.DISABLED)
        self.last_move = None

    def quit_game(self):
        self.destroy()


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Menu")
        self.geometry("300x300")
        self.create_menu_buttons()

    def create_menu_buttons(self):
        button1p = tk.Button(self, text="Start 1 player", command=self.start_1p)
        button2p = tk.Button(self, text="Start 2 player", command=self.start_2p)
        button_settings = tk.Button(self, text="Settings", command=self.open_settings)
        button_quit = tk.Button(self, text="Quit", command=self.quit_game)

        button1p.pack(pady=10)
        button2p.pack(pady=10)
        button_settings.pack(pady=10)
        button_quit.pack(pady=10)

    def start_1p(self):
        game = OnePlayer()
        game.mainloop()

    def start_2p(self):
        game = TwoPlayer()
        game.mainloop()

    def open_settings(self):
        settings_window = tk.Toplevel(self)
        settings_window.geometry("300x300")
        settings_window.title("Settings")

        setting_message = tk.Label(settings_window, text="Nothing to set yet", font=("Helvetica", 14))
        button_quit_setting = tk.Button(settings_window, text="OK", command=settings_window.destroy)

        setting_message.pack(pady=10)
        button_quit_setting.pack(pady=10)

    def quit_game(self):
        quit_window = tk.Toplevel(self)
        quit_window.geometry("300x300")
        quit_window.title("Are you sure you want to quit?")
        button_confirm_quit = tk.Button(quit_window, text="Yes", command=self.destroy)
        button_dont_quit = tk.Button(quit_window, text="No", command=quit_window.destroy)
        button_confirm_quit.pack(pady=10)
        button_dont_quit.pack(pady=10)


if __name__ == "__main__":
    app = Menu()
    app.mainloop()

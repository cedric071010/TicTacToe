import tkinter as tk
from tkinter import messagebox


class TwoPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("2 player")
        self.geometry("300x300")
        self.create_board()

    def create_board(self):
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        self.current_player = "X"

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
        self.destroy()

    def start_2p(self):
        app = TwoPlayer()
        app.mainloop()

    def open_settings(self):
        settings_window = tk.Toplevel(self)
        settings_window.geometry("300x300")
        settings_window.title("Settings")
        button_setting = tk.Button(settings_window, text="Nothing to set yet", command=settings_window.destroy)
        button_quit_setting = tk.Button(settings_window, text="OK", command=settings_window.destroy)
        button_setting.pack(pady=10)
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

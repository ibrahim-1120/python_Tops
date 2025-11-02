"""
Tkinter Tic-Tac-Toe Game (Python)

Run:
    python tic_tac_toe_tkinter.py

Features:
- Player vs Player
- Simple GUI
- Detects win/draw
- Restart button
"""

import tkinter as tk
from tkinter import messagebox


import tkinter as tk
from tkinter import messagebox

BG_COLOR = "#1e1f22"
BTN_BG = "#2b2d31"
BTN_FG = "#ffffff"
HIGHLIGHT = "#5865f2"

class TicTacToe:
    def __init__(self, root, vs_computer=True):
        self.root = root
        self.root.title("Tic Tac Toe - Tkinter")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.vs_computer = vs_computer

        self.buttons = []
        self.make_board()

        self.self.reset_button = tk.Button(root, text="Restart", font=("Arial", 16, "bold"), bg=HIGHLIGHT, fg="white", relief="flat", command=self.reset_game)(root, text="Restart", font=("Arial", 14), command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def make_board(self):
        for i in range(9):
            btn = tk.Button(
                self.root,
                text="",
                font=("Arial", 36, "bold"),
                width=4,
                height=1,
                bg=BTN_BG,
                fg=BTN_FG,
                activebackground=HIGHLIGHT,
                activeforeground="white",
                relief="flat",
                bd=3,
                highlightthickness=0,
                command=lambda i=i: self.on_click(i)
            )(
                self.root,
                text="",
                font=("Arial", 32),
                width=5,
                height=2,
                command=lambda i=i: self.on_click(i)
            )
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def on_click(self, index):
        if self.board[index] != " " or (self.vs_computer and self.current_player == "O"):
            return

        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

        if self.check_winner(self.current_player):
            messagebox.showinfo("Game Over", f"Player {self.current_player} WINS!")
            self.disable_board()
            return

        if " " not in self.board:
            messagebox.showinfo("Game Over", "It's a DRAW!")
            return

        self.current_player = "O" if self.current_player == "X" else "X"

        if self.vs_computer and self.current_player == "O":
            self.root.after(300, self.computer_move)

    def computer_move(self):
        move = self.best_move()
        if move is None:
            return

        self.board[move] = "O"
        self.buttons[move].config(text="O")

        if self.check_winner("O"):
            messagebox.showinfo("Game Over", "Computer WINS!")
            self.disable_board()
            return

        if " " not in self.board:
            messagebox.showinfo("Game Over", "It's a DRAW!")
            return

        self.current_player = "X"

    def best_move(self):
        # win
        for i in range(9):
            if self.board[i] == " ":
                temp = self.board[:]
                temp[i] = "O"
                if self.check_winner("O", temp):
                    return i
        # block
        for i in range(9):
            if self.board[i] == " ":
                temp = self.board[:]
                temp[i] = "X"
                if self.check_winner("X", temp):
                    return i
        # center
        if self.board[4] == " ": return 4
        # corners
        for c in [0,2,6,8]:
            if self.board[c] == " ": return c
        # sides
        for s in [1,3,5,7]:
            if self.board[s] == " ": return s
        return None

    def check_winner(self, player, board_override=None):
        board = board_override if board_override else self.board
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        return any(board[a] == board[b] == board[c] == player for a, b, c in wins)

    def highlight_win(self, a, b, c):
        for i in [a, b, c]:
            self.buttons[i].config(bg="#43b581", fg="black")

    def disable_board(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for btn in self.buttons:
            btn.config(text="", state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root, vs_computer=True)
    root.mainloop()()

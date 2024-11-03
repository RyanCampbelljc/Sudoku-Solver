import tkinter as tk
from frames.Board import Board
#inherit from tk
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Suduko Solver")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.board_frame = Board(self)
        self.board_frame.grid(row=0, column=0, padx=15, pady=15)

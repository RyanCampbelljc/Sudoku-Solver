import tkinter as tk
import json
from frames.Board import Board
#inherit from tk

file = open("Input.json")
data = json.load(file)
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Suduko Solver")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.board_frame = Board(self, data['board1'])
        self.board_frame.grid(row=0, column=0, padx=15, pady=15,sticky='nsew')

        self.entry_btn = tk.Button(self, text="Start")
        self.entry_btn.grid(row=1, column=0)

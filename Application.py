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

        self.entry_btn = tk.Button(self, text="Start", command=self.solveBoard)
        self.entry_btn.grid(row=1, column=0)

        self.sections_btn = tk.Button(self, text="check sections", command=self.board_frame.areSubsectionValid)
        self.sections_btn.grid(row=2, column=0)

    def solveBoard(self):
        self.board_frame.disableBoard()
        self.board_frame.solveBoard()
        self.entry_btn.config(state="disabled")
import tkinter as tk
from widgets.Tile import Tile
class Board(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, highlightbackground="black", highlightthickness=5)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        #wtf is this syntax
        self.tiles = [[Tile(self,[0 if i==0 else 5,0 if i==8 else 5],[0 if j==0 else 5,0 if j==8 else 5]) for i in range(9)] for j in range(9)]
        self.create_widgets()
    
    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                self.tiles[i][j].grid(row=i, column=j)
                
import tkinter as tk
from widgets.Tile import Tile
class Board(tk.Frame):
    def __init__(self, parent,boardData):
        super().__init__(parent, highlightbackground="black", highlightthickness=5, highlightcolor="black",bg="black")
        #3x3 subsections of a suduko board
        #j = row of board; i = col of board; x = row of subsection; y = col of subsection
        self.sections = [[BoardSubsection(self,[[ boardData[x + 3*j][y + 3*i] for y in range(3)] for x in range (3)]) for i in range(3)] for j in range(3)]
        self.create_widgets()
 
    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                self.sections[i][j].grid(row=i, column=j,padx=5,pady=5, sticky="nsew")
           

#one of the 3x3 subsections of the suduko board.
class BoardSubsection(tk.Frame):
    def __init__(self,parent, dataList):
        super().__init__(parent)
        self.tiles = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.tiles[i][j] = Tile(self,dataList[i][j],1,1)
                self.tiles[i][j].grid(row=i, column=j,sticky="nsew")


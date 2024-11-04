import tkinter as tk
from widgets.Tile import Tile
class Board(tk.Frame):
    def __init__(self, parent,boardData):
        super().__init__(parent, highlightbackground="black", highlightthickness=5, highlightcolor="black",bg="black")
        #3x3 subsections of a suduko board
        #j = row of board; i = col of board; x = row of subsection; y = col of subsection
        self.sections = [[BoardSubsection(self,[[ boardData[x + 3*j][y + 3*i] for y in range(3)] for x in range (3)]) for i in range(3)] for j in range(3)]
        #want the tiles held in normal 2d array as well to make row/col checks easier
        #3x3 array of subsections each with 3x3 array of tiles
        # print(self.sections[0][0].tiles[0][0].data)
        self.tiles = [[self.sections[int(i/3)][int(j/3)].tiles[i%3][j%3] for j in range(9)]for i in range(9)]
        for i in range(9):
            print("")
            for j in range(9):
                print(self.tiles[i][j].data, end="")
        self.create_widgets()
 
    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                self.sections[i][j].grid(row=i, column=j,padx=5,pady=5, sticky="nsew")
    
    def solveBoard(self):
        print("test")
    
    def disableBoard(self):
        for r in self.sections:
            for c in r:
                c.disableSubsection()
    
    def enableBoard(self):
        for r in self.sections:
            for c in r:
                c.enableSubsection()
    
    def areSubsectionValid(self):
        for r in self.sections:
            for section in r:
                print(section.subsectionValid())
    
    def isRowValid(self,row):
        numList = []
        for tile in self.tiles[row]:
            if tile.data == '':
                continue
            if numList.count(tile.data) > 0:
                return False
            else:
                numList.append(tile.data) 
        return True
    
    def isColumnValid(self,column):
        numList = []
        for row in range(9):
            data = self.tiles[row][column]
            if data == '':
                continue
            if numList.count(data) > 0:
                return False
            else:
                numList.append(data) 
        return True

           

#one of the 3x3 subsections of the suduko board.
#makes it easy to place them in gui to easy to check validity
class BoardSubsection(tk.Frame):
    def __init__(self,parent, dataList):
        super().__init__(parent,bg="#58666e",)
        self.tiles = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.tiles[i][j] = Tile(self,dataList[i][j],2,2)
                self.tiles[i][j].grid(row=i, column=j,sticky="nsew")
        
    def disableSubsection(self):
        for r in self.tiles:
            for c in r:
                c.disableTile()
    def enableSubsection(self):
        for r in self.sections:
            for c in r:
                c.enableTile()
    def subsectionValid(self) -> bool:
        numList = []
        for r in self.tiles:
            for tile in r:
                if tile.data == '':
                    continue
                if numList.count(tile.data) > 0:
                    return False
                else:
                    numList.append(tile.data) 
        return True

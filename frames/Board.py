import tkinter as tk
import time
from widgets.Tile import Tile

#increments r,c to the next board position.
#or out of bounds if necessary
def incrementRowsAndColumns(r,c):
        if c < 8:
            c = c + 1
            return r, c
        else:
            c = 0
            r = r + 1
            return r,c
#decrements r,c to the next board position.
#or out of bounds if necessary
def decrementRowsAndColumns(r,c):
        if c > 0:
            c = c - 1
            return r, c
        else:
            c = 8
            r = r - 1
            return r,c

class Board(tk.Frame):
    def __init__(self, parent,boardData):
        super().__init__(parent, highlightbackground="black", highlightthickness=5, highlightcolor="black",bg="black")
        #3x3 subsections of a suduko board
        #j = row of board; i = col of board; x = row of subsection; y = col of subsection
        self.sections = [[BoardSubsection(self,[[ boardData[x + 3*j][y + 3*i] for y in range(3)] for x in range (3)]) for i in range(3)] for j in range(3)]
        #want the tiles held in normal 2d array as well to make row/col checks easier
        self.tiles = [[self.sections[int(i/3)][int(j/3)].tiles[i%3][j%3] for j in range(9)]for i in range(9)]
        self.debugValue = 0
        self.create_widgets()
 
    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                self.sections[i][j].grid(row=i, column=j,padx=5,pady=5, sticky="nsew")
   
    #if tile not locked place next lowest number in it.
    #check if row, col, and subsection is valid.
    #if yes move to next tile
    # if no try updating prior tile.
    def solveBoard(self):
        #finds the first tile that isnt locked
        r, c = 0,0
        done = False
        for i in range(9):
            if done:
                break
            for j in range(9):
                if not self.tiles[i][j].locked:
                    r = i
                    c = j
                    done = True
                    break
        direction = 1
        self.recurse(r,c,direction)


    def recurse(self, r, c, direction):
        #base case is index out of ranges
        if r >= 9 or r < 0:
            return False
        #if a tile is locked then move forward or backward depending on algs current direction
        reset = True
        while(reset):
            if not self.tiles[r][c].locked:
                direction = -1 #assume go back unless you find a valid way to move forward
                for i in range (9):# the possible numbers a tile could have
                    self.tiles[r][c].increment()
                    if self.isRowValid(r) and self.isColumnValid(c) and self.areSubsectionsValid():
                        if self.tiles[r][c].data != 0: # 0 can be acceptable value if backtracking and work up until its back to 0 but shouldnt move forward still
                            direction = 1
                        break
                    if i == 8:#need to reset value to 0 here(no value was possible)
                        self.tiles[r][c].increment()
                # self.printBoard() #only print board if something change(ie not on locked tile)
                self.updateUI()

            #decrement = go to last recursion
            
            #return true so that the while loop runs again for prior tile
            if direction == -1:
                return True
            
            r,c = incrementRowsAndColumns(r,c) 
            reset = self.recurse(r,c,direction)
            if reset:
                r,c = decrementRowsAndColumns(r,c)#need r,c to be the i,j of this tile. (they wouldnt be since they were incremented before getting here)
                direction = -1#assume backwords
        
        return False

    
    def disableBoard(self):
        for r in self.sections:
            for c in r:
                c.disableSubsection()
    
    def enableBoard(self):
        for r in self.sections:
            for c in r:
                c.enableSubsection()
    
    def areSubsectionsValid(self):
        for r in self.sections:
            for section in r:
                if not section.subsectionValid():
                    # print("invalid subsection")
                    return False
            # print("valid subsection")
        return True
    
    def printBoard(self):
        print()
        for row in self.tiles:
            print()
            for tile in row:
                output = '-' if tile.data == 0 else tile.data
                print(output,end = " ")
  
    def isRowValid(self,row):
        numList = []
        for tile in self.tiles[row]:
            data = tile.data
            if data == 0:
                continue
            if numList.count(data) > 0:
                return False
            else:
                numList.append(data) 
        return True
    
    def isColumnValid(self,column):
        numList = []
        for row in range(9):
            data = self.tiles[row][column].data
            if data == 0:
                continue
            if numList.count(data) > 0:
                return False
            else:
                numList.append(data) 
        return True

    def isBoardValid(self):
        for i in range(9):
            if not self.isColumnValid(i) or not self.isRowValid(i):
                return False
        if not self.areSubsectionsValid():
            return False
        return True

    def updateUI(self):
        self.update_idletasks()#refreshes ui
        if self.debugValue == 1:
            self.after(300)

    def updateDebugValue(self, value):
        self.debugValue = value  
        self.update() # refreshes ui and also processes user input
    
    def resetBoard(self):
        for r in self.tiles:
            for tile in r:
                tile.resetTile()
    
    def clearBoard(self):
        for r in self.tiles:
            for tile in r:
                tile.clearTile()

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
        for r in self.tiles:
            for c in r:
                c.enableTile()
    def subsectionValid(self) -> bool:
        numList = []
        for r in self.tiles:
            for tile in r:
                if tile.data == 0:
                    continue
                if numList.count(tile.data) > 0:
                    return False
                else:
                    numList.append(tile.data) 
        return True

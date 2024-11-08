import tkinter as tk
from tkinter import ttk
import json
from frames.Board import Board
import threading 
#inherit from tk

file = open("Input.json")
data = json.load(file)
keys = list(data.keys())
buttonWidth = 6
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)

        #dropdown
        self.boardOption = tk.StringVar()
        
        #create the board
        self.changeBoard((keys[0]))
        self.boardMenuDropdown = ttk.OptionMenu(self, self.boardOption, keys[0], *keys, command=self.changeBoard)
        self.boardMenuDropdown.grid(row=0, column=1)
        self.boardOption.set(keys[0])

        
        buttonPaddingX = 3
        buttonPaddingY = 15
        #3 buttons
        self.entryBtn = ttk.Button(self, text="Start", command=self.startSolveBoardThread, width=buttonWidth)
        self.entryBtn.grid(row=2, column=0, padx=buttonPaddingX, pady=buttonPaddingY)
        self.resetBoardBtn = ttk.Button(self, text="Reset", command=self.resetBoard, width=buttonWidth)
        self.resetBoardBtn.grid(row=2, column=1, padx=buttonPaddingX, pady=buttonPaddingY)
        self.clearBoardBtn = ttk.Button(self, text="Clear", command=self.clearBoard, width=buttonWidth)
        self.clearBoardBtn.grid(row=2, column=2, padx=buttonPaddingX, pady=buttonPaddingY)
        #debug radio check
        self.checkValue = tk.IntVar()
        self.debugBtn = ttk.Checkbutton(self, text='debug', onvalue=1, offvalue=0, variable=self.checkValue, command=self.updateDebugValue)
        self.debugBtn.grid(row=3, column=1, padx=15, pady=15)
        #information label if a board is invalid or unsolveable
        self.informationLabel = tk.StringVar()
        self.label = ttk.Label(self,textvariable=self.informationLabel)
        self.label.grid(row=5, column=1, columnspan=1)
        #export button
        self.exportBtn = ttk.Button(self, text="Export", command=self.export, width=buttonWidth)
        self.exportBtn.grid(row=4, column=1)
 

        

    def updateDebugValue(self):
        self.boardFrame.updateDebugValue(self.checkValue.get())
    
    #due to the waits to make the ui slow down for debug mode
    #the window becomes unresponsive unless this is done on another thread
    

    def startSolveBoardThread(self):
        self.entryBtn.config(state="disabled")
        thread = threading.Thread(target=self.solveBoard)
        thread.start()
        
    def solveBoard(self):
        if not self.boardFrame.isBoardValid():
            self.informationLabel.set("invalidBoard")
            return
        self.informationLabel.set("")
        self.entryBtn.config(state="disabled")
        self.resetBoardBtn.config(state="disabled")
        self.clearBoardBtn.config(state="disabled")
        self.boardFrame.disableBoard()
        self.boardFrame.solveBoard()
        self.resetBoardBtn.config(state="normal")
        self.clearBoardBtn.config(state="normal")
        self.boardFrame.enableBoard()
    
    def resetBoard(self):
        self.boardFrame.resetBoard()
        self.entryBtn.config(state="normal")
    
    def clearBoard(self):
        self.boardFrame.clearBoard()
        self.entryBtn.config(state="normal")

    def changeBoard(self, boardName):
        self.boardFrame = Board(self, data[boardName])
        self.boardFrame.grid(row=1, column=0, padx=15, pady=15, columnspan=3)
    
    # nothing shows yet on the popup window
    def export(self):
        popup = tk.Toplevel(self)
        popup.rowconfigure(0, weight=1)
        # popup.columnconfigure(0,weight=1)
        popup.title("Export Window")
        popup.geometry("300x150")
        popup.grab_set()

        label = ttk.Label(popup, text="Name of board")
        label.grid(row=0,col=0)

        saveBtn = ttk.Button(popup, text="Save", command=self.test, width=buttonWidth)

    def test(self):
        c=1
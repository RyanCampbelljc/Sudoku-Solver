import tkinter as tk
import json
from frames.Board import Board
import threading 
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
        self.board_frame.grid(row=0, column=0, padx=15, pady=15, columnspan=3)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)

        buttonWidth = 5
        buttonPaddingX = 3
        buttonPaddingY = 15
        self.entry_btn = tk.Button(self, text="Start", command=self.startSolveBoardThread, width=buttonWidth)
        self.entry_btn.grid(row=1, column=0, padx=buttonPaddingX, pady=buttonPaddingY)

        self.resetBoard_btn = tk.Button(self, text="Reset", command=self.resetBoard, width=buttonWidth)
        self.resetBoard_btn.grid(row=1, column=1, padx=buttonPaddingX, pady=buttonPaddingY)

        self.clearBoard_btn = tk.Button(self, text="Clear", command=self.clearBoard, width=buttonWidth)
        self.clearBoard_btn.grid(row=1, column=2, padx=buttonPaddingX, pady=buttonPaddingY)


        self.checkValue = tk.IntVar()
        self.debug_btn = tk.Checkbutton(self, text='debug', onvalue=1, offvalue=0, variable=self.checkValue, command=self.updateDebugValue)
        self.debug_btn.grid(row=2, column=1, padx=15, pady=15)

        self.informationLabel = tk.StringVar()
        self.label = tk.Label(self,textvariable=self.informationLabel)
        self.label.grid(row=3, column=1, columnspan=1)
 

        # self.sections_btn = tk.Button(self, text="check rows", command=self.board_frame.areRowsValid)
        # self.sections_btn.grid(row=3, column=0)

        # self.sections_btn = tk.Button(self, text="check columns", command=self.board_frame.areColumnsValid)
        # self.sections_btn.grid(row=4, column=0)

    def updateDebugValue(self):
        self.board_frame.updateDebugValue(self.checkValue.get())
    
    #due to the waits to make the ui slow down for debug mode
    #the window becomes unresponsive unless this is done on another thread
    

    def startSolveBoardThread(self):
        self.entry_btn.config(state="disabled")
        thread = threading.Thread(target=self.solveBoard)
        thread.start()
        
    def solveBoard(self):
        if not self.board_frame.isBoardValid():
            self.informationLabel.set("invalidBoard")
            return
        self.informationLabel.set("")
        self.entry_btn.config(state="disabled")
        self.resetBoard_btn.config(state="disabled")
        self.clearBoard_btn.config(state="disabled")
        self.board_frame.disableBoard()
        self.board_frame.solveBoard()
        self.resetBoard_btn.config(state="normal")
        self.clearBoard_btn.config(state="normal")
        self.board_frame.enableBoard()
    
    def resetBoard(self):
        self.board_frame.resetBoard()
        self.entry_btn.config(state="normal")
    
    def clearBoard(self):
        self.board_frame.clearBoard()
        self.entry_btn.config(state="normal")
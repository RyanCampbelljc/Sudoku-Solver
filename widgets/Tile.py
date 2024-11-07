import tkinter as tk
class Tile(tk.Entry):
    def __init__(self,parent,data, padx, pady):
        super().__init__(parent, width = 3, font=("Helvetica", 18), insertwidth=2, justify="center", bd=0)
        if data >= '1' and data <= '9':
            self.data = (int)(data)
            self.locked = True #locked is so the board knows this one cannot change(was input prior to being solved)
        else:
            self.data = 0
            self.locked = False
        self.config(disabledforeground="black")
        self.grid(row=0,column=0, padx=padx, pady=pady,sticky="nsew")
        self.solvingStarted = False
        self.updateTextField()
        self.bind("<KeyRelease>", self.userChangedValue)
        

    #increments the tiles value to the next one
    def increment(self):
        self.data = self.data + 1 if self.data < 9 else 0
        self.updateTextField()

    #updates the text field of this tile based on self.data
    def updateTextField(self):
        output = '' if self.data == 0 else (str)(self.data)
        if self.solvingStarted:
            self.enableTile()
            self.config(fg="blue")
        super().delete(0, tk.END)
        super().insert(0, (str)(output))
        if self.solvingStarted:
            self.disableTile()
        

    def userChangedValue(self, event=None):
        if not self.solvingStarted:
            print("called")
            text = super().get()
            lastChar = '' if text == '' else text[-1]
            if lastChar >= '1' and lastChar <= '9':
                self.data = (int)(lastChar)
            if lastChar == '':
                self.data = 0
            self.updateTextField()
            
        

    def disableTile(self):
        self.config(state='readonly')
        self.solvingStarted = True
    
    def enableTile(self):
        self.config(state='normal')
        self.solvingStarted = False

    def resetTile(self):
        if not self.locked:
            self.data = 0
            self.updateTextField()
    
    def clearTile(self):
        self.locked = False
        self.data = 0
        self.updateTextField()
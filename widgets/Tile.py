import tkinter as tk

class Tile(tk.Entry):
    def __init__(self,parent,data, padx, pady):
        super().__init__(parent, width = 3, font=("Helvetica", 18), insertwidth=2, justify="center", bd=0)
        if data >= '0' and data <= '9':
            self.data = data
        else:
             self.data = ''
        self.config(disabledforeground="black")
        self.grid(row=0,column=0, padx=padx, pady=pady,sticky="nsew")

        self.entryInput = tk.StringVar()
        self.config(textvariable=self.entryInput)
        self.entryInput.trace_add("write", self.changeValue)
        self.insert(0,self.data)

    
    def changeValue(self, *args):
        text = super().get()
        data = '' if text == '' or (not text.isdigit()) else text[-1]
        super().delete(0, tk.END)
        super().insert(0, data)
        self.data = data

    def disableTile(self):
        self.config(state='disabled')
    
    def enableTile(self):
        self.config(state='enabled')

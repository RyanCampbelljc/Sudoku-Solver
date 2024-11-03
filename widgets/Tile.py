import tkinter as tk

class Tile(tk.Entry):
    def __init__(self,parent, padx, pady):
        super().__init__(parent, width = 3, font=("Helvetica", 18), insertwidth=2, justify="center")
        self.data = "x"
        self.insert(0,self.data)
        self.grid(row=0,column=0, padx=padx, pady=pady)
    def changeValue(self):
        text = super().get()
        last_char = text[text.__len__-1]
        super().delete(0, tk.END)
        super().insert(0, last_char)


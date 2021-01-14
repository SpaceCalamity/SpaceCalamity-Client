import tkinter as tk
from ttkthemes import ThemedTk

class consoleinput():
    def __init__(self, text):
        self.root = ThemedTk(theme="Equilux") 
        self.root.geometry("500x500")
        self.root.title("Space Calamity")
        self.label_file_name = tk.Label(self.root, text=text)
        self.label_file_name.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.entry.focus()
        self.root.mainloop()

    def getinput(self, value):
        self.get = value
        self.root.destroy()
        

myapp = consoleinput(text="Textinput") 

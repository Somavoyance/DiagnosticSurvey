from tkinter import *
import tkinter as tk

class App(tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        
app = App()
app.mainloop()
        
        
        

# window = tk.Tk()
# window.title("Endometriosis GUI")
# window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(), window.winfo_screenheight()))
# 
# window.mainloop()
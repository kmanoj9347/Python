# Bound Method 

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self.master, text="Click me", command=self.button_click)
        self.button.pack()

    def button_click(self):
        print("Button clicked!")

root = tk.Tk()
root.geometry('300x300')
app = Application(master=root)
app.mainloop()






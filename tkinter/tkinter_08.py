# use of a lambda function as a callback
from tkinter import *
import tkinter as tk
root =tk.Tk()
root.geometry('400x400')
button = tk.Button(root,text="Click me",command=lambda :print("Button clicked..",))
button.pack(side =BOTTOM)
root.mainloop()

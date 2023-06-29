# callback function for a button click event

import tkinter as tk
def button_click():
    print("Button clicked")
root =tk.Tk() 
root.geometry('500x400')
root.title("Button..")

button = tk.Button(root,text ="Click me",command = button_click)
button.pack()

root.mainloop()
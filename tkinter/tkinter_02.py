# Creating button using tkinter.
#importing everthing from tkinter module
from tkinter import *
from tkinter.ttk import *

#creating a tkinter window
root = Tk()

#open window having dimension 200x200
root.geometry('200x200')

#creating a Button
button =Button(root,text='Click me !',bg= 'blue',fg='black',bd='5',command=root.destroy)

#set the position of button on the top of window
button.pack(side='top')

root.mainloop()
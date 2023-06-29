# Menu widget in tkinter

from tkinter import *
from tkinter.ttk import *
from time import strftime

#Creating tkinter window
root = Tk()
root.title('MENU')

#Creating menubar
menubar = Menu(root)

#Adding File menu and commands
file =Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'File',menu = file)
file.add_command(label ='New File',command=None)
file.add_command(label = 'open...',command =None)
file.add_command(label = 'Save',command =None)
file.add_separator()
file.add_command(label = 'Exit',command=root.destroy)

#Adding Edit Menu and commands
edit = Menu(menubar,tearoff = 0)
menubar.add_cascade(label ='Edit',menu=edit)
edit.add_command(label='Cut',command =None)
edit.add_command(label='Copy',command=None)
edit.add_command(label='Paste',command=None)
edit.add_command(label = 'Select All',command=None)
edit.add_separator()
edit.add_command(label='Find...',command=None)
edit.add_command(label='Find again',command=None)

#Adding Help Menu
help = Menu(menubar,tearoff =0)
menubar.add_cascade(label = 'Help',menu = help)
help.add_command(label= 'Tk Help',command = None)
help.add_command(label='Demo',command=None)
help.add_separator()
help.add_command(label='About Tk',command =None)

#display menu
root.config(menu=menubar)
mainloop()
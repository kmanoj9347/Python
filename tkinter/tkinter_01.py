# importing tkinter module

from tkinter import *
# main window
root =Tk()
# width x height of the window
root.geometry('300x500')
#giving title to the main window
root.title("First_Program")
#Label will show output on the window
label =Label(root,text="Hello World")
label.pack()
#main loop tells that application is ready to run
#and it tells the code to keep displaying
root.mainloop()
# Radio Button
# Import Tkinter module
from tkinter import *
from tkinter.ttk import *

#Creating mastere Tkinter window
master = Tk()
master.geometry("180x180")

#tkinter sring varaible able to store 
# any string value
v= StringVar(master,"1")

# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1",
          "RadioButton 2" : "2",
          "RadioButton 3" : "3",
          "RadioButton 4" : "4",
          "RadioButton 5" : "5"}

#Loop is used to create multiple RadioButtons
#rather than creating each button separately
for (text,value) in values.items():
    Radiobutton(master,text= text,variable=v,
                value=value).pack(side=TOP,ipady=5)
mainloop()

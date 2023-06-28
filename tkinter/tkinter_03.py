# Label widget
from tkinter import *

top =Tk()
top.geometry("450x300")

#the label for username
username = Label(top,text="Username").place(x=40,y=60)
# the label for userpassword.
userpassword=Label(top,text="Password").place(x=40,y=100)
submit_button= Button(top,text='Submit').place(x=40,y=130)
#username_inputarea = Entry(top,width=30).place(x=110,y=60)
#userpassword_inputarea = Entry(top,width=30).place(x=110,y=100)
top.mainloop()
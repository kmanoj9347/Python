# Check Button

from tkinter import *
root =Tk()
root.geometry("300x200")
w = Label(root, text ='College',font ="50")
w.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

Button1 = Checkbutton(root,text = "Pvkk",
                       variable = Checkbutton1,
                       onvalue = 1,
                       offvalue = 0,
                       height = 2,
                       width = 10)
Button2 = Checkbutton(root,text="Srit",
                       variable=Checkbutton2,
                       onvalue = 1,
                       offvalue = 0,
                       height = 2,
                       width = 10)
Button3 = Checkbutton(root,text = "Trinity",
                       variable = Checkbutton3,
                       onvalue = 1,
                       offvalue = 0,
                       height = 2,
                       width = 10)
Button4 = Button(root,text= "Submit",bg= 'blue',command=root.destroy)
Button1.pack()
Button2.pack()
Button3.pack()  
Button4.pack()

mainloop()
                



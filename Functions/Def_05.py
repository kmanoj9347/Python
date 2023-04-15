#Accessing of varaibles of nested functions

def f1():
    s ='Learning a Python language'

    def f2():
        print(s)
    f2()
f1()

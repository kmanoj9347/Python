def exp(a,b):
    try:
        c =((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
exp(2,3)
exp(3,3)
exp(6,6)

#Pass by Reference or pass by value

def myFun(x):
    x[0] = 20
list = [10,11,12,13,14,15]
myFun(list)
print(list)
def myFun(arg1,**kwargs):
    for key,value in kwargs.items():
        print("%s = %s "%(key,value))

myFun("Hi",first='Iam',last='Manoj')
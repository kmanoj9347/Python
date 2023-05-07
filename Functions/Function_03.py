def myFun(**kwargs):
    for key ,value in kwargs.items():
        print("%s =%s"%(key,value))

myFun(first='K',mid='Manoj',last ='kumar')

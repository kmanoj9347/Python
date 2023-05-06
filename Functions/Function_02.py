def myFun(arg1,*argv):
    print("First argument: ",arg1)
    for arg in argv:
        print("next argument through *argv : ",argv)

myFun('Hello','Welcome','to','Coding')

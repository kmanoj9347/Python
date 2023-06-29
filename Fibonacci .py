while True:
    print("Menu Driven Program")
    print("1.Fibonacci Series using for consruct")
    print("2.Fibonacci Series using While Construct")
    print("3.Fibonacci Series using Do-While Construct")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        f1=0
        f2=1
        print("Fibonacci Sequence using for loop")
        num=int(input("Enter length of series :"))
        print("{}\n{}".format(f1,f2))
        for val in range(num-2):
            f3=f1+f2
            print(f3)
            f1=f2
            f2=f3
    elif choice==2:
        f1 =0
        f2=1
        print("Fibonacci Sequence using while loop")
        num = int(input("Enter length of series:"))
        print("{}\n{}".format(f1,f2))
        i=0
        while i<num-2:
            f3=f1+f2
            print(f3)
            f1=f2
            f2=f3
            i=i+1
    elif choice == 3:
        print("Fibonacci Sequence emulating do-while")
        num=int(input("Enter length of series : "))
        first =0
        second =1
        print("{}\n{}".format(first,second))
        i=0
        while(True):
            third=first+second
            print(third)
            first=second
            second=third
            i+=1
            if(i>=num-2):
                break
    elif choice==4:
        break
    else:
        print("please enter the correct choice")
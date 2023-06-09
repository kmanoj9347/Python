# Fibonacci sequence of numbers using do-while loop constructs.
print("Fibonacci Sequence emulating do-while")
num = int(input("Enter length of series : "))
first =0
second =1
print("{}\n{}".format(first,second))
i=0
while(True):
    third = first+second
    print(third)
    first = second
    second = third
    i+=1
    if(i>= num-2):
        break

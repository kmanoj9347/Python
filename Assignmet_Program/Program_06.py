# Tp display Fibonacci sequence of numbers using while loop constructs.

f1 = 0
f2 = 1
print("Fibonacci Sequence")
num = int(input("Enter length of series : "))
print("Fibonacci Sequence using while loop")
print("{}\n{}".format(f1,f2))
i=0
while i <num-2:
    f3 = f1+f2
    print(f3)
    f1=f2
    f2=f3
    i+=1
# Fibonacci sequence of numbers using for loop constructs.

f1=0
f2=1
print("Fibonacci Sequence using for loop ")
num =int(input("Enter length of series : "))
print("{}\n{}".format(f1,f2))
for val in range(num-2):
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3

#Write a python script to calculate the factorial of a given number.
num =int(input("Enter a number :"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of",num,"is",fact)
retrun 
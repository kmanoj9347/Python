#Program to check if a number is prime or not.
num =29
# To take input from the user
num =int(input("Enter number:"))
# define a flag variable
flag =False
# prime numners are greater than 1
if num >1:
    for i in range(2,num):
        if(num % i)==0:
            flag = True
            break
if flag:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")
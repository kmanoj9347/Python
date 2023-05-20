#Logical Operators
#logical and operator
a = 15
b =15
c =-15
if a > 0 and b > 0:
    print("The numbers are greater than Zero")
if a >0 and b > 0 and c > 0:
    print("The numbers are greater than zero")
else:
    print("Atleast one number is not greater than zero")

#Logical or operator
if a > 0 or b > 0:
    print("Either of the number is greater than zero")
else:
    print("No number is greater than zero")
if b>0 or c>0:
    print("Either of the number is greater than zero")
else:
    print("No number is greater than zero")

#logical not operator
a =10
if not a:
    print('Boolean value of a is True')
if not (a%3 ==0 or a%5 ==0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 0r 5")


#swapping of two variables
print("Using Navie approach") 
x =10
y = 50

# swapping of two variables 
# using third varaible
temp = x
x = y
x = y 
y = temp 
print("value of x:",x)
print("Value of y:",y)

print("Using comma operator")
x = 5
y = 6
 # Swapping of two varaible  
 # without using third varable
x ,y = y, x
print("Value of x:",x)
print("Value of y:",y)

print("Using XOR")
x =10
y =20
 #swapping using xor
x = x ^ y
y = x ^ y
x = x ^ y
print("Value of x:",x)
print("Value of y:",y)

print("Using arithmetic operators")
x =2
y =3
#Swapping of two variable
#using arithmetic operations
x = x + y
y = x - y
x = x - y
print("Value of x:",x)
print("Value of y:",y)

print("Using multiplication and division operator")
x = 1
y = 4
#Swapping of two numbers
#using multiplication operator
x = x * y
y = x / y
x = x / y
print("Value of x : ", x)
print("Value of y : ", y) 

print("Using Bitwise addition and subtraction for swapping")
a = 5
b = 1
a = (a & b) + (a | b)
b = a + (~b) + 1
a = a + (~b) + 1
print("a after swapping: ", a)
print("b after swapping: ", b)
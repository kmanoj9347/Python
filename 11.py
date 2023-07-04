import math
def compute_gcd(x,y):
if(x>0 and y>0):
if x>y:
smaller = y
else:
smaller = x
for i in range(1,smaller+1):
if((x%i==0) and(y%i==0)):
gcd = i
return gcd
else:
gcd = math.gcd(x,y)
return -gcd
def gcd(a,b):
if(b==0):
return a
else:
return gcd(b,a%b)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The gcd of two numbers using non
recursive:",compute_gcd(num1,num2))
GCD=gcd(num1,num2)
print("The gcd of two numbers using recursive:",GCD)
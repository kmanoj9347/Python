# Python script to find the largest number among three numbers and 
# dispaly them in ascending order using if-else construct.

print("To find largest among three numbers and display in ascending order")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter Second number : "))
num3 = int(input("Enter third number : "))
if num1>num2 and num1>num3:
    print("Largest number is : ",num1)
elif num2>num3:
    print("Largest number is : ",num2)
else:
    print("Largest number is : ",num3)
lis=[num1,num2,num3]
lis.sort()
print("Ascending order is : ",lis)
#Palindrome number program using while loop.
num =int(input("Enter a value: "))
temp =num
rev =0
while(num > 0):
    dig =num % 10
    revrev = rev * 10+dig
    num=num //10
if(temp == rev):
    print("This value is a plaindrome number")
else:
    print("This value is not a palindrome number!!")



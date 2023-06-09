# To create a list and add n number of user-defined values to the
# list and display the same on to the console screen
li= []
n = int(input("Enter the size of list : "))
for val in range(n):
    ele = int(input("Enter the {} element : ".format(val)))
    li.append(ele)
print("The elements in the list are : ")
for val in li:
    print(val,end=' ')
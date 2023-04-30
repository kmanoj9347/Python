#importing an array for array creations
import array as arr
#Creating an array with integer type
a = arr.array('i',[1,2,3])
print("The new created array is : ",end=" ")
for i in range(0,3):
    print(a[i],end=" ")

#creating an array with double type
b = arr.array('d',[2.5,3.2,3.3])
print("\nThe new created array is : ",end=" ")
for i in range(0,3):
    print(b[i],end=" ")

#inserting array using insert() function
a.insert(1,4)
print("\nArray after insertion : ",end=" ")
for i in (a):
    print(i,end=" ")

#adding an elements using append()
b.append(4.4)
print("\nArray after insertion : ",end=" ")
for i in (b):
    print(i,end=" ")
print()
#accesssing eleemts of array
print("Access element is: ",a[0])
print("Access element is: ",a[3])
print('Access element is: ',b[1])
print("Access element is: ",b[2])
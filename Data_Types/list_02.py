#creating a list
list = []
print("Blank list: ")
print(list)
 
#creating a list of numbers
list = [10,20,30]
print("\nlist of numbers: ")
print(list)

#creating a list of strings and accessing
#using index
list = ["python","Programming","language"]
print("\nlist items: ")
print(list[0])
print(list[-1])

 #getting the size of list
print("\nsize of list: ")
print(len(list))


#Addition of elements in the list
list.append(1)
list.append(2)
list.append(3)
print("\nlist after Addition of three elements: ")
print(list)

#Adding elements to the list using Iterator
for i in range(4,6):
    list.append(i)
print("\nlist after Addition of elements from 4-6: ")
print(list)
 
#Addition of elements at specific Position
# (using Insert Method) 
list.insert(0,'hi')
list.insert(7,7)
print("\nlist after performing insert operation: ")
print(list)

#Addition of multiple elements to the list at the end
#(using Extend method)
list.extend([8,'live','life'])
print("\nlist After performing Extend operation: ")
print(list)

#Reversing a list
list.reverse()
print("\nReversed string")
print(list)


#Removing elemts from list 
#using Remove()  method
list.reverse()
list.remove(7)
list.remove('hi')
print("\nlist after Removal of two elements: ")
print(list)

# Removing elements from the list
#using the pop() method
list.pop(2)
print("\nlist after poping an elements: ")
print(list)

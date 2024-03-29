#Creating of set 
set1 = set()
print("Initial blank set: ")
print(set1)

#Creating a set with the use of a string
set1 =set("manojkumar")
print("\nSet with the use of String: ")
print(set1)

#set with the use of cnstruction 
#(Using object to store String)
String ='Manojkumar'
set1 = set(String)
print("\nSet with the use of an Object: ")
print(set1)

#Creating a set with the use of a List
set1 = set(["Python","Language","DATATYPE"])
print("\nSet with the use of List: ")
print(set1)

#Creating a set with a list of Numbers 
#(Having duplicate values)
set1 = set([1,2,4,4,3,3,3,6,5])
print("\nSet with the use of numbers: ")
print(set1)

#Creating a set with a mixed type of values
#(Having numbers and strings)
set1 = set([1,2,'python',4,'language',6,'datatype'])
print("\nSet with the use of Mixed Values")
print(set1)

#Another Method to create sets in python
my_set ={1,2,3} 
print(my_set)

#Adding element and tuple to the Set
set1.add(8)
set1.add(9)
set1.add((6,7))
print("\nSet after Addition of three elements: ")
print(set1)

#ADdition of elements to the set using updation function.
set1 = set([4,5,(6,7)])
set1.update([10,11])
print("\nSet after Addition of elements using update: ")
print(set1)

#Accessing of eleemts using for loop
print("\nElements of set: ")
for i in set1:
    print(i,end=" ")

#Deletion of elements in a set using Remove() method.
set1 = set([1,2,3,4,5,6,7,8,9,11,12,13,14,15])
print(set1)
set1.remove(3)
set1.remove(6)
print("\n Set after Removal of two elements: ")
print(set1)

#Removing elements from set using Discard() method
set1.discard(8)
set1.discard(11)
print("\nSet after Discarding two elements: ")
print(set1)

#Using the pop() method.
set1.pop()
print("\nSet after popping an elements: ")
print(set1)

#Remving all the elements from set using clear() method.
set1.clear()
print("\nSet after clearing all the elements: ")
print(set1)

#Creating an empty tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

 #Creating a tuple with the use of Strings
Tuple1 = ('Ravi','For')
print("\nTuple with the use of String: ")
print(Tuple1)
 #Creating a Tuple with 
 # the use of list
list1 = [1,2,4,5,6]
print(tuple(list1))
 
#Creating a Tuple with the use of built-in function
Tuple1 = tuple('Raja')
print("\nTuple with the use of function: ")
print(Tuple1)

#Creating a Tuple with nested tuple
Tuple1 = (0,1,2,3)
Tuple2 = ('python','Language')
Tuple3 = (Tuple1,Tuple2)
print("\nTuplewith nested tuples: ")
print(Tuple3)
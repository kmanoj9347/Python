#Creating an empty tuple
tuple1 = ()
print("Intial empty tuple: ")
print(tuple1)

#Creating a tuple with the use of string
tuple1 = ('python','language')
print("\ntuple with the the use of string: ")
print(tuple1)

#use of list
list = [1,2,3,4,5]
print("\ntuple using list type: ")
print(tuple(list))

#use of loop
tuple1 = ('Manoj')
n =5 
for i in range(int(n)):
    tuple1 = (tuple1,)
    print(tuple1)

#Accesing of tuple with indexing.
print("\nFisrt element of tuple: ")
print(tuple1[0])
tuple1= ('python','data', 'type','tuple')
#unpack values of tuple1.
a,b,c,d= tuple1
print("\n Values after unpacking: ")
print(a)
print(b)
print(c)

#slicing of a tuple with numbers
tuple1 = tuple('manojkumar')
print("Removal of First Elements: ")
print(tuple[1:])

print("\ntuple after sequence of elements is reversed: ")
print(tuple1[::-1])

print("\nprinting elements between Range 4-9: ")
print(tuple1[4:9])

#Deleting a tuple
tuple1 = (0,1,2,3,4,5)
del tuple1
print(tuple1)
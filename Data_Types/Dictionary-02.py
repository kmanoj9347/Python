#Creating a Dictionary with Integer keys
Dict = {1:'one',2:'two',3:'three'}
print("\nDictionary with the use of Integer keys: ")
print(Dict)

#Creating a Dictionary with Mixed keys
Dict = {'Name':'Manoj',1:[1,2,3,4]}
print("\nDictinary with the use of Mixed keys: ")
print(Dict)

#Adding elements 
Dict[0] ='Zero'
Dict[4]='Four'
Dict[1]= 'Numbers'
Dict['Value_set']='a','b','c'
print("\nDictionary after adding elements: ")
print(Dict)

#Accessing a element using key.
print("Accessing a elements using key: ")
print(Dict['Name'])
print(Dict[1])

#Accessing a elements using get() method
print("Accessing a elements using get: ")
print(Dict.get(4))

#Deleting of the Dictionary data.
del(Dict[1])
del(Dict['Name'])
print("Data after deletion Dictioonary:")
print(Dict)


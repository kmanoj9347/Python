#Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
 
#Creating a Dictionary with Interger keys
Dict = {1:'Ravi',2:'Ram',3:'Raju'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
print(Dict[2])
print(Dict[3])
 
 #Creating a Dictionary with Mixed Keys
Dict = {'Name': 'Manoj',1:[1,2,3,4]}
print("\nDictionary with the use of mixed keys: ")
print(Dict)

#Creating a Dictionary with dict() method 
Dict = dict({1: 'Ravi',2 :'Raju',3:'Ramu'})
print("\nDictionary with the use of dict(): ")
print(Dict)

#Creating a Dictionary with each item as a pair
Dict = dict([(1, 'Manoj'),(2,'Kumar')])
print("\nDictionary with each item as a pair: ")
print(Dict)
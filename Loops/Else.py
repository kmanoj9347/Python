#for Loop
# Iterating over a list
print("List Itertion")
l =["Ravi","Manoj","Sohel"]
for i in l:
    print(i)

#Iterating over a tuple
print("\nTuple Iteration")
t = ("Ram","Shiv","Krish")
for i in t:
    print(i)

#Iterating over a String
print("\nString Iteration")
s ="Manoj"
for i in s:
    print(i)

#Iterating over dictionary
print("\nDictionary Iteration")
d =dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" %(i,d[i]))

#Iterating over a set
print("\nSet Iteration")
set1 = {1,2,3,4,5,6,7,8}
for i in set1:
    print(i)
# clearing a list  using clear and Reinitializing.

#Initializing lists
list1 =[1,2,3]
list2 =[4,5,6]
print("list1 before deleting is : "+str(list1))

#deleting list using clear()
list1.clear()
print("List1 after clearing using clear(): "+str(list1))
print("List2 before deleting is : "+str(list2))

#deleting list using reinitialization
list2 =[]
print("List2 after clearing using reinitialization : "+str(list2))

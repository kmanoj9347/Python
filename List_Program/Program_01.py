# To swap first and last element of a list
# Swap function
def swapList(newList):
    size =len(newList)

    #Swapping 
    temp =newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] =temp
    return newList
newList =[12,4,56,78,9]
print(swapList(newList))

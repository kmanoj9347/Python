# To swap elements at given positions using temp variable
# Swap function
def swapPositions(lis,pos1,pos2):
    temp=lis[pos1]
    lis[pos1]=lis[pos2]
    lis[pos2]=temp
    return lis
List =[23,14,67,83,55,89]
pos1,pos2=2,5
print(swapPositions(List,pos1-1,pos2-1))
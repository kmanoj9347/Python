from functools import reduce
def _sum(arr):
    #iterate over array using reduce 
    #and get sum on accumulator
    sum = reduce(lambda a,b:a+b,arr)
    return(sum)
arr =[]
arr =[12,3,4,15]
n =len(arr)
ans =_sum(arr)
print('Sum of the array is',ans)

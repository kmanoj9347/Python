#To find maximum in arr[] of size n
from functools import reduce
def largest(arr):
    #Sort the array
    ans = reduce(max,arr)
    return ans
arr = [10,345,67,34,6656,64,34,7]
n = len(arr)
print("largestin given array ",largest(arr))
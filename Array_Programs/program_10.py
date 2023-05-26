# To find remainder of array multiplication divided by n

#to use reduce function import reduce from functools
from functools import reduce
def find_remainder(arr,n):
    sum_1 = reduce(lambda x, y: x*y,arr)
    remainder = sum_1 % n
    print(remainder)
arr =[100,10,35,25,14,5]
n =11
find_remainder(arr,n)
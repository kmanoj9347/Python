import math
def find_remainder(arr,n):
    #Calculating the sum of logarothms of array elements
    # and storing them in the variable below
    log_sum =0
    for i in arr:
        log_sum +=math.log10(i)
    # Take exponential of the sum and retrun remainder
    remainder = int(pow(10,log_sum))%n
    return remainder
arr = [100,10,5,25,35,14]
ele =11
rem =find_remainder(arr,ele)
print(rem)
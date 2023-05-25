#To find maximum in arr[] of size n
#using built-in function max()
def largest(arr,n):
    ans = max(arr)
    return ans
if __name__=='__main__':
    arr = [10,12,45,68,34,5678]
    n=len(arr)
    print("Largest in given array is : ",largest(arr,n))
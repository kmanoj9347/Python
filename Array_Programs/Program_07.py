#To find maximum in arr[] of size n
#using sort() function
def largest(arr,n):
    #sort the array
    arr.sort()
    #The last elements of the array is 
    #the largest element
    return arr[n-1]
arr = [10,324,45,90,9808,5,67]
n= len(arr)
ans = largest(arr,n)
print("largest in given array",ans)
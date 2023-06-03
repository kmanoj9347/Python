#python program to find maximum 
#in arr[] of size n
def largest(arr,n):
    #initialize maximum elements
    max = arr[0]
    #Traverse array elements from second and
    #compare every elements with current max
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max 
arr =[10,325,35,67,84]
n =len(arr)
ans = largest(arr,n)
print("largest in given array is :",ans)
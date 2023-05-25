#python program to find maximum 
#in arr[] of size n
def largest(arr,n):
    max = arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max 
arr =[10,325,35,67,84]
n =len(arr)
ans = largest(arr,n)
print("largest in given array is :",ans)
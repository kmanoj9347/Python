def sum_of_array(arr,low,high):
    if low ==high:
        return arr[low]
    mid = (low+high)//2
    left_sum=sum_of_array(arr,low,mid)
    right_sum=sum_of_array(arr,mid+1,high)
    return left_sum+right_sum
arr =[1,2,3]
print("sum is ",sum_of_array(arr,0,len(arr)-1))
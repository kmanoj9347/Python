# To find sum of elements in given array
def _sum(arr):
    sum =0
    for i in arr:
        sum =sum+i
    return(sum)

#main function
if __name__ == "main__":
    #input values to list
    arr = [12,3,4,15]
    #calculating length of array
    n = len(arr)
    #calling function ans store the sum in ans
    ans = _sum(arr)
    #display sum
    print('Sum of the arrayi is ',ans)
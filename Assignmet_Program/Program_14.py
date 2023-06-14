# write a program to find a given element, if the element to be found and its 
# next element are the same then return true as output,otherwise return false
data = input("data: ")
list1=list(map(int,data.split(',')))
print("list: ",list1)
ele = int(input("num: "))
for i in range(1,len(list1)):
    if list1[i]==list1[i-1]:
        if ele==list1[i]:
            print("True")
            break
else:
    print("False")
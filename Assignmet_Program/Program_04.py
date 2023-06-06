# Python script to display the prime number series up to the given N value
start= int(input("Enter Starting value :"))
end=int(input("Enter Endiing value : "))
for i in range(start,end+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
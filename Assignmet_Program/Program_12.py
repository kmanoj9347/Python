# To arrange the given list of elements in ascending or descending order
l =input("Enter list of numbers : ")
n =list(map(int,l.split()))
n.sort()
print(n)
n.sort(reverse=True)
print(n)
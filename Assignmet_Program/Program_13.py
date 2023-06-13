# To find addition of two matrices.
m=int(input("Number of rows for matrix -A,m = "))
n=int(input("Number of columns for matrix - A,n = "))
p=int(input("Number of rows for matrix - B, p = "))
q=int(input("Number of columns for matrix - B, q = "))
matrix1= []
matrix2 =[]
if(m == p and n==q):
    print("Enter values for matrix - A")
    for i in range(1,m + 1):
        a=[]
        for j in range(1,n +1):
            print("Entry in row: {} column: {}".format(i,j))
            a.append(int(input()))
        matrix1.append(a)
    print("Enter values for matrix - B")
    for i in range(1, p+1):
        b =[]
        for j in range(1,q+1):
            print("Entry in row: {} column: {}".format(i,j))
            b.append(int(input()))
        matrix2.append(b)
    print("Matrix a=",matrix1)
    print("Matrix b=",matrix2)
    result=[[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    print("Addition of two matrices=",result)
else:
    print("Addition is not possible")
            
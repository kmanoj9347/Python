#matrix Addition
m=int(input("Number of rows for matrix A, m ="))
n=int(input("Number of columns for matrix A, n ="))
p=int(input("Number of rows for matrix B, p ="))
q=int(input("Number of columns for matrix B, q ="))
A=[]
B=[]
if m!=p or n!=q:
    print("Addition is not posssible")
else:
    print("Enter values for matrix A")
    for i in range(m):
        matrixa =[]
        for j in range(n):
            print("Entry in row : {} column: {}".format(i+1,j+1))
            matrixa.append(int(input()))
        A.append(matrixa)
    print("Enter values for matrix-B")
    for i in range(p):
        matrixb=[]
        for j in range(q):
            print("Entry in row:{} column: {}".format(i+1,j+1))
            matrixb.append(int(input()))
        B.append(matrixb)
print("Matrix a={}".format(A))
print("Matrix b={}".format(B))
Sum =A.copy()
for i in range(m):
    for j in range(n):
        Sum[i][j]=A[i][j]+B[i][j]
print("Addition of two matrixes {}".format(Sum))



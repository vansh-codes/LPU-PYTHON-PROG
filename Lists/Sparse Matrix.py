#Sparse Matrix
rows=int(input("Enter no of rows : "))
cols=int(input("Enter no of columns : "))
matrix=[[int(input("Enter El : ")) for i in range(cols)] for j in range(rows)]

for i in matrix:
    print(i)
#Gives index of every element of matrix ex : 1st el is at (0,0)...
for i in range(rows):
    for j in range(cols):
        print("({},{})".format(i,j),end=" ")
    print()

#Printing matrix like a Matrix
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")
    print()

#Sparse Matrix
for i in range(rows):
    for j in range(cols):
        if matrix[i][j]!=0:
            print("({},{})".format(i,j),matrix[i][j],end=" ")
    print()

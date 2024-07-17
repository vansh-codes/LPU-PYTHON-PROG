"""Matrix using List Comprehension"""

matrix=[int(input("Matrix: ")) for i in range(9)]
print(matrix)
#################################################################
rows=int(input("Enter no of rows : "))
cols=int(input("Enter no of columns : "))
matrix=[[int(input("Enter El : ")) for i in range(cols)] for j in range(rows)]
print(matrix)
    
for i in matrix:
    print(i)
################################################################

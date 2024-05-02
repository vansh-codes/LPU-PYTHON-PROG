n=int(input("Enter row of matrix : "))
l=[[int(input("Enter value : ")) for i in range(n)] for j in range(n)]
diagonal1=[]
print("Matrix : ")
for i in l:
    print(i)
for i in range(n):
    res=[]
    for j in range(n):
        if i==j:
            res+=[l[i][j]]
    diagonal1+=res
diagonal2=[]
for a in range(n):
    res=[]
    for b in range(n):
        if (a+b)==(n-1):
            res+=[l[a][b]]
    diagonal2+=res
main=[diagonal1,diagonal2]
print("Diagonal list : ")
print(main)
#in matirx form
print("Disgonal Matrix ")
for i in main:
    print(i)

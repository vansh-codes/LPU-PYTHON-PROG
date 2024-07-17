n=int(input("Enter n : "))
l=[[int(input("Enter el : "))for i in range(n)]for j in range(n)]
print("Matrix : ")
for i in l:
   print(i)
res=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        if l[i-1][j-1]==0:
            res+=((i,j),)
print(res)
   

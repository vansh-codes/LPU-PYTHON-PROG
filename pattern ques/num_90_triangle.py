n=int(input("enter rows : "))
for i in range(0,n):
    for j in range(n-i,0,-1):
        print(j,end=" ")
    print()

def rfibo(n):
    if n<=1:
        return n
    else:
        return(rfibo(n-1)+rfibo(n-2))

n=int(input("term required in series: "))

for i in range(n):
    print(rfibo(i),end=' ')

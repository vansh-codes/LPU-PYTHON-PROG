#Pascal triangle
n=int(input("Enter a num: "))
for i in range(1,n+1):
    c=1
    l=[]
    for j in range(1,i+1):
        l=l+[c]
        c=c*(i-j)//j
    for k in range(n-i):
        print(' ',end='')
    print(l)

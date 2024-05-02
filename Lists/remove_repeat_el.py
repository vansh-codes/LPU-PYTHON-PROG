##l=[1,2,3,4,5,2,1]
##n=[]
##for i in l:
##    if i not in n:
##        n+=[i]
##
##print(n)

l=list(map(int,input("Enter list : ").split()))
res=[]
for i in l:
    if i not in res:
        res=res+[i]

print(res)

n=list(map(int,input("Enter numbers : ").split(",")))
div=[]
for i in n:
    d=[]
    for j in range(1,i+1):
        if i%j==0:
            d+=[j]
    div+=[d]
d1={}
for i in range(len(div)):
    d1.update({n[i]:div[i]})
print(d1)

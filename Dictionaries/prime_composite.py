n=list(map(int,input("Enter numbers : (, separated)").split(",")))
d={}
for i in n:
    ans=""
    if i>2:
        for j in range(2,i):
            if i%j==0:
                ans="not prime"
                break
            else:
                ans="prime"
    else:
        if i==1:
            ans="not prime"
        elif i==2:
            ans="prime"
    d.update({i:ans})
print(d)

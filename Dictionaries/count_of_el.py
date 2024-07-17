#count of each element in a tuple
t=tuple(map(int,input("Enter el : ").split(",")))
t1=()
d={}
for i in t:
    if i not in t1:
        t1+=(i,)
for i in t1:
    c=t.count(i)
    d[i]=c
print(d)
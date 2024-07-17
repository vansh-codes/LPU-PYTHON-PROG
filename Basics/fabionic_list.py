l=[0,1]
n=int(input())
for i in range(n-2):  #n-2 bcoz 2 ele aready in list
    x=l[-1]+l[-2]
    l=l+[x]


for i in l:
    print(i,end=" ")

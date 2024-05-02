#all possible combinations
l=[]
combs=[]
n=int(input("Enter n : "))
for i in range(n):
    el=int(input("Enter el : "))
    l+=[el]

def combination(combs,l):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (i!=j and j!=k and i!=k):
                    combs+=[[l[i],l[j],l[k]]]
    return combs

for i in range(1):
    if l[0]==l[1] or l[1]==l[2] or l[0]==l[2]:
        print([])
    else:
        print(combination(combs,l))

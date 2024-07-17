l=input("Enter sent : ")
l1=[]
for i in l:
    if i not in l1:
        l1+=[i]
l2=[]
for i in range(len(l1)):
    count=0
    if l1[i]==" ":
        continue
    else:
        l2+=[l1[i] + " " + str(l.count(l1[i]))]
for i in sorted(l2):
    print(i)

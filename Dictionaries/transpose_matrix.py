a=int(input("Enter n : "))
l=[[int(input("Enter el : ")) for i in range(a)]for j in range(a)]
print("Matrix : ")
for i in l:
    print(i)

t=zip(*l)
trans=[]
print("Transpose Matrix : ")
for i in t:
    trans+=[list(i)]
    print(list(i))
d={}
print("Dict of corresponding els of matrix and transpose matrix ")
for i in range(len(l)):
    for j in range(len(trans)):
        d.update({trans[i][j]:l[i][j]})
print(d)

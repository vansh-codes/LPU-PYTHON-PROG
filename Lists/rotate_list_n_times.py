l1=list(map(int,input("Enter list1 : ").split(" ")))
n=int(input("How many times you want to rotate : "))

for i in range(n):
    temp=l1[-1]
    for j in range(len(l1)-1,0,-1):
        l1[j]=l1[j-1]
    l1[0]=temp

print(l1)
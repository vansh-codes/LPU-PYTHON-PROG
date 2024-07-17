
##names=list(map(str,input("Enter 5 names : ").split(" ")))
##print(sorted(names))

#Method 2
n=int(input("Enter no of students : "))
l=[]
for i in range(n):
    a=input("Enter name : ")
    l=l+[a]
print(sorted(l))

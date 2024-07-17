##t=tuple(map(int,input("ENter no : ").split(" ")))

n=int(input("Enter no of students : "))
l=()
for i in range(n):
    a=int(input("Enter name : "))
    l=l+(a,)    #l=l+tuple(a)

temp=l[::-1]
print(temp)
print(l.count(1))
print(temp.index(1))

##t1=(1,2)
##t2=(3,4)
##t3=([1,2],)
##print(t1+t2+t3)

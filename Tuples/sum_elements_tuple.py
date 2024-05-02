n=int(input("Enter no of students : "))
l=()
for i in range(n):
    a=int(input("Enter name : "))
    l=l+(a,)

print(sum(l))

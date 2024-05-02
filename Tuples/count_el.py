n=int(input("Enter no of students : "))
l=()
for i in range(n):
    a=int(input("Enter name : "))
    l=l+(a,)

a=int(input("Enter lower limit : "))
b=int(input("Enter upper limit : "))
el=int(input("Enter element to be count : "))
print(l[a:b+1].count(el))


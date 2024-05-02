import math as m
n=int(input("Enter upper limit of range : "))
def strong(n):
    result=0
    while n>0:
        x=n%10
        result+=m.factorial(x)
        n//=10
    return result

strong(n)
for i in range(1,n+1):
    if strong(i)==i:
        print(i,end=" ")


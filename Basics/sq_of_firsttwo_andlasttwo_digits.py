n=int(input())
t=n
y=n%100
x=y//10
z=y%10
s=x+z

while n!=0:
    q=n%10
    n=n//10
print("q:",q)
##print("l:",(len(str(t))-2))
print(t)
while t!=0:
    o=t%10**(len(str(t))-2)
    t=t//10**(len(str(t))-2)
print("o:",o)

o=o%10
r=q+o
print(r,s)
print(s*r)



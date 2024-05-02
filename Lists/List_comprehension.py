#List Comprehension
#Syntax
#expression iterator (optional if condition)]

x=[i for i in range(1,10)]
print(x)

y=[i for i in range(1,10) if(i%2==0)]
print(y)

z=[a*b for a in [1,2,3] for b in [10,20,30]]
print(z)

p=[a for a in [10,20,30] for b in [30,40,10] if(a==b)]
print(p)


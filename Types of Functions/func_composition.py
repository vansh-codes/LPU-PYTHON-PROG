def f1(x):
    return x*2

def f2(x):
    return x*x

a=10
b=f2(f1(a))   #first evalutas f1(a) which gives value 20 then evaluates f2(20) which gives output as 400
print('First func inside second func',b)

c=f1(f2(a))    #first evaluates f2(a) i.e 100 then f1(100) gives 100*2 gives output 200
print('Second func inside first func: ',c)

#Method made by me:)
def gcd(x,y):
    m=min(x,y)
    l=[]
    for i in range(1,m+1):
        if x%i==0 and y%i==0:
            l.append(i)
    return l[-1]

a=int(input("Enter  num: "))
b=int(input("Enter num: "))
print(gcd(a,b))


#Method 2  -- sir's method+
'''def gcd(x,y):
    m=min(x,y)
    result=1
    for i in range(1,m+1):
        if x%i==0 and y%i==0:
            result=i
    return result

a=int(input("Enter  num: "))
b=int(input("Enter num: "))
print(gcd(a,b))'''

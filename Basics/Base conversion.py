n=int(input("n: "))
base=int(input("base: "))
def Base(n,base):
    if n==0:
        return [0]

    digits=[]
    while n:
        digits.append(int(n%base))
        n//=base
    x=""
    for i in digits:
        x+=str(i)
    base7=str(x[::-1])
    return base7

print(Base(n,base))
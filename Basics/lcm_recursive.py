a=int(input("Enter first num :"))
b=int(input("Enter second num :"))
def run(a,b):   #gives gcd
    if b==0:
        return a
    else:
        return run(b,a%b)

def lcm(a,b):
    return (a*b) // run(a,b)

print(lcm(a,b))
# print(run(a,b)) gives gcd

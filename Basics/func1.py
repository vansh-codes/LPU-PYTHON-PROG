def add(n,m):      #n,m are parametes here
    print("Sum is",n+m)

def sub(n,m ):
    print("Difference is",n-m)

def product(m,n):
    print("Product is",m*n)

def divide(m,n):
    print("Quotient is",m/n)

def floordiv(m,n):
    print("Floor Divison is", m//n)

def all(n,m):
    print("sum is:",n+m)
    print("difference is:",n-m)
    print("product is:",n*m)
    print("quotient is:",n/m)
    print("floor division is:",n//m)
    print("remainder is:",n%m)

n=int(input("Enter a number: "))
m=int(input("Enter another number: "))
add(n,m)       #n,m are arguments here
sub(n,m)     #arguments can be a expression , constant or a defined varible
product(m,n)
divide(m,n)
floordiv(m,n)

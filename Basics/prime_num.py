n=int(input("Enter a number : "))
x=0

if n==1:
    print("1 is neither prime nor composite")
else:
    for i in range(2,n):
        if n%i==0:
            x+=1
    
if x==0:
    print("Prime number")
elif x!=0:
    print("Not a Prime number")
            
            
            

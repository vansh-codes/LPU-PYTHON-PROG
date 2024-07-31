#QUESTION 4 for PRACTICAL
n=int(input("Enter a number : "))
fact=1
if n<0:
    print("Factorial does'nt exists")
elif n==0:
    print("Factorial is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
print("Factorial of the given number is : ",fact)

n=int(input("Enter rows : "))
for i in range(n):
    for j in range(n):
        print(end=" ")
    n=n-1
    for j in range(i+1):
        print("* ",end="")
    print()
    

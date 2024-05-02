#Nested for loop
for i in range(5):
    for k in range(5-i):
        print(' ',end='')
    for j in range(i+1):
        print("*",end=" ")
    print()
## Legend Method :  print("*"*i)

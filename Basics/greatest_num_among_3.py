n1=int(input("Enter first num: "))
n2=int(input("Enter second num: "))
n3=int(input("Enter third num: "))
if n1>=n2 and n1>=n3:
    print("The greatest number is : ",n1)
elif n2>=n1 and n2>=n3:
    print("The greatest number is : ",n2)
elif n3>=n1 and n3>=n2:
    print("The greatest number is : ",n3)
else:
    print("Wrong Input")

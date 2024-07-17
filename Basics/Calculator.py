#QUESTION 1 FOR PRACTICAL
while True:
    print("Welcome to Vansh's Calculator")
    n1=int(input("Enter first number : "))
    n2=int(input("Enter second number : "))
    print("Press 1 for addition (+)")
    print("Press 2 for Subtraction (-)")
    print("Press 3 for Multiplication (*)")
    print("Press 4 for Division (/)")
    print("Press 5 for Floor Division (//)")
    print("Press 6 for Remainder (%) ")
    print("Press 7 to quit")
    ch=int(input("Enter your choice : "))
    if ch==1:
        print("Sum is \n",n1+n2)
    elif ch==2:                         
        print("Difference is ",n1-n2)
    elif ch==3:
        print("Product is ",n1*n2)
    elif ch==4:
        print("Division is ",n1/n2)
    elif ch==5:
        print("Floor Division value is ",n1//n2)
    elif ch==6:
        print("Remainder is : ",n1%n2)
    elif ch==7:
        print("Thank you!!")
        break
    if ch not in (1,2,3,4,5,6,7):
        print("\n")
        print("Invalid Operator")


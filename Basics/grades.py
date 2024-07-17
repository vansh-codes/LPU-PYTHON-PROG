m1=float(input("Enter marks for subject1 : "))

if m1>=90:
    print("A Grade")
elif m1>=80 and m1<90:
    print("B Grade")
elif m1>=70 and m1<80:
    print("C Grade")
elif m1>=60 and m1<70:
    print("D Grade")
elif m1<=60:
    print("F Grade")
else:
    print("Invalid input")
    

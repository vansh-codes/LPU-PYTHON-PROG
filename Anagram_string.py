n=input("Enter a string : ")
n1=input("Enter another string : ")

if len(n)==len(n1):
    #a=sorted(n)
    #b=sorted(n1)
    if sorted(n)==sorted(n1):
        print("True")
    else:
        print("False")
else:
    print("False")

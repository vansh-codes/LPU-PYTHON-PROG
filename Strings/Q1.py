s1=input("Enter str1: ")
s2=input("Enter str2: ")
l1=len(s1)
l2=len(s2)
if (l1>l2):
    print(s1+s2+s1)
elif (l1==l2):
    print("Strings are of same length.")
else:
    print(s2+s1+s1)

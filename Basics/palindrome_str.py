#to check whether palindrome or not :)

st=input("Enter a string to check : ")
for i in st:              #using loop   #practical question 6
    x=0
    if st==st[::-1]:
        x=1
    else:
        x=0
if x==1:
    print("String is palindrome")
else:
    print("Not Palindrome")


#easy basic method
'''if st==st[::-1]:                   
    print("String is Palindrome")
else:
    print("Not Palindrome")'''

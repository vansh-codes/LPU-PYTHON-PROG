x="qwerty"
access=0
guess=0
while guess<3:
    pd=input("Enter password: ")
    if pd!=x:
        access=0
    elif pd==x:
        access=access+1
    if access==1:
        break
    guess+=1
if access==1:
    print("You have successfully logged in")
elif access==0:
    print("Access denied")
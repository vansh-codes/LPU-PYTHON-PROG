#not perfect code
#its not complete

e=input("Enter gmail id : ")
k=e.split('@')
g=["gmail.com","yahoo.com","gov.in"]
c=['.','_']

if len(k)==2 and k[1] in g and k[1] in c:
    print("Valid")
else:
    print("Invalid")


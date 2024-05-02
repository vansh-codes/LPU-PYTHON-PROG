#PROJECT 3

m=input("Enter e-mail id : ")
##l=m.find("@")   #stores index of @
##k=len(m)
##s=k-l          #stores number of char after @
##u_n=""
##dom=""
##
##for i in range(l):
##    u_n+=m[i]
##print("USERNAME : ",u_n,end="")
##print()
##
##for i in range(s-1):
##    dom+=m[i+l+1]
##print("DOMAIN : ",dom.upper(),end="")

k=m.split("@")
print("Username : ",k[0])
print("DOmain : ",k[1].upper())

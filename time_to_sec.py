'''python  program to find the number of secs''' 

h=int(input("Enter hour : "))
m=int(input("Enter minute : "))
s=int(input("Enter seconds : "))
hs=h*3600
ms=m*60
s1=hs+ms+s
print("Number of seconds in ",h,"hours ",m,"minutes and ",s,"seconds are : ",s1)

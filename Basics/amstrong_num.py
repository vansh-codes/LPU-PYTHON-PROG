#armstrong number is a number whose sum of power of number of digits in equal to that number itself
#Example : 371 = 3**3 + 7**3 + 1**3 = 371

#9474 , 153 are also  armstrong numbers

num=int(input("Enter a number : "))
temp=num
sum=0
while num!=0:
   x=num%10
   sum=sum+x**(len(str(temp)))
   num=num//10
print(sum)

if temp==sum:
   print("Armstrong")
else:
   print("Not Armstrong")
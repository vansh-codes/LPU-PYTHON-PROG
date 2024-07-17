num=int(input("Enter the number : "))     #for example take number as 531
sum=0
while num!=0:
    x=num%10      #here x stores 1
    sum+=x             #1 gets add up to sum
    num=num//10          #num gets floor divide by 10...i.e 531 gets 53 and the while loop continues
print("Sum is :",sum)

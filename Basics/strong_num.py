#A number that is equal to the sum of the factorial of its individual digits is a strong number
#Examples of a strong num is 2, 145
sum1=0
num=int(input("Enter"))                          #suppose input given 145
temp=num
while num:
    i=1
    f=1
    r=num%10                               #here r will store 5 from 145
    while i<=r:                             #till i less than r i.e. 5
        f=f*i                               #f gets multipled by i...so f will store factorialof 5 i.e. 120
        i+=1
    sum1=sum1+f                           #f is added to sum1  i.e. 120 is added to sum1
    num=num//10                            #here the num i.e. 145 becomes 14 and the while loop continues

if sum1==temp:
    print("Strong number")
else:
    print("not a Strong number")

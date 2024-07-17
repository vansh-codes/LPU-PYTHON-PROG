#a number whose all factors sum up to the number itself is called perfect number:) 
#QUESTION 2 of PRACTICAL
#Examples : 28 , 496, 8128

n=int(input("Enter a number : "))
sum=0
for i in range(1,n):
    if (n % i) == 0:
        print(i,sep=" ")      #not required in code...just to see
        sum=sum+i
    print(sum)
if sum==n:
    print("Its a perfect number")
else:
    print("Its not a perfect number")

        

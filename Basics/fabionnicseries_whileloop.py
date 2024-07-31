n=int(input("n: "))
a=1
b=1
sum=0
count=1
print("Factorial series is : ")
print(sum,end=" ")
while count<n:
    a=b
    b=sum
    sum=a+b
    print(sum,end=" ")
    count+=1


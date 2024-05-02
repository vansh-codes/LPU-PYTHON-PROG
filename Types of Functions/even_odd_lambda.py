#Even Odd

n=int(input("Enter no of elements : "))
l=[]
for i in range(n):
    e=int(input("Enter element : "))
    l.append(e)
print("Original list : ")

even_l=list(filter(lambda x: x%2==0,l))
print("Even num list : ",even_l)

odd_l=list(filter(lambda x:x%2!=0,l))
print("Odd num list : ",odd_l)

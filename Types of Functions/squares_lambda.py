#Square of every el in list
n=int(input("Enter no of elements : "))
l=[]
for i in range(n):
    e=int(input("Enter element : "))
    l.append(e)
print("Original list : ")

sq=list(map(lambda x:x**2,l))
print(sq)

#take students name as key and their 4 subject marks as values and find the topper
n=int(input("Enter no of students : "))
data={}
top=0
for i in range(n):
    name=input("Enter Name :")
    marks=list(map(int,input("Enter Marks of 4 Subject: ").split(" ")))    
    data.update({name:marks})
    if sum(marks)>top:
        top=sum(marks)
print(data)

for key,values in data.items():
    if sum(values)==top:
        print(" Name :",key,", Marks :",top)

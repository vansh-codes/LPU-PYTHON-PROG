##f=open("student.txt","w")
##for i in range(1,13):
##    f.write(input("Enter name : "))
##    f.write("\n")
##f.close()

f=open("student.txt","r")
find=input("Enter rollno: ")
c=0
for i in f.readlines():
    if find in i.split(" "):
        print(i)
    else:
        c=1
if c==1:
    print("Rollno not found")



f=open("WritingReading.txt","w")
ch="y"
while ch not in "nN":
    f.write(input("Enter data : "))
    f.write("\n")
    ch=input("Do you want to continue [y/n] : ")
f.close()
f1=open("WritingReading.txt","r")
r=f1.read(7)   #reads 7 characters only.
print(r)
s=f1.seek(3)  #Takes the file pointer to 3rd character
r=f1.read(4)   
print(r)
s=f1.seek(0)
r=f1.readline()   
print(r)
r=f1.readlines(4) 
print(r)
f1.close()

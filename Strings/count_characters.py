import string as s
n=input("Enter a string : ")
count=0
characters=""
dig=s.digits
for i in n:
    if i not in dig:
        count+=1
    else:
        continue

print(count)

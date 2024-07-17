#z=str.digits  - all digits 0-9
#q=str.ascii_letters - prints all alphabets


import string as str
s=input("Enter : ")
p=str.punctuation
new=''
for i in s:
    if i  not in p:
        new+=i

print(new)

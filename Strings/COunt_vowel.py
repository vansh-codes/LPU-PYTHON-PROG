n=input("Enter a string : ")
count=0
vowel="AEIOUaeiou"
for i in n:
    if i in vowel:
        count+=1

print(count)

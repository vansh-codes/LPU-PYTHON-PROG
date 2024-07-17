f=open("aSearch.txt","r")
vowels=consonants=uppercase=lowercase=0
for i in f.readlines():
    for j in i:
        if j.isalpha():
            if j.isupper():
                uppercase+=1
            elif j.islower():
                lowercase+=1
            if j in "aeiouAEIOU":
                vowels+=1
            else:
                consonants+=1

print("Number of vowels are %s"%vowels)
print("Number of consonants are %s"%consonants)
print("Number of uppercase are %s"%uppercase)
print("Number of lowercase are %s"%lowercase)

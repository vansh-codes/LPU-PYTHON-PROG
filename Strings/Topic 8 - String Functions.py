#String functions
'''
rindex() - gives the index from right side
index()
title()
capitalize()
count(character,start,stop)
find(charater,start,stop)       returns -1 if character not found
lower()
upper()
swapcase()
'''
s="hello World"
print("rindex : ",s.rindex('o'))
print("Index : ",s.index('o'))
print("Title : ",s.title())
print("Capitalize : ",s.capitalize())
print("Count : ",s.count('o',2,9))
print("Find : ",s.find('r',2,9))
print("Lower : ",s.lower())
print("Upper : ",s.upper())
print("Swapcase : ",s.swapcase())

#String functions to check

'''
isalnum()   - if only alphabet and num then true
istitle()   - if every word first letter capital then True
isupper()   - if every character is upper then True
isalpha()   - if all characters alphabet then True
isascii()   - if all character ascii
isdecimal()  
isdigit()
isidentifier()
islower()
isprintable()
isspace()
'''
s="Hello World 12"
s1="None"
x='\n'   #\t \r this all are not printable
print("Alnum : ",s.isalnum())
print("Title : ",s.istitle())
print("Upper : ",s.isupper())
print("Lower : ",s.islower())
print("Alpha : ",s.isalpha())
print("Ascii : ",s.isascii())
print("Decimal : ",s.isdecimal())
print("Printable : ",s.isprintable(),x.isprintable())
print("Space : ",s.isspace())
print("Identifier : ",s1.isidentifier())


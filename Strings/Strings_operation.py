s1='Hello'
s2='Welcome'
s3=""" This is a
multiline
string."""
# Five types of function on strings: Indexing, slicing, repetition, memebership, concatenation
print(s1.capitalize())
print(s1.lower())
print(s1.upper())
#print(s1[8]) #shows IndexError: string index out of range
s4="Welcome"
print(s4[0:6])
print(s4[0:7])
print(s4[:-5]) # In negative index, -len(s4) is cosisidered as the index start default value, i.e [-7:-5]
print(s4[:])
print(s4[::])
print(s4[0:7:2])
print(s4[0:6:2]) #[start:end:step]
print(s4[::-2])
print(s4[-7:-1:-2])
print(s4[:-1:-2])
print(s4[:-1:-1])




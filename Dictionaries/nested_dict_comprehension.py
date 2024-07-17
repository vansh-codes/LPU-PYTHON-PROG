#nested dict
string=input("Enter string : ")
dict={
    x: {y: x+ y for y in string} for x in string}
print(dict)

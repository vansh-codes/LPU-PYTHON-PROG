#ErrorHandling
l=[10,20,30]
try:
    print(l[4])
except IndexError:
    print("There are only ",len(l),"elements")

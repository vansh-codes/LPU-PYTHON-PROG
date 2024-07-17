import math as m
try:
    l=[1,2,3,4]
    m.sqrt(-20)         #ValueError
    print(l[7])         #IndexError
    print(8 + "Hen")      #TypeError
    z=2/0               #ZeroDivisionError
except (ZeroDivisionError,ValueError,IndexError,TypeError):
    print("Error")

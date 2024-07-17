import math as m
a=10
b=10
x=[1,2,3]
try:
    print(a/b)
    print(x[0])
    print(a)
    print(m.sqrt(a))
    print(5+"abc")
##METHOD1
except ZeroDivisionError:
    print("Zero cannot be in denominator")
except ValueError:
    print("Invalid Value")
except IndexError:
    print("Invalod Index")
except NameError:
    print("There is a name error")
except TypeError:
    print("Type Error hai isme NOOB")
else:
    print("Perfecttttttt")
##finally:          #Always Runs....for use like closing a file,database,etc...
##    print("Finalllllll")

'''###METHOD2###'''
##except Exception as e:
##    print(e.__class__,"error occured")
##else:
##    print("Perfectttttttt")
##print("END")

import math as m

print("1.Square root function -> square root of num")
print(m.sqrt(9),m.sqrt(20),sep="\n")
print("----------------------")

print("2.Floor function -> smallest nearest integer")
print(m.floor(3.14))
print("----------------------")

print("3.Ceiling function -> greatest nearest integer ")
print(m.ceil(3.14))
print("----------------------")

print("4.Factorial function -> factorial of the num")
print(m.factorial(4),m.factorial(5),sep="\n")
print("----------------------")

print("5.Absolute function -> floating absolute value")
print(m.fabs(-32),m.fabs(32),sep="\n")
print("----------------------")

print("6.Power function -> (x,y) means x**Y")
print(m.pow(2,3),m.pow(3,5),sep="\n")
print("----------------------")

print("7.Pi Variable -> value of pi")
print(m.pi)
print("----------------------")

print("8.Mod function -> floating remainder")
print(m.fmod(10,3))
print("----------------------")

print("9.Log Function ->bydefault base is 'e', log value of num")
print(m.log(1000))
print("----------------------")

print("10.Log10 Function -> log with base 10")
print(m.log10(1000))
print("----------------------")

print("11.log2 function -> log with base 2")
print(m.log2(8))
print("----------------------")

print("12.e Variable -> value of e")
print(m.e)
print("----------------------")

print("13.tau Variable -> value of tau")
print(m.tau)
print("----------------------")

print("14.inf variable -> prints infinity")
print(m.inf)
print("----------------------")

print("15.nan variable -> not a number(nan)")
print(m.nan)
print("----------------------")

print("16.Trigonometric Functions")
x=m.radians(30)
print("Converting radians into degree>> 30 radians is : ",x)
print("sin takes the value in radians>>sin30: ",m.sin(x))
print("----------------------")





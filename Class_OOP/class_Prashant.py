'''class myfirstclassprogram:
    print('welcome to my class')

c=myfirstclassprogram()
print(c)'''
#############
class Reactangle:
    length=0;
    breadth=0;
R1=Reactangle()
r2=Reactangle()
r2.length=23
r2.breadth=30
Area=r2.length*r2.breadth
print('Area=',Area)
print ('Initial values print')
print('Length=',R1.length)
print('Breadth=',R1.breadth)
print ('Area of Rectangle=',R1.length*R1.breadth)
R1.breadth=30
R1.length =20
print ("After reassigning the value of attributes")
print('Length= ',R1.length)
print ('Breadth= ',R1.breadth )
print ('Area of Rectangle =',R1.length*R1.breadth)
################################
'''class demo:
    def display_message(self):
        print('hello,learn python')

d1=demo()
d1.display_message()'''
##################################
'''class circle:
    def __init__(self,pi):
        self.pi=pi
    def calc_area(self,radius):
        return self.pi*radius**2
c1=circle(3.14)
print('The area of circle=',c1.calc_area(5))
'''
#################################
'''class ABC:
    def __init__(self):
        print("hello")
a1=ABC()
a2=ABC()
###################################
class circle:
    def __init__(self,pi):
        self.pi=pi
    def calc_area(self,radius):
        r=int(input("Enter radius"))
        print(self.pi*r**2)
c1=circle(3.14)
print('The area of circle=',c1.calc_area(5))'''
####################################
'''class calc():
    a=0
    b=0
    def sum(self):
        a=int(input())
        b=int(input())
        c=a+b
        print(c)
    def sub(self):
        a=int(input())
        b=int(input())
        c=a-b
        print(c)
    def multi(self):
        a=int(input())
        b=int(input())
        c=a*b
        print(c)
        return a-b
p1=calc()
p1.sum()
p1.sub()
p1.multi()'''
###################################
'''class calc():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        n=self.a+self.b
        print("sum=",n)
    def sub(self):
        m=self.a-self.b
        print("sub=",m)
    def multi(self):
        e=self.a*self.b
        return e;
p=calc(2,3)
p.sum()
p.sub()
s=p.multi()
print(s)'''
################################
'''class person:
    def __init__(ram,name,age):
        ram.name=name
        ram.age=age
    def myfunc(ram):
        print("Hello my name is ",ram.name)
        print("age= ",ram.age)
p1=person("Jhon",36)
p1.myfunc()'''
####################################

'''class first:
    def a(self):
        print("Hello")
class second(first):
    def b(self):
        print("whats's")
class third(second):
    def c(self):
        print("ARE YOU OKK")
o=third()
o.a()
o.b()
o.c()'''
##############################
'''class first:
    def a(self):
        print("Hello")
class second:
    def b(self):
        print("whats's")
class third(first,second):
    def c(self):
        print("ARE YOU OKK")
o=third()
o.a()
o.b()
o.c()'''
#############################
'''class first:
    def a(self):
        print("Hello")
class second(first):
    def b(self):
        print("whats's")
class third(first):
    def c(self):
        print("ARE YOU OKK")
o=second()
i=third()
o.a()
o.b()
i.a()
i.c()'''
#############################

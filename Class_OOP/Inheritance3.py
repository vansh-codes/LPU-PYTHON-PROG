class base1:
    def getdata(self,i,j):
        self.i=i
        self.j=j
    def putdata(self):
        print("i : ",self.i)
        print("j : ",self.j)

class base2:
    def getdata2(self,a,b):
        self.a=a
        self.b=b
    def putdata2(self):
        print("a : ",self.a)
        print("b : ",self.b)

class derived(base1,base2):
    def derivedata(self,i,j,a,b,d):
        base1.getdata(self,i,j)
        base2.getdata2(self,a,b)
        self.d=d
    def printdata(self):
        base1.putdata(self)
        base2.putdata2(self)
        print("d : ",self.d)

'''Obj1=base1()'''
##Obj1.getdata(input("Enter i : "),input("Enter j : "))
##Obj1.putdata()
'''Obj2=base2()'''
##Obj2.getdata2(input("Enter a : "),input("Enter b : "))
##Obj2.putdata2()
##Obj3.derivedata(input("Enter d: "))
##Obj3.printdata()
'''Obj3.getdata(input("Enter i : "),input("Enter j : "))'''
#Obj3.putdata()
'''Obj3.getdata2(input("Enter a : "),input("Enter b : "))'''
#Obj3.putdata2()
Obj3=derived()
Obj3.derivedata(input("Enter i : "),input("Enter j : "),input("Enter a : "),input("Enter b : "),input("Enter d : "))
Obj3.printdata()
print(Obj3.i)

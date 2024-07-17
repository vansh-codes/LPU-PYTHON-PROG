class employee:
    def getdata(self,n,s,a):
        self.name=n
        self.salary=s
        self.__age=a
    def putdata(self):
        print("Name : ",self.name)
        print("Salary : ",self.salary)
        print("Age : ",self.__age)

E=employee()
E.getdata("Harsh",23000,20)

###Method1
##E.putdata()

#Method2
print(E.name)
print(E.salary)
##print(E.__age) private variable will not be printed by this method, it will throw error
###
print("__name__ : ",employee.__name__)
print("__module__ : ",employee.__module__)
print("__doc__ : ",employee.__doc__)
print("__dict__ : ",employee.__dict__)
##
E1=employee()
E1.getdata("Harsh",20000,20)
print(getattr(E1,"salary"))
setattr(E1,"salary",50000)
print(E1.salary)

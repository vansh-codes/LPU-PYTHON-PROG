#Inheritance
class person:
    def getdata(self,name,age):
        self.name=name
        self.age=age
    def putdata(self):
        print("Name : ",self.name)
        print("Age : ",self.age)

class employee(person):    #Class person inherited in employee
    def getsalary(self,salary):
        self.salary=salary
    def putsalary(self):
        person.putdata(self)
        print("Salary : ",self.salary)

class student(employee):
    def marks(self,m):
        self.marks=m
    def disp(self):
        employee.putsalary(self)
        print("Marks : ",self.marks)
Em=student()
Em.getdata(input("Enter name : "),int(input("Enter age : ")))
Em.getsalary(float(input("Enter Salary : ")))
Em.marks(int(input("Enter Marks : ")))
##Em.putdata()
##Em.putsalary()
Em.disp()


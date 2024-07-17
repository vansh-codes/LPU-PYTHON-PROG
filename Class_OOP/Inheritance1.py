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
        print("Salary : ",self.salary)


Em=employee()
Em.getdata(input("Enter name : "),int(input("Enter age : ")))
Em.getsalary(float(input("Enter Salary : ")))
Em.putdata()
Em.putsalary()


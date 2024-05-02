class employee:
    def __init__(self,n,s):
        self.name=n
        self.salary=s
    def putdata(self):
        print("Name : ",self.name, ",Salary : ",self.salary)

x=input("Enter name : ")
y=int(input("Enter Salary : "))
el=employee(x,y)
el.putdata()

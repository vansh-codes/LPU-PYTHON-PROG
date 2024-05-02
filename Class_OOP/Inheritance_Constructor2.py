class name:
    def __init__(self,name):
        self.name=name
    def putdata(self):
        print("Name : ",self.name)

class ages(name):
    def __init__(self,name,age):
        self.age = age
        super().__init__(name)
    def display(self):
        name.putdata(self)
        print("Age : ",self.age)

class marks(ages):
    def __init__(self,name,age,marks):
        self.marks=marks
        super().__init__(name,age)
    def disp(self):
        ages.display(self)
        print("Marks : ",self.marks)
    

S=marks(input("Enter name : "),int(input("Enter Age : ")),int(input("Enter Marks : ")))
S.disp()


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def putdata(self):
        print("Name : ",self.name)
        print("Age : ",self.age)

class student(person):
    def __init__(self,name,age,marks):
        self.marks= marks
        super().__init__(name,age)
    def display(self):
        person.putdata(self)
        print("Marks : ",self.marks)

P=person("Anshul",23)
P.putdata()

S=student(input("Enter name : "),int(input("Enter Age : ")),int(input("ENter Marks : ")))
S.display()
##S.putdata()

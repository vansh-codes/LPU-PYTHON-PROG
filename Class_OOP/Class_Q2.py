'''class Car:
    def setName(self,name):
        self.name=name                   #input("Enter name : ")
    def getName(self):
        print("Honda car name : ",self.name)
Honda=Car()
Honda.setName(input("Enter name : "))
Honda.getName()
'''

class Car:
    def setName(self):       #to get input from user we should not pass the name argument 
        name=input("Enter Name : ")
        self.name=name                   
    def getName(self):
        print("Honda car name : ",self.name)

Honda=Car()
Honda.setName()
Honda.getName()
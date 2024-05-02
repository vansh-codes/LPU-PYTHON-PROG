#Constructor
class Student:
    def __init__(self,name,rollno):   #This is the constructor function which is called automatically
        self.name=name
        self.rollno=rollno
    def putdata(self):
        print("Name : ",self.name)
        print("ROll no : ",self.rollno)
        print()
        
s=Student(input("Enter name : "),int(input("Enter rollno : ")))  #Object1
s.putdata()
s1=Student("Viraj",29)   #Object 2
s1.putdata()
s2=Student("Jai",66)      #obj 3  #This will not be printed bcoz putdata is not called for this
s3=Student("Jaya",34)     #obj4
s3.putdata()

print(type(s))

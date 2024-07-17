class car:
    def setengine(self,engine):
        self.engine=engine
    def getengine(self):
        print("Engine Model : ",self.engine)

class Honda(car):
    def setcarmodel(self,model):
        self.model=model
    def getcarmodel(self):
        print("Car Model : ",self.model)

mycar=Honda()
mycar.setengine(input("Enter Engine Name : "))
mycar.setcarmodel(input("Car Model : "))
mycar.getengine()
mycar.getcarmodel()

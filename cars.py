class Car():
    def __init__(self,model):
        self.model = model
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class Toyota(Car):
    def __init__(self,name,model):
        self.name = name
        super().__init__(model)
     
car1 = Toyota("prius","diesel")
print(car1.model)
        
        

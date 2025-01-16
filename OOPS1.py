class Student:
    #name = "Sahil"
    def __init__(self, firstname):
        #print(self)
        #print("New Student added to database..")
        self.first_name = firstname
    

s1 = Student("Sahil")
print(s1)
print(s1.first_name)

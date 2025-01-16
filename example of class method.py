class Person:
    name = "anonymous"
    def changeName(self, name):
        self.name = name
        #first method
        #Person.name = name
        #second method
        #self.__class__.name = name

p1 = Person()
p1.changeName("Sahil")
print(p1.name)
print(Person.name)

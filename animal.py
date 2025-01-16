class Animal():
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def bark(self):
        print("Woof!")

dog = Dog()
dog.eat()
dog.bark()

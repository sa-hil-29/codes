class Dog():

    #Class Object Attribute
    #Same for any Instances of a Class
    species = 'Mammal'

    def __init__(self,breed,name,spots):
        
        self.breed = breed
        self.name = name
        #boolean value True/False
        self.spots = spots

    #Operations/Actions ---> Methods
    def bark(self):
        print('Woof! My name is {}'.format(self.name))

my_dog = Dog('lab','Sammy','False')
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
my_dog.bark()

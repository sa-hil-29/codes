class Circle():

    pi = 3.14

    def __init__(self, radius = 1):

        self.radius = radius
        self.area = (radius**2)*Circle.pi


    def get_circumference(self):
        return self.radius*Circle.pi*2


my_circle = Circle()
print(my_circle.get_circumference())

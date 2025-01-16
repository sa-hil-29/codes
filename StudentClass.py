class Student1:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def avg_marks(self):
        self.avg_marks = (self.marks1 + self.marks2 + self.marks3)/3
        return self.avg_marks

s1 = Student1("Sahil",87,56,65)
print(s1.avg_marks())

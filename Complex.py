class Complex:
    def __init__(self,real, img):
        self.real = real
        self.img = img

    def printNum(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)


num1 = Complex(2,3)
num2 = Complex(1,5)
num3 = num1 + num2
num3.printNum() 

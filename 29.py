#Sum of 2 Complex Numbers

class Complex :
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real,"+",self.img,"i")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img

        return Complex(newReal,newImg)

num1 = Complex(6,4)
num1.showNum()

num2 = Complex(2,3)
num2.showNum()

print("-"*7)

num3 = num1 + num2
num3.showNum()
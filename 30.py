#Finding area of a circle and parameter using classes

class Circle :
    def __init__(self,radius):
        self.radius = radius

    def display(self):
        print("\nArea = ",round(self.area() , 2))
        print("Perimeter = ",round(self.perimeter() , 2))

    def area(self):
        return (self.radius ** 2) * 22/7

    def perimeter(self):
        return 2 * self.radius * 22/7

radius = float(input("\nEnter the radius of a circle : "))
circle1 = Circle(radius)
circle1.display()
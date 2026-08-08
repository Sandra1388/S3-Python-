'''
Define a class Circle with attribute radius.
Create a method get_area() to return the area and another method get_circumference() to return the circumference.
'''

class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def get_area(self):
        radius = self.radius
        ar = 3.14 * radius * radius
        return ar
    
    def get_circumference(self):
        radius = self.radius
        cir = 2 * 3.14 * radius
        return cir
    
radius = int(input("Enter radius:"))
c = Circle(radius)
print("Area = ",c.get_area())
print("Circumference = ",c.get_circumference())

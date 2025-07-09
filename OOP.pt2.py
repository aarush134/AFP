class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.1416  

    def get_area(self):
        return self.pi * self.radius * self.radius

    def get_perimeter(self):
        return 2 * self.pi * self.radius

# Input from user
r = float(input("Enter the radius of the circle: "))

# Create object
circle = Circle(r)

# Output
print(f"Area of the circle: {circle.get_area():.2f}")
print(f"Perimeter of the circle: {circle.get_perimeter():.2f}")

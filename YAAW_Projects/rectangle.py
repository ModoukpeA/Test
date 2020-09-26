class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return (self.length * self.width)

    def perimeter(self):
        return ((self.length + self.width)*2)

obj1 = Rectangle(10,5)
print(obj1.area())
print(obj1.perimeter())
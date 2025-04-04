class rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

l = float(input("Enter length: "))
w = float(input("Enter width: "))
rectangle = rectangle(l, w)
print("Area of rectangleangle:", rectangle.area())

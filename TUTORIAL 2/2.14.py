import math

def area_of_circle(radius):
    if radius <= 0:
        return "Please enter a positive value for radius."
    
    area = math.pi * radius ** 2
    return area

radius = float(input("Enter the radius of the circle: "))

area = area_of_circle(radius)

print(f"The area of the circle with radius {radius} is: {area:.2f}")

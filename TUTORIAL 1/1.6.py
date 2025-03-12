def is_right_angle_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return "The triangle is a right-angled triangle."
    else:
        return "The triangle is not a right-angled triangle."

side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

result = is_right_angle_triangle(side1, side2, side3)

print(result)

import math

def find_roots(a, b, c):
    # Calculate discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"The roots are real and distinct: {root1} and {root2}"
    
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"The root is real and the same: {root}"
    
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i"

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

result = find_roots(a, b, c)
print(result)

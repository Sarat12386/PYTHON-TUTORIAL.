import math

def sin_x(x, n_terms):
    sin_value = 0
    for n in range(n_terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        sin_value += term
    
    return sin_value

x = float(input("Enter the angle in radians: "))
n_terms = int(input("Enter the number of terms: "))

result = sin_x(x, n_terms)

print(f"The value of sin({x}) up to {n_terms} terms is: {result}")

def power(x, y):
    result = 1
    
    for _ in range(y):
        result *= x
    
    return result

x = int(input("Enter the base (X): "))
y = int(input("Enter the exponent (Y): "))

result = power(x, y)

print(f"{x}^{y} = {result}")

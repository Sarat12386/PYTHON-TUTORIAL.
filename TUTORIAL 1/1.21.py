def calculate_expression(n):
    result = 2**(2 * n) + n + 5
    return result

n = int(input("Enter a value for n: "))

result = calculate_expression(n)
print(f"The result of 2^(2n) + n + 5 for n = {n} is: {result}")

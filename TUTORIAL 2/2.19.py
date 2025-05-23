def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the position n to find the Fibonacci number: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = fibonacci(n)
    print(f"The {n}-th Fibonacci number is: {result}")

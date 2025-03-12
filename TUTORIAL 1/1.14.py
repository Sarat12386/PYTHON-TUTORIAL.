def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b  
    return fib_sequence

fib_numbers = fibonacci(10)

print("The first 10 Fibonacci numbers are:")
print(fib_numbers)

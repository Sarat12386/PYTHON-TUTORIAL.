import math

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

if r > n:
    print("r cannot be greater than n.")
else:
    result = nCr(n, r)
    print(f"The value of {n}C{r} is: {result}")

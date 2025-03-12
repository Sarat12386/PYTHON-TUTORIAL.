def sum_of_cubes_of_evens(n):
    total = 0
    for i in range(2, n + 1, 2):  
        total += i ** 3 
    return total


n = int(input("Enter a positive integer: "))


if n <= 0:
    print("Please enter a positive integer.")
else:

    result = sum_of_cubes_of_evens(n)
    print(f"The sum of the cubes of all positive even numbers less than or equal to {n} is: {result}")

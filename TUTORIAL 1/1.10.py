def sum_of_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0: 
            total += num  
    return total

N = int(input("Enter the number of elements: "))

numbers = []
for i in range(N):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

result = sum_of_even_numbers(numbers)

print(f"The sum of even numbers is: {result}")

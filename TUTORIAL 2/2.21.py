def sum_of_even_numbers():
    n = int(input("Enter the number of elements: "))
    
    sum_even = 0
    
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        if num % 2 == 0:  # Check if the number is even
            sum_even += num  # Add it to the sum of even numbers
    
    print(f"The sum of all even numbers is: {sum_even}")

sum_of_even_numbers()

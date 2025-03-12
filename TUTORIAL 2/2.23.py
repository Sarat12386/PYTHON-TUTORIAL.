def find_median():
    numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    
    numbers.sort()
    
    n = len(numbers)
    
    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        median = (numbers[(n // 2) - 1] + numbers[n // 2]) / 2
    
    print(f"The median is: {median}")

find_median()

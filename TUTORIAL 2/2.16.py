def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def check_positive_negative_zero(number):
    if number > 0:
        return f"{number} is positive."
    elif number < 0:
        return f"{number} is negative."
    else:
        return f"{number} is zero."

def generate_factors(number):
    if number <= 0:
        return "Please enter a positive integer."
    
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return f"Factors of {number} are: {', '.join(map(str, factors))}"

def main():
    while True:
        print("\nMenu:")
        print("1. Check Even or Odd")
        print("2. Check Positive, Negative, or Zero")
        print("3. Generate Factors of a Number")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            number = int(input("Enter a number: "))
            print(check_even_odd(number))
        elif choice == '2':
            number = int(input("Enter a number: "))
            print(check_positive_negative_zero(number))
        elif choice == '3':
            number = int(input("Enter a number: "))
            print(generate_factors(number))
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

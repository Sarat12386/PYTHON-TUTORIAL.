def is_prime(num):
    """Function to check if a number is prime."""
    if num <= 1:
        return False  
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return False      
return True  

def separate_prime_composite():
    user_input = input("Enter a list of positive integers separated by spaces: ")
    numbers = list(map(int, user_input.split()))  
    
    primes = []  
    composites = []  
    
    for num in numbers:
        if is_prime(num):
            primes.append(num)  
        elif num > 1:
            composites.append(num)  
    
    print("Prime Numbers:", primes)
    print("Composite Numbers:", composites)

separate_prime_composite()

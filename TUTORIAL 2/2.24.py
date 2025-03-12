from collections import Counter

def find_mode():
    numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    
    count = Counter(numbers)
    
    max_frequency = max(count.values())
    
    mode = [key for key, value in count.items() if value == max_frequency]
    
    if len(mode) == len(numbers):
        print("No mode: All numbers appear the same number of times.")
    else:
        print(f"The mode(s) is/are: {mode}")

find_mode()

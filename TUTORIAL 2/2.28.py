def bubble_sort(arr):
    """Function to sort the list using Bubble Sort."""
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break

def read_and_sort_list():
    """Function to read the list of numbers and sort them."""
    user_input = input("Enter a list of numbers separated by spaces: ")
    
    numbers = list(map(int, user_input.split()))
    
    bubble_sort(numbers)
    
    print("Sorted list in non-decreasing order:", numbers)

read_and_sort_list()

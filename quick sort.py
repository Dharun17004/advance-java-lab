# Quick Sort function
def quick_sort(arr):
    # Base case: if the list has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (here we are choosing the last element)
    pivot = arr[-1]
    
    # Partition the list into two sub-lists
    left = [x for x in arr[:-1] if x <= pivot]   # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]   # Elements greater than pivot
    
    # Recursively sort the left and right sub-lists, and combine them with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)
print("\t\tQuick Sort")
print("\t\t**********")
# Function to get user input
def get_user_input():
    try:
        # Take input from the user
        user_input = input("Enter a list of numbers separated by spaces: ")
        
        # Convert the input string to a list of integers
        arr = list(map(int, user_input.split()))
        
        print("Original Array:", arr)
        sorted_arr = quick_sort(arr)
        print("Sorted Array:", sorted_arr)
    
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")

# Run the function to get user input and sort the array
if __name__ == "__main__":
    get_user_input()

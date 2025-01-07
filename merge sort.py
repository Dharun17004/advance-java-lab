# Merge Sort function
def merge_sort(arr):
    # Base case: if the list has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Step 1: Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Step 2: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Step 3: Merge the sorted halves
    return merge(left_sorted, right_sorted)

# Merge function to combine two sorted lists
def merge(left, right):
    sorted_list = []
    i = j = 0
    
    # Merge the two lists by comparing elements one by one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # If there are any remaining elements in either list, add them
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list
print("\t\tMerge Sort")
print("\t\t**********")
# Function to take user input and perform merge sort
def get_user_input():
    try:
        # Take input from the user
        user_input = input("Enter a list of numbers separated by spaces: ")
        
        # Convert the input into a list of integers
        arr = list(map(int, user_input.split()))
        
        print("Original Array:", arr)
        sorted_arr = merge_sort(arr)
        print("Sorted Array:", sorted_arr)
    
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")

# Run the function to get user input
if __name__ == "__main__":
    get_user_input()

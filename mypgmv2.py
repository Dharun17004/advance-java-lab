def binary_sum(arr, start, end):
    if start > end:
        return 0
    if start == end:
        return arr[end]
    mid = (start + end) // 2
    return binary_sum(arr, start, mid) + binary_sum(arr, mid + 1, end)

print("\t\tBinary Recursion with List")
print("\t\t*******************************")
n=int(input("Enter the number of elements : "))
arr = [int(input(f"Enter the {i+1} element : ")) for i in range(n)]
print("Sum of elements in ", arr, "using binary recursion is :", binary_sum(arr, 0, len(arr)-1))



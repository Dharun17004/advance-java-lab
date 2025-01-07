def linear_sum(arr,n):
    if n==0:
        return 0
    return arr[n-1]+linear_sum(arr,n-1)
print("\t\tLinear Recursion With List")
print("\t\t*********************************")
n=int(input("Enter the number of Elements : "))
arr=[]
for i in range(n):
    element=int(input(f"Enter the {i+1} element : "))
    arr.append(element)
print("Sum Of elements in ",arr,"using linear recursion is :",linear_sum(arr,len(arr)))

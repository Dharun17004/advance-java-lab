def push(stack):
    """Pushes an element onto the stack."""
    element = int(input("Enter element to push: "))
    stack.append(element)
    print(f"Element {element} pushed successfully.")

def pop(stack):
    """Pops an element from the stack."""
    if not stack:
        print("Stack is empty.")
    else:
        element = stack.pop()
        print("Popped element:", element)

def peek(stack):
    """Peeks at the top element of the stack."""
    if not stack:
        print("Stack is empty.")
    else:
        print("Top element:", stack[-1])

def display(stack):
    """Displays the elements of the stack."""
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack:", stack)
def length(stack):
    """Displays the elements of the stack."""
    if not stack:
        print("Stack is empty.")
    else:
        print(f"Length of Stack {stack} is :", len(stack))

def main():
    """Main function to drive the menu."""
    stack = []

    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Length")
        print("5. Display")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            push(stack)
        elif choice == 2:
            pop(stack)
        elif choice == 3:
            peek(stack)
        elif choice == 4:
            length(stack)   
        elif choice == 5:
            display(stack)
        elif choice == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

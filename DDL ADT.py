class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        if self.is_empty():
            print("List is empty!")
            return

        temp = self.head

        if temp is not None and temp.data == data:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            temp = None
            return

        while temp and temp.data != data:
            temp = temp.next

        if temp is None:
            print(f"Node with value {data} not found!")
            return

        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
        temp = None

    def display(self):
        if self.is_empty():
            print("List is empty!")
            return
        temp = self.head
        elements = []
        while temp:
            elements.append(temp.data)
            temp = temp.next
        print("Doubly Linked List:", elements)

    def forward_traversal(self):
        if self.is_empty():
            print("List is empty!")
            return
        temp = self.head
        elements = []
        while temp:
            elements.append(temp.data)
            temp = temp.next
        print("Forward Traversal:", elements)

    def backward_traversal(self):
        if self.is_empty():
            print("List is empty!")
            return
        temp = self.head
        while temp.next:  # Move to the last node
            temp = temp.next
        elements = []
        while temp:
            elements.append(temp.data)
            temp = temp.prev
        print("Backward Traversal:", elements)

    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                print(f"Node with value {data} found!")
                return
            temp = temp.next
        print(f"Node with value {data} not found!")

    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


def menu():
    dll = DoublyLinkedList()

    while True:
        print("\nMenu:")
        print("1. Append (Insert at end)")
        print("2. Prepend (Insert at beginning)")
        print("3. Delete a node")
        print("4. Display the list")
        print("5. Search for a node")
        print("6. Size of the list")
        print("7. Forward Traversal")
        print("8. Backward Traversal")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            data = int(input("Enter the data to append: "))
            dll.append(data)
            print(f"{data} appended at the end")
        elif choice == '2':
            data = int(input("Enter the data to prepend: "))
            dll.prepend(data)
            print(f"{data} inserted  at the beginning")
        elif choice == '3':
            data = int(input("Enter the data to delete: "))
            dll.delete(data)
            print(f"{data} deleted from the Doubly Linked List")
        elif choice == '4':
            dll.display()
        elif choice == '5':
            data = int(input("Enter the data to search for: "))
            dll.search(data)
        elif choice == '6':
            print("Size of the Doubly Linked List:", dll.size())
        elif choice == '7':
            dll.forward_traversal()
        elif choice == '8':
            dll.backward_traversal()
        elif choice == '9':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

# Start the menu
if __name__ == "__main__":
    menu()

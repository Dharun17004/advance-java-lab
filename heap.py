import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        """Push an item with a given priority into the priority queue."""
        heapq.heappush(self.heap, (priority, item))
        print(f'Inserted: ({priority}, "{item}")')

    def pop(self):
        """Remove and return the item with the highest priority (lowest priority number)."""
        if self.is_empty():
            print("Priority Queue is empty!")
            return None
        return heapq.heappop(self.heap)[1]

    def peek(self):
        """Return the item with the highest priority WITHOUT removing it."""
        if self.is_empty():
            print("Priority Queue is empty!")
            return None
        return self.heap[0][1]  # ✅ Just returns the item, does NOT remove it

    def remove_by_priority(self, priority):
        """Remove an item with a specific priority."""
        found = False
        for i in range(len(self.heap)):
            if self.heap[i][0] == priority:  # Find item with matching priority
                del self.heap[i]  # Remove from list
                heapq.heapify(self.heap)  # Rebuild heap to maintain properties
                found = True
                print(f"Removed item with priority {priority}")
                break

        if not found:
            print(f"No item found with priority {priority}")

    def display(self):
        """Display the priority queue elements in sorted order (for visualization)."""
        if self.is_empty():
            print("Priority Queue is empty!")
        else:
            print("\nPriority Queue elements (sorted by priority):")
            for priority, item in sorted(self.heap):  # Sorted for correct display
                print(f'({priority}, "{item}")')

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.heap) == 0

    def size(self):
        """Return the number of elements in the priority queue."""
        return len(self.heap)

# Interactive User Input
def menu():
    pq = PriorityQueue()
    while True:
        print("\nPriority Queue Operations:")
        print("1. Insert (Push)")
        print("2. Remove Highest Priority (Pop)")
        print("3. View Highest Priority (Peek)")
        print("4. Remove Specific Priority")
        print("5. Display Priority Queue")
        print("6. Get Queue Size")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            item = input("Enter the task/item: ")
            while True:
                try:
                    priority = int(input("Enter the priority (lower is higher priority): "))
                    break  # Exit loop if valid
                except ValueError:
                    print("Invalid input! Please enter an integer for priority.")
            pq.push(item, priority)
        elif choice == '2':
            removed = pq.pop()
            if removed is not None:
                print(f"Removed: {removed}")
        elif choice == '3':
            highest = pq.peek()
            if highest is not None:
                print(f"Highest Priority Item: {highest}")  # ✅ Now it only displays
        elif choice == '4':
            while True:
                try:
                    priority = int(input("Enter the priority to remove: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter an integer for priority.")
            pq.remove_by_priority(priority)
        elif choice == '5':
            pq.display()
        elif choice == '6':
            print(f"Queue Size: {pq.size()}")
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

# Run the menu
menu()

class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty. Cannot dequeue.")
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty. Cannot peek.")
    def display(self):
        if not self.is_empty():
            print("Queue contents:")
            for item in self.items:
                print(item)
        else:
                print("Queue is empty")
    def size(self):
        return len(self.items)
queue = Queue()
while True:
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Size")
    print("5. Display")
    print("6. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        item = input("Enter the item to enqueue: ")
        queue.enqueue(item)
        print(f"{item} enqueued to the queue.")
    elif choice == "2":
        dequeued_item = queue.dequeue()
        if dequeued_item is not None:
            print(f"{dequeued_item} dequeued from the queue.")
    elif choice == "3":
        peeked_item = queue.peek()
        if peeked_item is not None:
            print(f"Front item in the queue: {peeked_item}")
    elif choice == "4":
        print(f"Size of the queue: {queue.size()}")
    elif choice == "5":
        queue.display()
    elif choice == "6":
        print("Exiting the program.")
        break
    else: 
        print("Invalid choice. Please enter a number between 1 and 5")
 

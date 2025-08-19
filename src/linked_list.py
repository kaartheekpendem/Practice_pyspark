class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node by value
    def delete(self, key):
        curr = self.head

        # If head node holds the key
        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return

        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if not curr:
            return  # Key not found

        prev.next = curr.next
        curr = None

    # Print the list
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.display()       # Output: 5 -> 10 -> 20 -> None
ll.delete(10)
ll.display()       # Output: 5 -> 20 -> None



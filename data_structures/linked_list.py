class Node:
  def __init__(self, data) -> None:
    self.data = data  # Store data
    self.next = None  # Store reference to the next node

class LinkedList:
  def __init__(self) -> None:
    self.head = None  # Initialize the head of the list

  # Method to add a node at the end of the list
  def append(self, data) -> None:
    new_node = Node(data)

    if not self.head:
      self.head = new_node
      return

    curr_node = self.head
    while (curr_node.next):
      curr_node = curr_node.next

    curr_node.next = new_node

  # Method to print the linked list
  def print_list(self) -> None:
    current = self.head
    while (current):
      print(current.data, end = " -> ")
      current = current.next

    print("None")

  # Method to insert a node at the beginning of the linked list
  def prepend(self, data) -> None:
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  # Method to delete a node
  def delete(self, key) -> None:
    current = self.head

    if (current and current.data == key):
      self.head = current.next
      current = None
      return

    prev = None
    while (current and current.data != key):
      prev = current
      current = current.next

    if current is not None:
      prev.next = current.next

    current = None


# Create a linked list and add some nodes
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

# Print the linked list
ll.print_list()

# Insert a node at the beginning
ll.prepend(0)
ll.print_list()

# Delete a node
ll.delete(2)
ll.print_list()
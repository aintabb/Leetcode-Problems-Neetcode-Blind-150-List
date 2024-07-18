from typing import Optional, Union

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val  = val   # Store data
        self.next = next  # Store reference to the next node


class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random


class LinkedList:
  def __init__(self) -> None:
    self.head = None  # Initialize the head of the list

  # Method to add a list node or a node at the end of the list
  def append(self, data, **kwargs) -> Union[ListNode, Node]:
    new_node = ListNode(data) if 'random' not in kwargs else Node(data, None, kwargs['random'])

    if not self.head:
      self.head = new_node

      return self.head

    curr_node = self.head
    while (curr_node.next):
      curr_node = curr_node.next

    curr_node.next = new_node

    return new_node

  # Method to insert a node at the beginning of the linked list
  def prepend(self, data) -> None:
    new_node      = ListNode(data)
    new_node.next = self.head
    self.head     = new_node

  # Method to delete a node
  def delete(self, key) -> None:
    current = self.head

    if (current and current.val == key):
      self.head = current.next
      current = None
      return

    prev = None
    while (current and current.val != key):
      prev = current
      current = current.next

    if current is not None:
      prev.next = current.next

    current = None

  # Method to print all the nodes in a linked list
  def print_list(self, head)-> None:
        if not head:
            print("None")
            return

        curr = head
        while (curr):
            print(curr.val, end = " -> ")

            if isinstance(curr, Node) and curr.random:
              print("random:", curr.random.val, end = " -> ")
            curr = curr.next

        print("None")

  # Method to compare equality between two linked list
  def compare_lists(self, head_one, head_two) -> bool:
      current_one = head_one
      current_two = head_two

      while (current_one and current_two):
          if (current_one.val != current_two.val):
              return False

          if (isinstance(current_one, Node) and isinstance(current_two, Node)):
            if ((current_one.random and current_two.random and current_one.random.val != current_two.random.val) or
             (not current_one.random) != (not current_two.random)):
              return False

          current_one = current_one.next
          current_two = current_two.next

      return current_one is None and current_two is None

  # Method to create a copy of a linked list
  def copy_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head:
          return None

      new_head      = ListNode(head.val)
      curr_new_node = new_head
      old_next      = head.next

      while (old_next):
          new_node           = ListNode(old_next.val)
          curr_new_node.next = new_node
          curr_new_node      = new_node
          old_next           = old_next.next

      return new_head

# Create a linked list and add some nodes
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

# Print a linked list
# ll.print_list(ll.head)

# Insert a node at the beginning
ll.prepend(0)
# ll.print_list(ll.head)

# Delete a node
ll.delete(2)
# ll.print_list(ll.head)

# Copy a linked list
ll_copy      = LinkedList()
ll_copy.head = ll.copy_list(ll.head)
# ll.print_list(ll.head)

# Compare two linked lists for equality
# print(ll.compare_lists(ll.head, ll_copy.head))
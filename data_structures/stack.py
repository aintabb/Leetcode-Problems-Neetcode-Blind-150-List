
class Stack:
  def __init__(self) -> None:
    self.items = []

  """
  Push an item to the stack.
  Time Complexity:  O(1)
  Space Complexity: O(1)

  Parameters:
    item: the item to be added to the stack

  Returns:
    None
  """
  def push(self, item) -> None:
    self.items.append(item)

  """
  Pop and return the top element from the stack.
  Time Complexity:  O(1)
  Space Complexity: O(1)

  Parameters:
    None

  Returns:
    int: The popped item from the stack
  """
  def pop(self) -> int:
    return self.items.pop()

  """
  Returns size of the stack
  Time Complexity:  O(1)
  Space Complexity: O(1)

  Parameters:
    None

  Returns:
    int: Size of the stack
  """
  def size(self) -> int:
    return len(self.items)

  """
  Checks whether given stack is empty or not
  Time Complexity:  O(1)
  Space Complexity: O(1)

  Parameters:
    None

  Returns:
    bool: True; if the stack is not empty
          False; otherwise
  """
  def is_empty(self) -> bool:
    return len(self.items) == 0

  """
  Returns the top item from the stack without removing it
  Time Complexity:  O(1)
  Space Complexity: O(1)

  Parameters:
    None

  Returns:
    int: The top item from the stack
  """
  def peek(self) -> int:
    return self.items[-1]

# Initialize a stack instance
stack = Stack()

stack.push(1)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(7)

# Perform several operations to validate and test stack functions are working fine
stack.pop()
popped_val = stack.pop()
assert popped_val == 5, "stack.pop() should return 5" # ? String literal
print(popped_val)

peeked_val = stack.peek()
assert peeked_val == 4, "stack.peek() should return 4"
print(peeked_val)

size_of_stack = stack.size()
assert size_of_stack == 3, "stack.size() should return 3"
print(size_of_stack)

is_stack_empty = stack.is_empty()
assert is_stack_empty == False, "stack.is_empty() should return false"
print(is_stack_empty)

stack.pop()
stack.pop()
stack.pop()

is_stack_empty = stack.is_empty()
assert is_stack_empty == True, "stack.is_empty() should return true"
print(is_stack_empty)

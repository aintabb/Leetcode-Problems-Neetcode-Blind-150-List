'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.



Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:
- -231 <= val <= 231 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''


# Time Complexity:  O(1)
# Space Complexity: O(N)
class MinStack:
    def __init__(self) -> None:
      self.item_stack = []
      self.min_stack  = []

    def push(self, val: int) -> None:
      self.item_stack.append(val)
      val = min(val, self.min_stack[-1] if self.min_stack else val)
      self.min_stack.append(val)

    def pop(self) -> None:
      self.item_stack.pop()
      self.min_stack.pop()

    def top(self) -> int:
      return self.item_stack[-1]

    def getMin(self) -> int:
      return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Create an instance of the class
min_stack = MinStack()
ops_dict = {
  "MinStack": None,
  "push": min_stack.push,
  "pop": min_stack.pop,
  "top": min_stack.top,
  "getMin": min_stack.getMin
}

err_msg_invalid_result = "Provided result is not correct for the given function. Something is wrong!"

# Test Case - 1
ops   = ["MinStack","push","push","push","getMin","pop","top","getMin"]
vals  = [[],[-2],[0],[-3],[],[],[],[]]

# Not a clever way to test this, but it works for our purposes
for op, val in zip(ops, vals):
  if op == "MinStack":
    min_stack = MinStack()
    continue

  if (op == "push"):
    result = ops_dict[op](val[0])
  else:
    result = ops_dict[op]()

  if (op == "getMin"):
    assert result in {-3, -2}, err_msg_invalid_result
    print(result)
  elif (op == "top"):
    assert result in {0}, err_msg_invalid_result
    print(result)

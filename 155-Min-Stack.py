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

Output:
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

Example 2:
Input
["MinStack","push","push","push","push","push","push","push", "pop", "pop", "pop", "getMin"]
[[],[8],[2],[3],[4],[0],[1],[5], [], [], [], []]

Output:
[null,null,null,null,null,null,null,null,0,null,5]

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

ops_dict = {
  "MinStack": MinStack,
  "push": MinStack.push,
  "pop": MinStack.pop,
  "top": MinStack.top,
  "getMin": MinStack.getMin
}

err_msg_invalid_result = "Provided result is not correct for the given function. Something is wrong!"

test_cases  = []

# Test Case - 1
ops_one   = ["MinStack","push","push","push","getMin","pop","top","getMin"]
vals_one  = [[],[-2],[0],[-3],[],[],[],[]]
expected_results = [None, None, None, None, -3, None, 0, -2]

test_cases.append((ops_one, vals_one, expected_results))

# Test Case - 2
ops_two = ["MinStack","push","push","push","push","push","push","push", "pop", "pop", "pop", "getMin"]
vals_two = [[],[8],[2],[3],[4],[0],[1],[5], [], [], [], []]
expected_results = [None, None, None, None, None, None, None, None, None, None, None, 2]

test_cases.append((ops_two, vals_two, expected_results))

for i in range(len(test_cases)):
  # Not a clever way to test this, but it works for our purposes
  for op, val, expected_result in zip(test_cases[i][0], test_cases[i][1], test_cases[i][2]):
    if op == "MinStack":
      min_stack = MinStack()
      # Update the "min_stack" instance
      ops_dict[op] = min_stack
      continue

    if (op == "push"):
      result = ops_dict[op](min_stack, val[0])
    else:
      result = ops_dict[op](min_stack)

    assert result == expected_result, err_msg_invalid_result
    print(result)

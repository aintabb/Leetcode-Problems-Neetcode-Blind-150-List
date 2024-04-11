'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


# Time Complexity:  O(N)
# Space Complexity: O(N)
class ValidParentheses:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s = "()"

        result = self.is_valid(s)
        assert result == True, err_msg_invalid_result
        print(result)

        s = "()[]{}"

        result = self.is_valid(s)
        assert result == True, err_msg_invalid_result
        print(result)

        s = "(]"

        result = self.is_valid(s)
        assert result == False, err_msg_invalid_result
        print(result)

        s = "){"

        result = self.is_valid(s)
        assert result == False, err_msg_invalid_result
        print(result)


    """
      Check if given string has matching parenthesis in order

      Args:
          s (str): An input string that contains parenthesis

      Returns:
        bool: Return True, if every opening parenthesis has a closing one
              False, otherwise
    """
    def is_valid(self, s: str) -> bool:
      if (len(s) == 1 or len(s) % 2 != 0):
        return False

      p_stack = []
      # Map closing parenthesis
      p_map   = { "}": "{", ")": "(", "]": "[" }

      for ch in s:
        # If we came across to a closing parenthesis
        if (ch in p_map):
          # Make sure if the stack is not empty and parenthesis matches
          if (p_stack and p_stack[-1] == p_map[ch]):
            p_stack.pop()
          else:
            return False
        else:
          p_stack.append(ch)

      # At the end, the stack should be empty since we pop every matching parenthesis
      return True if not p_stack else False


# Create an instance of the class
valid_parentheses = ValidParentheses()
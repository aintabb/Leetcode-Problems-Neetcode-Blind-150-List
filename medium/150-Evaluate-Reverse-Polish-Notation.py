"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:
1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""


# Time Complexity:  O(N)
# Space Complexity: O(N)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        tokens = ["2", "1", "+", "3", "*"]

        result = self.evalRPN(tokens)
        assert result == 9, err_msg_invalid_result
        print(result)

        tokens = ["4", "13", "5", "/", "+"]

        result = self.evalRPN(tokens)
        assert result == 6, err_msg_invalid_result
        print(result)

        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

        result = self.evalRPN(tokens)
        assert result == 22, err_msg_invalid_result
        print(result)

    def evalRPN(self, tokens: list[str]) -> int:
        if not tokens:
            return 0

        token_stack = []

        for token in tokens:
            match token:
                case "+":
                    num_one, num_two = int(token_stack.pop()), int(token_stack.pop())
                    token_stack.append(num_one + num_two)
                case "-":
                    num_one, num_two = int(token_stack.pop()), int(token_stack.pop())
                    token_stack.append(num_two - num_one)
                case "*":
                    num_one, num_two = int(token_stack.pop()), int(token_stack.pop())
                    token_stack.append(num_one * num_two)
                case "/":
                    num_one, num_two = int(token_stack.pop()), int(token_stack.pop())
                    token_stack.append(int(num_two / num_one))
                case _:
                    token_stack.append(int(token))

        return token_stack[-1]


# Create an instance of the class
solution = Solution()

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]


Constraints:
1 <= n <= 8
"""

"""
# Time Complexity:  O(4^n / sqrt(n))

This time complexity arises from the recursive backtracking approach used to generate valid parentheses combinations. At each recursive call, there are two choices: either add an opening parenthesis or add a closing parenthesis. Since we have to generate all valid combinations of parentheses for a given n, the total number of function calls made is proportional to the number of valid combinations.

The number of valid combinations is given by the n-th Catalan number, which is approximately 4^n / (n * sqrt(n)). This is because for a given n, there are 2n positions where we can place either an opening or a closing parenthesis, leading to a total of 2^(2n) possible combinations. However, because we need well-formed parentheses, we divide by n+1 to get the n-th Catalan number, which is O(4^n / sqrt(n)).
"""


# Space Complexity: O(N)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        n = 3

        result = self.generate_parenthesis(n)
        assert result == [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()",
        ], err_msg_invalid_result
        print(result)

        n = 2

        result = self.generate_parenthesis(n)
        assert result == ["(())", "()()"], err_msg_invalid_result
        print(result)

        n = 1

        result = self.generate_parenthesis(n)
        assert result == ["()"], err_msg_invalid_result
        print(result)

    def generate_parenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ["()"]

        result = []
        p_stack = []

        def backtrack(open: int, close: int) -> None:
            # Valid if open count == n == closed count, terminate
            if open == n == close:
                result.append("".join(p_stack))
                return

            # Only add a opening parenthesis if open < n
            if open < n:
                p_stack.append("(")
                backtrack(open + 1, close)
                p_stack.pop()

            # Only add a closing parenthesis if closing < opening
            if close < open:
                p_stack.append(")")
                backtrack(open, close + 1)
                p_stack.pop()

        backtrack(0, 0)
        return result


# Create an instance of the class
solution = Solution()

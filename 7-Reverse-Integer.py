"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21


Constraints:
-231 <= x <= 231 - 1
"""


# Time Complexity:  O(1)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        x = 123

        result = self.reverse(x)
        assert result == 321, err_msg_invalid_result
        print(result)

        x = -123

        result = self.reverse(x)
        assert result == -321, err_msg_invalid_result
        print(result)

        x = 120

        result = self.reverse(x)
        assert result == 21, err_msg_invalid_result
        print(result)


    def reverse(self, x: int) -> int:
        reversed_str = str(abs(x))[::-1]

        result = int(reversed_str) * (-1 if x < 0 else 1)
        int_limit = 2**31 - 1

        if (result > int_limit or result < -int_limit):
            return 0
        return result


# Create an instance of the class
solution = Solution()
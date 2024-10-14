"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.



Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5


Constraints:
-1000 <= a, b <= 1000
"""


# Time Complexity:  O(1)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        a, b = 1, 2

        result = self.get_sum(a, b)
        assert result == 3, err_msg_invalid_result
        print(result)

        a, b = 2, 3

        result = self.get_sum(a, b)
        assert result == 5, err_msg_invalid_result
        print(result)


    def get_sum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFF

        while (b != 0):
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask

        return a if a < 0x7FFFFFF else ~(a ^ mask)


# Create an instance of the class
solution = Solution()
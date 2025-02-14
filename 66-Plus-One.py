"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""


# Time Complexity:  O(N)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        digits = [1, 2, 3]

        result = self.plus_one(digits)
        assert result == [1, 2, 4], err_msg_invalid_result
        print(result)

        digits = [4, 3, 2, 1]

        result = self.plus_one(digits)
        assert result == [4, 3, 2, 2], err_msg_invalid_result
        print(result)

        digits = [9]

        result = self.plus_one(digits)
        assert result == [1, 0], err_msg_invalid_result
        print(result)

        digits = [9, 9, 9]

        result = self.plus_one(digits)
        assert result == [1, 0, 0, 0], err_msg_invalid_result
        print(result)


    def plus_one(self, digits: list[int]) -> list[int]:
        len_digits = len(digits)

        for i in range(len_digits - 1, -1, -1):
            if (digits[i] + 1 == 10):
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        return [1] + digits


# Create an instance of the class
solution = Solution()
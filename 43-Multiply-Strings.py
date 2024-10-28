"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


# Time Complexity:  O(len(num1)*len(num2))
# Space Complexity: O(len(num1)+len(num2))
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        num1, num2 = "2", "3"

        result = self.multiply(num1, num2)
        assert result == "6", err_msg_invalid_result
        print(result)

        num1, num2 = "123", "456"

        result = self.multiply(num1, num2)
        assert result == "56088", err_msg_invalid_result
        print(result)


    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        len_num1, len_num2 = len(num1), len(num2)

        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0] * (len_num1 + len_num2)

        for i in range(len_num1):
            for j in range(len_num2):
                digit = int(num1[i]) * int(num2[j])
                result[i + j] += digit
                result[i + j + 1] += result[i + j] // 10
                result[i + j] = result[i + j] % 10

        result = result[::-1]
        beginning = 0

        while (beginning < len(result) and result[beginning] == 0):
            beginning += 1

        result = map(str, result[beginning:])
        return "".join(result)


# Create an instance of the class
solution = Solution()
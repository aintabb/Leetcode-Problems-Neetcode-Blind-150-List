"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""


# Time Complexity:  O(logN)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        x, n = 2.00000, 10

        result = self.my_pow(x, n)
        assert result == 1024.00000, err_msg_invalid_result
        print(result)

        x, n = 2.10000, 3

        result = self.my_pow(x, n)
        assert result == 9.26100, err_msg_invalid_result
        print(result)

        x, n = 2.00000, -2

        result = self.my_pow(x, n)
        assert result == 0.25000, err_msg_invalid_result
        print(result)


    def my_pow(self, x: float, n: int) -> float:

        def helper(x: float, n: int) -> float:
            # Base Cases:
            if (x == 0):
                return 0

            if (n == 0):
                return 1

            result = helper(x, n // 2)
            result *= result

            return result if n % 2 == 0 else result * x

        result = helper(x, abs(n))
        return round(result if n >= 0 else 1 / result, 5)


# Create an instance of the class
solution = Solution()
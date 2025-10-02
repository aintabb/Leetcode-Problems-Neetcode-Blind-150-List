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
        assert abs(result - 1024.00000) < 0.00001, err_msg_invalid_result
        print(result)

        x, n = 2.10000, 3

        result = self.my_pow(x, n)
        assert abs(result - 9.26100) < 0.00001, err_msg_invalid_result
        print(result)

        x, n = 2.00000, -2

        result = self.my_pow(x, n)
        assert abs(result - 0.25000) < 0.00001, err_msg_invalid_result
        print(result)

    def my_pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.my_pow(x, -n)
        if n % 2 == 0:
            return self.my_pow(x * x, n // 2)
        else:
            return x * self.my_pow(x * x, n // 2)


# Create an instance of the class
solution = Solution()

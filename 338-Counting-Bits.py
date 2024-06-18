"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



Example 1:
Input: n = 2
Output: [0,1,1]

Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]

Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:
0 <= n <= 105


Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""


# Time Complexity:  O(N)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        n = 2

        result = self.count_bits_dp(n)
        assert result == [0, 1, 1], err_msg_invalid_result
        print(result)

        result = self.count_bits_shifting(n)
        assert result == [0, 1, 1], err_msg_invalid_result
        print(result)

        n = 5

        result = self.count_bits_dp(n)
        assert result == [0, 1, 1, 2, 1, 2], err_msg_invalid_result
        print(result)

        result = self.count_bits_shifting(n)
        assert result == [0, 1, 1, 2, 1, 2], err_msg_invalid_result
        print(result)


    def count_bits_dp(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if (offset * 2 == i):
                offset = i

            dp[i] = 1 + dp[i - offset]

        return dp

    def count_bits_shifting(self, n: int) -> list[int]:
        result = [0] * (n + 1)

        for i in range(n + 1):
            result[i] = result[i >> 1] + (i & 1)

        return result


# Create an instance of the class
solution = Solution()
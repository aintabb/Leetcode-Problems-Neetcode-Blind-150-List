"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:
1 <= n <= 45
"""


# Time Complexity:  O(2^N) -> R, O(N) -> T, with Memory or no memory
# Space Complexity: O(N) -> R, T with memory, O(1) -> T with no memory
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        n = 2

        # Recursive
        result = self.climb_stairs_recursive(n)
        assert result == 2, err_msg_invalid_result
        print(result, end=" - Recursive\n")

        # Tabulation - DP, extra space
        result = self.climb_stairs_tabulation_with_memory(n)
        assert result == 2, err_msg_invalid_result
        print(result, end=" - Tabulation - DP, extra space\n")

        # Tabulation - DP, no space
        result = self.climb_stairs_tabulation_with_memory(n)
        assert result == 2, err_msg_invalid_result
        print(result, end=" - Tabulation - DP, no space\n")

        n = 3

        # Recursive
        result = self.climb_stairs_recursive(n)
        assert result == 3, err_msg_invalid_result
        print(result, end=" - Recursive\n")

        # Tabulation - DP, extra space
        result = self.climb_stairs_tabulation_with_memory(n)
        assert result == 3, err_msg_invalid_result
        print(result, end=" - Tabulation - DP, extra space\n")

        # Tabulation - DP, no space
        result = self.climb_stairs_tabulation_no_memory(n)
        assert result == 3, err_msg_invalid_result
        print(result, end=" - Tabulation - DP, no space\n")

    # Possible Time limit exceeding issue
    def climb_stairs_recursive(self, n: int) -> int:
        # Base Case
        if (n == 0):
            return 1

        if (n < 0):
            return 0

        return (self.climb_stairs_recursive(n - 1) + self.climb_stairs_recursive(n - 2))

    def climb_stairs_tabulation_with_memory(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def climb_stairs_tabulation_no_memory(self, n: int) -> int:
        second = 1
        first = 1

        for _ in range(2, n + 1):
            num_of_steps = second + first
            first = second
            second = num_of_steps

        return num_of_steps


# Create an instance of the class
solution = Solution()
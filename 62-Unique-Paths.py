"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2**109.



Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3


Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:
1 <= m, n <= 100
"""


# Time Complexity:  O(M*N) - Same for both technique
# Space Complexity: O(M*N) - Same for both technique
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        # DP - Tabulation
        m, n = 1, 1
        result = self.unique_paths_tabulation(m, n)
        assert result == 1, err_msg_invalid_result
        print(result)

        # DP - Memoization
        m, n = 1, 1
        result = self.unique_paths_memoization(m, n)
        assert result == 1, err_msg_invalid_result
        print(result)

        # DP - Tabulation
        m, n = 3, 7
        result = self.unique_paths_tabulation(m, n)
        assert result == 28, err_msg_invalid_result
        print(result)

        # DP - Memoization
        m, n = 3, 7
        result = self.unique_paths_memoization(m, n)
        assert result == 28, err_msg_invalid_result
        print(result)

        # DP - Tabulation
        m, n = 3, 2
        result = self.unique_paths_tabulation(m, n)
        assert result == 3, err_msg_invalid_result
        print(result)

        # DP - Memoization
        m, n = 3, 2
        result = self.unique_paths_memoization(m, n)
        assert result == 3, err_msg_invalid_result
        print(result)


    def unique_paths_tabulation(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]


    def unique_paths_memoization(self, m: int, n: int) -> int:
        def memo_helper(row: int, col: int) -> int:
            # Base Cases
            if (row == 0 or col == 0):
                return 1

            if (row < 0 or col < 0):
                return 0

            if ((row, col) in cache):
                return cache[(row, col)]

            cache[(row, col)] = memo_helper(row - 1, col) + memo_helper(row, col - 1)

            return cache[(row, col)]

        cache = {}
        return memo_helper(m - 1, n - 1)


# Create an instance of the class
solution = Solution()
"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""


# Time Complexity:  O(3^(m+n)) -> R, O(m*n) -> T, M
# Space Complexity: O(m+n) -> R, O(m*n) -> T, M
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        word1, word2 = "horse", "ros"

        # DP, Tabulation
        result = self.min_distance_tabulation(word1, word2)
        assert result == 3, err_msg_invalid_result
        print(result, end=" - DP, Tabulation\n")

        # DP, Memoization
        result = self.min_distance_memoization_top_down(word1, word2)
        assert result == 3, err_msg_invalid_result
        print(result, end=" - DP, Memoization\n")

        word1, word2 = "intention", "execution"

        # DP, Tabulation
        result = self.min_distance_tabulation(word1, word2)
        assert result == 5, err_msg_invalid_result
        print(result, end=" - Tabulation\n")

        # DP, Memoization
        result = self.min_distance_memoization_top_down(word1, word2)
        assert result == 5, err_msg_invalid_result
        print(result, end=" - Memoization\n")

    def min_distance_memoization_top_down(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0

        dist_cache = {}

        def helper(i: int, j: int) -> int:
            if not i and not j:
                return 0

            if not i:
                return j

            if not j:
                return i

            if (i, j) in dist_cache:
                return dist_cache[(i, j)]

            if word1[i - 1] == word2[j - 1]:
                dist_cache[(i, j)] = helper(i - 1, j - 1)
            else:
                ins = 1 + helper(i, j - 1)
                delt = 1 + helper(i - 1, j)
                subst = 1 + helper(i - 1, j - 1)

                dist_cache[(i, j)] = min(ins, delt, subst)

            return dist_cache[(i, j)]

        return helper(len(word1), len(word2))

    def min_distance_tabulation(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0

        ROWS, COLS = len(word1), len(word2)
        dp = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]

        for row in range(ROWS + 1):
            dp[row][0] = row

        for col in range(COLS + 1):
            dp[0][col] = col

        for row in range(1, ROWS + 1):
            for col in range(1, COLS + 1):
                ins = 1 + dp[row][col - 1]
                delt = 1 + dp[row - 1][col]

                subst = dp[row - 1][col - 1]
                if word1[row - 1] != word2[col - 1]:
                    subst += 1

                dp[row][col] = min(ins, delt, subst)

        return dp[ROWS][COLS]


# Create an instance of the class
solution = Solution()

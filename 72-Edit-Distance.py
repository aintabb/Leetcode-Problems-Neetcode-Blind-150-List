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

        # Recursive
        result = self.min_distance_recursive(word1, word2)
        assert result == 3, err_msg_invalid_result
        print(result, end=" - Recursive\n")

        # DP, Tabulation
        result = self.min_distance_tabulation(word1, word2)
        assert result == 3, err_msg_invalid_result
        print(result, end=" - DP, Tabulation\n")

        # DP, Memoization
        result = self.min_distance_memoization(word1, word2)
        assert result == 3, err_msg_invalid_result
        print(result, end=" - DP, Memoization\n")

        word1, word2 = "intention", "execution"

        # Recursive
        result = self.min_distance_recursive(word1, word2)
        assert result == 5, err_msg_invalid_result
        print(result, end=" - Recursive\n")

        # DP, Tabulation
        result = self.min_distance_tabulation(word1, word2)
        assert result == 5, err_msg_invalid_result
        print(result, end=" - Tabulation\n")

         # DP, Memoization
        result = self.min_distance_memoization(word1, word2)
        assert result == 5, err_msg_invalid_result
        print(result, end=" - Memoization\n")


    def min_distance_recursive(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        def distance_helper(m, n) -> int:
            if (m == 0 and n == 0):
                return 0

            if (m == 0 and n > 0):
                return n

            if (m > 0 and n == 0):
                return m

            if (word1[m - 1] == word2[n - 1]):
                return distance_helper(m - 1, n - 1)
            else:
                return 1 + min(distance_helper(m - 1, n),
                               distance_helper(m, n - 1),
                               distance_helper(m - 1, n - 1))

        return distance_helper(m, n)

    def min_distance_tabulation(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            dp[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                insertion = 1 + dp[i][j - 1]
                deletion = 1 + dp[i - 1][j]

                substitution = dp[i - 1][j - 1]
                if (word1[i - 1] != word2[j - 1]):
                    substitution += 1

                dp[i][j] = min(insertion, deletion, substitution)

        return dp[m][n]

    def min_distance_memoization(self, word1: str, word2: str) -> int:
        def dp_memo(i: int, j: int) -> int:
            if i == 0: return j
            if j == 0: return i

            if (i, j) in cache:
                return cache[(i, j)]

            if (word1[i - 1] == word2[j - 1]):
                cache[(i, j)] = dp_memo(i - 1, j - 1)
            else:
                insertion = 1 + dp_memo(i, j - 1)
                deletion = 1 + dp_memo(i - 1, j)
                substitution = 1 + dp_memo(i - 1, j - 1)

                cache[(i, j)] = min(insertion, deletion, substitution)

            return cache[(i, j)]

        cache = {}
        return dp_memo(len(word1), len(word2))


# Create an instance of the class
solution = Solution()
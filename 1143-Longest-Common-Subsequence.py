"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""


# Time Complexity:  O(len(text1)*len(text2)) -> for both
# Space Complexity: O(len(text1)*len(text2)) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        text1, text2  = "abcde", "ace"

        result = self.longest_common_subsequence_memo(text1, text2)
        assert result == 3, err_msg_invalid_result
        print(result)

        result = self.longest_common_subsequence_tabulation(text1, text2)
        assert result == 3, err_msg_invalid_result
        print(result)

        text1, text2 = "abc", "abc"

        result = self.longest_common_subsequence_memo(text1, text2)
        assert result == 3, err_msg_invalid_result
        print(result)

        result = self.longest_common_subsequence_tabulation(text1, text2)
        assert result == 3, err_msg_invalid_result
        print(result)

        text1, text2 = "abc", "def"

        result = self.longest_common_subsequence_memo(text1, text2)
        assert result == 0, err_msg_invalid_result
        print(result)

        result = self.longest_common_subsequence_tabulation(text1, text2)
        assert result == 0, err_msg_invalid_result
        print(result)


    def longest_common_subsequence_memo(self, text1: str, text2: str) -> int:
        def lcs(i: int, j: int) -> int:
            # Base case: if we've reached the end of either string
            if i == len(text1) or j == len(text2):
                return 0

            # If characters match, include this character and recur for the rest
            if text1[i] == text2[j]:
                return 1 + lcs(i + 1, j + 1)

            # If characters don't match, return the max of two possibilities:
            # 1. Exclude current character of text1 and recur
            # 2. Exclude current character of text2 and recur
            else:
                return max(lcs(i + 1, j), lcs(i, j + 1))

        # Start the recursion from the beginning of both strings
        return lcs(0, 0)

    def longest_common_subsequence_tabulation(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)

        if (text1 == text2):
            return rows

        # Create a 2D DP table
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Fill the DP table
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if (text1[row - 1] == text2[col - 1]):
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        # The bottom-right cell contains the length of the LCS
        return dp[rows][cols]


# Create an instance of the class
solution = Solution()
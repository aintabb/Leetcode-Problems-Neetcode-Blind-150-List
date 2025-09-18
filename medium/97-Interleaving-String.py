"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m
substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.



Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true


Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.


Follow up: Could you solve it using only O(s2.length) additional memory space?
"""


# Time Complexity:  O(len(s1)*len(s2)) -> for memo
# Space Complexity: O(len(s1)*len(s2)) -> for memo
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"

        result = self.is_interleave_memo_top_down(s1, s2, s3)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.is_interleave_tabulation_bottom_up(s1, s2, s3)
        assert result == True, err_msg_invalid_result
        print(result)

        s1, s2, s3 = "aabcc", "dbbca", "aadbbbaccc"

        result = self.is_interleave_memo_top_down(s1, s2, s3)
        assert result == False, err_msg_invalid_result
        print(result)

        result = self.is_interleave_tabulation_bottom_up(s1, s2, s3)
        assert result == False, err_msg_invalid_result
        print(result)

        s1, s2, s3 = "", "", ""

        result = self.is_interleave_memo_top_down(s1, s2, s3)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.is_interleave_tabulation_bottom_up(s1, s2, s3)
        assert result == True, err_msg_invalid_result
        print(result)

    def is_interleave_memo_top_down(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)

        if len_s1 + len_s2 != len_s3:
            return False

        cache = {}

        def helper(i: int, j: int, k: int) -> bool:
            if k == len_s3:
                return i == len_s1 and j == len_s2

            if i + j > k:
                return False

            if (i, j) in cache:
                return cache[(i, j)]

            result = False
            if i < len_s1 and s1[i] == s3[k]:
                result = helper(i + 1, j, k + 1)

            if not result and j < len_s2 and s2[j] == s3[k]:
                result = helper(i, j + 1, k + 1)

            cache[(i, j)] = result
            return result

        return helper(0, 0, 0)

    def is_interleave_tabulation_bottom_up(self, s1: str, s2: str, s3: str) -> bool:
        ROWS, COLS, len_s3 = len(s1), len(s2), len(s3)

        if ROWS + COLS != len_s3:
            return False

        dp = [[False for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        dp[0][0] = True

        for col in range(1, COLS + 1):
            dp[0][col] = dp[0][col - 1] and s2[col - 1] == s3[col - 1]

        for row in range(1, ROWS + 1):
            dp[row][0] = dp[row - 1][0] and s1[row - 1] == s3[row - 1]

        for row in range(1, ROWS + 1):
            for col in range(1, COLS + 1):
                dp[row][col] = (
                    dp[row - 1][col] and s1[row - 1] == s3[row + col - 1]
                ) or (dp[row][col - 1] and s2[col - 1] == s3[row + col - 1])

        return dp[ROWS][COLS]


# Create an instance of the class
solution = Solution()

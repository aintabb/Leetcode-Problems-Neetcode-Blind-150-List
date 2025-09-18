"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.



Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag


Constraints:
1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""


# Time Complexity:  O(len_s*len_t) -> for both
# Space Complexity: O(len_s*len_t) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s = "rabbbit"
        t = "rabbit"

        result = self.num_distinct_memo_top_down(s, t)
        assert result == 3, err_msg_invalid_result
        print(result)

        s = "rabbbit"
        t = "rabbit"

        result = self.num_distinct_tabulation_bottom_up(s, t)
        assert result == 3, err_msg_invalid_result
        print(result)

        s = "babgbag"
        t = "bag"

        result = self.num_distinct_memo_top_down(s, t)
        assert result == 5, err_msg_invalid_result
        print(result)

        s = "babgbag"
        t = "bag"

        result = self.num_distinct_tabulation_bottom_up(s, t)
        assert result == 5, err_msg_invalid_result
        print(result)

    def num_distinct_memo_top_down(self, s: str, t: str) -> int:
        if not s or not t:
            return 0

        len_s = len(s)
        len_t = len(t)
        if len_t > len_s:
            return 0

        sub_cache = {}

        def helper(i: int, j: int) -> int:
            if j == len_t:
                return 1

            if i == len_s:
                return 0

            if (i, j) in sub_cache:
                return sub_cache[(i, j)]

            result = helper(i + 1, j)
            if s[i] == t[j]:
                result += helper(i + 1, j + 1)

            sub_cache[(i, j)] = result
            return result

        return helper(0, 0)

    def num_distinct_tabulation_bottom_up(self, s: str, t: str) -> int:
        if not s or not t:
            return 0

        len_s = len(s)
        len_t = len(t)
        if len_t > len_s:
            return 0

        dp = [[0 for _ in range(len_t + 1)] for _ in range(len_s + 1)]
        for i in range(len_s + 1):
            dp[i][len_t] = 1

        for row in range(len_s - 1, -1, -1):
            for col in range(len_t - 1, -1, -1):
                dp[row][col] = dp[row + 1][col]

                if s[row] == t[col]:
                    dp[row][col] += dp[row + 1][col + 1]

        return dp[0][0]


# Create an instance of the class
solution = Solution()

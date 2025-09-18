"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""


# Time Complexity:  O(len_s*len_p) -> for both
# Space Complexity: O(len_s*len_p) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s = "aa"
        p = "a"

        result = self.is_match_top_down_memo(s, p)
        assert result == False, err_msg_invalid_result
        print(result)

        s = "aa"
        p = "a"

        result = self.is_match_bottom_up_tabulation(s, p)
        assert result == False, err_msg_invalid_result
        print(result)

        s = "aa"
        p = "a*"

        result = self.is_match_top_down_memo(s, p)
        assert result == True, err_msg_invalid_result
        print(result)

        s = "aa"
        p = "a*"

        result = self.is_match_bottom_up_tabulation(s, p)
        assert result == True, err_msg_invalid_result
        print(result)

        s = "ab"
        p = ".*"

        result = self.is_match_top_down_memo(s, p)
        assert result == True, err_msg_invalid_result
        print(result)

        s = "ab"
        p = ".*"

        result = self.is_match_bottom_up_tabulation(s, p)
        assert result == True, err_msg_invalid_result
        print(result)

    def is_match_top_down_memo(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)

        match_cache = {}

        def helper(i: int, j: int) -> bool:
            if j == len_p:
                return i == len_s

            if (i, j) in match_cache:
                return match_cache[(i, j)]

            curr_match = i < len_s and s[i] == p[j] or p[j] == "."
            if (j + 1) < len_p and p[j + 1] == "*":
                match_cache[(i, j)] = helper(i, j + 2) or (
                    curr_match and helper(i + 1, j)
                )
                return match_cache[(i, j)]

            if curr_match:
                match_cache[(i, j)] = helper(i + 1, j + 1)
                return match_cache[(i, j)]

            match_cache[(i, j)] = False
            return False

        return helper(0, 0)

    def is_match_bottom_up_tabulation(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)

        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        dp[len_s][len_p] = True

        for row in range(len_s, -1, -1):
            for col in range(len_p - 1, -1, -1):
                curr_match = row < len_s and (s[row] == p[col] or p[col] == ".")

                if (col + 1) < len_p and p[col + 1] == "*":
                    dp[row][col] = dp[row][col + 2]

                    if curr_match:
                        dp[row][col] = dp[row + 1][col] or dp[row][col]
                elif curr_match:
                    dp[row][col] = dp[row + 1][col + 1]

        return dp[0][0]


# Create an instance of the class
solution = Solution()

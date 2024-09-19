"""
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:
Input: s = "12"
Output: 2
Explanation:
"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation:
"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0

Explanation:
"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.



Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""


# Time Complexity:  O(N) -> for both
# Space Complexity: O(N) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s = "12"

        result = self.num_decodings_memo(s)
        assert result == 2, err_msg_invalid_result
        print(result)

        result = self.num_decodings_tabulation(s)
        assert result == 2, err_msg_invalid_result
        print(result)

        s = "226"

        result = self.num_decodings_memo(s)
        assert result == 3, err_msg_invalid_result
        print(result)

        result = self.num_decodings_tabulation(s)
        assert result == 3, err_msg_invalid_result
        print(result)

        s = "06"

        result = self.num_decodings_memo(s)
        assert result == 0, err_msg_invalid_result
        print(result)

        result = self.num_decodings_tabulation(s)
        assert result == 0, err_msg_invalid_result
        print(result)


    def num_decodings_memo(self, s: str) -> int:
        if not s:
            return 1

        len_s = len(s)
        decode_cache = {}

        def dfs(idx: int) -> int:
            if (idx >= len_s):
                return 1

            if (s[idx] == '0'):
                return 0

            if (idx in decode_cache):
                return decode_cache[idx]

            ways = dfs(idx + 1)

            if (idx < len_s - 1 and '10' <= s[idx:idx + 2] <= '26'):
                ways += dfs(idx + 2)

            decode_cache[idx] = ways
            return decode_cache[idx]

        return dfs(0)

    def num_decodings_tabulation(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        len_s = len(s)
        dp = [0] * (len_s + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len_s + 1):
            if (s[i - 1] != '0'):
                dp[i] += dp[i - 1]

            if ('10' <= s[i - 2:i] <= '26'):
                dp[i] += dp[i - 2]

        return dp[len_s]


# Create an instance of the class
solution = Solution()

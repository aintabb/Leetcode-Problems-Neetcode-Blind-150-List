"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


# Time Complexity:  O(N) -> where "N" is the len(s) + len(t)
# Space Complexity: O(M) -> where "M" is the total number of unique characters in s and t
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s, t = "ADOBECODEBANC", "ABC"

        result = self.min_window(s, t)
        assert result == "BANC", err_msg_invalid_result
        print(result)

        s, t = "a", "a"

        result = self.min_window(s, t)
        assert result == "a", err_msg_invalid_result
        print(result)

        s, t = "a", "aa"

        result = self.min_window(s, t)
        assert result == "", err_msg_invalid_result
        print(result)

        s, t = "aa", "aa"

        result = self.min_window(s, t)
        assert result == "aa", err_msg_invalid_result
        print(result)

        s, t = "OUZODYXAZV", "XYZ"

        result = self.min_window(s, t)
        assert result == "YXAZ", err_msg_invalid_result
        print(result)

    def min_window(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window, count_t = {}, {}
        for ch in t:
            count_t[ch] = 1 + count_t.get(ch, 0)

        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("inf")

        left = 0

        for right in range(len(s)):
            curr_ch = s[right]
            window[curr_ch] = 1 + window.get(curr_ch, 0)

            if curr_ch in count_t and window[curr_ch] == count_t[curr_ch]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        left, right = res
        return s[left : right + 1] if res_len != float("inf") else ""


# Create an instance of the class
solution = Solution()

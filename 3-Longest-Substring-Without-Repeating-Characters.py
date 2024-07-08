"""
Given a string s, find the length of the longest substring without repeating characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


# Time Complexity:  O(N)
# Space Complexity: O(N)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s = "abcabcbb"

        result = self.length_of_longest_substring(s)
        assert result == 3, err_msg_invalid_result
        print(result)

        s = "bbbbb"

        result = self.length_of_longest_substring(s)
        assert result == 1, err_msg_invalid_result
        print(result)

        s = "pwwkew"

        result = self.length_of_longest_substring(s)
        assert result == 3, err_msg_invalid_result
        print(result)



    def length_of_longest_substring(self, s: str) -> int:
        char_set = set()

        left = max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


# Create an instance of the class
solution = Solution()
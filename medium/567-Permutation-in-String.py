"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


# Time Complexity:  O(N) -> length of the bigger string
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s1, s2 = "ab", "eidbaooo"

        result = self.character_replacement(s1, s2)
        assert result == True, err_msg_invalid_result
        print(result)

        s1, s2 = "ab", "eidboaoo"

        result = self.character_replacement(s1, s2)
        assert result == False, err_msg_invalid_result
        print(result)

    def character_replacement(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return True

        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1_char_freq = [0] * 26
        s2_char_freq = [0] * 26

        for idx in range(len_s1):
            s1_char_freq[ord(s1[idx]) - ord("a")] += 1
            s2_char_freq[ord(s2[idx]) - ord("a")] += 1

        if s1_char_freq == s2_char_freq:
            return True

        # Try every combination by moving the window
        for idx in range(len_s1, len_s2):
            s2_char_freq[ord(s2[idx]) - ord("a")] += 1
            s2_char_freq[ord(s2[idx - len_s1]) - ord("a")] -= 1

            if s1_char_freq == s2_char_freq:
                return True

        return False


# Create an instance of the class
solution = Solution()

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
        n1 = len(s1)
        n2 = len(s2)

        if (n1 > n2):
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        if (s1_counts == s2_counts):
            return True

        for i in range(n1, n2):
            s2_counts[ord(s2[i]) - ord('a')] += 1
            s2_counts[ord(s2[i - n1]) - ord('a')] -= 1

            if (s1_counts == s2_counts):
                return True

        return False


# Create an instance of the class
solution = Solution()
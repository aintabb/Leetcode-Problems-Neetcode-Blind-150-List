"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


# Time Complexity:  O(N)
# Space Complexity: O(1) -> since the array can only hold 26 characters
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s, k = "ABAB", 2

        result = self.character_replacement(s, k)
        assert result == 4, err_msg_invalid_result
        print(result)

        s, k = "AABABBA", 1

        result = self.character_replacement(s, k)
        assert result == 4, err_msg_invalid_result
        print(result)


    def character_replacement(self, s: str, k: int) -> int:
        longest, left = 0, 0

        counts = [0] * 26

        for right in range(len(s)):
            counts[ord(s[right]) - ord('A')] += 1

            while (right - left + 1) - max(counts) > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest


# Create an instance of the class
solution = Solution()
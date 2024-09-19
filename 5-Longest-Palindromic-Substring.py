"""
Given a string s, return the longest palindromic substring in s.



Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"


Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


# Time Complexity:  O(N**2)
# Space Complexity: O(N)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s = "babad"

        result = self.longest_palindrome(s)
        assert result == "bab", err_msg_invalid_result
        print(result)

        s = "cbbd"

        result = self.longest_palindrome(s)
        assert result == "bb", err_msg_invalid_result
        print(result)


    def longest_palindrome(self, s: str) -> str:
        if not s:
            return s

        len_s = len(s)

        def expand_around_center(left: int, right: int) -> str:
            while (left >= 0 and right < len_s and s[left] == s[right]):
                left -= 1
                right += 1

            return s[left + 1:right]

        longest = ""

        for i in range(len_s):
            odd_palindrome = expand_around_center(i, i)

            if (len(odd_palindrome) > len(longest)):
                longest = odd_palindrome

            even_palindrome = expand_around_center(i, i + 1)

            if (len(even_palindrome) > len(longest)):
                longest = even_palindrome

        return longest

# Create an instance of the class
solution = Solution()

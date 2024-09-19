"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.



Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""


# Time Complexity:  O(N**2)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s = "abc"

        result = self.count_substrings(s)
        assert result == 3, err_msg_invalid_result
        print(result)

        s = "aaa"

        result = self.count_substrings(s)
        assert result == 6, err_msg_invalid_result
        print(result)


    def count_substrings(self, s: str) -> int:
        if not s:
            return 0

        len_s = len(s)

        def expand_around_center(left: int, right: int) -> int:
            count = 0

            while (left >= 0 and right < len_s and s[left] == s[right]):
                left -= 1
                right += 1
                count += 1

            return count

        result = 0

        for i in range(len_s):
            result += expand_around_center(i, i)
            result += expand_around_center(i, i + 1)

        return result


# Create an instance of the class
solution = Solution()

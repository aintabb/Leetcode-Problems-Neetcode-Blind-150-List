"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.



Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]


Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""


# Time Complexity:  O(N*(2^N))
# Space Complexity: O(N*(2^N))
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s = "aab"

        result = self.partition(s)
        assert result == [["a", "a", "b"], ["aa", "b"]], err_msg_invalid_result
        print(result)

        s = "a"

        result = self.partition(s)
        assert result == [["a"]], err_msg_invalid_result
        print(result)

        s = "efe"

        result = self.partition(s)
        assert result == [["e", "f", "e"], ["efe"]]
        print(result)

    def partition(self, s: str) -> list[list[str]]:
        if not s:
            return [[]]

        result = []
        part = []

        len_s = len(s)

        def backtrack(start: int) -> None:
            if start == len_s:
                result.append(part[:])
                return

            for end in range(start, len_s):
                if self.is_palindrome(s, start, end):
                    part.append(s[start : end + 1])
                    backtrack(end + 1)
                    part.pop()

        backtrack(0)
        return result

    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False

            left = left + 1
            right = right - 1

        return True


# Create an instance of the class
solution = Solution()

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
        assert result == [["a","a","b"],["aa","b"]], err_msg_invalid_result
        print(result)

        s = "a"

        result = self.partition(s)
        assert result == [["a"]], err_msg_invalid_result
        print(result)


    def partition(self, s: str) -> list[list[str]]:
        result, part = [], []
        n = len(s)

        def backtrack(idx: int) -> None:
            if (idx == n):
                result.append(part[:])
                return

            for i in range(idx, n):
                if (self.is_palindrome(s, idx, i)):
                    part.append(s[idx:i+1])
                    backtrack(i + 1)
                    part.pop()

        backtrack(0)
        return result

    def is_palindrome(self, s: str, l: int, r: int) -> bool:
        while (l < r):
            if (s[l] != s[r]):
                return False

            l, r = l + 1, r - 1

        return True


# Create an instance of the class
solution = Solution()
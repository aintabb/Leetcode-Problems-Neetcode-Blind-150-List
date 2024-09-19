"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""


# Time Complexity:  O(N**2) -> for both
# Space Complexity: O(N) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s, word_dict = "leetcode", ["leet","code"]

        result = self.word_break_tabulation(s, word_dict)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.word_break_memoization(s, word_dict)
        assert result == True, err_msg_invalid_result
        print(result)

        s, word_dict = "applepenapple", ["apple","pen"]

        result = self.word_break_tabulation(s, word_dict)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.word_break_memoization(s, word_dict)
        assert result == True, err_msg_invalid_result
        print(result)

        s, word_dict = "catsandog", ["cats","dog","sand","and","cat"]

        result = self.word_break_tabulation(s, word_dict)
        assert result == False, err_msg_invalid_result
        print(result)

        result = self.word_break_memoization(s, word_dict)
        assert result == False, err_msg_invalid_result
        print(result)

    def word_break_tabulation(self, s: str, word_dict: list[str]) -> bool:
            word_set = set(word_dict)  # Convert list to set for O(1) look-up
            dp = [False] * (len(s) + 1)
            dp[0] = True  # Base case: empty string is considered segmented

            for i in range(1, len(s) + 1):
                for j in range(i):
                    if dp[j] and s[j:i] in word_set:
                        dp[i] = True
                        break

            return dp[len(s)]

    def word_break_memoization(self, s: str, word_dict: list[str]) -> bool:
        word_set = set(word_dict)
        memo = {}
        len_s = len(s)

        def can_segment(start: int) -> bool:
            if (start == len_s):
                return True

            if (start in memo):
                return memo[start]

            for end in range(start + 1, len_s + 1):
                if (s[start:end] in word_set and can_segment(end)):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return can_segment(0)


# Create an instance of the class
solution = Solution()

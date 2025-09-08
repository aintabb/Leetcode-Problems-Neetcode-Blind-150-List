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


# Time Complexity:  O(N^2) -> for both
# Space Complexity: O(N) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s, word_dict = "leetcode", ["leet", "code"]

        result = self.word_break_tabulation_bottom_up(s, word_dict)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.word_break_memoization_top_down(s, word_dict)
        assert result == True, err_msg_invalid_result
        print(result)

        s, word_dict = "applepenapple", ["apple", "pen"]

        result = self.word_break_tabulation_bottom_up(s, word_dict)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.word_break_memoization_top_down(s, word_dict)
        assert result == True, err_msg_invalid_result
        print(result)

        s, word_dict = "catsandog", ["cats", "dog", "sand", "and", "cat"]

        result = self.word_break_tabulation_bottom_up(s, word_dict)
        assert result == False, err_msg_invalid_result
        print(result)

        result = self.word_break_memoization_top_down(s, word_dict)
        assert result == False, err_msg_invalid_result
        print(result)

    def word_break_memoization_top_down(self, s: str, word_dict: list[str]) -> bool:
        if not s or not word_dict:
            return False

        len_s = len(s)
        word_set = set(word_dict)
        word_cache = {}

        def helper(start: int) -> bool:
            if start == len_s:
                return True

            if start in word_cache:
                return word_cache[start]

            for end in range(start + 1, len_s + 1):
                if s[start:end] in word_set and helper(end):
                    word_cache[start] = True
                    return True

            word_cache[start] = False
            return False

        return helper(0)

    def word_break_tabulation_bottom_up(self, s: str, word_dict: list[str]) -> bool:
        if not s or not word_dict:
            return False

        len_s = len(s)
        word_set = set(word_dict)
        dp = [False] * (len_s + 1)
        dp[0] = True

        for i in range(1, len_s + 1):
            for j in range(i):
                if s[j:i] in word_set and dp[j]:
                    dp[i] = True
                    break

        return dp[-1]


# Create an instance of the class
solution = Solution()

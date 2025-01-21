"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Input: s = "debit card", t = "bad credit"

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
Answer: Python's string and dictionary operations inherently support Unicode characters, so no special handling is required.
"""


# Time Complexity:  O(N)
# Space Complexity: O(N)
class ValidAnagram:
    def __init__(self) -> None:
        err_msg_anagram = (
            "Given string should be anagrams of each other. Something is wrong!"
        )

        s, t = "anagram", "nagaram"
        result = self.is_anagram(s, t)
        assert result == True, err_msg_anagram
        print(result)

        err_msg_no_anagram = (
            "Given string should not be anagrams of each other. Something is wrong!"
        )

        s, t = "rat", "car"
        result = self.is_anagram(s, t)
        assert result == False, err_msg_no_anagram
        print(result)

        s, t = "debit card", "bad credit"

        result = self.is_anagram(s, t)
        assert result == True, err_msg_anagram
        print(result)

        s, t = "你好", "好你"
        result = self.is_anagram(s, t)
        assert result == True, err_msg_anagram
        print(result)

        s, t = "你好", "你你"
        result = self.is_anagram(s, t)
        assert result == False, err_msg_no_anagram
        print(result)

    def is_anagram(self, s: str, t: str) -> bool:
        if not s or not t or len(s) != len(t):
            return False

        char_map = dict()

        for ch in s:
            char_map[ch] = 1 + char_map.get(ch, 0)

        for ch in t:
            if ch not in char_map:
                return False

            char_map[ch] -= 1
            if char_map[ch] == 0:
                del char_map[ch]

        return len(char_map) == 0


# Create an instance of the class
valid_anagram_checker = ValidAnagram()

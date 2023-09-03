'''
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
'''

class ValidAnagram:
	def __init__(self) -> None:
		err_msg_anagram = "Given string should be anagrams of each other. Something is wrong!"

		s, t = "anagram", "nagaram"
		result = self.is_valid_anagram_with_maps(s, t)
		assert result == True, err_msg_anagram
		print(result)

		err_msg_no_anagram = "Given string should not be anagrams of each other. Something is wrong!"

		s, t = "rat", "car"
		result = self.is_valid_anagram_with_maps(s, t)
		assert result == False, err_msg_no_anagram
		print(result)

		s, t = "debit card", "bad credit"

		result = self.is_valid_anagram_with_maps(s, t)
		assert result == True, err_msg_anagram
		print(result)

	def is_valid_anagram_with_maps(self, s: str, t: str) -> bool:
		if not isinstance(s, str) or not isinstance(t, str) or not s or not t:
			return False

		len_of_s, len_of_t = len(s), len(t)
		if (len_of_s != len_of_t):
			return False

		letter_map = {}
		for letter in s:
			if letter in letter_map.keys():
				letter_map[letter] += 1
			else:
				letter_map[letter] = 1

		for letter in t:
			if letter not in letter_map.keys() or letter_map[letter] == 0:
				return False
			else:
				letter_map[letter] -= 1
		return True

# Create an instance of the class
valid_anagram_checker = ValidAnagram()
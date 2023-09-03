'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

class GroupAnagrams:
  def __init__(self) -> None:
        err_msg_invalid_anagram_group = "Provided anagram group is not valid. Something is wrong!"
        strs = ["eat","tea","tan","ate","nat","bat"]

        result = self.group_anagrams(strs)
        assert result == [["bat"],["nat","tan"],["ate","eat","tea"]], err_msg_invalid_anagram_group
        print(result)

        strs = [""]
        result = self.group_anagrams(strs)
        assert result == [[""]], err_msg_invalid_anagram_group
        print(result)


        strs = ["a"]
        result = self.group_anagrams(strs)
        assert result == [["a"]], err_msg_invalid_anagram_group
        print(result)

  def group_anagrams():



group_anagrmas = GroupAnagrams()
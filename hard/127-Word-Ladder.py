"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

# Time Complexity:  O(N*M*26)
# Space Complexity: O(N*M)
## N is the length of the word_list, M is the maximum length of a word in the word_list, and 26 is the number of letters in the English alphabet.
import collections


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

        result = self.ladder_length(begin_word, end_word, word_list)
        assert result == 5, err_msg_invalid_result
        print(result)

        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log"]

        result = self.ladder_length(begin_word, end_word, word_list)
        assert result == 0, err_msg_invalid_result
        print(result)

    def ladder_length(
        self, begin_word: str, end_word: str, word_list: list[str]
    ) -> int:
        en_alphbt = "abcdefghijklmnopqrstuvwxyz"
        word_set = set(word_list)
        seen_set = {begin_word}

        word_q = collections.deque([(begin_word, 1)])

        while word_q:
            word, depth = word_q.pop()

            if word == end_word:
                return depth

            for idx in range(len(word)):
                for letter in en_alphbt:
                    copy_word_list = list(word)
                    copy_word_list[idx] = letter
                    copy_word = "".join(copy_word_list)

                    if copy_word in word_set and copy_word not in seen_set:
                        seen_set.add(copy_word)
                        word_q.appendleft((copy_word, depth + 1))

        return 0


# Create an instance of the class
solution = Solution()

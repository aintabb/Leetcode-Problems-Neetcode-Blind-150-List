"""
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

If the task is impossible, return -1.



Example 1:
source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.

Example 2:
source = "no", target = "go"
words = ["to"]

output: -1

Constraints:

- [time limit] 5000ms
- [input] string source
- 1 ≤ source.length ≤ 20
- [input] string target
- 1 ≤ target.length ≤ 20
- [input] array.string words
- 1 ≤ words.length ≤ 20
- [output] array.integer
"""

# Time Complexity:  O(N*K^2)
# Space Complexity: O(N*K)
import collections

class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        source, target, words = "bit", "dog", ["but", "put", "big", "pot", "pog", "dog", "lot"]
        result = self.shortest_word_edit_path(source, target, words)
        assert result == 5, err_msg_invalid_result
        print(result)

        source, target, words = "no", "go", ["to"]
        result = self.shortest_word_edit_path(source, target, words)
        assert result == -1, err_msg_invalid_result
        print(result)

        source, target, words = "aa", "bb", ["ab","bb"]
        result = self.shortest_word_edit_path(source, target, words)
        assert result == 2, err_msg_invalid_result
        print(result)

        source, target, words = "abc", "ab", ["abc","ab"]
        result = self.shortest_word_edit_path(source, target, words)
        assert result == -1, err_msg_invalid_result
        print(result)

        source, target, words = "aa", "bbb", ["ab","bb"]
        result = self.shortest_word_edit_path(source, target, words)
        assert result == -1, err_msg_invalid_result
        print(result)


    def shortest_word_edit_path(self, source: str, target: str, words: list[str]) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        word_set = set(words)

        word_queue = collections.deque()
        word_queue.appendleft((source, 0))

        seen_set = set([source])

        while (word_queue):
            word, depth = word_queue.popleft()
            if word == target:
                return depth

            for i in range(len(word)):
                for c in alphabet:
                    char_list    = list(word)
                    char_list[i] = c
                    copy_word    = "".join(char_list)

                    if (copy_word in word_set and copy_word not in seen_set):
                        word_queue.appendleft((copy_word, depth + 1))
                        seen_set.add(copy_word)

        return -1

# Create an instance of the class
solution = Solution()
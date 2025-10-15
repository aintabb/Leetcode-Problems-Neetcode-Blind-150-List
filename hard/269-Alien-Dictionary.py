"""
There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
a is a prefix of b and a.length < b.length.

Example 1:
Input: ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:
Input: ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"

Explanation:
from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know get 'r' < 'n'
from "enn" and "rfnn" we know 'e'<'r'
so one possible solution is "hernf"

Constraints:
The input words will contain characters only from lowercase 'a' to 'z'.
1 <= words.length <= 100
1 <= words[i].length <= 100
"""


# Time Complexity:  O(N+V+E)
# Space Complexity: O(V+E)
## Where V is the number of unique characters, E is the number of edges and N is the sum of lengths of all the strings.
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        words = ["z", "o"]

        result = self.foreign_dictionary(words)
        assert result == "zo", err_msg_invalid_result
        print(result)

        words = ["hrn", "hrf", "er", "enn", "rfnn"]

        result = self.foreign_dictionary(words)
        assert result == "hernf", err_msg_invalid_result
        print(result)

    def foreign_dictionary(self, words: list[str]) -> str:
        if not words:
            return ""

        adj_list = {ch: set() for word in words for ch in word}
        len_w = len(words)

        # Check for conflicting words
        for i in range(len_w - 1):
            w1 = words[i]
            w2 = words[i + 1]
            len_w1, len_w2 = len(w1), len(w2)
            min_len = min(len_w1, len_w2)

            if len_w1 > len_w2 and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break

        # Perform Topological sort using DFS
        result = []
        visited_map = {}

        def dfs(ch: str) -> bool:
            if ch in visited_map:
                return visited_map[ch]

            visited_map[ch] = True

            for neigh in adj_list[ch]:
                if dfs(neigh):
                    return True

            visited_map[ch] = False
            result.append(ch)
            return False

        for ch in adj_list.keys():
            if dfs(ch):
                return ""

        result.reverse()
        return "".join(result)


# Create an instance of the class
solution = Solution()

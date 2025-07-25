"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""


# Time Complexity:  O(m * n * 4^L) -> L is the max length of a word
# Space Complexity: O(N) - N is the total number of letters in all words
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        board, words = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ], ["oath", "pea", "eat", "rain"]

        result = self.find_words(board, words)
        assert result == ["eat", "oath"] or result == [
            "oath",
            "eat",
        ], err_msg_invalid_result
        print(result)

        board, words = [["a", "b"], ["c", "d"]], ["abcb"]

        result = self.find_words(board, words)
        assert result == [], err_msg_invalid_result
        print(result)

    def find_words(self, board: list[list[str]], words: list[str]) -> list[str]:
        if not board or not words:
            return []

        root = TrieNode()
        for word in words:
            curr_node = root
            for ch in word:
                if ch not in curr_node.children:
                    curr_node.children[ch] = TrieNode()

                curr_node = curr_node.children[ch]
            curr_node.end_word = True

        result = set()
        visited = set()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row: int, col: int, curr_node: TrieNode, word: str) -> None:
            if curr_node.end_word:
                result.add(word)
                curr_node.end_word = False

            if (
                row < 0
                or col < 0
                or row >= len(board)
                or col >= len(board[0])
                or board[row][col] not in curr_node.children
                or (row, col) in visited
            ):
                return

            visited.add((row, col))
            curr_letter = board[row][col]
            for dx, dy in dirs:
                dfs(
                    row + dx,
                    col + dy,
                    curr_node.children[curr_letter],
                    word + curr_letter,
                )

            visited.remove((row, col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, root, "")

        return list(result)


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_word = False


# Create an instance of the class
solution = Solution()

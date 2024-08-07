"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger board?
"""


# Time Complexity:  O((m*n)**2)
# Space Complexity: O(W) -> "W" is the word length
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"

        result = self.exist(board, word)
        assert result == True, err_msg_invalid_result
        print(result)

        board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"

        result = self.exist(board, word)
        assert result == True, err_msg_invalid_result
        print(result)

        board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"

        result = self.exist(board, word)
        assert result == False, err_msg_invalid_result
        print(result)

        board, word = [["A"]], "A"

        result = self.exist(board, word)
        assert result == True, err_msg_invalid_result
        print(result)

    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols, word_l = len(board), len(board[0]), len(word)

        if (rows == 1 and cols == 1):
            return board[0][0] == word

        def backtrack(pos: tuple, idx: int) -> bool:
            row, col = pos

            if (idx == word_l):
                return True

            if (board[row][col] != word[idx]):
                return False

            curr_ch = board[row][col]
            board[row][col] = '#'
            for row_off, col_off in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                r, c = row + row_off, col + col_off

                if (0 <= r < rows and 0 <= c < cols):
                    if (backtrack((r, c), idx + 1)):
                        return True

            board[row][col] = curr_ch
            return False


        for row in range(rows):
            for col in range(cols):
                if (backtrack((row, col), 0)):
                    return True

        return False


# Create an instance of the class
solution = Solution()
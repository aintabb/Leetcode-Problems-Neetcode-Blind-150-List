"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""


# Time Complexity:  O(ROWS*COLS)
# Space Complexity: O(ROWS*COLS)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]

        result = self.longest_increasing_path(matrix)
        assert result == 4, err_msg_invalid_result
        print(result)

        matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]

        result = self.longest_increasing_path(matrix)
        assert result == 4, err_msg_invalid_result
        print(result)

        matrix = [[1]]

        result = self.longest_increasing_path(matrix)
        assert result == 1, err_msg_invalid_result
        print(result)

        matrix = [[7, 8, 9], [9, 7, 6], [7, 2, 3]]

        result = self.longest_increasing_path(matrix)
        assert result == 6, err_msg_invalid_result
        print(result)

    def longest_increasing_path(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        ROWS, COLS = len(matrix), len(matrix[0])
        if ROWS == 1 and COLS == 1:
            return 1

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        lip_cache = {}

        def helper(row: int, col: int) -> int:
            if row < 0 or col < 0 or row == ROWS or col == COLS:
                return 0

            if (row, col) in lip_cache:
                return lip_cache[(row, col)]

            max_path = 1
            for dx, dy in dirs:
                next_row = row + dx
                next_col = col + dy

                if (
                    0 <= next_row < ROWS
                    and 0 <= next_col < COLS
                    and matrix[next_row][next_col] > matrix[row][col]
                ):
                    max_path = max(max_path, 1 + helper(next_row, next_col))

            lip_cache[(row, col)] = max_path
            return max_path

        max_path = 0
        for row in range(ROWS):
            for col in range(COLS):
                max_path = max(max_path, helper(row, col))

        return max_path


# Create an instance of the class
solution = Solution()

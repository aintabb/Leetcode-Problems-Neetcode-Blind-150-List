"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


# Time Complexity:  O(ROWS*COLS) -> for both
# Space Complexity: O(ROWS+COLS) -> with space, O(1) -> without extra space
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

        self.set_zeroes_with_memory(matrix)
        assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]], err_msg_invalid_result
        print(matrix)

        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

        self.set_zeroes_without_memory(matrix)
        assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]], err_msg_invalid_result
        print(matrix)

        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

        self.set_zeroes_with_memory(matrix)
        assert matrix == [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0],
        ], err_msg_invalid_result
        print(matrix)

        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

        self.set_zeroes_without_memory(matrix)
        assert matrix == [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0],
        ], err_msg_invalid_result
        print(matrix)

        matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]

        self.set_zeroes_with_memory(matrix)
        assert matrix == [
            [0, 0, 3, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ], err_msg_invalid_result
        print(matrix)

        matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]

        self.set_zeroes_without_memory(matrix)
        assert matrix == [
            [0, 0, 3, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ], err_msg_invalid_result
        print(matrix)

        matrix = [
            [-4, -2147483648, 6, -7, 0],
            [-8, 6, -8, -6, 0],
            [2147483647, 2, -9, -6, -10],
        ]

        self.set_zeroes_with_memory(matrix)
        assert matrix == [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [2147483647, 2, -9, -6, 0],
        ], err_msg_invalid_result
        print(matrix)

        matrix = [
            [-4, -2147483648, 6, -7, 0],
            [-8, 6, -8, -6, 0],
            [2147483647, 2, -9, -6, -10],
        ]

        self.set_zeroes_without_memory(matrix)
        assert matrix == [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [2147483647, 2, -9, -6, 0],
        ], err_msg_invalid_result
        print(matrix)

    def set_zeroes_with_memory(self, matrix: list[list[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        ROWS, COLS = len(matrix), len(matrix[0])
        row_set = set()
        col_set = set()

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)

        for row in range(ROWS):
            for col in range(COLS):
                if row in row_set or col in col_set:
                    matrix[row][col] = 0

        return

    def set_zeroes_without_memory(self, matrix: list[list[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        ROWS, COLS = len(matrix), len(matrix[0])
        first_row_zero = False

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        first_row_zero = True
                    matrix[0][col] = 0

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for row in range(ROWS):
                matrix[row][0] = 0

        if first_row_zero:
            for col in range(COLS):
                matrix[0][col] = 0


# Create an instance of the class
solution = Solution()

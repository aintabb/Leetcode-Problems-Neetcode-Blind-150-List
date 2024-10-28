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


# Time Complexity:  O(rows * cols) -> for both
# Space Complexity: O(rows + cols) -> with space, O(1) -> without extra space
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        matrix = [[1,1,1],[1,0,1],[1,1,1]]

        self.set_zeroes_with_memory(matrix)
        assert matrix == [[1,0,1],[0,0,0],[1,0,1]], err_msg_invalid_result
        print(matrix)

        matrix = [[1,1,1],[1,0,1],[1,1,1]]

        self.set_zeroes_without_memory(matrix)
        assert matrix == [[1,0,1],[0,0,0],[1,0,1]], err_msg_invalid_result
        print(matrix)

        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

        self.set_zeroes_with_memory(matrix)
        assert matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]], err_msg_invalid_result
        print(matrix)

        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

        self.set_zeroes_without_memory(matrix)
        assert matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]], err_msg_invalid_result
        print(matrix)


    def set_zeroes_with_memory(self, matrix: list[list[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])
        row_map, col_map = {}, {}

        for row in range(rows):
            for col in range(cols):
                if (matrix[row][col] == 0):
                    row_map[row] = True
                    col_map[col] = True

        for row in range(rows):
            for col in range(cols):
                if (row in row_map or col in col_map):
                    matrix[row][col] = 0


    def set_zeroes_without_memory(self, matrix: list[list[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = False

        for row in range(rows):
            for col in range(cols):
                if (matrix[row][col] == 0):
                    if (row > 0):
                        matrix[row][0] = 0
                    else:
                        first_row_zero = True
                    matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if (matrix[row][0] == 0 or matrix[0][col] == 0):
                    matrix[row][col] = 0

        if (matrix[0][0] == 0):
            for row in range(rows):
                matrix[row][0] = 0

        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0


# Create an instance of the class
solution = Solution()
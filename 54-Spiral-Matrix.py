"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


# Time Complexity:  O(rows*cols)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        matrix = [[1,2,3],[4,5,6],[7,8,9]]

        result = self.spiral_order(matrix)
        assert result == [1,2,3,6,9,8,7,4,5], err_msg_invalid_result
        print(result)

        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

        result = self.spiral_order(matrix)
        assert result == [1,2,3,4,8,12,11,10,9,5,6,7]
        print(result)

        matrix = [[6, 9, 7]]

        result = self.spiral_order(matrix)
        assert result == [6,9,7], err_msg_invalid_result
        print(result)


    '''
    left           right
    top

    bottom
    '''
    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        result = []

        if not matrix or not matrix[0]:
            return result

        rows, cols = len(matrix), len(matrix[0])
        bottom, top, left, right = rows - 1, 0, 0, cols - 1

        while (len(result) != rows * cols):
            # left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # top to bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if (len(result) == rows * cols):
                break

            # right to left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

            # bottom to top
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

        return result


# Create an instance of the class
solution = Solution()
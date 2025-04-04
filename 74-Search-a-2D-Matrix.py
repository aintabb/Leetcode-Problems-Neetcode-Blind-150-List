"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

# Time Complexity:  O(log(m*n))
# Space Complexity: O(1)


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3

        result = self.search_matrix(matrix, target)
        assert result == True, err_msg_invalid_result
        print(result)

        matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13

        result = self.search_matrix(matrix, target)
        assert result == False, err_msg_invalid_result
        print(result)

        matrix, target = [[1, 3]], 3

        result = self.search_matrix(matrix, target)
        assert result == True, err_msg_invalid_result
        print(result)

    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_row = mid // cols
            mid_col = mid % cols

            if matrix[mid_row][mid_col] == target:
                return True

            if matrix[mid_row][mid_col] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


# Create an instance of the class
solution = Solution()

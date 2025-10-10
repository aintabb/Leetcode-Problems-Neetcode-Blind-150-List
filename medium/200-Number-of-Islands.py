"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


# Time Complexity:  O(m*n)
# Space Complexity: O(m*n)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]

        result = self.num_islands_with_set(grid)
        assert result == 1, err_msg_invalid_result
        print(result)

        result = self.num_islands_without_set(grid)
        assert result == 1, err_msg_invalid_result
        print(result)

        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]

        result = self.num_islands_with_set(grid)
        assert result == 3, err_msg_invalid_result
        print(result)

        result = self.num_islands_without_set(grid)
        assert result == 3, err_msg_invalid_result
        print(result)

    def num_islands_without_set(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def traverse(row: int, col: int) -> None:
            for row_offset, col_offset in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                new_r, new_c = row + row_offset, col + col_offset

                if (
                    0 <= new_r < rows
                    and 0 <= new_c < cols
                    and grid[new_r][new_c] == "1"
                ):
                    grid[new_r][new_c] = "0"
                    traverse(new_r, new_c)

        num_of_islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    num_of_islands += 1
                    traverse(row, col)

        return num_of_islands

    def num_islands_with_set(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited_set = set()

        def helper(row: int, col: int) -> None:
            for dx, dy in dirs:
                new_row = row + dx
                new_col = col + dy

                if (
                    0 <= new_row < ROWS
                    and 0 <= new_col < COLS
                    and grid[new_row][new_col] == "1"
                    and (new_row, new_col) not in visited_set
                ):
                    visited_set.add((new_row, new_col))
                    helper(new_row, new_col)

        result = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited_set:
                    visited_set.add((row, col))
                    result += 1
                    helper(row, col)

        return result


# Create an instance of the class
solution = Solution()
